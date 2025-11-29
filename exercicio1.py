
# Criação do arquivo 'teste.log' com algumas linhas de exemplo
with open('teste.log', 'w') as arquivo:
    arquivo.write('Linha A\n')
    arquivo.write('Linha B\n')
    arquivo.write('Linha C\n')
    arquivo.write('Linha D\n')
    arquivo.write('Linha E\n')

# Abre o arquivo em modo leitura
with open('teste.log', 'r') as arquivo:
    conteudo = arquivo.readlines()  # Lê todas as linhas e retorna uma lista de strings

# Percorre as linhas pelo índice usando range
for linha in range(len(conteudo)):
    # Exibe o número da linha (começando em 1) e o conteúdo sem quebras de linha
    print(f"{linha + 1}: {conteudo[linha].strip()}")

       

 



