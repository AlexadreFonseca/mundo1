# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude
# ele, lendo o nome deles e escrevendo o nome do escolhido
import random

a1 = input('Qual o nome do primeiro aluno:')
a2 = input('Qual o nome do segundo aluno:')
a3 = input('Qual o nome do terceiro aluno:')
a4 = input('Qual o nome do quarto aluno:')

list = [a1, a2, a3, a4]

sorteado = random.choice(list)

print('O aluno sorteado para apagar o quadro foi {}!'.format(sorteado))
