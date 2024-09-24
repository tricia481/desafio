# Dicionário para armazenar os usuários
usuarios = {}

# Função para cadastrar um novo usuário
def cadastrar_usuario():
    email = input("Digite o e-mail do usuário: ")
    
    if email in usuarios:
        print("E-mail já cadastrado.")
    else:
        nome = input("Digite o nome do usuário: ")
        senha = input("Digite a senha: ")
        usuarios[email] = {'nome': nome, 'senha': senha}
        print(f"Usuário {nome} cadastrado com sucesso.")

# Função para listar todos os usuários cadastrados
def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        print("\nUsuários cadastrados:")
        for email, dados in usuarios.items():
            print(f"E-mail: {email} | Nome: {dados['nome']}")

# Função para autenticar um usuário
def autenticar_usuario():
    email = input("Digite o e-mail: ")
    senha = input("Digite a senha: ")
    
    if email in usuarios and usuarios[email]['senha'] == senha:
        print(f"Bem-vindo, {usuarios[email]['nome']}!")
    else:
        print("E-mail ou senha incorretos.")

# Menu principal
def menu():
    while True:
        print("\nSistema de Cadastro de Usuários:")
        print("1. Cadastrar usuário")
        print("2. Listar usuários")
        print("3. Autenticar usuário")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar_usuario()
        elif opcao == '2':
            listar_usuarios()
        elif opcao == '3':
            autenticar_usuario()
        elif opcao == '4':
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Iniciar o programa
if _name_ == "_main_":
    menu()

