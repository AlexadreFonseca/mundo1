#Crie um programa que leia o nome completo de uma pessoa e mostre:
#-O nome com todas as letras maiúsculas
#-O nome com todas as letras minúsculas
#-Quantas letras no total, sem considerar espaços
#-Quantas letras tem o primeiro nome

name = input('Digite seu nome completo:').strip()

listName = name.split()
print('O nome digitado foi {}'.format(name))
print('Em maiúsculo:{}. \nEm minúsculo: {}'.format(name.upper(),name.lower()))
print('O total de letras são {}.\nO primeiro nome tem {} letras.'.format(len(name) - name.count(' '),len(listName[0])))

