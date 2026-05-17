# ABAP-9 — The Hitchhiker’s Guide to ABAP

**Caixa de ferramentas de IA local especializada em SAP ABAP**

> “Don’t Panic.” — Guia do Mochileiro das Galáxias

## Objetivo

Criar um ambiente completo, eficiente e **local** para desenvolvimento ABAP usando IA, com foco em:
- Modelos pequenos e otimizados (Qwen Coder)
- RAG poderoso com **ChromaDB**
- Integração nativa com **Continue.dev**
- Suporte a endpoint na nuvem como fallback

## Stack Principal

- **LLM Principal**: `qwen3-coder:30b-a3b` (MoE)
- **RAG**: ChromaDB + **Chroma MCP Server**
- **Editor**: Continue.dev (VS Code)
- **Hardware alvo**: RTX 3060 12 GB VRAM
- **Fallback**: Hugging Face Inference Endpoints

## Como Começar (Passo a Passo)

### 1. Máquina Servidor (IA)

```bash
# Instale Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Puxe os modelos
ollama pull qwen3-coder:30b-a3b
ollama pull nomic-embed-text

# Inicie o Chroma MCP Server
uvx chroma-mcp --client-type persistent --data-dir ./chroma_abap_data --host 0.0.0.0 --port 8000
```
### 2. Configure para rede (acesso remoto)
```bash
export OLLAMA_HOST=0.0.0.0
export OLLAMA_ORIGINS=*
```
# Ou crie um serviço systemd para rodar sempre

### 3. Instale Open WebUI (Docker — mais fácil)
```bash
docker run -d -p 3000:8080 \
  -e OLLAMA_BASE_URL=http://host.docker.internal:11434 \
  --add-host=host.docker.internal:host-gateway \
  --name open-webui \
  -v open-webui:/app/backend/data \
  ghcr.io/open-webui/open-webui:main
```

### 4. RAG com LangChain + Chroma (Python)
```bash
pip install langchain langchain-community langchain-ollama chromadb pypdf sentence-transformers tqdm
```

### 5. Chroma MCP Server
```bash
uvx chroma-mcp --client-type persistent --data-dir ./chroma_abap_data --host 0.0.0.0 --port 8000
```
