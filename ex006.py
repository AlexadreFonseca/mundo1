#Faça um programa que leia um número inteiro e mostre na tela o dobro, triplo e raíz quadrada.

n = int(input('Digite um número:'))

print('O número digitado foi {}, seu dobro é {}, seu triplo é {}.'.format(n, n * 2, n * 3), end='')
print('E sua raíz quadrada é {}.'.format(n ** (1/2)))

