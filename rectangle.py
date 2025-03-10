import math
base = float(input("Base do retangulo: "))
altura = float(input("Altura do retangulo: "))


def calculo(base, altura):
    area = base * altura
    areaA = round(area, 4)
    print(f"Area: {areaA:.4f}")

    perimetro = 2 * base + 2 * altura
    perimetroA = round(perimetro, 4)
    print(f"Perimetro: {perimetroA:.4f}")

    diagonal = math.sqrt(base **2 + altura ** 2)
    diagonalA = round(diagonal, 4)
    print(f"Diagonal: {diagonalA:.4f}")

resultado = calculo(base, altura)