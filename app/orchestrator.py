import json

from app.llm_client import LLMClient
from app.tools.registry import TOOLS, TOOL_DESCRIPTIONS


class Orchestrator:
    def __init__(self):
        self.llm = LLMClient()

    def handle(self, user_message: str):
        decision = self._decide_tool(user_message)

        tool_name = decision.get("tool")
        arguments = decision.get("arguments", {})

        if tool_name == "responder":
            return decision.get("answer", "")

        if tool_name not in TOOLS:
            return "Não foi possível selecionar uma ferramenta válida."

        result = TOOLS[tool_name](**arguments)

        return self._final_answer(user_message, tool_name, result)

    def _decide_tool(self, user_message: str):
        messages = [
            {
                "role": "system",
                "content": (
                    "Selecionar uma ferramenta para atender a solicitação. "
                    "Responder apenas em JSON válido. "
                    "Formato: {\"tool\": \"nome\", \"arguments\": {}}. "
                    "Usar responder apenas quando nenhuma ferramenta for necessária. "
                    f"Ferramentas: {json.dumps(TOOL_DESCRIPTIONS, ensure_ascii=False)}"
                )
            },
            {
                "role": "user",
                "content": user_message
            }
        ]

        response = self.llm.generate(messages, temperature=0)

        try:
            return json.loads(response)
        except json.JSONDecodeError:
            return {
                "tool": "responder",
                "answer": response
            }

    def _final_answer(self, user_message: str, tool_name: str, result):
        messages = [
            {
                "role": "system",
                "content": (
                    "Gerar resposta final clara e objetiva com base no resultado da ferramenta."
                )
            },
            {
                "role": "user",
                "content": (
                    f"Solicitação: {user_message}\n"
                    f"Ferramenta: {tool_name}\n"
                    f"Resultado: {json.dumps(result, ensure_ascii=False)}"
                )
            }
        ]

        return self.llm.generate(messages, temperature=0.3)
