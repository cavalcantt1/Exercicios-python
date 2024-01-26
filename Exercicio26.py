frase = str(input("digite a frase ")).lower()
repeticao = frase.count("a")

print(f"a letra 'a' aparece {repeticao} no texto")
print(f"a letra a aparece pela primeira vez {frase.find('a')} e a ultima {frase.rfind('a')}")

