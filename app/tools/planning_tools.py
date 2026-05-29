from app.llm_client import LLMClient
from app.tools.agenda_tools import consultar_agenda
from app.tools.rag_tools import buscar_material_rag
from app.tools.task_tools import listar_tarefas
from app.utils.logger import log_tool_call


def planejar_estudos(objetivo: str):
    agenda = consultar_agenda("semana")
    tarefas = listar_tarefas()
    materiais = buscar_material_rag(objetivo)

    messages = [
        {
            "role": "system",
            "content": (
                "Gerar plano de estudos academico objetivo. "
                "Considerar agenda, tarefas e materiais."
            )
        },
        {
            "role": "user",
            "content": (
                f"Objetivo: {objetivo}\n\n"
                f"Agenda: {agenda}\n\n"
                f"Tarefas: {tarefas}\n\n"
                f"Materiais: {materiais}"
            )
        }
    ]

    resposta = LLMClient().generate(messages)

    saida = {
        "objetivo": objetivo,
        "plano": resposta
    }

    log_tool_call("planejar_estudos", objetivo, saida)

    return saida