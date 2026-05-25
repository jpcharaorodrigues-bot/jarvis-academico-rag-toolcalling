import json
from pathlib import Path
from uuid import uuid4

from app.config import Config
from app.utils.logger import log_tool_call


def _load_tasks():
    path = Path(Config.TASKS_PATH)

    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("[]", encoding="utf-8")

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def _save_tasks(tasks):
    path = Path(Config.TASKS_PATH)

    with open(path, "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=2)


def adicionar_tarefa(descricao: str, prazo: str = ""):
    tasks = _load_tasks()

    tarefa = {
        "id": str(uuid4()),
        "descricao": descricao,
        "prazo": prazo,
        "concluida": False
    }

    tasks.append(tarefa)
    _save_tasks(tasks)

    log_tool_call("adicionar_tarefa", descricao, tarefa)

    return tarefa


def listar_tarefas(apenas_pendentes: bool = True):
    tasks = _load_tasks()

    if apenas_pendentes:
        tasks = [task for task in tasks if not task["concluida"]]

    saida = {
        "tarefas": tasks
    }

    log_tool_call("listar_tarefas", apenas_pendentes, saida)

    return saida


def concluir_tarefa(task_id: str):
    tasks = _load_tasks()
    encontrada = None

    for task in tasks:
        if task["id"] == task_id:
            task["concluida"] = True
            encontrada = task
            break

    if encontrada is None:
        raise ValueError("Tarefa não encontrada.")

    _save_tasks(tasks)

    log_tool_call("concluir_tarefa", task_id, encontrada)

    return encontrada
