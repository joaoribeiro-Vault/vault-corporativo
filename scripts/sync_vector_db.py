import os
import google.generativeai as genai
from pinecone import Pinecone

# Puxa as senhas do GitHub Secrets
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
pc = Pinecone(api_key=os.environ["VECTOR_DB_API_KEY"])
index = pc.Index("vault-index") # Certifique-se que o nome do index no Pinecone é este

def sync_to_vector_db():
    content_path = "./content"
    
    for filename in os.listdir(content_path):
        if filename.endswith(".md"):
            with open(os.path.join(content_path, filename), 'r', encoding='utf-8') as f:
                text = f.read()
                
                # Cria o vetor com o Gemini
                embedding = genai.embed_content(
                    model="models/text-embedding-004",
                    content=text,
                    task_type="retrieval_document"
                )
                
                # Salva no Banco
                index.upsert(vectors=[{
                    "id": filename, 
                    "values": embedding['embedding'], 
                    "metadata": {"source": filename, "status": "oficial"}
                }])
                print(f"🧠 Sincronizado com IA: {filename}")

if __name__ == "__main__":
    sync_to_vector_db()