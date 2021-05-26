#Escreva um programa que leia um valor em metros e exiba convertido em centímetros e milímetros
n = float(input('Digite um valor em metros: '))

print('A valor corresponde à {:.2f} cm, ou {:.2f}mm'.format(n * 100, n * 1000))
