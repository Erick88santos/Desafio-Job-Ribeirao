import json

# leitura do arquivo JSON
with open('dados_faturamentos.json', 'r') as f:
    dados = json.load(f)

# cálculo do menor e do maior valor de faturamento
menor_valor = min(dados)
maior_valor = max(dados)

# cálculo da média mensal, desconsiderando dias sem faturamento
dias_com_faturamento = [faturamento for faturamento in dados if faturamento > 0]
media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)

# cálculo do número de dias em que o faturamento diário foi superior à média mensal
dias_acima_da_media = sum(1 for faturamento in dias_com_faturamento if faturamento > media_mensal)

# impressão dos resultados
print('Menor valor de faturamento diário:', menor_valor)
print('Maior valor de faturamento diário:', maior_valor)
print('Número de dias com faturamento acima da média mensal:', dias_acima_da_media)