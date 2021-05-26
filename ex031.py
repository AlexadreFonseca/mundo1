#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$ 0,50 por Km
# para viagens de até 200 km, e R$ 0,45 para viagens mais longas

distancia = int(input('Qual a distância da viagem em km: '))
'''if dist <= 200:
    custo = dist * 0.50
else:
    custo = dist * 0.45'''
custo = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('O valor da viagem será R${:.2f}'.format(custo))
