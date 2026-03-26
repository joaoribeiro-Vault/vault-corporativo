import os
import shutil
import pymupdf4llm
import mammoth

INPUT_DIR = "input_docs"
OUTPUT_DIR = "site/content"

def process_files():
    # Garante que a pasta de destino existe
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # Lê tudo o que você jogou na gaveta de entrada
    for filename in os.listdir(INPUT_DIR):
        input_path = os.path.join(INPUT_DIR, filename)
        
        if not os.path.isfile(input_path):
            continue
            
        name, ext = os.path.splitext(filename)
        ext = ext.lower()
        output_path = os.path.join(OUTPUT_DIR, f"{name}.md")

        try:
            if ext == '.md':
                # Se já for Markdown, só copia
                shutil.copy2(input_path, output_path)
                print(f"Copiado direto: {filename}")
                
            elif ext == '.pdf':
                # Se for PDF, extrai o texto página por página
                reader = PdfReader(input_path)
                text = f"# {name}\n\n" # Cria o título principal da página
                for page in reader.pages:
                    extracted = page.extract_text()
                    if extracted:
                        text += extracted + "\n\n"
                
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(text)
                print(f"Convertido de PDF: {filename}")
                
            elif ext == '.docx':
                # O NOVO MOTOR PARA WORD: Mantém tabelas, negritos e listas!
                with open(input_path, "rb") as docx_file:
                    result = mammoth.convert_to_markdown(docx_file)
                    text = f"# {name}\n\n{result.value}"
                    
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(text)
                print(f"Convertido de DOCX com formatacao: {filename}")
                
            else:
                print(f"Formato ignorado (apenas MD, PDF e DOCX): {filename}")
                
        except Exception as e:
            print(f"Erro ao processar {filename}: {e}")

if __name__ == "__main__":
    process_files()