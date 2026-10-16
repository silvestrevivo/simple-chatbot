from chatbot.client import ask, create_client
from chatbot.constants import EXIT_COMMANDS
from chatbot.display import print_answer, print_summary, print_welcome, read_question, thinking
from chatbot.usage import TokenUsage


def main():
    client = create_client()
    previous_response_id = None
    total = TokenUsage()
    print_welcome()

    while True:
        try:
            question = read_question()
        except (EOFError, KeyboardInterrupt):
            break

        if question.lower() in EXIT_COMMANDS:
            break
        if not question:
            continue

        with thinking():
            response = ask(client, question, previous_response_id)
        print_answer(response.output_text)
        previous_response_id = response.id

        total.add(TokenUsage.from_response(response))

    print_summary(total)


if __name__ == "__main__":
    main()
