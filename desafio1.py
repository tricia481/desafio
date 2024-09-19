import os

def menu():
    print(30*'-',  ' MENU ',  30*'*')
    print("1. Adicionar produto")
    print("2. Atualizar quantidade de produto")
    print("3. Listar todos")
    print("4. Calcular valor total")
    print("5. Sair")
    print(66*"*")
produtos = []

def adicionar(l, n, q, p):
    l.append(n)
    l.append(q)
    l.append(p)

def atualizar(n, nq):
    for d in produtos:
        if d[0] == n:
            d[1] = nq
            print(d)

os.system("cls")

while True:
    menu()
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        novoprod = []
        prodnome = input("NOME DO PRODUTO: ")
        quantidade = int(input("QUANTIDADE: "))
        preco = float(input("PREÇO: "))
        adicionar(novoprod, prodnome, quantidade, preco)
        produtos.append(novoprod)
        print(f"{quantidade} de {prodnome} por R${preco:.2f} adicionado com sucesso.")
    if opcao == 2:
        nome = input("NOME DO PRODUTO: ")
        novaquant = input("NOVA QUANTIDADE: ")
        atualizar(nome, novaquant)
    if opcao == 3:
        for p in produtos:
            print("Nome:" , str(p[0]) , "| Quantidade:" , str(p[1]) , "| Preço:" , str(p[2]))
    if opcao == 4:
        somaq = 0
        somap = 0 
        for d in produtos:
            e = d[1]
            f = d[2]
            somaq += e
            somap += f
            multi = somaq * somap
        print(f"Valor total do estoque: R${multi:.2f}")
    if opcao == 5:
        print("Saindo...")
        break