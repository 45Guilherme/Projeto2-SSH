
from collections import Counter  # Importa Counter, útil para contagem de elementos (não usado neste snippet, mas disponível para expansão)

# Criação do arquivo 'teste.log' com algumas linhas de exemplo
with open('teste.log', 'w') as arquivo:
    arquivo.write('Linha A\n')
    arquivo.write('Linha B\n')
    arquivo.write('Linha C\n')
    arquivo.write('Linha D\n')
    arquivo.write('Linha E\n')

# Abre o arquivo em modo leitura
with open('teste.log', 'r') as arquivo:
    conteudo = arquivo.readlines()  # Lê todas as linhas do arquivo e retorna uma lista
    
    # Percorre cada linha junto com seu índice usando enumerate
    for numero_linha, linha in enumerate(conteudo):
        # Verifica se a linha contém a letra 'C' (maiúscula ou minúscula)
        if "C" in linha or "c" in linha:
            # Exibe o número da linha (começando em 1) e o conteúdo da linha sem quebras
            print(f"{numero_linha + 1}: {linha.strip()}")


