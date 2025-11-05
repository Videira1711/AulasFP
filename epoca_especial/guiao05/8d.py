def evenThenOdd():
    lista = []
    c=0
    while True:
        num=input("N? ")
        if num=="":
            break
        lista.append(int(num))
    for i in lista:
        if i>c:
            c=i
    return c


print(evenThenOdd())
    