'''
Exercício 004
Gustavo Guanabara - Estudonauta
by Marcelo Paulino
Programa que leia algo pelo teclado e mostre na tela seu tipo primiivo e todas as informações possíveis sobre ele.
Autor: Marcelo Paulino********************************************************************************************
'''

print('Atividade 004')
print('***************************************************************************************************************')


a = input('Digite algo: ') # Nesse formato - input - sempre será 'str'
print('O tipo primitivo desse valor é ', type(a))
print('Só tem espaços? ', a.isspace()) # verifica se é apenas espaço
print('É um número? ', a.isnumeric())  # verifica se é numérico
print('É alfabético? ', a.isalpha())  # verifica se é alfabético
print('É alfanumérico? ', a.isalnum())  # verifica se é numérico
print('É CAIXA ALTA? ', a.isupper())  # verifica se é MAIÚSCULA
print('É CAIXA baixa? ', a.islower())  # verifica se é minúscula
print('É capitalizada? ', a.istitle())  # verifica se é parte maiúscula e parte minúscula
# neste caso o a é o objeto








print('***************************************************************************************************************')

