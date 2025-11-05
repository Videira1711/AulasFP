def soma(arquivo):
    soma=0
    with open(arquivo,'w') as file:
        file.write('9\n')
        file.write('1\n')
        file.write('2\n')
        file.write('8\n')
    with open(arquivo,'a') as file:
        file.write('9')
    with open (arquivo,'r') as file:
        for i in file:
            n=float(i)
            soma+=n
    return soma
arquivo='numeros.txt'
resultado=soma(arquivo)
print(resultado)