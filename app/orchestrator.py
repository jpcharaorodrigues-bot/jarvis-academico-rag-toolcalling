import json

from app.llm_client import LLMClient
from app.tools.registry import TOOLS, TOOL_DESCRIPTIONS


class Orchestrator:
    def __init__(self):
        self.llm = LLMClient()

    def handle(self, user_message: str):
        fallback = self._fallback_tool(user_message)

        if fallback:
            tool_name, arguments = fallback

            try:
                result = TOOLS[tool_name](**arguments)
            except Exception as error:
                return f"Erro ao executar ferramenta: {error}"

            return self._format_local_answer(tool_name, result)

        decision = self._decide_tool(user_message)

        if decision.get("tool") == "erro":
            return decision.get("answer")

        tool_name = decision.get("tool")
        arguments = decision.get("arguments", {})

        if tool_name not in TOOLS:
            return "Ferramenta invalida."

        try:
            result = TOOLS[tool_name](**arguments)
        except Exception as error:
            return f"Erro ao executar ferramenta: {error}"

        return self._generate_final_answer(user_message, tool_name, result)

    def _fallback_tool(self, user_message: str):
        text = user_message.lower()

        if "liste" in text and "tarefa" in text:
            return "listar_tarefas", {}

        if "agenda" in text or "hoje" in text or "amanha" in text or "semana" in text:
            return "consultar_agenda", {"periodo": "semana"}

        if "rag" in text or "busca semantica" in text or "embedding" in text or "embeddings" in text:
            return "buscar_material_rag", {"pergunta": user_message}

        return None

    def _format_local_answer(self, tool_name: str, result):
        if tool_name == "listar_tarefas":
            tarefas = result.get("tarefas", [])

            if not tarefas:
                return "Nao ha tarefas pendentes."

            linhas = ["Tarefas pendentes:"]

            for tarefa in tarefas:
                descricao = tarefa.get("descricao", "")
                prazo = tarefa.get("prazo", "")
                linhas.append(f"- {descricao} | prazo: {prazo}")

            return "\n".join(linhas)

        if tool_name == "consultar_agenda":
            eventos = result.get("eventos", [])

            if not eventos:
                return "Nao ha eventos encontrados na agenda."

            linhas = ["Eventos encontrados:"]

            for evento in eventos:
                data = evento.get("data", "")
                hora = evento.get("hora", "")
                titulo = evento.get("titulo", "")
                linhas.append(f"- {data} {hora} | {titulo}")

            return "\n".join(linhas)

        if tool_name == "buscar_material_rag":
            return str(result)

        return json.dumps(result, ensure_ascii=False, indent=2)

    def _decide_tool(self, user_message: str):
        messages = [
            {
                "role": "system",
                "content": (
                    "Selecionar a ferramenta correta. "
                    "Responder apenas JSON valido. "
                    "Formato: {\"tool\":\"nome\",\"arguments\":{}} "
                    f"Ferramentas: {json.dumps(TOOL_DESCRIPTIONS, ensure_ascii=False)}"
                )
            },
            {
                "role": "user",
                "content": user_message
            }
        ]

        response = self.llm.generate(messages, temperature=0)
        response = response.strip()

        if response.startswith("Erro ao acessar LLM externa"):
            return {
                "tool": "erro",
                "answer": response
            }

        if response.startswith("```json"):
            response = response.replace("```json", "")
            response = response.replace("```", "")
            response = response.strip()

        try:
            return json.loads(response)
        except json.JSONDecodeError:
            return {
                "tool": "erro",
                "answer": f"Resposta invalida da LLM externa: {response}"
            }

    def _generate_final_answer(self, user_message: str, tool_name: str, result):
        messages = [
            {
                "role": "system",
                "content": (
                    "Responder de forma clara e objetiva "
                    "utilizando o resultado da ferramenta."
                )
            },
            {
                "role": "user",
                "content": (
                    f"Pergunta: {user_message}\n"
                    f"Ferramenta: {tool_name}\n"
                    f"Resultado: {json.dumps(result, ensure_ascii=False)}"
                )
            }
        ]

        return self.llm.generate(messages, temperature=0.3)