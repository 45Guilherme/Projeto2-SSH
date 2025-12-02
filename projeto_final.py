import re  # Importa o módulo 're', usado para trabalhar com expressões regulares

print("Analisador de Logs SSH Completo")

# Criação do arquivo 'lista.txt' com algumas linhas de exemplo
with open("lista.txt", "w") as arquivo:
    arquivo.write("Nov 12 14:33:01 server sshd[1201]: Failed password for root from 177.233.10.45 port 445 ssh2  # 120 tentativas totais\n")
    arquivo.write("Nov 12 15:12:44 server sshd[982]:  Accepted password for root from 201.55.18.10 port 55874 ssh2  # 87 tentativas totais\n")
    arquivo.write("Nov 12 16:09:22 server sshd[774]: Invalid user for admin from 185.12.245.90 port 2231 ssh2  # 45 tentativas totais\n")
    arquivo.write("Nov 12 17:42:55 server sshd[555]: Failed password for root from 3.3.3.3 port 1022 ssh2  # 30 tentativas totais\n")
    arquivo.write("Nov 12 18:05:10 server sshd[331]: Failed password for invalid user test from 1.1.1.1 port 7781 ssh2  # 10 tentativas totais\n")
# Abre o arquivo 'lista.txt' no modo leitura ('r')

with open("lista.txt", "r") as arquivo:
    conteudo = arquivo.readlines()  # Lê todas as linhas do arquivo e retorna uma lista

    # Expressão regular para capturar:
    # 1) Tipo do evento ("Failed" ou "Accepted")
    # 2) Usuário alvo da tentativa
    # 3) Endereço IP de origem
    padrao = r"(Failed|Accepted|Invalid) user for (\w+) from ([\d\.]+)"

    match = re.search(padrao, linha)

    # Se houver correspondência, extrai os grupos capturados
    if match:
            evento = match.group(1)   # "Failed" ou "Accepted"
            usuario = match.group(2)  # Usuário (ex.: root)
            ip = re.match.group(3)       # IP de origem (ex.: 192.168.1.10)
    
   






    




