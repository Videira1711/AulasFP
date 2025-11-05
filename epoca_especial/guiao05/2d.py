def media():
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
    max=lista[0]
    min=lista[0]
    for i in lista:
        if i>max:
            max=i
        elif i<min:
            min=i
    media= (max + min)/2
    print("A média entre o max e o min é", media)
    c = 0
    for i in lista:
        if i < media:
            c += 1
    return c
print( media())