with open('a.txt', encoding='UTF-8') as file:
    file.readline()
    while True:
        i = file.readline()
        if i == '': break
        if i == '\n': continue
        i = i.strip().split(',')
        i = [int(i[0]),i[1],float(i[2]),float(i[3]),float(i[4])]
        nome = i[1]
        valores = i[2:]
        total=0
        for val in valores:
            total+=val
        media=total/len(valores)
        print(nome,media)
