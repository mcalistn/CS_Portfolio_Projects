// Nathan McAlister
// 3/4/2021
// CSE142
// TA: Shananda Dokka
// Assignment #7
//
// This program takes the results of answering 70 questions of the Keirsey 
// personality test and converts the answers into a person's personality 
// type (INFP, ESTJ, etc.).

// Java Imports
import java.io.*;
import java.util.*;

public class Personality {

   public static final int ARRAY_MAX = 4;

   public static void main(String[] args) throws FileNotFoundException {
      
      Scanner console = new Scanner(System.in);
      
      getIntro();
      
      String inputFileName = getInputFileName(console);
      Scanner input = new Scanner(new File(inputFileName.toLowerCase()));

      String outputFileName = getOutputFileName(console);
      PrintStream output = new PrintStream(new File(outputFileName.toLowerCase()));
      
      outputPersonalityType(input, output);
            
   }
   
   // Introduces user to the program.
   public static void getIntro() {
   
      System.out.println("This program processes a file of answers to the");
      System.out.println("Keirsey Temperament Sorter.  It converts the");
      System.out.println("various A and B answers for each person into");
      System.out.println("a sequence of B-percentages and then into a");
      System.out.println("four-letter personality type.");
      System.out.println("");
   
   }
   
   // Determines a persons personality type and writes it to the output file.
   public static void outputPersonalityType(Scanner input, PrintStream output) {
      
      while (input.hasNextLine()) {
         String nameLine = input.nextLine();
         String testLine = input.nextLine().toUpperCase();
         
         int[] testResults_A = getTestResults(testLine, 'A');
         int[] testResults_B = getTestResults(testLine, 'B');
         int[] testResults_PercentB = calcPercentB(testResults_A, testResults_B);
         
         String personalityType = getPersonalityType(testResults_PercentB);
         output.println(nameLine + ": " + Arrays.toString(testResults_PercentB) 
                        + " = " + personalityType);
      }
      
   }
      
   // Prompt user for the input file name.
   // Returns the input file name.   
   public static String getInputFileName(Scanner console) {
   
      System.out.print("input file name? ");
      String inputFileName = console.next();
      
      return inputFileName;
   
   }

   // Prompts user to designate the output file name.
   // Returns the output file name.
   public static String getOutputFileName(Scanner console) {
   
      System.out.print("output file name? ");
      String outputFileName = console.next();
      System.out.println("");
      
      return outputFileName;
   
   }
   
   // Counts the answers (A or B) of the personality test questions for each 
   // personality category (E vs. I, S vs N, etc.).
   // Returns the total count for each personality category.
   public static int[] getTestResults(String testScoreLine, char charCheck) {
   
      int[] testResults = new int[ARRAY_MAX];
      int count = 0;
      
      for (int i = 0; i <= testScoreLine.length() - 1; i++) {
         char letterCheck = testScoreLine.charAt(i);
         if (letterCheck == charCheck) {
            if (i + 1 == 1 || i % 7 == 0) {
               testResults[ARRAY_MAX - 4] = testResults[ARRAY_MAX - 4] + 1;
            } else if ((i - 1) % 7 == 0 || (i - 2) % 7 == 0) {
               testResults[ARRAY_MAX - 3] = testResults[ARRAY_MAX - 3] + 1;
            } else if ((i - 3) % 7 == 0 || (i - 4) % 7 == 0) {
               testResults[ARRAY_MAX - 2] = testResults[ARRAY_MAX - 2] + 1;
            } else if ((i - 5) % 7 == 0 || (i - 6) % 7 == 0) {
               testResults[ARRAY_MAX - 1] = testResults[ARRAY_MAX - 1] + 1;
            }
         }
      }

      return testResults;
   }
   
   // Calculates and returns the pecentage of questions that were answered with 'B'.
   public static int[] calcPercentB(int[] testResults_A, int[] testResults_B) {
      
      int[] percentage = new int[ARRAY_MAX];
      
      for (int i = 0; i < ARRAY_MAX; i++) {
         int sum = testResults_A[i] + testResults_B[i];
         double percent = ((double) testResults_B[i] / (double) sum) * 100;
         percentage[i] = (int) Math.round(percent);
      }
      
      return percentage;
   }
   
   // Determines the personality type based on the percentage of questions 
   // answered with 'B'.
   // Returns the personality type (ISTJ, etc.)
   public static String getPersonalityType(int[] percent) {

      String personalityTypeS = "";
      
      personalityTypeS = personalityTypeS + getExtIntro(percent[ARRAY_MAX - 4]);
      personalityTypeS = personalityTypeS + getSenInt(percent[ARRAY_MAX - 3]);
      personalityTypeS = personalityTypeS + getThinkFeel(percent[ARRAY_MAX -2 ]);
      personalityTypeS = personalityTypeS + getJudgePerc(percent[ARRAY_MAX - 1]);
               
      return personalityTypeS;

   }
   
   // Determine if Extrovert or Introvert.
   // Returns personality type for E or I, or 'X' if neither (50%).
   public static String getExtIntro(int percent) {
      
      String personalityType = "";
      
      if (percent > 50) {
         personalityType = "I";
      } else if ( percent < 50) {
         personalityType = "E";
      } else {
         personalityType = "X";
      }
      
      return personalityType;
      
   }
   
   // Determine if Sensation or Intuition.
   // Returns personality type for S or N, or 'X' if neither (50%).
   public static String getSenInt(int percent) {
      
      String personalityType = "";
      
      if (percent > 50) {
         personalityType = "N";
      } else if ( percent < 50) {
         personalityType = "S";
      } else {
         personalityType = "X";
      }
      
      return personalityType;
      
   }

   // Determine if Thinking or Feeling.
   // Returns personality type for T or F,  or 'X' if neither (50%).
   public static String getThinkFeel(int percent) {
      
      String personalityType = "";      
      
      if (percent > 50) {
         personalityType = "F";
      } else if ( percent < 50) {
         personalityType = "T";
      } else {
         personalityType = "X";
      }
      
      return personalityType;
      
   }
   
   // Determine if Judging or Perceiving.
   // Returns personality type for J or P,  or 'X' if neither (50%).
   public static String getJudgePerc(int percent) {
      
      String personalityType = "";      
      
      if (percent > 50) {
         personalityType = "P";
      } else if ( percent < 50) {
         personalityType = "J";
      } else {
         personalityType = "X";
      }
      
      return personalityType;
      
   }
   
}