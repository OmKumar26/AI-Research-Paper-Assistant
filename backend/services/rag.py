import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_answer(query, context):

    prompt = f"""
You are an AI Research Paper Assistant.

Answer ONLY using the retrieved context below.

If the answer cannot be found in the context, reply:

"I couldn't find this information in the uploaded paper."

Be concise.

Do not make up information.

Context:
{context}

Question:
{query}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text