cidade = str(input("digite o nome da cidade")).lower

if any (x in cidade for x in ["joao", "lucas", "mateus", "santo", "são"]):
    print("Essa cidade tem nome religioso")
    
else:
    print("Essa cidade não tem nome religioso")


