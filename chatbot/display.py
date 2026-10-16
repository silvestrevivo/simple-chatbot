from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.table import Table

from chatbot.constants import (
    BOT_COLOR,
    BOT_NAME,
    CODE_THEME,
    EXIT_COMMANDS,
    INFO_COLOR,
    MODEL,
    USER_COLOR,
    USER_LABEL,
)

console = Console()


def print_welcome():
    exit_words = " or ".join(f"'{word}'" for word in EXIT_COMMANDS)
    console.print(
        Panel(
            f"Hi! I'm [bold {BOT_COLOR}]{BOT_NAME}[/], your Python teacher.\n"
            f"Ask me anything about Python. Type {exit_words} to quit.",
            title=f"[bold]{BOT_NAME}[/]",
            border_style=BOT_COLOR,
        )
    )


def read_question():
    console.print()
    return console.input(
        f"[bold {USER_COLOR}]{USER_LABEL} ›[/] What do you want to know? "
    ).strip()


def thinking():
    return console.status(f"[{BOT_COLOR}]{BOT_NAME} is thinking...", spinner="dots")


def print_answer(text):
    console.print(
        Panel(
            Markdown(text, code_theme=CODE_THEME),
            title=f"[bold {BOT_COLOR}]{BOT_NAME}[/]",
            title_align="left",
            border_style=BOT_COLOR,
        )
    )


def print_summary(total):
    table = Table(show_header=False, box=None)
    table.add_column(style=INFO_COLOR)
    table.add_column(justify="right")
    table.add_row("Model", MODEL)
    table.add_row("Input tokens", f"{total.input_tokens} ({total.cached_tokens} cached)")
    table.add_row("Output tokens", str(total.output_tokens))
    table.add_row("Total cost", f"[bold]${total.cost:.6f}[/]")

    console.print()
    console.print(
        Panel(table, title="Conversation summary", border_style=INFO_COLOR, expand=False)
    )
    console.print(f"[{BOT_COLOR}]Bye! Keep coding.[/]")
