#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
print ("Python version:", (sys.version), '\n')

# -------------------------------------------------------------------------------
# Data entry using input

dict_data = {
    "JOTELLY": "250e87",
    "ANA": "123456",
    "FABIO": "34050",
    "MARINS": "bobagem123",
    "LUAN": "must25"
}

# Calling a Function search_user_name
def search_user_name(user, password):
    # search name value and password value in dict_data
    for x in dict_data:
        if user in x:
            # print("{user_name}!".format(user_name=x))
            if(dict_data[x] == password):
                return True
    return False

while (1):
    # Takes input name user
    my_name = str(raw_input('Insert your name: '))

    # Takes input name user
    my_passwords = str(raw_input('Insert your passwords: '))

    if search_user_name(my_name.upper(), my_passwords):
        print("Welcome {0}".format(my_name))
    else:
        print("{0} you have an access denied \n\n".format(my_name))