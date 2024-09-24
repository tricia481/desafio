# Dicionário para armazenar nome e média dos alunos
alunos = {}

# Cadastro de 5 alunos
for i in range(5):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    nota1 = float(input("Digite a 1ª nota: "))
    nota2 = float(input("Digite a 2ª nota: "))
    nota3 = float(input("Digite a 3ª nota: "))
    
    # Calcula a média
    media = (nota1 + nota2 + nota3) / 3
    
    # Armazena o nome e a média no dicionário
    alunos[nome] = media

# Exibe o nome e a média de cada aluno
print("\nMédia dos alunos:")
for nome, media in alunos.items():
    print(f"{nome}: {media:.2f}")
