from dataclasses import dataclass

from chatbot.constants import PRICE_CACHED_INPUT, PRICE_INPUT, PRICE_OUTPUT


def calculate_cost(input_tokens, cached_tokens, output_tokens):
    uncached_tokens = input_tokens - cached_tokens
    return (
        uncached_tokens * PRICE_INPUT
        + cached_tokens * PRICE_CACHED_INPUT
        + output_tokens * PRICE_OUTPUT
    ) / 1_000_000


@dataclass
class TokenUsage:
    input_tokens: int = 0
    cached_tokens: int = 0
    output_tokens: int = 0

    @classmethod
    def from_response(cls, response):
        usage = response.usage
        return cls(
            input_tokens=usage.input_tokens,
            cached_tokens=usage.input_tokens_details.cached_tokens,
            output_tokens=usage.output_tokens,
        )

    def add(self, other):
        self.input_tokens += other.input_tokens
        self.cached_tokens += other.cached_tokens
        self.output_tokens += other.output_tokens

    @property
    def cost(self):
        return calculate_cost(self.input_tokens, self.cached_tokens, self.output_tokens)
