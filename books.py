import xml.etree.ElementTree as ET

# Read XML
tree = ET.parse("Day 22/books.xml")
root = tree.getroot()
print(root)

# Print Book Elements
for book in root.findall("book"):
    print(book)

# Print Book Titles and Author
for book in root.findall("book"):

    title = book.find("title").text
    author = book.find("author").text

    print("-----BOOK-----")
    print("Title:", title)
    print("Author:", author)

# Add New Book 

title_input = input("Enter book title: ")
author_input = input("Enter author: ")

new_book = ET.SubElement(root, "book")

title = ET.SubElement(new_book, "title")
title.text = title_input

author = ET.SubElement(new_book, "author")
author.text = author_input

print("-----BOOK-----")
print("Title:", title_input)
print("Author:", author_input)

# Save Updated XML
tree.write("Day 22/books.xml")