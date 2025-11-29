
# -*- coding: utf-8 -*-
"""
Relatório de Ataques SSH
Autor: Seu Nome
Descrição: Cria um relatório de tentativas de login falhas, 
conta a quantidade de erros e lista os IPs mais frequentes.
"""

# Criar arquivo 'relatorio.txt' e adicionar cabeçalho
with open("relatorio.txt", "w") as arquivo:
    arquivo.write("=== Relatório de Ataques SSH ===\n\n")  # Cabeçalho
    arquivo.write("Linhas de tentativas de login falhas:\n")
    
    # Escreve 11 linhas simulando tentativas de login falhas
    for _ in range(11):
        arquivo.write('Failed password: error\n')

# Criar um dicionário com IPs e quantidade de ataques
ip = {"1.1.1.1": 10, "2.2.2.2": 5, "3.3.3.3": 20}

# Ordenar os IPs do que teve mais ataques para o que teve menos
ordenado = sorted(ip.items(), key=lambda item: item[1], reverse=True)

# Escrever os IPs ordenados no arquivo, numerados
with open("relatorio.txt", "a") as arquivo:
    arquivo.write("\nTop IPs mais frequentes:\n")
    for i, (ip_addr, qtd) in enumerate(ordenado, 1):
        arquivo.write(f"{i}) {ip_addr} → {qtd}\n")

# Contar quantas vezes a palavra 'error' aparece no arquivo
contador = 0
with open("relatorio.txt", "r") as arquivo:
    for linha in arquivo:
        if 'error' in linha:
            contador += 1

# Escrever o total de tentativas no arquivo
with open("relatorio.txt", "a") as arquivo:
    arquivo.write(f"\nTotal de tentativas: {contador}\n")



       

           
    


       
            
    

    
    








