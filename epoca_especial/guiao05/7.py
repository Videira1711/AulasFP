def ispalindrome():
    string = input("Qual é a palavra? ")
    return string == string[::-1]
print(ispalindrome())