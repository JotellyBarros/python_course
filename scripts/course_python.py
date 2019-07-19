#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
print ("Python version:", (sys.version), '\n')

# -------------------------------------------------------------------------------
# Class Dogs


class Dogs():
    cover = 'Hair'
    food = 'Meat'
    paws = 4
    habitat = 'Domestic'
    name = 'Rex'

# The internal attribute __name__, if it exists, returns the name of the object which is applied
# print(Dogs.__name__)

# Techniques of introspections
# print(dir(Dogs))


Poodle = Dogs()
Poodle.name = 'Mel'
print(Poodle.name)

# ---------------------------------------------------------------


class Circulos:
    valor = 0

    def soma_Valores(self, novo_valor):
        self.soma = (novo_valor + self.valor)


Valor1 = Circulos()
Valor2 = Circulos()

Valor1.valor = 1
Valor2.valor = 2

# print(Valor1.valor)
# print(Valor2.valor)

Valor1.soma_Valores(5)
print(Valor1.soma)

Valor2.soma_Valores(5)
print(Valor2.soma)

# ---------------------------------------------------------------

class Bank:
    def __init__(self, name, account, cpf):
        self.name = name
        self.account = account
        self.cpf = cpf
    
    def print_Informations(self):
        print("Welcome: {name}".format(name = self.name))
        print("Account: {account}".format(account = self.account))
        print("Cpf: {cpf}".format(cpf = self.cpf))

client = Bank('Jotely Barros', '10031141', '03338262566')
client.print_Informations()
# print("Welcome: {name}\n account: {account}\n cpf: {cpf}".format(name = client.name, account = client.account, cpf = client.cpf))
