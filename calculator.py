while True:
    sinal = input("Escolha qual operação você deseja usar(se deseja encerrar, digite 'fim'): ")
    
    numeros = []
    numeros.clear
    if sinal != "soma": 
        resultado = 1
    else:
        resultado = 0 
    while True:

        if sinal != "soma" and sinal != "multiplicacao" and sinal != "multiplicação" and sinal != "divisao" and sinal != "divisão" and sinal != "subtracao" and sinal != "subtração" and sinal != "potencia" and sinal != "potência" and sinal != "resto" and sinal != "resto da divisao" and sinal != "resto divisao":
            resultado = 0
            break

        numero = input("insira o primeiro numero (caso esteja pronto para calcular, digite 'pronto'): ")
        if numero =="pronto":
            break
        numeros.append(int(numero))  # Converte o número para inteiro ao adicionar à lista
    
    for n in numeros:
        if sinal == "soma":
            resultado += n
        elif sinal == "multiplicacao" or sinal == "multiplicação":
            resultado *= n
        elif sinal == "divisao" or sinal == "divisão":
            resultado /= n
        elif sinal == "subtracao" or sinal == "subtração":
            resultado -= n
        elif sinal == "potencia" or sinal == "potência":
            resultado **= n
        elif sinal == "resto" or sinal == "resto da divisao" or sinal == "resto divisao":
            resultado %= n
    
    if sinal != "soma" and sinal != "multiplicacao" and sinal != "multiplicação" and sinal != "divisao" and sinal != "divisão" and sinal != "subtracao" and sinal != "subtração" and sinal != "potencia" and sinal != "potência" and sinal != "resto" and sinal != "resto da divisao" and sinal != "resto divisao":
            resultado = 0
            break
    else: 
        print(f"O resultado da {sinal} é: {resultado}")
    
    if sinal == "fim" or sinal == "Fim":
        resultado = 0
        break

