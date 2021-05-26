#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$ 7,00 por cada km/h acima do limete.

velocity = int(input('Digite a velicidade do carro: '))
if velocity <= 80:
    print('Está dentro do limite de 80km/h')
else:
    bill = (velocity - 80) * 7
    print('O carro excedeu a velocidade permitida, a multa custa R${:.2f}'.format(bill))
