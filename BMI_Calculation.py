peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imcf = float(peso / (altura ** 2))
imc = f"{imcf:.2f}"
print(f"Seu IMC é {imc}")