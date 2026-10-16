# PyTutor

A terminal chatbot that teaches Python to beginners. It uses the
[OpenAI Responses API](https://developers.openai.com/api/docs), remembers the
conversation, and shows how many tokens you used and what it cost when you
finish.

```
╭────────────────────────── PyTutor ───────────────────────────╮
│ Hi! I'm PyTutor, your Python teacher.                        │
│ Ask me anything about Python. Type 'exit' or 'quit' to quit. │
╰──────────────────────────────────────────────────────────────╯

You › What do you want to know? How do I add two numbers?
╭─ PyTutor ────────────────────────────────────────────────────╮
│ In Python, you add two numbers with +.                       │
│                                                              │
│  a = 3                                                       │
│  b = 5                                                       │
│  print(a + b)                                                │
│                                                              │
│ Try it: What does print(10 + 2) output?                      │
╰──────────────────────────────────────────────────────────────╯

╭───── Conversation summary ──────╮
│  Model            gpt-5.4-nano  │
│  Input tokens   422 (0 cached)  │
│  Output tokens             108  │
│  Total cost          $0.000219  │
╰─────────────────────────────────╯
```

## Features

- Python tutor role: simple explanations, runnable examples, hints before
  solutions and small exercises.
- Replies in the language you write in.
- Stays on topic: politely declines questions that are not about Python.
- Remembers the conversation.
- Colored terminal UI with formatted Markdown and syntax-highlighted code.
- Token and cost summary at the end of each conversation.

## Requirements

- [uv](https://docs.astral.sh/uv/)
- An [OpenAI API key](https://platform.openai.com/api-keys)

uv installs the right Python version (3.14) and all dependencies for you.

## Setup

```bash
uv sync
cp .env.example .env
```

Then open `.env` and add your key:

```
OPENAI_API_KEY=sk-...
```

`.env` is git-ignored, so your key is never committed.

## Usage

```bash
uv run main.py
```

Type your question and press Enter. Type `exit` or `quit` (or press `Ctrl+C`)
to end the conversation and see the cost summary.

## Project structure

```
main.py                 # entry point: the chat loop
chatbot/
├── constants.py        # all settings: model, tutor role, API params, prices, colors
├── client.py           # creates the OpenAI client and sends questions
├── usage.py            # counts tokens and calculates the cost
└── display.py          # terminal UI (rich)
```

## Configuration

Everything is set in `chatbot/constants.py`:

| Setting | What it does |
| --- | --- |
| `MODEL` | OpenAI model used (default `gpt-5.4-nano`) |
| `INSTRUCTIONS` | The tutor's role and teaching rules |
| `MODEL_PARAMS` | API parameters: reasoning, temperature, verbosity, max tokens |
| `PRICE_*` | Model prices in USD per 1M tokens, used for the cost summary |
| `EXIT_COMMANDS` | Words that end the conversation |
| `*_COLOR`, `CODE_THEME` | Terminal colors and code highlighting theme |

### API parameters

- `reasoning={"effort": "none"}`: answers directly, without thinking first.
  Fast and cheap.
- `temperature`: randomness of the answers (0 = predictable, higher = more
  varied).
- `top_p`: alternative randomness control, left at `1.0` (off).
- `text={"verbosity": "low"}`: keeps answers short.
- `max_output_tokens`: hard limit on answer length.

`temperature` and `top_p` only work while reasoning effort is `"none"`. If you
enable reasoning, remove them.

### Changing the model

When you change `MODEL`, also update the `PRICE_*` values from the
[OpenAI pricing page](https://developers.openai.com/api/docs/pricing),
otherwise the cost summary will be wrong.

## Cost tracking

Each API response reports its input, cached input and output tokens. PyTutor
adds them up and calculates the cost with the prices in `constants.py`. The
whole conversation history counts as input on every question, so long
conversations cost a bit more per question.

The cost is an estimate based on published prices. Your
[OpenAI usage dashboard](https://platform.openai.com/usage) has the exact
amount.
