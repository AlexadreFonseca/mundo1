#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle
a1 = input('Qual o nome do primeiro aluno:')
a2 = input('Qual o nome do segundo aluno:')
a3 = input('Qual o nome do terceiro aluno:')
a4 = input('Qual o nome do quarto aluno:')

list = [a1, a2, a3, a4]
shuffle(list)

print('A ordem de apresentação será:')
print(list)