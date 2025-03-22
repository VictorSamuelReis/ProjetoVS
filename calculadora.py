# Descrição: Calculadora simples com 4 operações básicas

def escolha(primeiroN, segundoN, operacao):
    if operacao == "+":
        resultado = primeiroN + segundoN
        return resultado
    elif operacao == "-":
        resultado = primeiroN - segundoN
        return resultado
    elif operacao == "*":
        resultado = primeiroN * segundoN
        return resultado
    elif operacao == "/":
        resultado = primeiroN / segundoN
        return resultado
    else:
        return "Operacao invalida, tente novamente"
    

while True:
    primeiroN = float(input("Digite o primeiro numero: "))

    segundoN = float(input("Digite o segundo numero: "))
    operacao = input("Digite a operacao desejada: ")

    print(f'O resultado é {escolha(primeiroN, segundoN, operacao)}')
    continuar = input("Deseja continuar [s/n]? ")
    while (continuar != "n" and continuar != "s"):
        print("Resposta incorreta")
        continuar = input("Deseja continuar [s/n]? ")
        if continuar == "n" and continuar != "s":
            print("Resposta incorreta")
            break
        else:
            continue
    
    if continuar == "n":
        print("Obrigado por usar a calculadora")
        break