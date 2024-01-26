numero = int(input("Digite um número para conversão: "))
opcoes = int(input(" Digite 1 para binario, 2 para octal e 3 para hexadecimal "))

if opcoes == 1:
    resultado = bin(numero)
    print(f"Resultado: {resultado}")
elif opcoes == 2:
    resultado = oct(numero)
    print(f"Resultado: {resultado} ")
else:
    resultado = hex(numero)
    print(f"Resultado: {resultado} ")

