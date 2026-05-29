# Dataset

O dataset contém 10 documentos em texto sobre Inteligência Artificial aplicada ao JARVIS Acadêmico.

## Origem

Textos técnicos autorais produzidos para validação do sistema RAG.

## Tipo de conteúdo

- RAG
- embeddings
- tool calling
- transformers
- busca semântica
- chunking
- modelos de linguagem
- avaliação de RAG
- active recall
- planejamento de estudos

## Limitações

Os documentos são sintéticos e controlados. Servem para testar recuperação semântica, geração de respostas e avaliação inicial. Para uso em cenário real, recomenda-se incluir PDFs de aula, anotações da disciplina e artigos acadêmicos.

## Estratégia de chunking

O sistema utiliza tamanho de chunk definido em `CHUNK_SIZE` e sobreposição definida em `CHUNK_OVERLAP`.

## Impacto no RAG

O chunking divide documentos em trechos menores, melhora a recuperação semântica e reduz envio de contexto irrelevante para a LLM. A sobreposição preserva continuidade entre trechos consecutivos.