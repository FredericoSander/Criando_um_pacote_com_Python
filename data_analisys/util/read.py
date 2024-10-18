import pandas as pd

df = pd.read_csv("F:/Git/Projeto_01_Analise_de_dados_com_Pandas/netflix_titles.csv")

print("\nPrimeiras 5 linhas do arquivo por padrão:")
print(df.head())

print("\nEstatística descritivas:")
print(df.describe())

print("\nInformações do DataFrame:")
print(df.info())

print("\nContagem de valores únicos por coluna:")
print(df.nunique())
