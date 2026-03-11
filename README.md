# 100 Days of Python

This repository contains my solutions and projects as I work through the 100 Days of Python coding challenge. I'm learning core Python concepts and practicing by building small projects each day.

## Progress

**FOUNDATIONAL CONCEPTS:**
- **Day 1:** Band Name Generator – asked user for city and pet name.  
- **Day 2:** Tip Calculator – combined user inputs and printed a calculated bill.  
- **Day 3:** Treasure Island – text adventure game with nested conditionals.  
- **Day 4:** Rock, Paper, Scissors – used lists and random choice.  
- **Day 5:** Loops – highest score and Gauss sum.  
- **Day 6:** Functions – wrote reusable functions like even/odd and square calculator.  
- **Day 7:** Hangman – implemented a word guessing game.  
- **Day 8:** Number Guessing Game – learned how to loop until correct guess.  
- **Day 9:** Student Grade Tracker – practiced tuples, lists, and dictionaries.
- **Day 10:** Secure Login System – implemented login/registration with exception handling, user input validation, and account lock after failed attempts.
- **Day 11:** File Operations – practiced reading, writing, appending, and manipulating files using Python’s built-in I/O and os module.
- **Day 12:** String Functions – practiced string methods like .isalpha(), .isdigit(), .isalnum(), .strip(), and slicing.

**INTERMEDIATE CONCEPTS:**
- **Day 13:** Classes & Objects – built a Bank Account simulator to understand constructors (__init__), attributes, methods, and modifying object state using self.
- **Day 14:** Inheritance & Vectors - practiced parent and child classes using Animal and Person/Worker examples. Reused parent attributes and methods, overrode methods (__str__), and used super() to access parent constructors.
  - **Operator Overloading & Vectors:** Built a custom Vector class supporting addition (+) and subtraction (-) using __add__ and __sub__. Learned to represent vectors in code and output them in a readable format.
- **Day 15:** Multithreading – Learned about threads and how they allow Python programs to run multiple tasks simultaneously for I/O-bound operations like file downloads or web requests. Built a Multi-Threaded File Downloader that downloads files from Pinterest concurrently, handling URLs safely and naming files based on the last numbers in the URL.
- **Day 16:** Synchronizing Threads – Learned about race conditions when multiple threads access shared data simultaneously. Practiced Locks to prevent concurrent modifications and BoundedSemaphore to limit access to a shared resource. Built examples that safely double and halve a number concurrently while avoiding conflicts.
- **Day 17:** Events & Daemon Threads – Learned how to coordinate threads using Event objects to signal and control execution flow. Built a program where a thread waits for a trigger before continuing. Explored daemon threads by creating a background file reader that continuously updates shared data while another thread prints it, understanding how daemon threads terminate automatically when the main program exits.
- **Day 18:** Queues & Port Scanner – Learned how queues can safely share work between multiple threads without conflicts. Built a multi-threaded port scanner using Python’s queue, socket, and threading modules. Practiced scanning multiple ports concurrently, handling timeouts, and collecting results in a shared list. Learned about TCP connections, common ports, and how to structure a threaded program to efficiently process tasks from a queue.
- **Day 19:** Day 19: Socket Programming – Built a basic TCP client-server system using Python’s socket library. Implemented a server that binds to a local IP and port, listens for incoming connections, accepts clients, and sends a message when a connection is established. Created a separate client program that connects to the server, receives the message using recv(), decodes it, and prints it. This project introduced the fundamentals of network communication, including sockets, binding to ports, listening for connections, accepting clients, sending/receiving data, and encoding/decoding messages.
- **Day 20:** SQLite & Databases – Learned how to use Python’s sqlite3 module to create and interact with a local database. Built a users table, inserted records, and retrieved data using SQL queries. Refactored the database logic into an OOP-based User class with methods for loading and inserting users while safely passing parameters into SQL queries.
- **Day 21:** Recursion – Learned how recursive functions solve problems by calling themselves with smaller inputs until reaching a base case. Implemented recursive and non-recursive versions of factorial and Fibonacci calculations to understand the difference in approach and performance. Explored how missing base cases can cause infinite recursion or stack overflow errors.
- **Day 22:** XML Processing – Learned how to parse and work with XML in Python. Explored xml.sax for event-driven parsing and xml.etree.ElementTree for tree-based parsing. Practiced reading, extracting, adding, and saving elements dynamically, understanding the structure of XML files and how to manipulate them programmatically.
- **Day 23:** Logging – Learned how to use Python’s logging module to track program events instead of relying on print(). Explored logging levels (DEBUG, INFO, WARNING, ERROR, CRITICAL) and created a custom logger called ZEN Logger. Implemented file logging with FileHandler, custom log formatting, and practiced writing structured logs to a .log file.

## Languages & Tools
- Python
- SQLite
- Threading
- Socket Programming
- VS Code
