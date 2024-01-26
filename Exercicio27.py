nome = str(input("digite seu nome completo: "))
n = nome.split()
cont = int(len(n))
prinome = n[0]
ultnome = n[cont-1]
print(f"primeiro nome {prinome}, ultimo nome {ultnome} ")
