MODEL = "gpt-5.4-nano"

INSTRUCTIONS = (
    "You are a helpful Python teacher and assistant. Answer clearly and concisely."
)

# temperature and top_p are only accepted while reasoning effort is "none".
MODEL_PARAMS = {
    "reasoning": {"effort": "none"},
    "temperature": 0.7,
    "top_p": 1.0,
    "text": {"verbosity": "low"},
    "max_output_tokens": 500,
}

# USD per 1 million tokens for MODEL, from https://developers.openai.com/api/docs/pricing
PRICE_INPUT = 0.20
PRICE_CACHED_INPUT = 0.02
PRICE_OUTPUT = 1.25

EXIT_COMMANDS = ("exit", "quit")
