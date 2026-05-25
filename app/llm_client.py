from openai import OpenAI

from app.config import Config


class LLMClient:
    def __init__(self):
        if not Config.API_KEY:
            raise ValueError(
                "A variável GEMMA_API_KEY não foi encontrada. "
                "Crie um arquivo .env com GEMMA_API_KEY=sua_chave."
            )

        self.client = OpenAI(
            base_url=Config.BASE_URL,
            api_key=Config.API_KEY
        )

    def generate(self, messages, temperature=0.3):
        response = self.client.chat.completions.create(
            model=Config.MODEL_NAME,
            messages=messages,
            temperature=temperature
        )

        return response.choices[0].message.content
