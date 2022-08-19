# CS Portfolio Projects

# CS-261 - Data Structures
Hash Map Implementation - Chaining
 - Use a dynamic array to store your hash table and implement chaining for collision
resolution using a singly linked list. Chains of key / value pairs must be stored in
linked list nodes.

Hash Map Implementation - Open Addressing
 - Use a dynamic array to store your hash table and implement Open Addressing
with Quadratic Probing for collision resolution inside that dynamic array. Key /
value pairs must be stored in the array.

# CS-271 - Assembly Language
The purpose of this assignment is to reinforce concepts related to string primitive instructions and macros by:
 - Implementing and testing two macros for string processing.
   - mGetString:  Display a prompt (input parameter, by reference), then get the user’s keyboard input into a memory location (output parameter, by reference).
   - mDisplayString:  Print the string which is stored in a specified memory location (input parameter, by reference).
 - Implementing and testing two procedures for signed integers which use string primitive instructions
   - ReadVal: Convert (using string primitives) the string of ascii digits to its numeric value representation (SDWORD), validating the user’s input is a valid number (no letters, symbols, etc).
   - WriteVal: Convert a numeric SDWORD value (input parameter, by value) to a string of ascii digits
 - Writing a test program (in main) which uses the ReadVal and WriteVal procedures above to:
   - Get 10 valid integers from the user. 
   - Stores these numeric values in an array.
   - Display the integers, their sum, and their truncated average.
 
# CS-290 - Web Development
Create a MERN stack to write a Single Page Application (SPA) that tracks exercises completed by the user. Program uses React for the front-end UI app and REST API, using Node and Express, for the back-end web service. Program uses MongoDB for persistence.
