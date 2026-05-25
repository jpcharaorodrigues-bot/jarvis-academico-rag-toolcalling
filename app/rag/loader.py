from pathlib import Path
from typing import Dict, List

from pypdf import PdfReader


class DocumentLoader:
    def load_documents(self, documents_path: str) -> List[Dict[str, str]]:
        path = Path(documents_path)

        if not path.exists():
            raise FileNotFoundError(f"Pasta não encontrada: {documents_path}")

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
        return {
            "source": file.name,
            "content": file.read_text(encoding="utf-8", errors="ignore")
        }

    def _load_pdf(self, file: Path) -> Dict[str, str]:
        text = ""
        reader = PdfReader(str(file))

        for page in reader.pages:
            extracted = page.extract_text()

            if extracted:
                text += extracted + "\n"

        return {
            "source": file.name,
            "content": text
        }
