import os


mensagens = []

nome = input("Nome: ")

while True: 

    #limpa o terminal
    os.system('cls')

    if len(mensagens) >0:
        for m in mensagens:
            print(m['nome'], "-", m['texto'])
    

    print("______________________")
    
    #obtem o texto
    texto = input("mensagens: ")
    if texto == "fim":
        break

    # adiciona o nome e o texto na lista
    mensagens.append({
        "nome": nome,
        "texto": texto,
    })

