# CS Portfolio Projects
  ---------------------

# CS-142 - Fundamentals I
This program processes an input file of data for a personality test known as the Keirsey Temperament Sorter. The Keirsey personality test involves answering 70 questions each of which have two answers. The input file will contain a series of line pairs, one per person. The first line will have the person’s name (possibly including spaces) and the second line will have a series of 70 letters all in a row. The program computes the scores and overall result for each person and reports this information to an output file.

# CS-143 - Fundamentals II
This program practices using binary trees and priority queues. In this program text files are compressed by using a coding scheme based on the frequency of characters, called Huffman coding. Instead of using the usual seven or eight bits per character, Huffman's method uses only a few bits for characters that are used often and more bits for those that are rarely used.

# CS-261 - Data Structures
Hash Map Implementation - Chaining
 - Use a dynamic array to store a hash table and implement chaining for collision resolution using a singly linked list. Chains of key / value pairs must be stored in linked list nodes.

Hash Map Implementation - Open Addressing
 - Use a dynamic array to store a hash table and implement Open Addressing with Quadratic Probing for collision resolution inside that dynamic array. Key/value pairs must be stored in the array.

# CS-271 - Assembly Language
The purpose of this assignment is to reinforce concepts related to string primitive instructions and macros by:
 - Implementing and testing two macros for string processing.
 - Implementing and testing two procedures for signed integers which use string primitive instructions
 - Writing a test program (in main) which uses theses implementations to:
   - Get 10 valid integers from the user. 
   - Stores these numeric values in an array.
   - Display the integers, their sum, and their truncated average.
 
# CS-290 - Web Development
Create a MERN stack to write a Single Page Application (SPA) that tracks exercises completed by the user. Program uses React for the front-end UI app and REST API, using Node and Express, for the back-end web service. Program uses MongoDB for persistence.

# CS-325 - Analysis of Algorithms
The programs is given: 
 - A 2-D puzzle of size MxN, that has N rows and M column (M and N can be different). Each cell in the puzzle is either empty or has a barrier. An empty cell is marked by ‘-’ (hyphen) and the one with a barrier is marked by ‘#’.
 - Two coordinates from the puzzle (a,b), which represents the source node, and (x,y), which represents the destination node. The program is only allowed to move to an empty cell and cannot move to a cell with a barrier in it.
 
The goal of the program is to reach the destination cell by covering the minimum number of cells possible.

# CS-340 - Intro to Databases
The project for this class was a term-long project to create a front-end web application that connected to a back-end SQL database. My partner and I decided to create a web portal for a small business, Canine Munchies, that would help the owners of the company keep track of their purchase orders. Here is a excerpt from the Project Overview:
 - To determine the production schedule the owners have commissioned the development of a backend database, Munchies Orders, that will record customer purchase orders. The database has complete CRUD (create, read, update, and delete) functionality and consists of five entity tables (Customers, Products, Orders, OrderDetails, and Employees) that record all relevant information regarding a customer’s purchase. In addition to the CRUD functionality, the database will be capable of creating a Customers entity without purchasing a product. However, if a product is purchased, a Customers entity must be tied to that purchase (ie. no “Guest” checkout).

More information about the project overview, database outline, ERD, and Schema can be found in the attached PDF.

# CS-344 - Operating Systems
This program implements a subset of features of well-known shells, such as bash. Specifically, the program:
 - Provide a prompt for running commands
 - Handle blank lines and comments, which are lines beginning with the # character
 - Provide expansion for the variable $$
 - Execute 3 commands exit, cd, and status via code built into the shell
 - Execute other commands by creating new processes using a function from the exec family of functions
 - Support input and output redirection
 - Support running commands in foreground and background processes
 - Implement custom handlers for 2 signals, SIGINT and SIGTSTP

# CS-361 - Software Engineering I
The project for this class was a term-long project of our choosing. I chose to develop an application that gives a BUY/SELL recommendation for a given stock based off of technical analysis (TA) indicators. However, the primary focus of this course was not the technical aspects of coding, but instead focused on the Agile work process and microservice architecture. We used the project to demonstrate proficiency in:
 - Using a task management system (Jira, Asana, etc.)
 - Collected user stories and developed them into actionable tickets
 - Functional vs. non-functional requirements (ie. Quality Attributes)
 - Practice using the "Sprint" methodology
 - Microservice architecture, including implementation and development
 
Here is a video link for the implementation of the project - https://www.youtube.com/watch?v=-7wvbI_fydo
 
# CS-362 - Software Engineering II
This class focused on Software Engineering testing and pipeline workflow via a centralized repository (GitHub). The main testing topics of the course were black-box testing, white-box testing, random-testing, and test-driven development. The end-of-the-term project was to use these testing techniques along with continuous integration methodology to develop a software development pipeline, in which code from individual contributors could be automatically built and tested on GitHub. The project had three contributors, each having a separate assignment that required the use of the shard repository. When a contributors was done editing their code they would initiate a pull request that would automatically run a build/testing suite and, assuming it passed the automatic tests, would notify the other contributors to perform code reviews. 

# CS-372 - Computer Networks
This project implements a client/server chat program that allows two people to converse over a network, via sockets. The client will initiate a conversation with a server by connecting to the host address and port number of the server. After the connection is established, the client will start the conversation by typing some message to the client. After the client’s message is received, the server will respond back with its own message. The communication will flow back-and-forth in this manner until either the client or server enters in ‘/q’, which is the kill signal for the program.
