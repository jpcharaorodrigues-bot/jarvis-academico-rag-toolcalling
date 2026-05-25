import json
from datetime import date, datetime, timedelta
from pathlib import Path

from app.config import Config
from app.utils.logger import log_tool_call


def _load_agenda():
    path = Path(Config.AGENDA_PATH)

    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("[]", encoding="utf-8")

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def consultar_agenda(periodo: str = "hoje"):
    agenda = _load_agenda()
    hoje = date.today()

    if periodo == "amanha":
        inicio = hoje + timedelta(days=1)
        fim = inicio
    elif periodo == "semana":
        inicio = hoje
        fim = hoje + timedelta(days=7)
    else:
        inicio = hoje
        fim = hoje

    eventos = []

    for item in agenda:
        data_item = datetime.strptime(item["data"], "%Y-%m-%d").date()

        if inicio <= data_item <= fim:
            eventos.append(item)

    saida = {
        "periodo": periodo,
        "eventos": eventos
    }

    log_tool_call("consultar_agenda", periodo, saida)

    return saida
