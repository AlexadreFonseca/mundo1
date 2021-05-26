#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e último nome separadamente.
name = input('Digite seu nome completo:').strip()
list = name.split()
print('Seu primeiro nome é {}, e o último é {}'.format(list[0], list[len(list) - 1]))
