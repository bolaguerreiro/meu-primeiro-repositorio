import pandas as pd

sujo = pd.read_csv("contatos_sujos.csv")
media = sujo["nota"].mean()
sujo["nota"] = sujo["nota"].fillna(media)
sujo = sujo.drop_duplicates()
print("Media usada para preencher os valores nulos:", media)

sujo["nome"] = (sujo["nome"].str.strip()
                .str.replace(r"\s+", " ", regex=True)
                .str.title()) 

sujo["telefone"] = sujo["telefone"].str.replace(r"\D", "", regex=True)

sujo["data_cadastro"] = pd.to_datetime(sujo["data_cadastro"], format="%d/%m/%Y")

sujo.to_csv("contatos_limpos.csv", index=False)

print(sujo)
print("Arquivo contatos_limpos.csv gravado.")