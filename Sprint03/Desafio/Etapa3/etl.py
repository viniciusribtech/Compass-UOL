import pandas as pd
df = pd.read_csv("/volume/concert_tours_by_women.csv")

# essa função foi feita com ajuda de IA para resolver erros específicos da leitura de números
def dinheiro(valor):
    if pd.isna(valor):
        return 0
    valor = str(valor).strip()
    # Remove $ e vírgulas
    valor = valor.replace("$", "").replace(",", "")
    # Remove colchetes e letras
    limpo = ""
    for c in valor:
        if c.isdigit() or c == ".":
            limpo += c
    if limpo == "":
        return 0
    return float(limpo)
    
# pega o "-" como separador e cria as colunas Start year e End year a partir do Year(s)
df[["Start year", "End year"]] = df["Year(s)"].apply(
    lambda x: pd.Series(str(x).split("-") if "-" in str(x) else [x, x])
)

coluna = ["Rank", "Actual gross", "Adjustedgross (in 2022 dollars)", "Artist", "Tour title", "Shows", "Average gross", "Start year", "End year"]
df = df[coluna] #mantém só essas colunas
print(df.head())

#aplicar a função dinheiro nas colunas necessárias
df["Actual gross"] = df["Actual gross"].apply(dinheiro)
df["Adjustedgross (in 2022 dollars)"] = df["Adjustedgross (in 2022 dollars)"].apply(dinheiro)
df["Average gross"] = df["Average gross"].apply(dinheiro)

if "Year(s)" in df.columns:
    df = df.drop(columns=["Year(s)"]) #tive que criar esse trecho de código pois a coluna Year(s) estava aparecendo não importa o que eu fizesse

#criar novo arquivo
df.to_csv("/volume/csv_limpo.csv", index=False)
print("Arquivo gerado") #ter certeza que todo o código foi executado