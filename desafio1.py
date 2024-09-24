inventario = {}

while True:
    opcao = input("\n1.Adicionar/Atualizar\n2.Listar\n3.Total\n4.Sair\nEscolha: ")
    if opcao == '1':
        nome = input("Produto: ")
        inventario[nome] = {'quantidade': int(input("Quantidade: ")), 'preco': float(input("Preço: "))}
    elif opcao == '2':
        for nome, dados in inventario.items():
            print(f"{nome}: {dados['quantidade']} unidades, R${dados['preco']:.2f}")
    elif opcao == '3':
        total = sum(d['quantidade'] * d['preco'] for d in inventario.values())
        print(f"Total em estoque: R${total:.2f}")
    elif opcao == '4':
        break