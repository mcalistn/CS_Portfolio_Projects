#define _POSIX_SOURCE
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <stdbool.h>
#include <fcntl.h>
#include <signal.h>


// !~!~! Global Variables !~!~!
#define MAX_LEN 2048    // Maximum length of command line input
#define MAX_ARG 512     // Maximum number of command line arguments
int bgCounter = 0;      // Counter for background child processes
int bgArr[100] = {0};   // Background child processes' PID array
int exitStatus = 0;     // Exit status
bool noBG = false;      // No background processes allowed flag
bool termSig = false;   // Termination signal flag


// !~!~! Structures !~!~!

/*
 * Structure is used to record store information about the user input, most 
 * importantly the array of tokens that represents the command and arguments 
 * of the user's input.
 */
struct cmd_args {
  char arr[MAX_ARG][MAX_LEN];   // Array containing tokenized command/arguments
  char in_filename[MAX_LEN];    // Input redirection file name
  char out_filename[MAX_LEN];   // Output redirection file name
  int count;
  bool inRedirFlag;             // Input redirection flag
  bool outRedirFlag;            // Output redirection flag
  bool backgroundFlag;          // Background process flag
};


// !~!~! Methods !~!~!

/*
 * SIGTSTP handler function used to toggle to foreground-only mode or 
 * background/foreground mode
 *
 * @params - signo - Signal number
 */
void handle_SIGTSTP(int signo){

  char* trueMessage = "\nEntering foreground-only mode (& is now ignored)\n";
  char *falseMessage = "\nExiting foreground-only mode\n";

  if (noBG) {
    noBG = false;
    write(STDOUT_FILENO, falseMessage, 30);
  } else {
    noBG = true;
    write(STDOUT_FILENO, trueMessage, 50);
  }
}


/*
 * Check on the status of all background child processes. If the process has terminated
 * normally or abnormally, print out a message to identify the process as being completed.
 */
void checkOnChildren() {

  int childStatus = 0;

  for (int i = 0; i < bgCounter; i++) {
    int childPid = waitpid(bgArr[i], &childStatus, WNOHANG);
    if (childPid > 0) {
      // Terminated normally
      if (WIFEXITED(childStatus)) {
        printf("Background child process PID #%d has exited. ", bgArr[i]);
        printf("Exit status: '%d'.\n", WEXITSTATUS(childStatus));
        fflush(stdout);
      }
      // Terminated abnormally
      if (WIFSIGNALED(childStatus)) {
        printf("Background child process PID #%d has terminated. ", bgArr[i]);
        printf("Termination signal: '%d'.\n", WTERMSIG(childStatus));
        fflush(stdout);
      }
    }
  }
}


/*
 * Expands any instance of '$$' into the process ID of the command shell
 *
 * @params - token - token from the user input that contains '$$' that needs
 *                   to be expanded
 * @return - the expanded token containing the process ID of the command shell
 */
char *expansion(char *token) {

  pid_t pid = getpid();
  char *pidstr = {0};
  int n = snprintf(NULL, 0, "%jd", pid);
  int j = 0;
  char *token_exp = malloc (MAX_LEN);

  pidstr = malloc((n + 1) * sizeof *pidstr);
  sprintf(pidstr, "%jd", pid);
  for (int i = 0; i < strlen(token); i++) {
    if (token[i] == '$' && token[i + 1] == '$') {
      strcat(token_exp, pidstr);
      i++;
      j += strlen(pidstr) - 2;
    } else {
      token_exp[i + j] = token[i];
    }
  }

  return token_exp;
}


/*
 * Initialize the command token array with '0'
 *
 * @params - cmd_tk - structure used to store information about the user input
 * @return - initialized structure array full of '0's
 */
struct cmd_args init_struct(struct cmd_args cmd_tk) {

  for (int i = 0; i < MAX_ARG; i++) {
    for (int j = 0; j < MAX_LEN; j++) {
      cmd_tk.arr[i][j] = 0;
    }
  }

  return cmd_tk;
}


/*
 * Tokenizes the user inputed command line. Each command/argument that the user
 * inputed will be put into an individual element of an array.
 *
 * @params - userInput - user's inputed command from STDIN
 * @return - structure containing an array with all commands/arguments inside of
 *           an individual element of an array
 */
struct cmd_args tokenizer(char *userInput) {
  
  struct cmd_args cmd_tk;
  init_struct(cmd_tk);    // Initialize the cmd_args structure
  char *token = strtok(userInput, " ");
  int count = 0;
  char *prevToken = {0};        // Previous token string
  cmd_tk.inRedirFlag = false;   // Input redirection flag
  cmd_tk.outRedirFlag = false;  // Output redirection flag

