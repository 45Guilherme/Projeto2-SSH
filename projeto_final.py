import re  # Importa o módulo 're', usado para trabalhar com expressões regulares

print("Analisador de Logs SSH Completo")  # Exibe um título no console

# Criação do arquivo 'lista.txt' com algumas linhas de exemplo
with open("lista.txt", "w") as arquivo:  # Abre (ou cria) o arquivo em modo escrita
    arquivo.write("Nov 12 14:33:01 server sshd[1201]: Failed password for root from 177.233.10.45 port 445 ssh2  # 120 tentativas totais\n")
    arquivo.write("Nov 12 15:12:44 server sshd[982]:  Accepted password for root from 201.55.18.10 port 55874 ssh2  # 87 tentativas totais\n")
    arquivo.write("Nov 12 16:09:22 server sshd[774]: Invalid user for admin from 185.12.245.90 port 2231 ssh2  # 45 tentativas totais\n")
    arquivo.write("Nov 12 17:42:55 server sshd[555]: Failed password for root from 3.3.3.3 port 1022 ssh2  # 30 tentativas totais\n")
    arquivo.write("Nov 12 18:05:10 server sshd[331]: Failed password for invalid user test from 1.1.1.1 port 7781 ssh2  # 10 tentativas totais\n")

# Abre o arquivo 'lista.txt' no modo leitura
with open("lista.txt", "r") as arquivo:
    conteudo = arquivo.readlines()  # Lê todas as linhas do arquivo e armazena em uma lista

# Expressão regular para capturar:
# 1) Tipo do evento (Failed password, Accepted password, Invalid user)
# 2) Endereço IP após a palavra "from"
padrao = r"(Failed password|Accepted password|Invalid user).*from ([\d\.]+)"

ataques = []  # Lista onde vamos armazenar as tuplas (evento, ip)

# Percorre cada linha do arquivo para procurar correspondências com o padrão
for linha in conteudo:
    match = re.search(padrao, linha)  # Procura o padrão na linha
    if match:  # Se encontrou o padrão
        evento = match.group(1)  # Captura o tipo do evento
        ip = match.group(2)      # Captura o endereço IP
        ataques.append((evento, ip))  # Adiciona a tupla à lista 'ataques'

ips = []  # Lista onde depois armazenaremos os IPs ordenados
contagem = {}  # Dicionário para contar quantas vezes cada IP aparece

# Conta quantas vezes cada IP aparece na lista 'ataques'
for _, ip in ataques:  # "_" significa que ignoramos o primeiro valor (evento)
    if ip not in contagem:  # Se IP ainda não está no dicionário
        contagem[ip] = 0    # Inicializa a contagem
    contagem[ip] += 1       # Soma +1 para o IP

# Ordena os IPs do que mais atacou para o que menos atacou
ips = sorted(contagem.items(), key=lambda item: item[1], reverse=True)

# Cria o arquivo 'relatorio_final.txt' com o Top 5 IPs
with open("relatorio_final.txt", "w") as r:
    r.write("Top 5 IPs que mais atacaram:\n\n")  # Título do relatório
    top = ips[:5]  # Pega apenas os 5 primeiros da lista
    for posicao, (ip, qtd) in enumerate(top, start=1):  # Enumera começando de 1
        r.write(f"{posicao}) {ip} → {qtd} tentativas\n")  # Escreve cada linha no arquivo
