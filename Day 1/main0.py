# Day 1 - New Name Generator
# Working with Variables in Python to Manage Data

print("Welcome to the Name Generator.")
pet = input("What's your pet's name?\n").strip()
street = input("What's name of the street you grew up in?\t").strip()
city = input("Enter the city you like : ").strip()
#print("Your band name could be " + street + " " + pet)
print('Your new name could be {1} {2} {0} {1}'.format(street ,pet ,city))
#print(f'Your band name could be {street} {city} {city} {pet}')

errors = """ Types of Errors : 
Syntax Error 
Type Error
Value Error
"""
print(errors)
