import datetime
# Importa o módulo datetime, que permite trabalhar com datas e horas.

agora = datetime.datetime.now()
# Captura a data e hora atuais do sistema no momento da execução
# e armazena na variável 'agora'.

relatorio = f"""
Relatório de Teste
-----------------
Data e Hora do Teste: {agora:%d/%m/%Y %H:%M:%S}
Status: Sucesso
Observações: Todos os testes foram concluídos corretamente.
"""
# Cria uma string multilinha usando f-string para inserir a data formatada.
# O trecho {agora:%d/%m/%Y %H:%M:%S} formata o datetime no padrão:
# dia/mês/ano horas:minutos:segundos.

with open("relatorio.txt", "w") as arquivo:
    # Abre (ou cria, se não existir) o arquivo 'relatorio.txt' no modo escrita ("w").
    # O bloco with garante que o arquivo será fechado automaticamente após o uso.
    
    arquivo.write(relatorio)
    # Escreve o conteúdo da variável 'relatorio' dentro do arquivo.

print("Relatório salvo em 'relatorio.txt' com sucesso.")
# Exibe uma mensagem confirmando que o arquivo foi salvo.



