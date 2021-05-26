#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#Considerando US$1,00 = R$5,37 (cotação 21.05.2021)

n = float(input('Quantos Reais tem na carteira?'))

dol = n / 5.37

print('É possível comprar US${:.2f}'.format(dol))
