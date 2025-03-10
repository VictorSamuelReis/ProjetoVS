from datetime import datetime
from typing import List, Dict, Optional

class Categoria:
    def __init__(self, id_categoria: int, nome: str):
        self.id_categoria = id_categoria
        self.nome = nome

class Produto:
    def __init__(self, id_produto: int, nome: str, categoria: Categoria, quantidade: int = 0):
        self.id_produto = id_produto
        self.nome = nome
        self.categoria = categoria
        self.quantidade = quantidade

class Movimentacao:
    def __init__(self, id_movimentacao: int, id_produto: int, tipo: str, quantidade: int, data: datetime):
        self.id_movimentacao = id_movimentacao
        self.id_produto = id_produto
        self.tipo = tipo  
        self.quantidade = quantidade
        self.data = data

categorias: Dict[int, Categoria] = {}
produtos: Dict[int, Produto] = {}
movimentacoes: List[Movimentacao] = []

def cadastrar_categoria():
    id_categoria = int(input("Digite o ID da categoria: "))
    nome = input("Digite o nome da categoria: ")
    categorias[id_categoria] = Categoria(id_categoria, nome)
    print(f"Categoria '{nome}' cadastrada com sucesso.")

def cadastrar_produto():
    produto = int(input("Digite o ID do produto: "))
    nome = input("Digite o nome do produto: ")
    id_categoria = int(input("Digite o ID da categoria do produto: "))
    quantidade_inicial = int(input("Digite a quantidade inicial do produto: "))
    
    if id_categoria in categorias:
        categoria = categorias[id_categoria]
        produtos[produto] = Produto(produto, nome, categoria, quantidade_inicial)
        print(f"Produto '{nome}' cadastrado com sucesso.")
    else:
        print("ID da categoria não encontrado. Cadastre a categoria antes de cadastrar o produto.")

def consultar_produto():
    id_produto = int(input("Digite o ID do produto para consulta: "))
    produto = produtos.get(id_produto, None)
    if produto:
        print(f"Produto: {produto.nome} | Categoria: {produto.categoria.nome} | Quantidade em estoque: {produto.quantidade}")
    else:
        print("Produto não encontrado.")

def consultar_categoria():
    id_categoria = int(input("Digite o ID da categoria para consulta: "))
    categoria = categorias.get(id_categoria, None)
    if categoria:
        print(f"Categoria: {categoria.nome}")
    else:
        print("Categoria não encontrada.")

def registrar_movimentacao():
    produto = int(input("Digite o ID do produto para movimentação: "))
    tipo = input("Digite o tipo de movimentação ('entrada' ou 'saida'): ").strip().lower()
    quantidade = int(input("Digite a quantidade: "))
    
    if produto not in produtos:
        print("Produto não encontrado.")
        return
    if tipo not in ['entrada', 'saida']:
        print("Tipo de movimentação inválido.")
        return
    
    produto = produtos[produto]
    
    if tipo == 'saida' and produto.quantidade < quantidade:
        print("Quantidade insuficiente em estoque.")
        return
    
    if tipo == 'entrada':
        produto.quantidade += quantidade
    elif tipo == 'saida':
        produto.quantidade -= quantidade

    id_movimentacao = len(movimentacoes) + 1
    movimentacao = Movimentacao(id_movimentacao, produto, tipo, quantidade, datetime.now())
    movimentacoes.append(movimentacao)
    print(f"Movimentação '{tipo}' de {quantidade} unidades registrada com sucesso para o produto '{produto.nome}'.")

def geraração_relatorio_produtos():
    for produto in produtos.values():
        print(f"ID: {produto.id_produto} | Nome: {produto.nome} | Categoria: {produto.categoria.nome} | Quantidade: {produto.quantidade}")

def geraração_relatorio_movimentacoes():
    for movimentacao in movimentacoes:
        produto = produtos.get(movimentacao.id_produto)
        if produto:
            print(f"Movimentação do ID: {movimentacao.id_movimentacao} | Produto: {produto.nome} | Tipo: {movimentacao.tipo} | Quantidade: {movimentacao.quantidade} | Data: {movimentacao.data}")
        else:
            print(f"Movimentação do ID: {movimentacao.id_movimentacao} | Produto removido | Tipo: {movimentacao.tipo} | Quantidade: {movimentacao.quantidade} | Data: {movimentacao.data}")

def menu():
    while True:
        print("\n1 - Cadastrar Categoria")
        print("2 - Cadastrar Produto")
        print("3 - Consultar Produto")
        print("4 - Consultar Categoria")
        print("5 - Registrar Movimentação")
        print("6 - Gerar Relatório de Produtos")
        print("7 - Gerar Relatório de Movimentações")
        print("8 - Sair")

        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '1':
            cadastrar_categoria()
        elif opcao == '2':
            cadastrar_produto()
        elif opcao == '3':
            consultar_produto()
        elif opcao == '4':
            consultar_categoria()
        elif opcao == '5':
            registrar_movimentacao()
        elif opcao == '6':
            geraração_relatorio_produtos()
        elif opcao == '7':
            geraração_relatorio_movimentacoes()
        elif opcao == '8':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente de novo escolhendo uma das opções acima.")

# Iniciar o menu
menu()
