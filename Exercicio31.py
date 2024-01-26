distancia = int(input("Qual a distancia da viagem? "))
passagem = distancia * 0.50

if distancia > 200 :
    passagem = distancia * 0.45
    print(f"Você vai gastar {passagem}")
else:
    print(f"Você vai gastar: {passagem}")