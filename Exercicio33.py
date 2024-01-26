num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

if num1 >= num2 and num1 >= num3:
    print(f" O {num1} é o maior número!")

elif num2 >= num1 and num2 >= num3:
    print(f"O {num2} é o maior número!")

else:
    print(f"O {num3} é o maior!")
    
    
if num1 <= num2 and num1 <= num3:
    print(f" O {num1} é o menor número!")

elif num2 <= num1 and num2 <= num3:
    print(f"O {num2} é o menor número!")

else:
    print(f"O {num3} é o menor!")





