"""
Aplicativos Simples para Aprender Python
App 02
Joguinho de Adivinhação
Conceitos: #if/else, #inteiros, #tipos,
#random, #numeros, #comparacao,
#python-em-pt-br
Autor: Bruno Calheira
"""
import random

print("-"*20)
print("Adivinhe o Número!")
print("-"*20)
print()

numero = random.randint(0,100)

numero_chute = -3

while(numero_chute != numero):
    chute = input("Chute um número de 0 a 100: ")

    numero_chute = int(chute)

    if (numero_chute == numero):
        print("Você acertou!")
    elif (numero_chute < numero):
        print("Você errou! Chute mais alto.")
    else:
        print("Você errou! Chute mais baixo.")


