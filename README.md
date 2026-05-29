# JARVIS Academico

Sistema academico baseado em Retrieval-Augmented Generation (RAG) e tool calling utilizando Large Language Models.

## Objetivo

O projeto implementa um assistente academico capaz de:

- recuperar materiais de estudo utilizando busca semantica;
- responder perguntas contextualizadas;
- consultar agenda academica;
- gerenciar tarefas;
- gerar planejamento de estudos;
- gerar perguntas de active recall;
- avaliar respostas do estudante;
- registrar dificuldades de aprendizagem.

O sistema utiliza embeddings vetoriais, indice FAISS e integracao com LLM externa.

---

# Arquitetura

O projeto possui arquitetura modular dividida em componentes independentes.

## Componentes principais

### RAG
Responsavel por:
- carregamento documental;
- chunking;
- embeddings;
- indexacao vetorial;
- recuperacao semantica.

### Tool Calling
Responsavel por:
- selecao de ferramentas;
- execucao automatica;
- orquestracao entre LLM e modulos internos.

### Learning
Responsavel por:
- active recall;
- avaliacao de respostas;
- deteccao de dificuldades;
- geracao de exercicios.

### Agenda e tarefas
Responsavel por:
- consulta academica;
- gerenciamento de tarefas;
- planejamento de estudos.

---

# Tecnologias utilizadas

- Python
- FAISS
- Sentence Transformers
- OpenAI SDK
- Gemma 3
- JSON
- RAG
- Tool Calling

---

# Estrutura do projeto

```text
app/
├── rag/
├── tools/
├── learning/
├── utils/
├── main.py
├── orchestrator.py

data/
├── documents/
├── agenda.json
├── tasks.json
```

---

# Dataset

O dataset possui documentos textuais relacionados a:

- RAG;
- embeddings;
- transformers;
- busca semantica;
- chunking;
- tool calling;
- active recall;
- planejamento de estudos.

Os documentos sao utilizados durante recuperacao semantica.

---

# Execucao

## Instalar dependencias

```bash
pip install -r requirements.txt
```

## Criar indice vetorial

```bash
python -m app.build_index
```

## Executar sistema

```bash
python -m app.main
```

---

# Exemplos de comandos

```text
Explique o que e RAG
```

```text
Liste minhas tarefas
```

```text
Planeje meus estudos sobre transformers
```

```text
Gere uma pergunta sobre embeddings
```

---

# Funcionalidades implementadas

- recuperacao semantica;
- embeddings vetoriais;
- indice FAISS;
- tool calling;
- agenda academica;
- gerenciamento de tarefas;
- planejamento academico;
- active recall;
- avaliacao automatica;
- logs de execucao.

---

# Limitacoes

O sistema utiliza dataset controlado e sintetico. Em ambientes reais, recomenda-se:

- utilizar PDFs academicos;
- ampliar base documental;
- melhorar reranking;
- adicionar memoria conversacional;
- expandir cobertura do dataset.

---

# Consideracoes finais

O projeto demonstra integracao entre RAG, embeddings, recuperacao vetorial e tool calling aplicados ao contexto academico.

A arquitetura modular permite expansao futura para novos modulos e funcionalidades relacionadas a apoio educacional baseado em inteligencia artificial.