#Crie um programa que leia o nome da pessoa e diga se tem 'Silva' no nome.

name = input('Digite seu nome:').strip()
print('O nome {} tem \'Silva\'? {}'.format(name, 'silva' in name.lower()))
