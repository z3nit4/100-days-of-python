# LOCKING

# Threads running at the same time can fight over shared data.

# The Problem: Race Conditions

counter = 0

# Two threads both do 
counter =+ 1

# You expect:
counter = 2

# But sometimes you get: 
counter = 1

# Why? 
"""
Because counter += 1 is NOT one operation internally. Its:
1. Read counter
2. Add 1
3. Write counter

If two threads read at the same time before either writes, you lose an update.

Thats called a race condition.
"""

# Solution: Locking 
# The most common synchronization tool:

# import threading

# lock = threading.Lock()

# A Lock ensures only ONE thread runs a protected section at a time.

# EG. Handling threads that counteract each other

# Original code before applying thready synchronization

"""
import threading
import time

x = 8192 # Power of 2 (shared resource)

def double():
    global x # Defines x as a global variable to use it anywhere in the script

    while x < 16384:
        x *= 2
        print(x)
        time.sleep(1) # Wait 1 sec before printing next value (easier to track)
    print("Reached the maximum!")



def halve():
    global x
    while x > 1:
        x /= 2
        print(x)
        time.sleep(1)
    print("Reached the minimum!")


t1 = threading.Thread(target=halve)
t2 = threading.Thread(target=double)


t1.start()
t2.start()

OUTPUT: 
4096.0
8192.0
4096.0
8192.0
4096.0
8192.0
...

Prints the same thing over and over
"""

import threading
import time

x = 8192 # Power of 2 (shared resource)

lock = threading.Lock() # Allows/forbids us to access resource

def double():
    global x, lock # Defines x and lock as a global variable to use it anywhere in the script
    lock.acquire() # Acquire the lock if it's free
    while x < 16384:
        x *= 2
        print("Double:", x)
        time.sleep(1) # Wait 1 sec before printing next value (easier to track)
    print("Reached the maximum!")
    lock.release()

def halve():
    global x, lock
    lock.acquire()
    while x > 1:
        x /= 2
        print("Halve:", x)
        time.sleep(1)
    print("Reached the minimum!")
    lock.release()

t1 = threading.Thread(target=halve)
t2 = threading.Thread(target=double)

t1.start()
t2.start()

t1.join()
t2.join()


# One thread at a time can access the resource.

# Another useful way to limit the access to a resource is through semaphores
# They limit the access to the resource through a maximum value. Do not lock resource completely

import threading
import time

semaphore = threading.BoundedSemaphore(value=5) # Maximum value of accesses allowed, so xax 5 threads allowed simultaneously. 

def access(thread_number): # Thread identification
    print(f"{thread_number} is trying to access!")
    semaphore.acquire()
    print(f"{thread_number} was granted access!")
    time.sleep(10) # Keep the semaphore acquired for 10 sec
    print(f"{thread_number} is now releasing!")
    semaphore.release()

for thread_number in range (1, 11): # Range: 1 - 10
    t = threading.Thread(target = access, args=(thread_number,)) # Pass a parameter which is the thread number
    t.start()
    time.sleep(1)


# 10 threads. Only 5 allowed inside at once. Others queue. 