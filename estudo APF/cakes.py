receita={}
while True:
    i = input('Ingrediente? ')
    if i =='': break
    qtd = input('Quantidade? ')
    receita[i] = int(qtd)

print('Agora o que tens')
ingredientes={}
while True:
    i = input('Ingrediente? ')
    if i =='': break
    qtd = input('Quantidade? ')
    ingredientes[i] = int(qtd)
    
lst = []
for i in receita:
    nvezes=ingredientes[i]//receita[i]
    lst.append(nvezes)

nfinal=min(lst)
print(nfinal)