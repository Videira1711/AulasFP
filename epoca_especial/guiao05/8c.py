def numbers():
    n=int(input("n? "))
    resultado=[]
    for i in range(1, n + 1):
        resultado.extend([i] * i)
    lista_str = [str(x) for x in resultado]
    final= "".join(lista_str[::1])
    return final
print(numbers())        