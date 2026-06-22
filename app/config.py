import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    MODEL_NAME = "Qwen/Qwen2.5-14B-Instruct-AWQ"
    BASE_URL = "https://llm.liaufms.org/v1/qwen2-5-14b-instruct-awq"
    API_KEY = os.getenv("GEMMA_API_KEY")

    DATA_PATH = "data"
    AGENDA_PATH = "data/agenda.json"
    TASKS_PATH = "data/tasks.json"
    LOGS_PATH = "data/logs.jsonl"
    DOCUMENTS_PATH = "data/documents"
    VECTOR_STORE_PATH = "data/vector_store"

    CHUNK_SIZE = 500
    CHUNK_OVERLAP = 50
    MAX_CONTEXT_DOCUMENTS = 5