while True:
    numero = int(input("Digite um número (digite 'fim' para encerrar): "))
    primo = 1

    for a in range(2,numero):
        if(numero % a == 0):
            primo = 0
        
    if(primo == 1):
            print("Este número é primo")
    else: 
            print("Este número não é primo")
