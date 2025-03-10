largura = float(input("Digite a largura do terreno: "))
larguraA = round(largura, 1)
comprimento = float(input("Digite o comprimento do terreno: "))
comprimentoA = round(comprimento, 1)
preco = float(input("Digite o valor do metro quadrado: "))
precoA = round(preco, 2 )



def calculoArea(largura, comprimento, preco):
    area = float(largura * comprimento)
    areaA = round(area, 2)
    print(f"Area do terreno: {areaA:.2f}")

    valor = float(area * preco)
    valorA = round(valor, 2)
    print(f"Preco do terreno: {valor:.2f}")

resultado = calculoArea(largura, comprimento, preco)