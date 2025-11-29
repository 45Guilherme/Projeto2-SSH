# Dicionário para armazenar a contagem de ataques por IP
ataques = {}

# Loop infinito para permitir múltiplas entradas do usuário
while True:
    # Solicita ao usuário que digite o IP do atacante ou 'sair' para encerrar
    ip = input("Digite o IP do atacante (ou 'sair'): ")
    
    # Condição para sair do loop quando o usuário digitar 'sair'
    if ip == "sair":
        break

    # Se o IP já estiver no dicionário, incrementa a contagem
    if ip in ataques:
        ataques[ip] += 1
    # Caso contrário, adiciona o IP ao dicionário com contagem inicial 1
    else:
        ataques[ip] = 1

# Exibe o dicionário final com todos os IPs e suas contagens
print(ataques)




