# YAMMS - Yet Another Mark Management System

Ein lokales, DSGVO-freundliches Notenverwaltungstool für Lehrkräfte.

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Documentation Status](https://readthedocs.org/projects/yamms/badge/?version=latest)](https://yamms.readthedocs.io/en/latest/?badge=latest)

## Überblick

YAMMS ist ein Desktop-Tool zur schnellen und transparenten Notenverwaltung, das speziell für einzelne Lehrkräfte entwickelt wurde. Es läuft vollständig offline und bietet:

- 📚 **Klassen- und Schülerverwaltung** mit flexibler Organisation
- 📝 **Aufgabenverwaltung** mit konfigurierbaren Gewichtungen
- 🧮 **Automatische Notenberechnung** mit transparenten Algorithmen
- 📊 **Import/Export** für CSV und Excel-Dateien
- 📄 **PDF-Reports** für Übersichten und Einzelberichte
- 🔒 **Sichere lokale Datenhaltung** mit optionaler Verschlüsselung
- 💾 **Automatische Backups** mit Rotation

## Schnellstart

### Voraussetzungen

- Python 3.12 oder höher
- Git (für Entwicklung)

### Installation (Entwicklung)

```bash
# Repository klonen
git clone https://github.com/MisfitFred/yamms.git
cd yamms

# Virtuelle Umgebung erstellen und aktivieren
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# oder: venv\Scripts\activate  # Windows

# Abhängigkeiten installieren
pip install -e ".[dev]"

# Tests ausführen
make test
# oder: nox -s tests

# Dokumentation bauen
make docs
# oder: nox -s docs
```

### Dokumentation bauen

Die vollständige Dokumentation wird mit Sphinx generiert:

```bash
# Entwicklungsumgebung aktivieren
source venv/bin/activate

# Dokumentation bauen
cd docs
sphinx-build -b html source build/html

# Oder mit Make/nox
make docs
nox -s docs

# Lokalen Server starten
make docs-serve
# dann http://localhost:8000 öffnen
```

## Architektur

YAMMS folgt den Prinzipien der Hexagonal Architecture:

- **Domain:** Kerngeschäftslogik ohne externe Abhängigkeiten
- **Application:** Use-Cases und Orchestrierung
- **Infrastructure:** Adapter für Datenbank, Dateien, etc.
- **UI:** PySide6-basierte Desktop-Oberfläche

## Entwicklung

### Setup

```bash
# Entwicklungsumgebung einrichten
make install

# Code formatieren
make format

# Linting
make lint

# Alle Tests
make test

# Alle CI-Checks
make ci
```

### Verfügbare Tasks

```bash
# Alle verfügbaren Make-Targets anzeigen
make help

# Oder nox-Sessions anzeigen
nox -l
```

## Technologie-Stack

- **Python 3.12** - Moderne Python-Features
- **PySide6 (Qt)** - Native Desktop-UI
- **SQLModel** - Typsichere ORM mit SQLAlchemy
- **SQLite** - Lokale Datenbank
- **Pandas** - Datenverarbeitung
- **Sphinx** - Dokumentation
- **pytest** - Testing
- **nox** - Task-Orchestrierung

## Projektstruktur

```
yamms/
├── yamms/                  # Hauptpaket
│   ├── domain/            # Domain-Logik
│   ├── application/       # Use-Cases
│   ├── infrastructure/    # Externe Adapter
│   └── ui_pyside/        # PySide6 UI
├── tests/                 # Test-Suite
├── docs/                  # Sphinx-Dokumentation
├── noxfile.py            # nox-Konfiguration
├── pyproject.toml        # Projekt-Konfiguration
└── Makefile              # Entwicklungs-Shortcuts
```

## Beitragen

Beiträge sind willkommen! Siehe [CONTRIBUTING.md](CONTRIBUTING.md) für Details.

1. Fork des Repositories
2. Feature-Branch erstellen (`git checkout -b feature/amazing-feature`)
3. Commits mit aussagekräftigen Nachrichten
4. Tests hinzufügen/aktualisieren
5. Pull Request erstellen

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Siehe [LICENSE](LICENSE) für Details.

## Status

🚧 **Aktuell in Entwicklung** - Version 0.1 (MVP)

- [x] Projekt-Setup und Architektur
- [x] Dokumentations-Framework
- [ ] Domain-Modelle
- [ ] Datenbank-Layer
- [ ] UI-Implementierung
- [ ] Import/Export-Funktionen
- [ ] PDF-Reports

## Support

- 📖 [Dokumentation](https://yamms.readthedocs.io)
- 🐛 [Bug Reports](https://github.com/MisfitFred/yamms/issues)
- 💬 [Diskussionen](https://github.com/MisfitFred/yamms/discussions)
- 📧 [E-Mail Support](mailto:support@yamms.de)
