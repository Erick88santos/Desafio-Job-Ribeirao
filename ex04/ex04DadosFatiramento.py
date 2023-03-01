# valores de faturamento mensal por estado
faturamento_mensal = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# cálculo do valor total mensal
valor_total_mensal = sum(faturamento_mensal.values())

# cálculo do percentual de representação de cada estado
percentuais = {}
for estado, valor in faturamento_mensal.items():
    percentuais[estado] = (valor / valor_total_mensal) * 100

# impressão dos resultados
for estado, percentual in percentuais.items():
    print(f'{estado}: {percentual:.2f}%')
