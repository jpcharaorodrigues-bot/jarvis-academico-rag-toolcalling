# JARVIS Acadêmico

Sistema acadêmico inteligente baseado em Retrieval-Augmented Generation (RAG), Tool Calling e Large Language Models (LLMs), desenvolvido para auxiliar estudantes na organização acadêmica, recuperação de conhecimento e apoio ao aprendizado.

---

# Objetivo

O objetivo do projeto é implementar um assistente acadêmico capaz de integrar recuperação semântica de informações, gerenciamento acadêmico e funcionalidades voltadas ao aprendizado.

O sistema permite:

* consultar materiais de estudo utilizando RAG;
* responder perguntas contextualizadas;
* consultar agenda acadêmica;
* gerenciar tarefas;
* gerar planejamento de estudos;
* gerar exercícios;
* aplicar técnicas de Active Recall;
* avaliar respostas do estudante;
* registrar dificuldades de aprendizagem;
* apoiar processos de revisão e preparação para avaliações.

O projeto segue as diretrizes da disciplina para integração de RAG, Tool Calling e Large Language Models em um sistema acadêmico unificado.

---

# Arquitetura do Sistema

A arquitetura foi organizada de forma modular, com separação de responsabilidades entre os componentes.

## Módulo RAG

Responsável por:

* carregamento documental;
* pré-processamento textual;
* chunking;
* geração de embeddings;
* indexação vetorial utilizando FAISS;
* recuperação semântica.

Fluxo:

```text
Documentos
↓
Chunking
↓
Embeddings
↓
FAISS
↓
Recuperação
↓
LLM
↓
Resposta
```

---

## Módulo de Tool Calling

Responsável por:

* seleção automática de ferramentas;
* interpretação da decisão da LLM;
* execução das ferramentas;
* geração da resposta final.

Ferramentas implementadas:

* consultar_agenda
* listar_tarefas
* adicionar_tarefa
* concluir_tarefa
* buscar_material_rag
* planejar_estudos
* gerar_exercicios
* gerar_pergunta_recall
* avaliar_resposta
* registrar_dificuldade
* listar_dificuldades

---

## Módulo de Aprendizagem

Responsável por funcionalidades educacionais.

### Active Recall

Geração automática de perguntas de revisão.

### Avaliação de Respostas

Avaliação das respostas fornecidas pelo estudante.

### Geração de Exercícios

Criação de exercícios contextualizados.

### Identificação de Dificuldades

Registro de dificuldades encontradas durante o estudo.

---

## Agenda Acadêmica

Permite:

* consultar compromissos;
* visualizar eventos acadêmicos;
* verificar atividades futuras.

---

## Gerenciamento de Tarefas

Permite:

* adicionar tarefas;
* listar tarefas;
* concluir tarefas;
* acompanhar pendências acadêmicas.

---

## Planejamento de Estudos

Implementado conforme as diretrizes da disciplina.

O sistema combina:

* agenda acadêmica;
* tarefas pendentes;
* materiais recuperados pelo RAG;

para gerar planos de estudo personalizados.

Exemplos:

```text
Planeje meus estudos sobre transformers
```

```text
O que devo priorizar hoje?
```

---

# Tecnologias Utilizadas

* Python
* FAISS
* Sentence Transformers
* OpenAI SDK
* JSON
* Retrieval-Augmented Generation (RAG)
* Tool Calling
* Embeddings Vetoriais
* Busca Semântica
* Large Language Models (LLMs)
* Git
* GitHub
* VS Code

---

# Integração com LLM

O sistema utiliza uma API compatível com OpenAI disponibilizada pela infraestrutura da disciplina.

A LLM é utilizada para:

* seleção de ferramentas;
* geração de respostas;
* planejamento de estudos;
* geração de exercícios;
* Active Recall;
* avaliação de respostas.

---

# Ferramentas de IA Utilizadas

Durante o desenvolvimento do projeto foi utilizada a seguinte ferramenta de apoio:

