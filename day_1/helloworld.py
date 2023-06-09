# Day 1: Exercise: Level 2

# Import libraries

import sys
import platform

print()
print('Day 1: Exercise: Level 2')
print()

# Step 1: Display Version of Python

print('Exercise: Level 2: Step 1:')
print('The installed version of Python is',sys.version)
print()

# Step 2: Mathematical Operations

print('Exercise: Level 2: Step 2:')
print(3+4)  # Addition
print(3-4)  # Subtraction
print(3*4)  # Multiplication
print(3%4)  # Modulus
print(3/4)  # Division
print(3**4) # Exponential
print(3//4) # Floor Division
print()

# Step 3: String Operations

print('Exercise: Level 2: Step 3:')
print('Tom')                             # First Name
print('Dean')                            # Family Name
print('United States of America')        # Country
print('I am enjoying 30 days of Python') # Sentence
print()

# Step 4: Data Types

print('Exercise: Level 2: Step 4:')
print(type(10))                                # Integer
print(type(9.8))                               # Float
print(type(3.14))                              # Float
print(type(4 - 4j))                            # Complex
print(type(['Asabeneh', 'Python', 'Finland'])) # List
print(type('Tom'))                             # String
print(type('Dean'))                            # String
print(type('United States of America'))        # String
print()

# Day 1: Exercise: Level 3

# Import libraries

import math

print()
print('Day 1: Exercise: Level 3')
print()

# Step 1: Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary

print('Exercise: Level 3: Step 1:')
print()
print('Number Types:')
print(type(52))     # Integer
print(type(4.11))   # Float
print(type(1 + 2j)) # Complex
print()
print('Other Data Types:')
print()
print('String')
print(type('This is a string.')) # String
print()
print ('Boolean')
print(type(False)) # Boolean
print()
print('List')
print(type(['Tom', 'Dean', 'United States of America'])) # List
print()
print('Tuple')
print(type((5, 6, 7))) # Tuple
print()
print('Set')
print(type({8, 9, 10})) # Set
print()
print('Dictionary')
print(type({
    'firstname': 'Tom',
    'lastname': 'Dean',
    'country': 'United States of America'
    })) # Dictionary
print()

# Step 2: Find an Euclidian distance between (2, 3) and (10, 8)

print('Exercise: Level 3: Step 2:')
print()
print(math.sqrt(((2-10)**2)+((3-8)**2)))