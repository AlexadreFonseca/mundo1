#Faço um programa que leia a largura e a altura de uma parede em metros, calcule a sua área
#e a quantidade de tinta necessária para pintá-la, sabendo que  cada litro de tinta pinta uma área de 2m²

l = float(input('Digite a largura da parede: '))
a = float(input('Digite a altura da parede:'))

t = (l * a) / 2
print('A área da parede é {}m².'.format((l * a)))
print('Precisa de {:.2f} litro(s) de tinta para pintar toda a parede.'.format(t))
