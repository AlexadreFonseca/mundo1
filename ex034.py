#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$ 1.250,00, calcule um aumento de 10%
#Para os inferiores ou iguais, o aumento é de 15%

salario = float(input('Digite o valor do salário: R$'))
if salario > 1250:
    print('Com aumento de 10%, o novo salário será R${:.2f}'.format(salario * 1.1))
else:
    print('Com aumento de 15%, o novo salário será R${:.2f}'.format(salario * 1.15))
