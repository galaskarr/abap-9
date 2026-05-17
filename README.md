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
ollama pull qwen-coder-abap
ollama pull nomic-embed-text
ollama pull qwen3-coder:30b-a3b   # opcional

# Inicie o Chroma MCP Server
uvx chroma-mcp --client-type persistent --data-dir ./chroma_abap_data --host 0.0.0.0 --port 8000
