def countDigits():
    c=0
    texto= input("Qual a palavra?  ")
    lista_de_letras = []
    for i in texto:
        lista_de_letras.append(i)
    for i in lista_de_letras:
        if i.isdigit() == True:
            c+=1
    return c
print (countDigits())