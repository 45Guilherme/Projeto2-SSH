# Dicionário de IPs com o número de ataques registrados em um servidor SSH
ip = {"1.1.1.1": 10, "2.2.2.2": 5, "3.3.3.3": 20}

# Ordena os IPs pelo número de ataques em ordem decrescente
# .items() retorna uma lista de tuplas (IP, quantidade)
# key=lambda item: item[1] indica que a ordenação será pelo valor (número de ataques)
# reverse=True garante que os IPs com mais ataques apareçam primeiro
ips = sorted(ip.items(), key=lambda item: item[1], reverse=True)

# Exibe a lista de IPs ordenada pelo número de ataques
print(ips)
