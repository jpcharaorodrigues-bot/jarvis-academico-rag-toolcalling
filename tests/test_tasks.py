from app.tools.task_tools import adicionar_tarefa, listar_tarefas


def test_adicionar_e_listar_tarefa():
    tarefa = adicionar_tarefa("Estudar embeddings", "2026-05-30")
    tarefas = listar_tarefas()

    assert tarefa["descricao"] == "Estudar embeddings"
    assert tarefa["concluida"] is False
    assert "tarefas" in tarefas
