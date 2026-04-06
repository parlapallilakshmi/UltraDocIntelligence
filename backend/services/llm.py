import google.generativeai as genai
import os


genai.configure(api_key="AIzaSyC7Jd4hqCk457rdmtH66dtzlHifehShlaQ")
model = genai.GenerativeModel("gemini-2.5-flash")


def generate_answer(context, question):
    prompt = f"""
    You are a logistics AI assistant.

    Use the context strictly.

    Also understand synonyms like:
    - shipment id = load id
    - pickup datetime = pickup date + time

    Context:
    {context}

    Question:
    {question}
    """

    response = model.generate_content(prompt)
    return response.text