def evenThenOdd():
    string= input("Qual é a palavra?  ")
    lista=[]
    for i in string:
        lista.append(i)
    pares= "".join(lista[::2])
    impares="".join(lista[1::2])
    resultado= pares + impares
    return resultado
print(evenThenOdd())