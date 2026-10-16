from chatbot.constants import MODEL


def print_usage(usage):
    print(
        f"[tokens: {usage.input_tokens} in ({usage.cached_tokens} cached), "
        f"{usage.output_tokens} out | ${usage.cost:.6f}]"
    )


def print_summary(total):
    print("\n--- Conversation summary ---")
    print(f"Model:         {MODEL}")
    print(f"Input tokens:  {total.input_tokens} ({total.cached_tokens} cached)")
    print(f"Output tokens: {total.output_tokens}")
    print(f"Total cost:    ${total.cost:.6f}")
