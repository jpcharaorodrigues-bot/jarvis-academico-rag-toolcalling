from pathlib import Path
from typing import Dict, List

from pypdf import PdfReader


class DocumentLoader:
    """
    Responsável por carregar documentos acadêmicos usados pelo RAG.

    Formatos suportados:
    - .txt
    - .pdf

    Cada documento carregado é retornado como um dicionário contendo:
    - source: nome do arquivo
    - content: texto extraído
    """

    def load_documents(self, documents_path: str) -> List[Dict[str, str]]:
        path = Path(documents_path)

        if not path.exists():
            raise FileNotFoundError(f"Pasta de documentos não encontrada: {documents_path}")

        documents = []

        for file in path.glob("*"):
            if file.is_dir():
                continue

            if file.suffix.lower() == ".txt":
                documents.append(self._load_txt(file))

            elif file.suffix.lower() == ".pdf":
                documents.append(self._load_pdf(file))

        return documents

    def _load_txt(self, file: Path) -> Dict[str, str]:
        content = file.read_text(
            encoding="utf-8",
            errors="ignore"
        )

        return {
            "source": file.name,
            "content": content
        }

    def _load_pdf(self, file: Path) -> Dict[str, str]:
        text = ""

        reader = PdfReader(str(file))

        for page in reader.pages:
            extracted_text = page.extract_text()

            if extracted_text:
                text += extracted_text + "\n"

        return {
            "source": file.name,
            "content": text
        }