* ChatGPT

A ferramenta foi utilizada para:

* revisão de código;
* identificação de erros;
* sugestões de melhoria;
* apoio na documentação.

Todas as implementações foram compreendidas, adaptadas e integradas manualmente ao projeto.

---

# Estrutura do Projeto

```text
app/
├── learning/
├── rag/
├── tools/
├── utils/
├── config.py
├── llm_client.py
├── orchestrator.py
├── build_index.py
└── main.py

data/
├── documents/
├── agenda.json
├── tasks.json
├── logs.jsonl
├── difficulties.json
└── vector_store/

tests/

screenshots/

README.md
RELATORIO.md
AVALIACAO.md
requirements.txt
```

---

# Dataset

## Origem dos Dados

O dataset foi construído especificamente para fins acadêmicos.

Os documentos foram produzidos e organizados para permitir experimentação controlada das técnicas de recuperação semântica.

---

## Tipo de Conteúdo

Documentos acadêmicos em formato TXT.

Temas:

* Retrieval-Augmented Generation (RAG)
* Embeddings
* Transformers
* Busca Semântica
* Chunking
* Tool Calling
* Modelos de Linguagem
* Avaliação de Sistemas RAG
* Active Recall
* Planejamento de Estudos

---

## Quantidade de Documentos

O dataset contém 10 documentos.

---

## Estratégia de Chunking

Os documentos são divididos em múltiplos trechos antes da geração dos embeddings.

Objetivos:

* melhorar recuperação semântica;
* reduzir perda de contexto;
* aumentar precisão da busca vetorial.

---

## Impacto do Chunking no RAG

Chunks pequenos podem perder contexto.

Chunks muito grandes podem reduzir a precisão da recuperação.

A estratégia adotada busca equilíbrio entre contexto e relevância.

---

## Limitações do Dataset

* conjunto documental reduzido;
* ausência de PDFs extensos;
* cobertura limitada dos temas;
* ausência de reranking;
* ausência de atualização automática.

---

# Execução

## Instalar Dependências

```bash
pip install -r requirements.txt
```

## Construir Índice Vetorial

```bash
python -m app.build_index
```

## Executar o Sistema

```bash
python -m app.main
```

---

# Exemplos de Comandos

```text
Explique o que é RAG
```

```text
Como funciona busca semântica?
```

```text
Liste minhas tarefas
```

```text
O que tenho hoje?
```

```text
Planeje meus estudos sobre transformers
```

```text
Gere exercícios sobre tool calling
```

```text
Gere uma pergunta sobre embeddings
```

```text
Avalie minha resposta sobre embeddings
```

---

# Funcionalidades Implementadas

## RAG

* recuperação semântica;
* embeddings vetoriais;
* indexação FAISS;
* recuperação contextual.

## Tool Calling

* seleção automática;
* execução de ferramentas;
* orquestração baseada em LLM.

## Agenda Acadêmica

* consulta de eventos;
* acompanhamento de compromissos.

## Gerenciamento de Tarefas

* criação;
* consulta;
* conclusão.

## Planejamento de Estudos

* integração entre agenda, tarefas e materiais.

## Aprendizagem

* Active Recall;
* geração de exercícios;
* avaliação de respostas;
* identificação de dificuldades.

## Engenharia de Software

* arquitetura modular;
* separação de responsabilidades;
* tratamento de erros;
* logs;
* testes básicos.

---

# Limitações

O sistema apresenta algumas limitações:

* ausência de memória conversacional;
* ausência de reranking;
* dataset reduzido;
* dependência de infraestrutura externa;
* ausência de interface gráfica.

---

# Considerações Finais

O projeto demonstra a integração prática entre Retrieval-Augmented Generation, embeddings vetoriais, recuperação semântica, Tool Calling e funcionalidades voltadas ao aprendizado.

A arquitetura modular facilita manutenção, expansão e evolução futura do sistema, permitindo incorporar novos recursos de apoio educacional baseados em Inteligência Artificial.
