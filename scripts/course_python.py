#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
print ("Python version:", (sys.version), '\n')

# -------------------------------------------------------------------------------

# The internal attribute __name__, if it exists, returns the name of the object which is applied


class PersonDocumentation:
    """ 
        This is the class PersonDocumentation
    """
    # Method contructor

    def __init__(self, nome, account, ativo, apelido, sexo, email, endereco, foneCelular, dataNascimento):
        self.nome = nome
        self.account = account
        self.isActive = ativo
        self.apelido = apelido
        self.sexo = sexo
        self.email = email
        self.endereco = endereco
        self.foneCelular = foneCelular
        self.dataNascimento = dataNascimento


class PhysicalPerson(PersonDocumentation):
    """ 
        This is the class PhysicalPerson
    """
    # Method contructor

    def __init__(self, rg, cpf, nome):
        PersonDocumentation.__init__(self, nome, account=None, ativo=None, apelido=None, sexo=None,
                                     email=None, endereco=None, foneCelular=None, dataNascimento=None)
        self.rg = rg
        self.cpf = cpf


class Banks():
    """ 
        This is the class Bank documentation
    """

    # Method contructor
    def __init__(self):
        self.clients = []

    # Method to register new clients
    def registerClients(self, client):
        client.account = len(self.clients)+1
        self.clients.append(client)

    def printClientByCpf(self, cpf):
        for client in self.clients:
            if client.cpf == cpf:
                print("\nAccount: {0}".format(client.account))
                print("Nome: {0}".format(client.nome))
                print("Rg: {0}".format(client.rg))
                print("Cpf: {0}".format(client.cpf))
                print("Ativo: {0}".format(client.isActive))
                print("Apelido: {0}".format(client.apelido))
                print("Sexo: {0}".format(client.sexo))
                print("Email: {0}".format(client.email))
                print("Endereco: {0}".format(client.endereco))
                print("FoneCelular: {0}".format(client.foneCelular))
                print("DataNascimento: {0}\n".format(client.dataNascimento))

if __name__ == '__main__':

    bradesco = Banks()

    client_001 = PhysicalPerson("0458637844", "0338262876", "Jotelly Barros")
    client_001.email = "jotelly@gmail.com"
    bradesco.registerClients(client_001)
    
    client_002 = PhysicalPerson("84654ds655", "0215645458", "Jean Xavier")
    bradesco.registerClients(client_002)
    
    client_003 = PhysicalPerson("8451841543", "0875654650", "Lucas Marins")
    bradesco.registerClients(client_003)

    bradesco.printClientByCpf("0338262876")
    bradesco.printClientByCpf("0215645458")
    bradesco.printClientByCpf("0875654650")
