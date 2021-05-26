#Desenvolva um programa que leia o comprimento de trÊs retas e diga ao usuário se elas podem ou não formar um triângulo
r1 = int(input('Digite o valor da reta 1: '))
r2 = int(input('Digite o valor da reta 2: '))
r3 = int(input('Digite o valor da reta 3: '))

if (r1 < r2 + r3) and (r2 < r1 + r3) and (r3 < r1 + r2):
    print('As retas formam um triângulo!!')
else:
    print('As retas não formam um triângulo.')
