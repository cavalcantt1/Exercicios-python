nota1 = float(input("insira sua primeira nota "))
nota2 = float(input("insira sua segunda nota "))
media = float((nota1 + nota2) / 2)
print(f"Sua nota é :{(nota1 + nota2) / 2}")

if media < 7:
    print("Você foi reprovado")

else:
    print("Você foi aprovado")
