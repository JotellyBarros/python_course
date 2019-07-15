#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

print ("Python version:", (sys.version), '\n')

# Recommended typing.
my_nome = 'Jótelly Barros'
idade = 32

print ("{0} do tipo {tipo}".format(my_nome, tipo = type(my_nome)))
print (str(idade)[0])

print (my_nome[:5])
print (my_nome[5:])
print (my_nome[0:3])

# palindromo test
palindromo = 'socorram me subi no onibus em marrocos'
print (palindromo[::-1])