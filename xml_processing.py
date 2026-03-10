# Extensible Markup Language 

# XML is used to store and transpprt structured data.
# It looks like HTML but is meant for data, not websites.

# ElementTree

import xml.etree.ElementTree as ET

# Parsing XML File

tree = ET.parse("Day 22/data.xml")
root = tree.getroot()

print(root)

# root is the top element(group)

# Loop Through Elements

# Get all <person> elements:
for person in root.findall("person"):
    print(person)

# Acess Child Elements

for person in root.findall("person"):

    name = person.find("name").text
    age = person.find("age").text
    weight = person.find("weight").text
    height = person.find("height").text

    print("-----PERSON-----")
    print("Name:", name)
    print("Age:", age)
    print("Weight:", weight)
    print("Height:", height)


# Access XML Attributes

person_id = person.get("id")
print(f"ID: {person_id}")

# Generating XML files

import xml.etree.ElementTree as ET

root = ET.Element("group")

person = ET.SubElement(root, "person", id="3")

name = ET.SubElement(person, "name")
name.text = "KHOLS"

age = ET.SubElement(person, "age")
age.text = "22"

tree = ET.ElementTree(root)
tree.write("data.xml")

# Editing XML 

for person in root.findall("person"):
    person.find("name").text = "Updated"

tree.write("data.xml")

# SAX

import xml.sax

class GroupHandler(xml.sax.ContentHandler):
    def startElement(self, name, attrs):
        self.current = name
        if self.current == "person":
            print("-----PERSON-----")
            print(f"ID: {attrs['id']}")

    def characters(self, content):
        if self.current == "name":
            self.name = content
        elif self.current == "age":
            self.age = content
        elif self.current == "weight":
            self.weight = content
        elif self.current == "height":
            self.height = content

    def endElement(self, name):
        if self.current == "name":
            print(f"Name is {self.name}")
        elif self.current == "age":
            print(f"Age is {self.age}")
        elif self.current == "weight":
            print(f"Weight is {self.weight}")
        elif self.current == "height":
            print(f"Height is {self.height}")       
        self.current = ""    

handler = GroupHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse("Day 22/data.xml")
