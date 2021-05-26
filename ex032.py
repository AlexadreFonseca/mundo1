#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date
ano = int(input('Digite um ano para saber se é bissexto, caso digite 0 será analisado o ano atual: '))
if ano == 0:
    ano = date.today().year
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('O ano {} é bissexto'.format(ano))
else:
    print('O anor {} não é bissexto.'.format(ano))