import pandas as pd

clientes = {
    'ID': [1, 2, 3, 4, 5, 6, 7, 8],
    'Nome': ['João', 'Maria', 'Pedro', 'Ana', 'Carlos', 'Lucia', 'Bruno', 'Sofia'],
    'Compras': [15, 2, 8, 25, 3, 20, 5, 18],
    'Gasto_Total': [5000, 300, 2000, 12000, 500, 8000, 1000, 7000],
    'Dias_Sem_Comprar': [10, 120, 45, 5, 200, 15, 90, 20]
}

df = pd.DataFrame(clientes)

def classificar_cliente(gasto, compras, dias):
    if gasto >= 7000 and compras >= 10 and dias <= 30:
        return 'VIP'
    elif gasto >= 5000:
        return 'OURO'
    elif dias > 100:
        return 'INATIVO'
    else:
        return 'BRONZE'

df['Segmento'] = df.apply(
    lambda row: classificar_cliente(row['Gasto_Total'], row['Compras'], row['Dias_Sem_Comprar']),
    axis=1
)

print("=== ANÁLISE RFM ===")
print(df)
print(f"\nVIPs: {(df[df['Segmento'] == 'VIP']['Gasto_Total'].sum() / df['Gasto_Total'].sum()) * 100:.1f}% da receita")
