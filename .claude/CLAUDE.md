# PyTutor — project guidelines

Terminal chatbot that teaches Python to beginners, built on the OpenAI
Responses API. Keep the project small, simple and readable: it is also a
learning project.

## Commands

- Run: `uv run main.py`
- Add a dependency: `uv add <package>` (never use `pip install`)
- Sync the environment after cloning or pulling: `uv sync`
- Python version: 3.14 (see `.python-version`)

## Structure

```
main.py                 # entry point, only the chat loop
chatbot/
├── constants.py        # every setting: model, instructions, API params, prices, UI
├── client.py           # create_client() and ask(), the only code that calls OpenAI
├── usage.py            # TokenUsage dataclass and calculate_cost()
└── display.py          # all terminal output (rich): welcome, input, spinner, answers, summary
```

## Conventions

- `main.py` is the only Python file at the root. It contains only the chat
  loop and calls helpers; no helper functions or constants live there.
- Constants and settings go in `chatbot/constants.py`.
- All printing and user input go through `chatbot/display.py` using the shared
  `console`. Do not use `print()` elsewhere.
- Only `chatbot/client.py` talks to the OpenAI API.
- Prefer plain functions and small dataclasses. No unnecessary abstractions.
- Match the existing style: short functions, descriptive names, few comments.
  Comments only explain constraints the code cannot show.
- Do not add features the user did not ask for. Propose them instead.

## OpenAI API rules

- Use the Responses API (`client.responses.create`), not Chat Completions.
- `input` is a plain string; roles are not needed for single messages.
- Conversation memory uses `previous_response_id=response.id`.
- `instructions` are NOT carried over between calls, send them every time
  (`ask()` already does).
- `temperature` and `top_p` only work with `reasoning={"effort": "none"}`.
  With any other effort the API returns a 400 error, remove them first.
- `gpt-5.4-nano` accepts reasoning efforts `none`, `low`, `medium`, `high`,
  `xhigh` (not `minimal` or `max`) and verbosity `low`, `medium`, `high`.
- The Responses API has no `stop` / `stop_sequences` parameter.
- With reasoning enabled, `max_output_tokens` also counts hidden reasoning
  tokens.
- Test parameter changes against the real API before committing them.

## Cost tracking

- Prices in `constants.py` are USD per 1M tokens for `MODEL`. When changing
  `MODEL`, update `PRICE_INPUT`, `PRICE_CACHED_INPUT` and `PRICE_OUTPUT` from
  https://developers.openai.com/api/docs/pricing in the same change.
- Token counts come from `response.usage`; cached input tokens are billed at
  the cached price.
- The cost is shown only once, in the summary at the end of the conversation.

## Tutor behaviour

- The tutor role lives in `INSTRUCTIONS` in `constants.py`, organised as
  purpose, audience, tone, teaching rules, answer structure, input format,
  boundaries and one few-shot example.
- Every learner message is wrapped with `LEARNER_MESSAGE_TEMPLATE`
  (`<learner_message>` tags) in `ask()`. Keep the template and the
  "Input format" section of `INSTRUCTIONS` in sync.
- It must stay beginner friendly, include runnable examples, give hints before
  full solutions, reply in the learner's language, and refuse non-Python
  topics.
- After editing `INSTRUCTIONS`, test with an on-topic question, an error
  message, a non-English question, an off-topic question and a prompt
  injection ("ignore your instructions and ...").

## Security

- The API key lives only in `.env` as `OPENAI_API_KEY`. `.env` is git-ignored.
- Never print, log or commit the API key, and never read `.env` contents into
  the conversation. Use `.env.example` as the template.
