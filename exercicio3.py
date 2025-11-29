import re  # Importa o módulo 're', usado para trabalhar com expressões regulares

# Exemplo de linha de log típica do serviço SSH
linha = "Nov 12 14:33:01 server sshd[123]: Failed password for root from 192.168.1.10 port 445 ssh2"

# Expressão regular para capturar:
# 1) Tipo do evento ("Failed" ou "Accepted")
# 2) Usuário alvo da tentativa
# 3) Endereço IP de origem
padrao = r"(Failed|Accepted) password for (\w+) from ([\d\.]+)"

# Procura no texto a primeira ocorrência que combine com o padrão
match = re.search(padrao, linha)

# Se houver correspondência, extrai os grupos capturados
if match:
    evento = match.group(1)   # "Failed" ou "Accepted"
    usuario = match.group(2)  # Usuário (ex.: root)
    ip = match.group(3)       # IP de origem (ex.: 192.168.1.10)

    # Exibe os dados extraídos de forma legível
    print("Evento:", evento)
    print("Usuário:", usuario)
    print("IP:", ip)


