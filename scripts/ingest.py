from langchain_community.document_loaders import DirectoryLoader, PyPDFDirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
import os
from tqdm import tqdm

def ingest_abap_documents(docs_dir="docs_abap", persist_dir="./chroma_abap_data", collection_name="abap_knowledge"):
    print("🚀 Iniciando ingestão de documentos ABAP...")
    
    # Embeddings (roda no Ollama)
    embeddings = OllamaEmbeddings(
        model="nomic-embed-text",
        base_url="http://localhost:11434"
    )
    
    # Carregar diferentes tipos de arquivos
    pdf_loader = PyPDFDirectoryLoader(os.path.join(docs_dir, "pdfs"))
    text_loader = DirectoryLoader(
        docs_dir, 
        glob="**/*.txt",
        loader_cls=TextLoader,
        loader_kwargs={"encoding": "utf-8"}
    )
    abap_loader = DirectoryLoader(
        docs_dir, 
        glob="**/*.abap",
        loader_cls=TextLoader,
        loader_kwargs={"encoding": "utf-8"}
    )
    
    print("Carregando documentos...")
    docs = []
    for loader in [pdf_loader, text_loader, abap_loader]:
        try:
            loaded = loader.load()
            docs.extend(loaded)
            print(f"  ✓ {len(loaded)} documentos carregados")
        except Exception as e:
            print(f"  ⚠ Erro ao carregar: {e}")
    
    if not docs:
        print("Nenhum documento encontrado!")
        return
    
    # Split em chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=700,
        chunk_overlap=100
    )
    splits = text_splitter.split_documents(docs)
    
    print(f"Criando {len(splits)} chunks...")
    
    # Criar vector store
    vectorstore = Chroma.from_documents(
        documents=splits,
        embedding=embeddings,
        collection_name=collection_name,
        persist_directory=persist_dir
    )
    
    print(f"✅ Ingestão concluída! {len(splits)} chunks salvos em {persist_dir}")

if __name__ == "__main__":
    ingest_abap_documents()