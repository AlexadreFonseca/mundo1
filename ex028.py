#Escrever um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O computador deverá escrever na tela se o usuário venceu ou perdeu

from random import randint

print('O computador está sorteando um número...')
num = int(input('Tente acertar, digite um número de 0 a 5:'))
pcNum = randint(0, 5)
if num == pcNum:
    print('Parabéns!!! O número sorteado foi {}, você acertou!!'.format(pcNum))
else:
    print('Infelizmente você errou, o número sorteado foi {}'.format(pcNum))




