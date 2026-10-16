import os

from dotenv import load_dotenv
from openai import OpenAI

from chatbot.constants import INSTRUCTIONS, MODEL, MODEL_PARAMS


def create_client():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    print(f"OPENAI_API_KEY: {api_key}")
    return OpenAI(api_key=api_key)


def ask(client, question, previous_response_id=None):
    return client.responses.create(
        model=MODEL,
        instructions=INSTRUCTIONS,
        input=question,
        previous_response_id=previous_response_id,
        **MODEL_PARAMS,
    )
