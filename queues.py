# QUEUES

# Queues are data structures similar to lists and sequences. They follow a specific order of entry and exit which is FIFO = First In, First Out 

"""
queue.Queue() is thread safe

Meaning:
- Multiple threads can safely add items
- Multiple threads can safely remove items
- No locks needed manually

The queue handles synchronization internally.

Core Queue Methods

q.put(item)      # Add item
q.get()          # Remove item (waits if empty) | Important one. If queue is empty → thread WAITS.
q.empty()        # Check if empty
q.task_done()    # Signal completion
q.join()         # Wait until all tasks are done

"""

import queue

# Queues are useful to organize multiple running threads

# FIFO

q1 = queue.Queue()

numbers = [1, 2, 3, 4, 5]

for num in numbers:
    q1.put(num)

print(q1.get())
print(q1.get())
print("***************************")

#LIFO

q2 = queue.LifoQueue()

nums = [1, 2, 3, 4, 5]

for x in nums:
    q2.put(x)

print(q2.get())
print(q2.get())
print("***************************")

# Priority Queue - Every element gets a priortiy by passing a tuple

q3 = queue.PriorityQueue()

q3.put((1, "Hello World")) # 1 is High Prioriy (The lower the number the higher the priority)
q3.put((10, "Hi"))
q3.put((2, 5 + 2))
q3.put((5, True))

while not q3.empty(): # As long as theres elements in the queue, print the next element
    print(q3.get())