#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
angle = float(input('Digite um ângulo:'))
seno = math.sin(math.radians(angle))
cosseno = math.cos(math.radians(angle))
tangente = math.tan(math.radians(angle))
print('Para o ângulo {}, o seno é {:.2f}, o cosseno é {:.2f}, e a tangente é {:.2f}'.format(angle, seno,
                                                                                            cosseno, tangente))
