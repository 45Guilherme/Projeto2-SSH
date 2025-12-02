import datetime
# Importa o módulo datetime, que permite trabalhar com datas e horas.

agora = datetime.datetime.now()
# Cria uma variável 'agora' que recebe a data e hora atuais do sistema.

status = input("Status: Sucesso/falha? ")
# Pergunta ao usuário qual é o status do teste (Sucesso ou Falha) e armazena na variável 'status'.

observações = input("Observações: ")
# Pergunta ao usuário quais são as observações do teste e armazena na variável 'observações'.

relatorio = f"""
Relatório de Teste
-----------------
Data e Hora do Teste: {agora:%d/%m/%Y %H:%M:%S}
Status: {status}
Observações: {observações}
"""
# Cria uma string formatada (f-string) chamada 'relatorio' que contém:
# - Título do relatório
# - Linha separadora
# - Data e hora do teste (formatada como dia/mês/ano hora:minuto:segundo)
# - Status informado pelo usuário
# - Observações informadas pelo usuário

with open("relatorio.txt", "w") as arquivo:
    arquivo.write(relatorio)
# Abre (ou cria) um arquivo chamado 'relatorio.txt' em modo de escrita ("w").
# Escreve o conteúdo da variável 'relatorio' dentro do arquivo.
# O 'with' garante que o arquivo será fechado automaticamente após a escrita.
