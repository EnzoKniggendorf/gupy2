import json

dados_faturamento = '''
{
    "dias": [15000, 22000, 0, 30000, 25000, 27000, 0, 32000, 33000, 0, 0, 24000, 0, 20000, 31000, 28000, 29000, 0, 0, 32000, 34000, 35000, 0, 0, 36000, 37000, 0, 39000, 40000, 41000, 0, 42000, 0, 43000, 44000, 45000, 46000, 47000, 0, 48000, 49000, 0, 50000]
}
'''

faturamento = json.loads(dados_faturamento)["dias"]
faturamento = [f for f in faturamento if f > 0]  # Ignora dias sem faturamento
media_mensal = sum(faturamento) / len(faturamento)
menor_faturamento = min(faturamento)
maior_faturamento = max(faturamento)
dias_acima_media = len([f for f in faturamento if f > media_mensal])

print(f"Menor valor de faturamento: R${menor_faturamento:.2f}")
print(f"Maior valor de faturamento: R${maior_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_media}")
