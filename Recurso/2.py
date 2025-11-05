def score(guess,secret):
    assert len(guess)==len(secret)
    bulls=0
    cows=0
    lv=[]
    for i,letra in enumerate(guess):
        if guess[i]==secret[i]:
            bulls+=1
            lv.append(letra)
    for i,letra in enumerate(guess):
        if letra in secret and letra not in lv:
            cows+=1
            lv.append(letra)
    return bulls, cows