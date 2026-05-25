from app.llm_client import LLMClient
from app.rag.retriever import Retriever
from app.utils.logger import log_tool_call


def buscar_material_rag(pergunta: str):
    retriever = Retriever()
    trechos = retriever.retrieve(pergunta)

    contexto = "\n\n".join(
        [
            f"Fonte: {item['source']}\nTrecho: {item['content']}"
            for item in trechos
        ]
    )

    messages = [
        {
            "role": "system",
            "content": (
                "Responder usando apenas os trechos fornecidos. "
                "Indicar quando o contexto for insuficiente."
            )
        },
        {
            "role": "user",
            "content": f"Pergunta: {pergunta}\n\nContexto:\n{contexto}"
        }
    ]

    resposta = LLMClient().generate(messages)

    saida = {
        "pergunta": pergunta,
        "trechos": trechos,
        "resposta": resposta
    }

    log_tool_call("buscar_material_rag", pergunta, saida)

    return saida
