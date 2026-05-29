# RELATORIO TECNICO - JARVIS ACADEMICO

## 1. Introducao

O projeto JARVIS Academico implementa um assistente academico baseado em Retrieval-Augmented Generation (RAG), embeddings vetoriais e tool calling utilizando Large Language Models.

O objetivo principal foi desenvolver um sistema capaz de recuperar materiais de estudo, responder perguntas contextualizadas, auxiliar organizacao academica e apoiar revisao ativa de conteudos.

O sistema integra recuperacao semantica, gerenciamento de tarefas, agenda academica, planejamento de estudos e funcionalidades voltadas ao aprendizado.

---

# 2. Objetivos do projeto

Os principais objetivos do sistema foram:

- implementar pipeline RAG completo;
- utilizar embeddings vetoriais;
- aplicar recuperacao semantica;
- integrar tool calling com LLM;
- criar ferramentas academicas;
- desenvolver planejamento de estudos;
- implementar active recall;
- registrar logs de execucao;
- organizar arquitetura modular.

---

# 3. Arquitetura do sistema

O sistema foi dividido em modulos independentes para facilitar manutencao, expansao e organizacao do codigo.

## Estrutura principal

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
├── vector_store/

tests/
```

## Modulos implementados

### RAG
Responsavel por:
- carregamento documental;
- chunking;
- embeddings;
- indexacao vetorial;
- recuperacao semantica.

### Tool calling
Responsavel por:
- selecao automatica de ferramentas;
- execucao de funcoes;
- orquestracao entre LLM e sistema interno.

### Learning
Responsavel por:
- active recall;
- avaliacao de respostas;
- deteccao de dificuldades;
- geracao de exercicios.

### Agenda e tarefas
Responsavel por:
- gerenciamento academico;
- consulta de agenda;
- planejamento de estudos.

---

# 4. Implementacao do RAG

O sistema implementa um pipeline RAG completo.

## Fluxo de funcionamento

1. carregar documentos;
2. dividir documentos em chunks;
3. gerar embeddings vetoriais;
4. armazenar embeddings em indice FAISS;
5. recuperar trechos relevantes;
6. gerar resposta contextualizada utilizando LLM.

## Embeddings

Os embeddings foram gerados utilizando Sentence Transformers.

Os vetores representam semanticamente os documentos e permitem comparacao contextual entre perguntas e materiais armazenados.

## Busca semantica

A recuperacao utiliza similaridade vetorial para localizar os chunks semanticamente mais proximos da pergunta realizada pelo usuario.

## FAISS

O armazenamento vetorial foi realizado utilizando FAISS.

Arquivos gerados:

```text
data/vector_store/index.faiss
data/vector_store/metadata.json
```

---

# 5. Tool Calling

O sistema utiliza tool calling para permitir que a LLM selecione ferramentas automaticamente.

A decisao da ferramenta ocorre em formato JSON.

Exemplo:

```json
{
  "tool": "buscar_material_rag",
  "arguments": {
    "pergunta": "O que e RAG?"
  }
}
```

O orquestrador interpreta a resposta da LLM, executa a ferramenta correspondente e gera resposta final contextualizada.

## Ferramentas implementadas

- consultar_agenda
- listar_tarefas
- adicionar_tarefa
- concluir_tarefa
- buscar_material_rag
- planejar_estudos
- gerar_exercicios
- gerar_pergunta_recall
- avaliar_resposta
- registrar_dificuldade
- listar_dificuldades

---

# 6. Dataset

O dataset utilizado esta localizado em:

```text
data/documents
```

Foram criados 10 documentos academicos relacionados a:

- RAG;
- embeddings;
- transformers;
- busca semantica;
- chunking;
- modelos de linguagem;
- tool calling;
- active recall;
- avaliacao de RAG;
- planejamento de estudos.

Os documentos foram utilizados para testes de recuperacao semantica e geracao contextual.

## Chunking

Os documentos sao divididos em chunks menores antes da indexacao vetorial.

O chunking reduz excesso de contexto irrelevante e melhora qualidade da recuperacao.

---

# 7. Funcionalidades implementadas

## Recuperacao semantica

O sistema responde perguntas utilizando materiais indexados no RAG.

Teste realizado:

```text
Explique o que e RAG
```

Resultado:
- recuperacao correta de contexto;
- resposta contextualizada.

## Agenda academica

A agenda academica e armazenada em JSON.

Arquivo:

```text
data/agenda.json
```

## Gerenciamento de tarefas

As tarefas sao armazenadas em:

```text
data/tasks.json
```

Teste realizado:

```text
Liste minhas tarefas
```

Resultado:
- listagem correta das tarefas pendentes.

## Planejamento de estudos

Teste realizado:

```text
Planeje meus estudos sobre transformers
```

Resultado:
- plano de estudos contextualizado;
- utilizacao de materiais recuperados;
- integracao com agenda e tarefas.

## Active Recall

Teste realizado:

```text
Gere uma pergunta sobre embeddings
```

Resultado:
- geracao automatica de pergunta de revisao ativa.

---

# 8. Logs

O sistema registra logs de execucao em:

```text
data/logs.jsonl
```

Os logs armazenam:
- ferramenta utilizada;
- entrada recebida;
- resposta produzida;
- horario de execucao.

---

# 9. Testes realizados

Foram realizados testes de:

- recuperacao RAG;
- chunking;
- tarefas;
- agenda;
- tool calling;
- planejamento;
- active recall.

Arquivos de teste:

```text
tests/test_agenda.py
tests/test_chunker.py
tests/test_tasks.py
```

---

# 10. Analise de erros

Durante o desenvolvimento ocorreram diferentes problemas tecnicos.

## Erro de encoding UTF-8

Alguns arquivos continham caracteres invalidos no Windows.

Problema:
- caracteres acentuados quebravam arquivos Python.

Solucao:
- remover acentos de arquivos `.py`;
- utilizar UTF-8 corretamente em `.txt` e `.md`.

## Erros de importacao

Ocorreram erros de importacao entre modulos.

Problema:
- imports apontavam para caminhos incorretos.

Solucao:
- reorganizacao dos imports;
- padronizacao da estrutura modular.

## Erros no tool calling

Inicialmente o sistema retornava apenas JSON bruto.

Problema:
- o orchestrator nao executava corretamente as ferramentas.

Solucao:
- tratamento adequado do JSON;
- execucao automatica das funcoes selecionadas.

---

# 11. Limitacoes

O sistema possui algumas limitacoes.

## Dataset sintetico

Os documentos foram criados especificamente para validacao inicial do sistema.

## Base documental pequena

O numero de documentos ainda e reduzido para cenarios reais.

## Sem memoria conversacional

O sistema nao possui memoria persistente entre conversas.

## Sem reranking

Nao foi implementado reranking adicional de documentos recuperados.

---

# 12. Melhorias futuras

Melhorias futuras incluem:

- ampliacao do dataset;
- uso de PDFs reais;
- memoria conversacional;
- reranking;
- interface grafica;
- testes automatizados mais avancados;
- persistencia de usuarios;
- dashboards de acompanhamento academico.

---

# 13. Ferramentas utilizadas

Durante o desenvolvimento foram utilizadas:

- Python;
- FAISS;
- Sentence Transformers;
- OpenAI SDK;
- Gemma 3;
- VSCode;
- GitHub;
- ChatGPT.

---

# 14. Conclusao

O projeto implementou um assistente academico funcional baseado em RAG e tool calling.

O sistema demonstrou:
- recuperacao semantica;
- integracao com embeddings;
- indexacao vetorial;
- planejamento academico;
- active recall;
- gerenciamento de tarefas;
- logs de execucao;
- arquitetura modular.

A implementacao permite expansao futura para novos recursos relacionados a apoio academico baseado em inteligencia artificial.