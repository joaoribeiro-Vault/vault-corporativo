import os
import frontmatter
from datetime import datetime
import shutil

# Configuração de caminhos
INPUT_DIR = "./input_docs"
OUTPUT_DIR = "./content"
SITE_DIR = "./site/content"

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(SITE_DIR, exist_ok=True)

def process_markdowns():
    # Pega todos os arquivos da pasta de input
    for filename in os.listdir(INPUT_DIR):
        if filename.endswith(".md"):
            input_path = os.path.join(INPUT_DIR, filename)
            output_path = os.path.join(OUTPUT_DIR, filename)
            site_path = os.path.join(SITE_DIR, filename)
            
            # Carrega o arquivo
            with open(input_path, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)
            
            # Injeta a Governança
            post['status'] = 'oficial'
            post['owner'] = 'Equipe Vault'
            post['last_updated'] = datetime.now().strftime("%Y-%m-%d")
            
            # Salva na pasta content oficial
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(frontmatter.dumps(post))
                
            # Copia para a pasta do site (Quartz)
            shutil.copy2(output_path, site_path)
            print(f"✅ Processado e enviado para o site: {filename}")

if __name__ == "__main__":
    process_markdowns()