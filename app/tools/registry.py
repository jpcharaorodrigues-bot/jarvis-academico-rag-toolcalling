from app.learning.active_recall import avaliar_resposta, gerar_pergunta_recall
from app.learning.difficulty_detector import listar_dificuldades, registrar_dificuldade
from app.learning.quiz_generator import gerar_exercicios
from app.tools.agenda_tools import consultar_agenda
from app.tools.planning_tools import planejar_estudos
from app.tools.rag_tools import buscar_material_rag
from app.tools.task_tools import adicionar_tarefa, concluir_tarefa, listar_tarefas


TOOLS = {
    "consultar_agenda": consultar_agenda,
    "listar_tarefas": listar_tarefas,
    "adicionar_tarefa": adicionar_tarefa,
    "concluir_tarefa": concluir_tarefa,
    "buscar_material_rag": buscar_material_rag,
    "planejar_estudos": planejar_estudos,
    "gerar_exercicios": gerar_exercicios,
    "gerar_pergunta_recall": gerar_pergunta_recall,
    "avaliar_resposta": avaliar_resposta,
    "registrar_dificuldade": registrar_dificuldade,
    "listar_dificuldades": listar_dificuldades
}


TOOL_DESCRIPTIONS = [
    {
        "name": "consultar_agenda",
        "description": "Consultar eventos acadêmicos por período.",
        "parameters": {"periodo": "hoje, amanha ou semana"}
    },
    {
        "name": "listar_tarefas",
        "description": "Listar tarefas acadêmicas.",
        "parameters": {"apenas_pendentes": "true ou false"}
    },
    {
        "name": "adicionar_tarefa",
        "description": "Adicionar tarefa acadêmica.",
        "parameters": {"descricao": "texto da tarefa", "prazo": "data opcional"}
    },
    {
        "name": "concluir_tarefa",
        "description": "Marcar tarefa como concluída.",
        "parameters": {"task_id": "identificador da tarefa"}
    },
    {
        "name": "buscar_material_rag",
        "description": "Buscar resposta nos materiais de estudo.",
        "parameters": {"pergunta": "pergunta sobre os materiais"}
    },
    {
        "name": "planejar_estudos",
        "description": "Gerar plano de estudos acadêmico.",
        "parameters": {"objetivo": "objetivo do estudo"}
    },
    {
        "name": "gerar_exercicios",
        "description": "Gerar exercícios sobre um tema.",
        "parameters": {"tema": "tema de estudo", "quantidade": "número de exercícios"}
    },
    {
        "name": "gerar_pergunta_recall",
        "description": "Gerar pergunta de revisão ativa.",
        "parameters": {"tema": "tema de estudo"}
    },
    {
        "name": "avaliar_resposta",
        "description": "Avaliar resposta do estudante.",
        "parameters": {
            "tema": "tema de estudo",
            "pergunta": "pergunta feita",
            "resposta_usuario": "resposta do estudante"
        }
    },
    {
        "name": "registrar_dificuldade",
        "description": "Registrar dificuldade identificada.",
        "parameters": {"tema": "tema", "avaliacao": "avaliação da dificuldade"}
    },
    {
        "name": "listar_dificuldades",
        "description": "Listar dificuldades registradas.",
        "parameters": {}
    }
]