  while (token != NULL) {
    // Expand token
    token = expansion(token);
    // Determine if an input file is used
    if (strcmp(token, "<") == 0 && cmd_tk.inRedirFlag == 0) {
      cmd_tk.inRedirFlag = true;
      token = strtok(NULL, " ");
      strcpy(cmd_tk.in_filename, token);
    // Determine if an output file is used
    } else if (strcmp(token, ">") == 0 && cmd_tk.outRedirFlag == 0) {
      cmd_tk.outRedirFlag = true;
      token = strtok(NULL, " ");
      strcpy(cmd_tk.out_filename, token);
    // Record token in structure array
    } else {
    strcpy(cmd_tk.arr[count], token);
    count++;
    }
  prevToken = token;
  token = strtok(NULL, " ");
  }
  // Determine if last token was '&' sign, indicating the process will be a
  // background process
  if (strcmp(prevToken, "&") == 0) {
    // Ensure background processes are allowed
    if (noBG == 0) {
      cmd_tk.backgroundFlag = true;
    }
    strcpy(cmd_tk.arr[count], "\0");
    count--;
  }
  cmd_tk.count = count;
  
  return cmd_tk;
}


/*
 * Fork child process(es) off of the shell parent process as necessary for execution.
 * Execution of all processes will be completed in the foreground or background and
 * will all be completed in a child process.
 *
 * @params - cmd_tk - structure used to store information about the user input
 * @params - SIGINT_action - sigaction structure that is used in the capture and
 *                           re-establishment of default action for the SIGINT signal
 * @return - Returns the success or failure of the parent and child processes
 */
int runFork(struct cmd_args cmd_tk, struct sigaction SIGINT_action) {

  pid_t spawnpid = -5;
  int childStatus = -5;
  int childPid = -5;
  int i = 0;
  char *ex_argv[cmd_tk.count];

  // Convert structural array (many empty elements) to an execution array (has only
  // the specific number of elements in the array).
  for (int i = 0; i < cmd_tk.count; i++) {
    ex_argv[i] = cmd_tk.arr[i];
  }
  // Fork the child process off of the parent process
  ex_argv[cmd_tk.count] = NULL;
  spawnpid = fork();
  switch (spawnpid) {
    // Fork failure error
    case -1:
      perror("fork() failed!");
      fflush(stdout);
      exit(1);
      break;
    case 0:
      // Convert SIGINT back to default functionality
      if (cmd_tk.backgroundFlag == 0) {
        SIGINT_action.sa_handler = SIG_DFL;
        sigaction(SIGINT, &SIGINT_action, NULL);
      }
      // Open input file for reading and error check
      if (cmd_tk.inRedirFlag || cmd_tk.backgroundFlag) {
        if (cmd_tk.backgroundFlag && cmd_tk.inRedirFlag == 0) {
          strcpy(cmd_tk.in_filename, "/dev/null");
        }
        int sourceFD = open(cmd_tk.in_filename, O_RDONLY);
        if (sourceFD == -1) {
          perror("Error opening file.");
          exit(1);
        }
        // Duplicate open file from STDIN
        int result = dup2(sourceFD, 0);
        if (result == -1) {
          perror("Error opening file.");
          exit(1);
        }
        // Close file
        fcntl(sourceFD, F_SETFD, FD_CLOEXEC);
      } 
      // Open output file for writing and error check
      if (cmd_tk.outRedirFlag || cmd_tk.backgroundFlag) {
        if (cmd_tk.backgroundFlag && cmd_tk.outRedirFlag == 0) {
          strcpy(cmd_tk.out_filename, "/dev/null");
        }
        int targetFD = open(cmd_tk.out_filename, O_WRONLY | O_CREAT | O_TRUNC, 0644);
        if (targetFD == -1) {
          perror("Error opening file.");
          exit(1);
        }
        // Duplicate STDOUT to targeted output file.
        int result = dup2(targetFD, 1);
        if (result == -1) {
          perror("Error opening file.");
          exit(1);
        }
        // Close file
        fcntl(targetFD, F_SETFD, FD_CLOEXEC);
      } 
      // Execute the user inputed command line all arguements and error check the command
      // executed properly
      int result = execvp(ex_argv[0], ex_argv);
      if (result =- -1) {
        perror("Error executing command");
        exit(1);
      }
      fflush(stdout);
      exit(0);
    default:
      if (cmd_tk.backgroundFlag) {
        // Background processes
        childPid = waitpid(spawnpid, &childStatus, WNOHANG);
        bgArr[bgCounter] = spawnpid;    // Record child process ID in global array
        bgCounter++;
        cmd_tk.backgroundFlag = false;
        printf("Background PID: %d\n", spawnpid);
        fflush(stdout);
      } else {
        // Foreground processes
        childPid = waitpid(spawnpid, &childStatus, 0);
        // Update exit/termination status
        if (WIFEXITED(childStatus)) {
          exitStatus = WEXITSTATUS(childStatus);
          termSig = false;
        } else {
          exitStatus = WTERMSIG(childStatus);
          termSig = true;         
          printf("Terminated by signal '%d'\n", exitStatus);
        }
      }
      break;
  }
  return 0;
}

