import json
from pathlib import Path

from app.config import Config


def registrar_dificuldade(tema: str, avaliacao: str):
    path = Path(Config.DATA_PATH) / "difficulties.json"

    if not path.exists():
        path.write_text("[]", encoding="utf-8")

    with open(path, "r", encoding="utf-8") as file:
        dados = json.load(file)

    registro = {
        "tema": tema,
        "avaliacao": avaliacao
    }

    dados.append(registro)

    with open(path, "w", encoding="utf-8") as file:
        json.dump(dados, file, ensure_ascii=False, indent=2)

    return registro


def listar_dificuldades():
    path = Path(Config.DATA_PATH) / "difficulties.json"

    if not path.exists():
        return []

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)
