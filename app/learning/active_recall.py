from app.llm_client import LLMClient
from app.tools.rag_tools import buscar_material_rag


def gerar_pergunta_recall(tema: str):
    material = buscar_material_rag(tema)

    messages = [
        {
            "role": "system",
            "content": "Gerar uma pergunta curta de revisao ativa com base no material."
        },
        {
            "role": "user",
            "content": f"Tema: {tema}\nMaterial: {material}"
        }
    ]

    pergunta = LLMClient().generate(messages)

    return {
        "tema": tema,
        "pergunta": pergunta
    }


def avaliar_resposta(tema: str, pergunta: str, resposta_usuario: str):
    material = buscar_material_rag(tema)

    messages = [
        {
            "role": "system",
            "content": "Avaliar resposta do estudante. Classificar como correta, parcial ou incorreta."
        },
        {
            "role": "user",
            "content": (
                f"Tema: {tema}\n"
                f"Pergunta: {pergunta}\n"
                f"Resposta do estudante: {resposta_usuario}\n"
                f"Material: {material}"
            )
        }
    ]

    avaliacao = LLMClient().generate(messages)

    return {
        "tema": tema,
        "pergunta": pergunta,
        "resposta_usuario": resposta_usuario,
        "avaliacao": avaliacao
    }