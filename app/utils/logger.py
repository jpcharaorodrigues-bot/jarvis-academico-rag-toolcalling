import json
from datetime import datetime
from pathlib import Path

from app.config import Config


def log_tool_call(tool_name, tool_input, tool_output):
    Path(Config.DATA_PATH).mkdir(exist_ok=True)

    log_record = {
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "tool": tool_name,
        "input": tool_input,
        "output": tool_output
    }

    with open(Config.LOGS_PATH, "a", encoding="utf-8") as file:
        file.write(json.dumps(log_record, ensure_ascii=False) + "\n")
