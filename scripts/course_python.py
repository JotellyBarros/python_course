#!/usr/bin/env python
import rospy
import sys

print(sys.version)

texto = 'Hello world!'
cidade = 'Salvador'
ano = 2019

print texto + ': ' + str(ano) + " OK."
print texto, ':', ano, ' OK'
print "Vivo em %s: %s: %i OK" %(cidade, texto, ano) # Similar ao C++
print 'Moro em {0}: {1}: {2} OK'.format(cidade, texto, ano) # Novo padrao

# ----------------------------------------------------------------

valor_1 = 5
valor_2 = 8
soma = valor_1 + valor_2

print 'O resultado da soma he {valor}'.format(valor=soma)

# ----------------------------------------------------------------

print 'Teste print'
print "Teste print"
print ('Teste print')
print ("Teste print")
print ('Teste print');
print ("Teste print");