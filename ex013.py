#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

s = float(input('Digite o valor do salário:'))

print('O novo valor com aumento de 15% é de R${:.2f}'.format(s * 1.15))