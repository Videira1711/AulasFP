def minmax():
    lista=[]
    while True:
        entrada= input("Digite um numero:")
        if entrada == "":
            break
        try:
            numero= float(entrada)
            lista.append(numero)
        except ValueError:
            print("Nao aceite este caracter")
    if lista==[]:
        print("(0.0,0.0)")
    else:
        max=lista[0]
        min=lista[0]
        for i in lista:
            if i>max:
                max=i
            elif i<min:
                min=i
        return max, min
print (minmax())