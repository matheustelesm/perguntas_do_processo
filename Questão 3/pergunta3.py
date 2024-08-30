# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.



import json

# Nome do arquivo JSON
nome_arquivo = 'dados.json'

# Abrir e ler o arquivo JSON
with open(nome_arquivo, 'r') as file:
    dados = json.load(file)

# Extrair valores de faturamento maiores que zero
faturamentos = [item['valor'] for item in dados['faturamento'] if item['valor'] > 0]

# Verificar se há dados válidos
if not faturamentos:
    print("Não há dados de faturamento válidos.")
else:
    # Calcular menor e maior faturamento
    menor_faturamento = min(faturamentos)
    maior_faturamento = max(faturamentos)
    
    # Calcular a média mensal
    media_mensal = sum(faturamentos) / len(faturamentos)
    
    # Contar dias acima da média
    dias_acima_da_media = sum(1 for faturamento in faturamentos if faturamento > media_mensal)

    # Exibir resultados
    print("Menor faturamento:", menor_faturamento)
    print("Maior faturamento:", maior_faturamento)
    print("Número de dias acima da média:", dias_acima_da_media)








