def upper():
    lista = []
    maiusculas=[]
    frase = input("Digite a sua frase:  ")
    for i in frase:
        lista.append(i)
    for j in lista:
        if j.isupper():
            maiusculas.append(j)
    palavra = ''.join(maiusculas)
    return palavra


print(upper())

