print("*******************************************")
greeting = "Hi, welcome to the Band Name Generator!"
print(greeting)
print("*******************************************")

city = input("What city do you live? \n").strip()
print("...........................................")
print("Ah ha, " + city + " is an awesome city." )
print("...........................................")

pet_name = input("What is your pet's name? \n").strip()
print("...........................................")
print("Ooo, " + pet_name + ". Such a cool name. ")
print("...........................................")

band_name = city + " " + pet_name

print("Your band name is..." + band_name.title() + "!")
print("...........................................")
print("Awesome band name! Hope you like it 👌")
print("...........................................")
