import random

numero = int(input("Digite um número para ser sorteado"))
lista = [1, 2, 3, 4, 5]
sorteio = random.choice(lista)

if numero == sorteio:
    input("você ganhou!")
else:
    input(f"você perdeu!, o número escolhido é: {sorteio}")

