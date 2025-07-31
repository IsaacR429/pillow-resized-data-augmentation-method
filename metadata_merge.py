import pandas as pd

df_faso = pd.read_csv("faso_dan_fani_metadata.csv")
df_kente = pd.read_csv("kente_metadata.csv")
df_kancheepuram = pd.read_csv("kancheepuram_metadata.csv")

df_all_fabrics = pd.concat([df_faso, df_kente, df_kancheepuram], ignore_index=True)


df_all_fabrics.to_csv("all_fabric_metadata.csv", index=False)
