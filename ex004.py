# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ele.

var = input('Digite algo: ')

print('O tipo da variável é? ', type(var))
print('A variável é numérica? ', var.isnumeric())
print('A variável é alfabética? ', var.isalpha())
print('A variável é alfanumérica? ', var.isalnum())
print('A variável está maiúscilas?', var.isupper())
print('A variável está maiúscilas?', var.islower())
print('A variável está captalizada?', var.istitle())
