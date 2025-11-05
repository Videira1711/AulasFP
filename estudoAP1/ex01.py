#Função para verificar se um número é primo
def isprime(n):
    if n<0 :
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

#Função para verificar se um número é par ou ímpar 
def oddOrEven(n):
    if n%2!=0:
        return 'Ímpar'
    return 'Par'

def main():
    #Verifica se a função isprime está a funcionar corretamente
    assert(isprime(2) == True)
    assert(isprime(9) == False)
    assert(isprime(17) == True)
    assert(isprime(-5) == False)
    print("All tests passed!")

    #Verifica se a função oddOrEven está a funcionar corretamente
    assert(oddOrEven(5) == "Ímpar")
    assert(oddOrEven(12) == "Par")
    assert(oddOrEven(18) == "Par")
    assert(oddOrEven(23) == "Ímpar")
    print("All tests passed!")

if __name__ == "__main__":
    main()
