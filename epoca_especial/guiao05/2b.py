def countLower(lst, v):
    lst=[]
    while True:
        v = float(input("Introduza o valor de v: "))
        entrada = input("Introduza um número (ou ENTER para terminar): ")
        if entrada == "":
            break
        try:
            numero = float(entrada)
            lst.append(numero)
        except ValueError:
            print("Entrada inválida. Por favor, introduza um número válido.")
    lst.sort()
    c = 0
    for i in lst:
        if i < v:
            c += 1
    return c
print(countLower([], 0))