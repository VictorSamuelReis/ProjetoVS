while True:
    numero = int(input("Digite um número: "))
    
    valores = [numero]
    resultado = 1 
    for i in range(1,numero):
        valores.append(int(i))

    for a in valores:
        resultado *= a

    print(f"O fatorial do número é {resultado}")
    
    