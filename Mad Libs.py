print("Hello world")
"""
This program generates passages that are generated in mad-lib format
Author: Mark Carey 
"""

# The template for the story

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world."

print ("Mad Libs is starting!")
name = input("Enter a name: ")
adjective_1 = input("Provide an adjective: ")
adjective_2 = input("Provide a second adjective: ")
adjective_3 = input("Provide one more adjective: ")
verb = input("Now give us a verb: ")
noun_1 = input("Provide a first noun: ")
noun_2 = input("And now a second noun: ")
animal = input("Name an animal: ")
food = input("Name a food: ")
fruit = input("Name a fruit: ")
superhero = input("Pick a superhero: ")
country = input("Name a country: ")
dessert = input("Name a dessert: ")
year = input("Finally, pick a year: ")

print ()
print (STORY % (name, adjective_1, adjective_2, animal, food, verb, noun_1, fruit, adjective_3, name, superhero, name, country, name, dessert, name, year, noun_2))

