#Faça um programa que leia uma frase pelo teclado e mostre:
#-Quantas vezes aparece a letra 'A'
#-Em que posição ela aparece pela primeira vez
#-Em que posição ela aparece pela última vez

frase = input('Digite uma frase:').strip()
print('A frase contém {} letras \'a\''.format(frase.lower().count('a')))
print('Sua primeira ocorrência é na posição {}'.format(frase.lower().find('a') + 1)) #Considerando a leitura da frase
print('E sua última ocorrência é na posição {}'.format(frase.lower().rfind('a') + 1))
