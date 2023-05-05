'''
Exercício 006
Gustavo Guanabara - Estudonauta
by Marcelo Paulino
Programa que leia um número e mostre seu dobro, triplo e quadradoantecessor e sucessor de um número
Autor: Marcelo Paulino********************************************************************************************
'''

print('Atividade 006')
print('***************************************************************************************************************')

N1 = int(input('Digite um número inteiro: '))

D = N1 * 2
T = N1 * 3
R = N1 ** (1/2) # Raíz quadrada é número elevado a dois, dividido por 1/2

print(' Você digitou {}.\n Seu dobro é {}.\n Seu triplo é {} .\n Sua raíz quadrada é {:.2f}' . format(N1,D, T, R)) # :.2f número casa decimal

# Outro formato possível abaixo
#print(' Você digitou {}.\n Seu dobro é {}.\n Seu triplo é {} .\n Sua raíz quadrada é {:.2f}' . format(N1, (N1 * 2), N1, (N1 * 3), N1, (N1 **(1/2)))) # :.2f número casa decimal


# R2 = pow(N1, (1/2)) outra forma de raíz quadrada
