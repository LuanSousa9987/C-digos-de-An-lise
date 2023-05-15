import pandas as pd

# Carregar dados em um DataFrame
df = pd.read_csv("large_data.csv")

# Mostrar as primeiras linhas do DataFrame
print(df.head())

# Calcular a média de uma coluna específica
mean = df["column_name"].mean()
print("Média:", mean)

# Agrupar dados por uma coluna e calcular a média de outra coluna
grouped = df.groupby("group_column_name")["column_to_average"].mean()
print(grouped)
