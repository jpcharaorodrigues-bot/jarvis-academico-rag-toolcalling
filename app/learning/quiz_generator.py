from app.llm_client import LLMClient
from app.tools.rag_tools import buscar_material_rag


def gerar_exercicios(tema: str, quantidade: int = 3):
    material = buscar_material_rag(tema)

    messages = [
        {
            "role": "system",
            "content": "Gerar exercicios curtos com gabarito, usando apenas o material informado."
        },
        {
            "role": "user",
            "content": f"Tema: {tema}\nQuantidade: {quantidade}\nMaterial: {material}"
        }
    ]

    exercicios = LLMClient().generate(messages)

    return {
        "tema": tema,
        "quantidade": quantidade,
        "exercicios": exercicios
    }