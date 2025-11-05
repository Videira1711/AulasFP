def matches():
    allMatches= []
    while True:
        clubes = input("Escolha um clube  ")
        if clubes =="":
            break
        allMatches.append(clubes)
    jogos = []
    for i in range(len(allMatches)):
        for j in range(len(allMatches)):
            if i != j:
                jogos.append((allMatches[i], allMatches[j]))
    return jogos
print (matches())