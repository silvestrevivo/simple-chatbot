from chatbot.client import ask, create_client
from chatbot.constants import EXIT_COMMANDS
from chatbot.display import print_summary
from chatbot.usage import TokenUsage


def main():
    client = create_client()
    previous_response_id = None
    total = TokenUsage()
    print("Type 'exit' to quit.")

    while True:
        try:
            question = input("\nWhat do you want to know? ").strip()
        except (EOFError, KeyboardInterrupt):
            break

        if question.lower() in EXIT_COMMANDS:
            break
        if not question:
            continue

        response = ask(client, question, previous_response_id)
        print(response.output_text)
        previous_response_id = response.id

        total.add(TokenUsage.from_response(response))

    print_summary(total)
    print("Bye!")


if __name__ == "__main__":
    main()
