from openai import OpenAI

from app.config import Config


class LLMClient:
    def __init__(self):
        if not Config.API_KEY:
            raise ValueError("Chave da LLM nao encontrada no .env.")

        self.client = OpenAI(
            base_url=Config.BASE_URL,
            api_key=Config.API_KEY,
            timeout=120
        )

    def generate(self, messages, temperature=0.3):
        try:
            response = self.client.chat.completions.create(
                model=Config.MODEL_NAME,
                messages=messages,
                temperature=temperature
            )

            return response.choices[0].message.content

        except Exception as error:
            return f"Erro ao acessar LLM externa: {error}"