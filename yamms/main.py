"""YAMMS Hauptanwendung."""

import sys

from rich.console import Console

from .config import get_settings


def main(args: list[str] | None = None) -> int:
    """Haupteinstiegspunkt für YAMMS.

    Args:
        args: Kommandozeilenargumente (optional, für Tests)

    Returns:
        Exit-Code (0 bei Erfolg)
    """
    console = Console()
    console.print("[bold green]YAMMS - Yet Another Mark Management System[/bold green]")
    console.print("Version: 0.1.0")
    console.print()

    settings = get_settings()
    console.print(f"Datenbank: {settings.database_url}")
    console.print(f"Debug-Modus: {settings.debug}")

    # TODO: Implementierung der Hauptanwendung
    console.print("[yellow]Implementierung folgt...[/yellow]")

    return 0


if __name__ == "__main__":
    sys.exit(main())
