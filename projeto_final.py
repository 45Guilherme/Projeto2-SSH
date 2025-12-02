import re  # Importa o módulo 're', usado para trabalhar com expressões regulares

print("Analisador de Logs SSH Completo")

# Criação do arquivo 'lista.txt' com algumas linhas de exemplo
with open("lista.txt", "w") as arquivo:
    arquivo.write("Nov 12 14:33:01 server sshd[1201]: Failed password for root from 177.233.10.45 port 445 ssh2  # 120 tentativas totais\n")
    arquivo.write("Nov 12 15:12:44 server sshd[982]:  Accepted password for root from 201.55.18.10 port 55874 ssh2  # 87 tentativas totais\n")
    arquivo.write("Nov 12 16:09:22 server sshd[774]: Invalid user for admin from 185.12.245.90 port 2231 ssh2  # 45 tentativas totais\n")


