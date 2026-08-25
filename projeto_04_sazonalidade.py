import pandas as pd

vendas = {
    'Mes': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
    'Faturamento': [50000, 45000, 55000, 48000, 52000, 58000, 72000, 70000, 65000, 75000, 85000, 120000]
}

df = pd.DataFrame(vendas)

print("=== ANÁLISE DE SAZONALIDADE ===")
print(df)

media = df['Faturamento'].mean()
melhor = df.loc[df['Faturamento'].idxmax()]
pior = df.loc[df['Faturamento'].idxmin()]

print(f"\nMédio: R${media:,.2f}")
print(f"Melhor: {melhor['Mes']} - R${melhor['Faturamento']:,.2f}")
print(f"Pior: {pior['Mes']} - R${pior['Faturamento']:,.2f}")

crescimento = ((df['Faturamento'].iloc[-1] - df['Faturamento'].iloc[0]) / df['Faturamento'].iloc[0]) * 100
print(f"Crescimento: {crescimento:.1f}%")