/*
 * Parse user's input command line and determine if the command contains one of the three required
 * built-in commands (exit, cd, status).
 *
 * @params - userInput - user's inputed command from STDIN
 * @params - cmd_tk - structure used to store information about the user input
 * @params - SIGINT_action - sigaction structure that is used in the capture and
 *                           re-establishment of default action for the SIGINT signal
 * @params - SIGTSTP_action - sigaction structure that is used in the capture and
 *                            re-direction of the default action for the SIGTSTP signal
 * @returns - Exit status (-1 for closing of the program)                           
 */
int parseUserInput(char *userInput, struct cmd_args cmd_tk, struct sigaction SIGINT_action, struct sigaction SIGTSTP_action) {
  char cwd[MAX_LEN] = {0};
  SIGTSTP_action.sa_handler = SIG_IGN;
  sigaction(SIGTSTP, &SIGTSTP_action, NULL); 

  // 'exit' built-in command
  if (strcmp(cmd_tk.arr[0], "exit") == 0) {
    return -1;
  // 'cd' built-in command
  } else if (strcmp(cmd_tk.arr[0], "cd") == 0) {
    getcwd(cwd, sizeof(cwd));
    if (cmd_tk.count < 2) {
      chdir(getenv("HOME"));
    } else {
      if (strlen(cmd_tk.arr[1]) > strlen(cwd)) {
        chdir(cmd_tk.arr[1]);
      } else {
        char *newDir = malloc(strlen(cwd) + strlen(cmd_tk.arr[1]) + 2);
        strcpy(newDir, cwd);
        strcat(newDir, "/");
        strcat(newDir, cmd_tk.arr[1]);
        chdir(newDir);
        free(newDir);
      }
    }
    getcwd(cwd, sizeof(cwd));
    printf("%s\n", cwd);
    fflush(stdout);
  // 'status' built-in command
  } else if (strcmp(cmd_tk.arr[0], "status") == 0) {
    if (termSig) {
      printf("Terminated by signal '%d'\n", exitStatus);
    } else {
      printf("Exit status: '%d'\n", exitStatus);
    }
    fflush(stdout);
  } else {
    // User input command is not a built-in command
    runFork(cmd_tk, SIGINT_action);
  }
  return 0;
}


/*
 * Request and execute the user's command
 */
int main(int argc, char *argv[]) {

  char userInput[MAX_LEN] = {0};
  // Establish SIGINT sigaction structure
  struct sigaction SIGINT_action = {0};
  sigfillset(&SIGINT_action.sa_mask);
  SIGINT_action.sa_flags = 0;
  // Establish SIGTSTP sigaction structure
  struct sigaction SIGTSTP_action = {0};
  sigfillset(&SIGTSTP_action.sa_mask);
  SIGTSTP_action.sa_flags = 0;

  while (1) {
    // Check on background children to determine if they have exited/terminated
    checkOnChildren();
    SIGINT_action.sa_handler = SIG_IGN;
    sigaction(SIGINT, &SIGINT_action, NULL);
    SIGTSTP_action.sa_handler = handle_SIGTSTP;
    sigaction(SIGTSTP, &SIGTSTP_action, NULL);
    printf(":");
    // Get user input
    fgets(userInput, sizeof userInput, stdin);
    userInput[strlen(userInput) - 1] = '\0';    // Remove new line due to 'enter'
    if (userInput[0] != '#' && userInput[0] != '\0') {
      // Tokenize user input
      struct cmd_args cmd_tk = tokenizer(userInput);
      // Parse and execute user input
      int d = parseUserInput(userInput, cmd_tk, SIGINT_action, SIGTSTP_action);
      if (d == -1) {
        break;    // exit command
      }
    }  
  }
  return 0;
}

