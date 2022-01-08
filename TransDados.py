import os
import tabula
import shutil
import pandas as pd

file = "padrao.pdf"
folder_name = "tables"

#Extraindo as tabelas do pdf
tables = tabula.read_pdf(file, pages='114-120', pandas_options={'header': None})
table_cat = pd.concat([tables[1],tables[2],tables[3],tables[4],tables[5],tables[6]], ignore_index=True)

#Criando uma pasta para salvar as tabelas
if not os.path.isdir(folder_name):
    os.mkdir(folder_name)

#Convertendo e salvando as tabelas
tables[0].to_csv(os.path.join(folder_name, f"30.csv"), index=False)
table_cat.to_csv(os.path.join(folder_name, f"31.csv"), index=False)
tables[7].to_csv(os.path.join(folder_name, f"32.csv"), index=False)

#Zipando o conteudo da pasta
shutil.make_archive("Teste_Lucas_Calabria", "zip", folder_name)