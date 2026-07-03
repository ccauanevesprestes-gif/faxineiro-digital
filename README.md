📄 CHEAT SHEET — FAXINEIRO DIGITAL (Python)
🧹 Automação de Arquivos com Python
🎯 Problema Resolvido

Organizar automaticamente centenas de arquivos em pastas, sem precisar mover manualmente.

📚 Biblioteca usada
🐍 os (nativa do Python)

Permite o Python conversar com o sistema operacional (Windows/Mac/Linux).

📦 shutil (nativa do Python)

Permite copiar e mover arquivos.

⚙️ Principais comandos
📂 Listar arquivos de uma pasta
os.listdir("nome_da_pasta")

✔ Mostra todos os arquivos dentro da pasta.

📁 Criar pasta automaticamente
os.makedirs("nome_da_pasta", exist_ok=True)

✔ Cria a pasta se ela não existir.

📍 Juntar caminhos de arquivos
os.path.join(pasta, arquivo)

✔ Evita erros de caminho no Windows.

🚚 Mover arquivos
shutil.move(origem, destino)

✔ Move arquivos de uma pasta para outra.

🚀 Fluxo do Faxineiro Digital
Lê todos os arquivos da pasta antiga
Cria uma nova pasta organizada
Lista os arquivos automaticamente
Move tudo sozinho para a nova pasta
💡 Código base (resumo)
import os
import shutil

origem = "Relatorios_Antigos"
destino = "Relatorios_Organizados"

os.makedirs(destino, exist_ok=True)

for arquivo in os.listdir(origem):
    caminho = os.path.join(origem, arquivo)

    if os.path.isfile(caminho):
        shutil.move(caminho, os.path.join(destino, arquivo))
⚡ Resultado

✔ 500 arquivos organizados em segundos
✔ Zero trabalho manual
✔ Menos erros humanos
✔ Automação com Python

🧠 Mensagem principal do projeto

“O Python transforma tarefas repetitivas em automação simples usando poucas linhas de código.”

📌 COMO VIRAR PDF (rápido)
Opção 1 (mais fácil):
Copia isso para o Word
Ajusta em 1 página
Exporta como PDF
Opção 2:
Cola no Canva
Escolhe template “Cheat Sheet”
Baixa em PDF
