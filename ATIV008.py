'''
Exercício 008
Gustavo Guanabara - Estudonauta
by Marcelo Paulino
Programa que faça conversor de medidas METRO para CENTÍMETRO E MIÍMETRO
Autor: Marcelo Paulino********************************************************************************************
'''

print('Atividade 008')
print('***************************************************************************************************************')

Medida =  float(input('Digite o valor da medida em metros: '))
CM = Medida * 100
MM = Medida * 1000

print('A medida de {:.1f} em metro corresponte a {:.1f} centímetros e {:.1f} milímetros '. format(Medida, CM, MM))





