x = int(input("Quantos numeros voce vai digitar? "))
numeros = []
a = 0

for i in range(x):
    numero = int(input("Digite um numero: "))
    a = a + 1
    numeros.append(numero)
    if a == x:
        break

print("NUMEROS NEGATIVOS: ")
for n in numeros:
    if n < 0:
        print(n)