# RELATORIO TECNICO - JARVIS ACADEMICO

# 1. Introducao

O projeto JARVIS Academico implementa um assistente inteligente para apoio ao estudante utilizando tecnicas modernas de Inteligencia Artificial.

O sistema integra:

* Retrieval-Augmented Generation (RAG);
* recuperacao semantica;
* embeddings vetoriais;
* tool calling;
* planejamento de estudos;
* funcionalidades de aprendizagem;
* Large Language Models (LLMs).

O objetivo principal foi desenvolver um sistema capaz de auxiliar o estudante na organizacao academica, revisao de conteudos e planejamento de estudos.

---

# 2. Objetivos do Projeto

Os principais objetivos do sistema foram:

* implementar um pipeline RAG completo;
* utilizar embeddings vetoriais;
* implementar busca semantica;
* integrar uma LLM ao sistema;
* implementar tool calling;
* desenvolver funcionalidades academicas;
* apoiar o processo de aprendizagem;
* gerar planejamento de estudos;
* registrar logs;
* organizar o software em arquitetura modular.

---

# 3. Arquitetura do Sistema

O sistema foi organizado em modulos independentes.

## Estrutura principal

```text
app/
├── rag/
├── learning/
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

README.md
RELATORIO.md
AVALIACAO.md
```

---

# 4. Modulos Implementados

## RAG

Responsavel por:

* carregamento dos documentos;
* chunking;
* geracao de embeddings;
* indexacao vetorial;
* recuperacao semantica.

---

## Tool Calling

Responsavel por:

* selecao automatica de ferramentas;
* interpretacao da resposta da LLM;
* execucao das ferramentas;
* geracao da resposta final.

---

## Learning

Responsavel por:

* Active Recall;
* avaliacao de respostas;
* geracao de exercicios;
* identificacao de dificuldades.

---

## Agenda e Tarefas

Responsavel por:

* agenda academica;
* gerenciamento de tarefas;
* planejamento de estudos.

---

# 5. Implementacao do RAG

O sistema implementa o seguinte fluxo:

```text
Documentos
↓
Chunking
↓
Embeddings
↓
FAISS
↓
Recuperacao
↓
LLM
↓
Resposta
```

O pipeline permite recuperar trechos semanticamente relevantes antes da geracao da resposta.

---

## Embeddings

Foram utilizados modelos Sentence Transformers para representacao vetorial dos documentos.

Os embeddings permitem comparar semanticamente perguntas e documentos.

---

## Recuperacao Semantica

A busca utiliza similaridade vetorial para recuperar os chunks mais relevantes.

---

## Indexacao Vetorial

A indexacao foi realizada utilizando FAISS.

Arquivos produzidos:

```text
data/vector_store/index.faiss
data/vector_store/metadata.json
```

---

# 6. Integracao com LLM

O sistema utiliza a API disponibilizada pela infraestrutura da disciplina.

Configuracao:

* OpenAI SDK;
* endpoint compativel com API OpenAI;
* modelo disponibilizado pela disciplina.

A LLM e utilizada para:

* decidir ferramentas;
* gerar respostas;
* produzir exercicios;
* avaliar respostas;
* gerar planejamento de estudos.

---

# 7. Tool Calling

O sistema implementa tool calling baseado em LLM.

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

A decisao da ferramenta ocorre automaticamente.

---

# 8. Dataset

O dataset foi construido especificamente para o projeto.

Localizacao:

```text
data/documents
```

Quantidade:

* 10 documentos academicos.

Temas:

* RAG;
* embeddings;
* transformers;
* busca semantica;
* chunking;
* tool calling;
* modelos de linguagem;
* active recall;
* avaliacao de sistemas RAG;
* planejamento de estudos.

---

## Estrategia de Chunking

Os documentos sao divididos em chunks menores antes da geracao dos embeddings.

Objetivos:

* preservar contexto;
* melhorar recuperacao;
* reduzir ruido.

---

## Impacto do Chunking

Chunks pequenos podem perder contexto.

Chunks muito grandes podem reduzir a precisao.

A estrategia adotada busca equilibrio entre contexto e relevancia.

---

# 9. Funcionalidades Implementadas

## Recuperacao Semantica

Exemplo:

```text
Explique o que e RAG
```

---

## Agenda Academica

Exemplo:

```text
O que tenho hoje?
```

---

## Tarefas

Exemplo:

```text
Liste minhas tarefas
```

---

## Planejamento de Estudos

Exemplo:

```text
Planeje meus estudos sobre transformers
```

O sistema combina:

* agenda;
* tarefas;
* materiais recuperados.

---

## Active Recall

Exemplo:

```text
Gere uma pergunta sobre embeddings
```

---

## Geracao de Exercicios

Exemplo:

```text
Gere exercicios sobre tool calling
```

---

# 10. Logs

Os logs sao armazenados em:

```text
data/logs.jsonl
```

Os registros armazenam:

* ferramenta;
* entrada;
* saida;
* horario.

---

# 11. Testes

Foram implementados testes basicos para:

* agenda;
* chunking;
* tarefas.

Arquivos:

```text
tests/test_agenda.py
tests/test_chunker.py
tests/test_tasks.py
```

---

# 12. Analise de Erros

## Erro de Encoding

Problema:

* caracteres invalidos.

Solucao:

* padronizacao UTF-8.

---

## Erros de Importacao

Problema:

* imports incorretos.

Solucao:

* reorganizacao modular.

---

## Erros no Tool Calling

Problema:

* JSON nao era interpretado.

Solucao:

* implementacao do orchestrator.

---

## Timeout da Infraestrutura

Problema:

* indisponibilidade temporaria da API.

Solucao:

* aumento do timeout e repeticao das requisicoes.

---

# 13. Limitacoes

* dataset reduzido;
* ausencia de memoria conversacional;
* ausencia de reranking;
* dependencia da infraestrutura externa;
* ausencia de interface grafica.

---

# 14. Ferramentas Utilizadas

* Python;
* FAISS;
* Sentence Transformers;
* OpenAI SDK;
* VS Code;
* GitHub;
* ChatGPT.

---

# 15. Conclusao

O projeto implementou um assistente academico baseado em RAG, tool calling e integracao com LLM.

O sistema demonstrou:

* recuperacao semantica;
* embeddings vetoriais;
* indexacao FAISS;
* planejamento de estudos;
* active recall;
* geracao de exercicios;
* identificacao de dificuldades;
* logs;
* arquitetura modular;
* tratamento de erros.

Os resultados obtidos demonstraram atendimento aos requisitos estabelecidos pelas diretrizes da disciplina e permitiram a construcao de um sistema academico inteligente voltado ao apoio ao estudante.
