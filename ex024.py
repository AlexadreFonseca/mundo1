#Crie um programa que leia o nome de uma cidade e diga se começa ou não com o nome 'Santo'
city = input('Qual o nome da sua cidade?').strip()
print('A cidade {} começa com a palavra \'Santo\'? {}'.format(city, city.lower().startswith('santo')))
