# STRING FUNCTIONS 

# 1. Changing Case
text = "Kill Switch"

print(text.upper())      # All uppercase
print(text.lower())      # All lowercase
print(text.title())      # Title
print(text.capitalize()) # Capitalizes first word


# 2. Stripping Spaces
text = "   hello   "

print(text.strip())   # Removes both sides
print(text.lstrip())  # Left only
print(text.rstrip())  # Right only


# 3. Finding Things
text = "Python is powerful"

print(text.find("is"))     # Find Funcion | Returns index (7)
print(text.index("is"))    # Same but errors if not found
print("Python" in text)    # True


# 4. Replacing Text
text = "I love Java"

new_text = text.replace("Java", "Python")
print(new_text)
# Original string doesn't change


# 5. Splitting Strings
# Turn sring into a list:
text = "apple,banana,grape"

fruits = text.split(",") # Define seperator ",", " ", "/" etc.
print(fruits)
# Commom when parsing user input


# 6. Joining Strings
# Turn list into string:
words = ["Python", "is", "elite"]

sentence = " ".join(words) # Join Function
print(sentence)


# 7. Checking String Type
print("123".isdigit())   # True | Only numbers, no letters, no spaces
print("hello".isalpha()) # True | Only letters, no numbers, no spaces, no symbols
print("abc123".isalnum()) # True | Letters and/or numbers, no spaces, no symbols
print(" ".isspace())     # True | Only whitespace
# All these methods return False if the string is empy "" or theres even one invalid character \


# 8. String Length
len("Zenith")


# 9. f-Strings
name = "Zeen"
age = 22

print(f"My name is {name} and I am {age} years old.")
# Cleanest formatting style instead of concatenating strings 


# 10. String Slicing 
text2 = "Python"

print(text2[0])      # P
print(text2[-1])     # n
print(text2[0:3])    # Pyt | Start index at 0 but ends at 2, returns a substring from start up to end - 1
print(text2[:4])     # Pyth
print(text2[2:])     # thon
print(text2[::-1])   # nohtyP (reverse)


# 11. Escape Characters
text3 = "Hi, how are you? \nI'm great, thanks." # \n for line break or """", \t for tab, \b for backspace, \s for space 
print(text3)


# 12. Iterating Over a String 
for letter in text2:
    print(letter) # Processes individual characters in a string by iterating over them



# 13. Count Fucntion
text4 = "Hi, my name is Zeen. My pet's name is Xeno" 
print(text4.count("name")) # Counts how many times a substring is contained within a string


