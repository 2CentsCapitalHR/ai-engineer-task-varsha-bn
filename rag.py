# rag.py
# Placeholder helpers for RAG workflows.
# For the take-home, this file contains helper functions that can be extended to:
# - convert ADGM PDFs to text,
# - create embeddings (OpenAI or sentence-transformers),
# - index with FAISS, and
# - retrieve context for LLM prompts.
#
# This is intentionally minimal for offline demo.

from typing import List

def embed_texts(texts: List[str], use_openai: bool = False, openai_api_key: str = None):
    # In a real deployment, either call OpenAI embeddings or sentence-transformers
    raise NotImplementedError("Implement embedding logic depending on your provider.")

class SimpleIndex:
    def __init__(self):
        self.texts = []
    def add(self, texts: List[str]):
        self.texts.extend(texts)
    def search(self, query: str, k=3):
        # naive substring search
        results = []
        q = query.lower()
        for t in self.texts:
            if q in t.lower():
                results.append(t)
        return results[:k]
