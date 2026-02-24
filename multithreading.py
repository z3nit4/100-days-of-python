# THREADING

# Threading allows a program to run multiple tasks concurrently. 
# A thread is the smallest unit of execution inside a process.
# A process can contain multiple threads.
# Threads share the same memory space within a process.

# Process - A running program (restaurant)
# Thread - A worker inside that program (chefs)

import threading # To work with threads 

def helloworld(): # Function
    print("Hello World!")

t1 = threading.Thread(target=helloworld)
# t1.start()

# Threads can execute multiple functions at the same time, which work in parallel

def function1(): 
    for x in range(10000):
        print("ONE")

def function2(): 
    for x in range(10000):
        print("TWO")

t2 = threading.Thread(target=function1)
t3 = threading.Thread(target=function2)

# t2.start()
# t3.start()

# Waiting for Threads

def hello():
    for x in range(50):
        print("Hello!")

t4 = threading.Thread(target=hello)
t4.start()
t4.join()

print("Another Text") # To wait for thread to finish before execute anything use join fucntion

""" Python threading is best for:
- Web scraping
- File downloads
- Network requests
Waiting tasks

For heavy math and CPU-intensive loops multiprocessing is required
"""