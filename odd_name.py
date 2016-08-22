"""
Ramisa
"""

name = str(input("Please enter your name"
                 "\n> "))
while name == "":
    print("Invalid input!")
    name = str(input("Please enter your name"
                     "\n> "))
print(name[::2])