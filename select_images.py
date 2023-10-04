import os
import shutil

# Diretório de origem e destino
diretorio_origem = r"D:\Tecnologia da Informação (TI)\P4 2023.2\Aprendizado de Máquina\ProjetoCatsDogs\images"
diretorio_destino = r"D:\Tecnologia da Informação (TI)\P4 2023.2\Aprendizado de Máquina\ProjetoCatsDogs\dataset"

# Lista de palavras-chave para procurar nos nomes dos arquivos
palavras_chave = ["Sphynx", "saint_bernard", "leonberger", "Bengal"]

# Verifica se o diretório de destino existe, caso contrário, cria-o
if not os.path.exists(diretorio_destino):
    os.makedirs(diretorio_destino)

# Itera sobre os arquivos na pasta de origem
for root, dirs, files in os.walk(diretorio_origem):
    for file in files:
        if file.endswith(".jpg"):
            for palavra_chave in palavras_chave:
                if palavra_chave.lower() in file.lower():
                    origem = os.path.join(root, file)
                    destino = os.path.join(diretorio_destino, file)
                    shutil.move(origem, destino)
                    print(f"Transferido: {file}")

print("Transferência concluída.")
