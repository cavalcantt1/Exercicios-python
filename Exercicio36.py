casa = float(input("Qual o valor da casa? "))
salario = float(input("Qual o seu salário? "))
anos = int(input("Em quantos anos você irá pagar? "))
prestacoes = anos * 12
parcela = casa / prestacoes

if parcela > salario * 0.30:
    print("Empréstimo não aprovado!")
else:
    print("Empréstimo aprovado!")