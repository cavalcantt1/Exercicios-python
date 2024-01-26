velocar = float(input("Qual foi a velocidade do carro? "))
multa = (velocar - 80) * 7

if velocar > 80 :
    print(f"Você foi multado! valor da multa: R${multa}")
else:
    print("bom!Continue dirigindo com cuidado!")
    