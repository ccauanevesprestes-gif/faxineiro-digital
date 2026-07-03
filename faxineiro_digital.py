import os
import shutil

pasta_origem = "Relatorios_Antigos"


pasta_destino = "Relatorios_Organizados"


os.makedirs(pasta_destino, exist_ok=True)

print("Arquivos encontrados:\n")


for arquivo in os.listdir(pasta_origem):
    caminho_origem = os.path.join(pasta_origem, arquivo)


    if os.path.isfile(caminho_origem):
        print(arquivo)


        shutil.move(caminho_origem, os.path.join(pasta_destino, arquivo))

print("\nTodos os arquivos foram movidos com sucesso!")