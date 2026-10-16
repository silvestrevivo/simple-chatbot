import os

from dotenv import load_dotenv
from openai import OpenAI


def main():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    print(f"OPENAI_API_KEY: {api_key}")

    client = OpenAI(api_key=api_key)

    question = input("What do you want to know? ")
    response = client.responses.create(
        model="gpt-5.4-nano",
        instructions="You are a helpful assistant. Answer clearly and concisely.",
        input=question,
        reasoning={"effort": "none"},
        temperature=0.7,
        top_p=1.0,
        text={"verbosity": "low"},
        max_output_tokens=500,
    )
    print(response.output_text)


if __name__ == "__main__":
    main()
