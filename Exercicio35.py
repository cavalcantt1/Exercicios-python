reta1 = float(input("Digite o primeiro valor: ")) 
reta2 = float(input("Digite o segundo valor: "))
reta3 = float(input("Digite o terceiro valor: "))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
     print("As retas podem formar um triangulo.")
else:
    print("As retas não podem formar um triângulo.")
 