def palavras():
    string=input("Qual é a palavra?  ")
    lista=[]
    c=0
    for i in string:
        lista.append(i)
    for c in range(len(lista) - 1):
        if lista[c] == lista[c + 1]:
            lista.pop()
    return lista

print(palavras())