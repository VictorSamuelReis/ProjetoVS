def verificarVogal(c):
    vogal = "aeiou"
    if(c in vogal):
        return True
    else: 
        return False

def contarVoagais(contador):
    contador = contador.lower()
    soma = 0
    for c in contador:
        if(verificarVogal(c)==True):
            soma+=1
    print(soma)
    return soma

    
vogais = input("Insira uma palavra: ")
vogal = contarVoagais(vogais)