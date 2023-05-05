'''
Exercício 010
Gustavo Guanabara - Estudonauta
by Marcelo Paulino
Programa que converta moeda: real para dólar
Autor: Marcelo Paulino********************************************************************************************
'''

R = float(input('Digite o valor em real psrs ser convertido em dólar R$ '))
C = float(input('Digite o valor do câmbio para dólar hoje US '))
Vdólar = R / C

print('Você tem R$ {:.2f} reais e em dólar é US {:.2f}'.format(R, Vdólar))


