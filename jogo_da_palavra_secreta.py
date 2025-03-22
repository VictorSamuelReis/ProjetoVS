import os

palavra_secreta = "python"
tentativas = 0
letras_acertadas = ''

while True:
    letra = input("Digite uma letra: ")
    qta_letras = len(letra)
    tentativas += 1
    
    if qta_letras > 1:
        print("Digite apenas uma letra")
        continue
    
    if letra in palavra_secreta:
        letras_acertadas += letra
    
    palavra_formada = ''
    for i in palavra_secreta:
        if i in letras_acertadas:
            palavra_formada += i
        else:
            palavra_formada += "*"
            
    print(palavra_formada)
    if palavra_formada == palavra_secreta:
        os.system('cls')
        print(f"Você acertou a palavra secreta '{palavra_secreta}' em {tentativas} tentativas")
        palavra_secreta = "python"
        tentativas = 0
        letras_acertadas = ''
    
