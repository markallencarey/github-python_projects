"""
Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:
Add on to the previous program by asking the user for another number and 
printing out that many copies of the previous message. 
(Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. 
(Hint: the string "\n is the same as pressing the ENTER button)
"""

# print("Hello World!")

name = input("Give me your name: ")
age = int(input("Now give me your age: "))
age = age + 100
age_statement = f"Your age in 100 years will be {age}."

copies = int(input("And now give me a random number: "))

while copies > 0:
    print (age_statement)
    copies = copies - 1