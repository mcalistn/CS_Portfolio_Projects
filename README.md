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
