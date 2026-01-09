import os
from openai import OpenAI


class LLM:
    def __init__(self, model: str = "gpt-4.1-mini"):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = model

    def answer(self, question: str, context: str) -> str:
        prompt = f"""
You are an AI assistant.
Answer the question using ONLY the context below.
If the answer is not in the context, say "I don't know".

Context:
{context}

Question:
{question}
"""

        response = self.client.responses.create(
            model=self.model,
            input=prompt,
        )

        return response.output_text.strip()
