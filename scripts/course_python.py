#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

print ("Python version:", (sys.version), '\n')

# -------------------------------------------------------------------------------
# Lists
my_list = ['Jotelly', 32, 'M', 1.84, "Solteiro"]  # List define "[]"
my_list[3] = 1.82  # new replacement value
# print(type(my_list))
# print(my_list[::])

print("\n{nome} : {idade} : {sexo} : {altura}".format(
    nome=my_list[0], idade=my_list[1], sexo=my_list[2], altura=my_list[3]))

# -------------------------------------------------------------------------------
# Tuples
my_tuple = ('Jotelly', 32)  # Tuple define "()"

# Not Recommended
# my_tuple[1] = 1.82 # new replacement value

print("\n{nome} : {idade}\n".format(
    nome=my_tuple[0], idade=my_tuple[1]))

# -------------------------------------------------------------------------------
# Dictionaries
print("\nDictionaries\n")
dict_cars = {
    "Brand": "Ford",
    "Color": "Black",
    "Model": "Mustang",
    "Year": 1964
}

print(dict_cars)
print(dict_cars.get("year"))

# -------------------------------------------------------------------------------
# Loop using "FOR" through a dictionary
print("\nLoop using 'FOR' through a dictionary\n")
for x in dict_cars:
    if "Brand" in dict_cars:
        print("{name} : {value}".format(
            name=x, value=dict_cars[x]))
    else:
        print("Don't exist!")

# Loop using "WHILE" through a dictionary
print("\nLoop using 'WHILE' through a dictionary\n")
num_1 = 0
num_2 = 200
cont = 10

while num_1 < num_2:
    num_1 += 1  # Python doesn't support (num_1 ++)
    print("{num_1:03d} ".format(num_1=num_1)),
    cont -=1
    if cont == 0: 
        cont = 10
        print('\n')
else:
    print("\n[ {num_2} < {num_1} ]".format(num_1=num_1, num_2=num_2))
