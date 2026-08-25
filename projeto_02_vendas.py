import pandas as pd

vendas = {
    'Produto': ['Notebook', 'Mouse', 'Teclado', 'Monitor', 'Webcam'],
    'Quantidade': [50, 200, 150, 30, 100],
    'Preco_Unitario': [3000, 50, 150, 800, 200]
}

df = pd.DataFrame(vendas)
df['Total_Vendas'] = df['Quantidade'] * df['Preco_Unitario']

print("=== ANÁLISE DE VENDAS ===")
print(df)
print(f"\nProduto mais vendido: {df.loc[df['Quantidade'].idxmax(), 'Produto']}")
print(f"Maior faturamento: {df.loc[df['Total_Vendas'].idxmax(), 'Produto']}")
print(f"Total: R${df['Total_Vendas'].sum():,.2f}")
