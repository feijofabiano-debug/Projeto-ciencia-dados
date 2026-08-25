import pandas as pd

clientes = {
    'Cliente': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
    'Meses': [24, 3, 12, 36, 2, 18, 6, 48],
    'Ticket': [5000, 200, 3000, 8000, 150, 4000, 500, 10000],
    'Dias_Ultima_Compra': [5, 60, 30, 2, 90, 20, 80, 1]
}

df = pd.DataFrame(clientes)

def calcular_risco(meses, ticket, dias):
    risco = 0
    if meses < 6:
        risco += 30
    if dias > 60:
        risco += 40
    if ticket < 500:
        risco += 20
    return min(risco, 100)

df['Risco'] = df.apply(
    lambda row: calcular_risco(row['Meses'], row['Ticket'], row['Dias_Ultima_Compra']),
    axis=1
)

df['Status'] = df['Risco'].apply(lambda x: 'CRÍTICO' if x >= 70 else 'RISCO' if x >= 40 else 'SEGURO')

print("=== ANÁLISE DE CHURN ===")
print(df)
print(f"\n⚠️ {len(df[df['Status'] == 'CRÍTICO'])} clientes em risco crítico!")
