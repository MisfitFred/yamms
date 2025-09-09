# Copyright 2025 MisfitFred
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
