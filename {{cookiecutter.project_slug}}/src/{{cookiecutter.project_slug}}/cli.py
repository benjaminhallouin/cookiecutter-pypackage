{% if cookiecutter.include_cli == "yes" -%}
{% if cookiecutter.command_line_interface == "Click" -%}
"""Command-line interface for {{ cookiecutter.project_slug }}."""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

import click
from rich.console import Console

from {{ cookiecutter.project_slug }} import __version__

if TYPE_CHECKING:
    from typing import Any

console = Console()


@click.group()
@click.version_option(version=__version__, prog_name="{{ cookiecutter.project_slug }}")
@click.option("-v", "--verbose", is_flag=True, help="Enable verbose output")
@click.pass_context
def cli(ctx: click.Context, *, verbose: bool) -> None:
    """{{ cookiecutter.project_short_description }}"""
    ctx.ensure_object(dict)
    ctx.obj["verbose"] = verbose


@cli.command()
@click.argument("name", type=str)
@click.pass_context
def hello(ctx: click.Context, name: str) -> None:
    """Say hello to NAME."""
    verbose = ctx.obj["verbose"]
    if verbose:
        console.print(f"[bold green]Verbose mode enabled[/bold green]")
    console.print(f"Hello, {name}!")


def main() -> int:
    """Execute the CLI."""
    try:
        cli(obj={})
        return 0
    except Exception as e:  # noqa: BLE001
        console.print(f"[bold red]Error:[/bold red] {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
{% elif cookiecutter.command_line_interface == "Typer" -%}
"""Command-line interface for {{ cookiecutter.project_slug }}."""

from __future__ import annotations

import sys
from typing import Annotated

import typer
from rich.console import Console

from {{ cookiecutter.project_slug }} import __version__

app = typer.Typer(
    name="{{ cookiecutter.project_slug }}",
    help="{{ cookiecutter.project_short_description }}",
    add_completion=True,
)
console = Console()


def version_callback(*, value: bool) -> None:
    """Print version and exit."""
    if value:
        console.print(f"{{ cookiecutter.project_slug }} version: {__version__}")
        raise typer.Exit


@app.callback()
def main(
    version: Annotated[
        bool | None,
        typer.Option("--version", callback=version_callback, is_eager=True),
    ] = None,
    verbose: Annotated[bool, typer.Option("--verbose", "-v")] = False,
) -> None:
    """{{ cookiecutter.project_short_description }}"""
    if verbose:
        console.print("[bold green]Verbose mode enabled[/bold green]")


@app.command()
def hello(name: Annotated[str, typer.Argument(help="Name to greet")]) -> None:
    """Say hello to NAME."""
    console.print(f"Hello, {name}!")


def cli() -> int:
    """Execute the CLI."""
    try:
        app()
        return 0
    except Exception as e:  # noqa: BLE001
        console.print(f"[bold red]Error:[/bold red] {e}")
        return 1


if __name__ == "__main__":
    sys.exit(cli())
{% endif -%}
{% endif -%}
