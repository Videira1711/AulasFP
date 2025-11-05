def inputFloatList():
    lista = []
    while True:
        entrada = input("Introduza um número (ou ENTER para terminar): ")
        if entrada == "":
            break
        try:
            numero = float(entrada)
            lista.append(numero)
        except ValueError:
            print("Entrada inválida. Por favor, introduza um número válido.")
    lista.sort(reverse=True)
    return lista
print(inputFloatList())