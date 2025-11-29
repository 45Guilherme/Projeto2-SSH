# Abre (ou cria) o arquivo 'dados.txt' no modo de escrita ('w')
# e garante que o arquivo será fechado automaticamente após o bloco
with open('dados.txt', 'w') as arquivo:
    # Escreve 11 linhas iguais no arquivo
    arquivo.write('Failed password: error\n')
    arquivo.write('Failed password: error\n')
    arquivo.write('Failed password: error\n')
    arquivo.write('Failed password: error\n')
    arquivo.write('Failed password: error\n')
    arquivo.write('Failed password: error\n')
    arquivo.write('Failed password: error\n')
    arquivo.write('Failed password: error\n')
    arquivo.write('Failed password: error\n')
    arquivo.write('Failed password: error\n')
    arquivo.write('Failed password: error\n')

# Abre o arquivo 'dados.txt' no modo leitura ('r')
with open('dados.txt', 'r') as arquivo:
    # Lê todas as linhas do arquivo e guarda na lista 'conteudo'
    conteudo = arquivo.readlines()
    
    # Inicializa um contador para a palavra 'error'
    contador = 0
    
    # Percorre cada linha do arquivo
    for linha in conteudo:
        # Se a palavra 'error' estiver na linha, incrementa o contador
        if 'error' in linha:
            contador += 1
    
    # Exibe o resultado de forma legível
    print(f"A palavra 'error' apareceu {contador} vezes.")
# Dicionário de IPs com o número de ataques registrados em um servidor SSH