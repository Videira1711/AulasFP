A=0
B=0
N=0
while True:
    v=input('voyo?')
    if v=='End':break
    elif v=='A':
        A+=1
    elif v=='B':
        B+=1
    else:
        N+=1
Af=(A/(A+B))*100
Bf=(B/(A+B))*100
print(f"Nulos:{N}")
print(f"A:{Af:.1f}%")
print(f"B:{Bf:.1f}%")