from app.tools.agenda_tools import consultar_agenda
from app.tools.rag_tools import buscar_material_rag
from app.tools.task_tools import adicionar_tarefa, concluir_tarefa, listar_tarefas


TOOLS = {
    "consultar_agenda": consultar_agenda,
    "listar_tarefas": listar_tarefas,
    "adicionar_tarefa": adicionar_tarefa,
    "concluir_tarefa": concluir_tarefa,
    "buscar_material_rag": buscar_material_rag
}


TOOL_DESCRIPTIONS = [
    {
        "name": "consultar_agenda",
        "description": "Consultar eventos acadêmicos por período.",
        "parameters": {
            "periodo": "hoje, amanha ou semana"
        }
    },
    {
        "name": "listar_tarefas",
        "description": "Listar tarefas acadêmicas.",
        "parameters": {
            "apenas_pendentes": "true ou false"
        }
    },
    {
        "name": "adicionar_tarefa",
        "description": "Adicionar tarefa acadêmica.",
        "parameters": {
            "descricao": "texto da tarefa",
            "prazo": "data opcional"
        }
    },
    {
        "name": "concluir_tarefa",
        "description": "Marcar tarefa como concluída.",
        "parameters": {
            "task_id": "identificador da tarefa"
        }
    },
    {
        "name": "buscar_material_rag",
        "description": "Buscar resposta nos materiais de estudo.",
        "parameters": {
            "pergunta": "pergunta sobre os materiais"
        }
    }
]
