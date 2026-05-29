# AVALIACAO DO SISTEMA - JARVIS ACADEMICO

## Objetivo

O objetivo desta avaliacao foi verificar funcionamento do sistema RAG, tool calling, recuperacao semantica e ferramentas academicas implementadas.

---

# Teste 1 - Recuperacao RAG

## Pergunta

```text
Explique o que e RAG
```

## Documentos recuperados

- 01_rag.txt
- 02_embeddings.txt

## Resposta

O sistema explicou Retrieval-Augmented Generation utilizando contexto relacionado a embeddings, recuperacao vetorial e documentos externos.

## Classificacao

correta

---

# Teste 2 - Listagem de tarefas

## Pergunta

```text
Liste minhas tarefas
```

## Documentos recuperados

- tasks.json

## Resposta

O sistema listou corretamente tarefas pendentes armazenadas localmente.

## Classificacao

correta

---

# Teste 3 - Planejamento de estudos

## Pergunta

```text
Planeje meus estudos sobre transformers
```

## Documentos recuperados

- 04_transformers.txt
- agenda.json
- tasks.json

## Resposta

O sistema gerou plano de estudos utilizando materiais, agenda e tarefas.

## Classificacao

parcialmente correta

## Observacao

A resposta foi adequada, mas simplificada.

---

# Teste 4 - Active Recall

## Pergunta

```text
Gere uma pergunta sobre embeddings
```

## Documentos recuperados

- 02_embeddings.txt

## Resposta

O sistema gerou pergunta contextualizada para revisao ativa.

## Classificacao

correta

---

# Teste 5 - Busca semantica

## Pergunta

```text
Como funciona busca semantica?
```

## Documentos recuperados

- 05_busca_semantica.txt
- 02_embeddings.txt

## Resposta

O sistema explicou embeddings, similaridade vetorial e recuperacao contextual.

## Classificacao

correta

---

# Teste 6 - Consulta de agenda

## Pergunta

```text
O que tenho hoje na agenda?
```

## Documentos recuperados

- agenda.json

## Resposta

O sistema retornou corretamente eventos academicos cadastrados.

## Classificacao

correta

---

# Teste 7 - Geracao de exercicios

## Pergunta

```text
Gere exercicios sobre tool calling
```

## Documentos recuperados

- 03_tool_calling.txt

## Resposta

O sistema gerou exercicios relacionados a tool calling.

## Classificacao

parcialmente correta

## Observacao

A geracao depende da disponibilidade da LLM externa.

---

# Teste 8 - Avaliacao de respostas

## Pergunta

```text
Avalie uma resposta sobre embeddings
```

## Documentos recuperados

- 02_embeddings.txt

## Resposta

O sistema classificou coerencia e qualidade da resposta fornecida.

## Classificacao

correta

---

# Teste 9 - Registro de dificuldades

## Pergunta

```text
Registrar dificuldade sobre transformers
```

## Documentos recuperados

- difficulties.json

## Resposta

O sistema armazenou corretamente dificuldade relacionada ao tema.

## Classificacao

correta

---

# Teste 10 - Logs

## Pergunta

```text
Verificar logs do sistema
```

## Documentos recuperados

- logs.jsonl

## Resposta

O sistema registrou corretamente execucao das ferramentas.

## Classificacao

correta

---

# Analise geral

O sistema apresentou funcionamento adequado para:

- recuperacao semantica;
- embeddings;
- FAISS;
- tool calling;
- agenda academica;
- gerenciamento de tarefas;
- planejamento de estudos;
- active recall;
- logs;
- recuperacao contextual.

A arquitetura modular permitiu organizacao adequada dos componentes.

---

# Analise de erros

## Erro 1 - Encoding UTF-8

### Tipo

encoding/infraestrutura

### Problema

Caracteres acentuados causavam falhas em arquivos Python.

### Causa

Arquivos continham caracteres invalidos no Windows.

### Solucao

Padronizacao UTF-8 e remocao de caracteres invalidos.

---

## Erro 2 - Imports incorretos

### Tipo

arquitetura/importacao

### Problema

Alguns modulos utilizavam caminhos incorretos.

### Causa

Estrutura modular inicial estava inconsistente.

### Solucao

Reorganizacao dos imports e da arquitetura.

---

## Erro 3 - JSON bruto no tool calling

### Tipo

tool calling/orquestracao

### Problema

O sistema retornava apenas JSON sem executar ferramentas.

### Causa

O orchestrator nao interpretava corretamente a resposta da LLM.

### Solucao

Implementacao adequada do fluxo de tool calling.

---

## Erro 4 - API externa 502

### Tipo

infraestrutura/API externa

### Problema

Servidor da LLM retornava erro 502 Bad Gateway.

### Causa

Instabilidade do endpoint externo.

### Solucao

Implementacao de tratamento de excecao e repeticao de tentativa.

---

## Erro 5 - Token invalido 401

### Tipo

autenticacao/API externa

### Problema

A API rejeitou autenticacao da chave utilizada.

### Causa

Token invalido ou expirado.

### Solucao

Solicitar novo token valido da infraestrutura da disciplina.

---

# Limitacoes observadas

- dataset pequeno;
- ausencia de memoria conversacional;
- ausencia de reranking;
- dependencia de API externa;
- base documental sintetica.

---

# Conclusao

O projeto implementou um assistente academico baseado em RAG e tool calling utilizando Gemma 12B.

O sistema demonstrou:

- recuperacao semantica;
- embeddings vetoriais;
- indexacao FAISS;
- planejamento academico;
- active recall;
- logs;
- arquitetura modular;
- tratamento de erros;
- integracao com LLM externa.

Os testes realizados mostraram funcionamento adequado dos principais requisitos exigidos pelas diretrizes do trabalho.