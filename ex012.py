#Faça um algotitmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

p = float(input('Qual o valor do produto: R$'))

print('Com desconto de 5% o produto custará R${:.2f}.'.format(p * 0.95))
