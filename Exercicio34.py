salario = float(input("Qual valor do seu salário? "))
aumento = salario + (salario * 0.10)

if salario <= 1250:
    aumento = salario +(salario * 0.15)
    print(f"seu salário reajustado é {aumento}")
    
else:
    print(f"Seu salario reajustado por 10%: {aumento}")

