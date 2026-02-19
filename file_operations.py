
""" How to Open a File
Whenever we want to do anything with a file in Python we need a file stream
"""

file = open("myfile.txt", 'r')  # Three modes: Reading, Writing and Appending 

file.close() # To end/close file stream when no longer using file 

with open("file.txt", 'r') as f: # You use a 'with' statement whenever you have to work with streams if you need to use it once.
    # ALL OF MY CODE
    pass

# Reading a file

with open('Day 11/file.txt', 'r') as f:
    content = f.read()
    pass

print(content)

# Without with statement

f = open('Day 11/file.txt', 'r')
content = f.read()
f.close()

# Using write method

with open('Day 11/file.txt', 'w') as f:
    content = f.write("Python is the best programming language + I love snakes!")

print(content)

# You can write and append into a file that does not exist, it creates the file. Yoyu can't read into a file that doesn't exist

# Exception Handling with streams

try: 
    # some stream code
    pass
except: 
    # catch
    pass
finally:
    # close
    pass

# Append onto files

with open('Day 11/file.txt', 'a') as f:
    content = f.write("\n...Mmmh Ball Pythons to be exact :)")

print(content)

# To read and write in the same file, use "r+"

with open('Day 11/file.txt', 'r+') as f:
    f.seek(0, 2) # Move cursor to the end before writing
    f.write("\nAdding this line without reopening!")
    f.seek(0) # Moves cursor back to the start to read everything
    content = f.read()

print(content)


# Other File Operations 
# rename file, remove files, change directories, remove directories etc

import os 

# or 

from os import * # For specifics from os import remove, rename etc

mkdir("test") # Creates directory
chdir("test") # Change directory 
mkdir("newdir")

rename("Day 11/file.txt", "ilovepy.txt") # Rename files
# remove("Day 11/file.txt", "ilovepy.txt") # Delete files