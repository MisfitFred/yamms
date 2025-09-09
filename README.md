# YAMMS - Yet Another Mark Management System

> **⚠️ TRAININGSPROJEKT ⚠️**
> Dies ist ein Lernprojekt zur Demonstration moderner Python-Entwicklungspraktiken.
> **Noch keine Funktionen implementiert** - aktuell nur Projekt-Setup und Entwicklungsumgebung.

Ein lokales, DSGVO-freundliches Notenverwaltungstool für Lehrkräfte *(geplant)*.

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Documentation Status](https://readthedocs.org/projects/yamms/badge/?version=latest)](https://yamms.readthedocs.io/en/latest/?badge=latest)

## Überblick

YAMMS soll ein Desktop-Tool zur schnellen und transparenten Notenverwaltung werden, das speziell für Lehrkräfte entwickelt wird. Es soll vollständig offline laufen und bieten *(geplante Features)*:

- 📚 **Klassen- und Schülerverwaltung** mit flexibler Organisation
- 📝 **Aufgabenverwaltung** mit konfigurierbaren Gewichtungen
- 🧮 **Automatische Notenberechnung** mit transparenten Algorithmen
- 📊 **Import/Export** für CSV und Excel-Dateien
- 📄 **PDF-Reports** für Übersichten und Einzelberichte
- 🔒 **Sichere lokale Datenhaltung** mit optionaler Verschlüsselung
- 💾 **Automatische Backups** mit Rotation

> **Aktueller Stand:** Nur Entwicklungsumgebung und Projekt-Setup implementiert.

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

# Entwicklungsumgebung einrichten (Dependencies + Pre-commit hooks)
nox -s dev_install

# Funktionalität testen
nox -s tests           # Tests ausführen
nox -s docs           # Dokumentation bauen
nox -s lint           # Code-Qualität prüfen
```

### Schnelle Entwicklung

```bash
# Entwicklungsumgebung aktivieren
source venv/bin/activate

# Dokumentation mit Live-Server
nox -s docs_serve
# dann http://localhost:8000 öffnen

# Alle verfügbaren Tasks anzeigen
nox -l
```

## Architektur

YAMMS nutzt eine **feature-orientierte Architektur** nach modernen Prinzipien (2025):

### 🎯 Feature-Module
- **Students:** Schülerverwaltung (UI + Logik + Tests)
- **Grades:** Noteneingabe und -berechnung
- **Classes:** Klassenverwaltung und -organisation
- **Reports:** PDF-Export und Berichte
- **Import/Export:** Datenimport aus Excel/CSV

### 🏗️ Shared Components
- **Models:** SQLModel-basierte Datenmodelle
- **Database:** SQLite mit typsicheren Queries
- **UI Framework:** PySide6 mit reaktiven Components
- **Utils:** Gemeinsame Hilfsfunktionen

### 💡 Design-Prinzipien
- **Colocation:** UI und Logik pro Feature zusammen
- **Reactive:** Datenänderungen propagieren automatisch zur UI
- **Type Safety:** Vollständige Typisierung mit MyPy
- **Testability:** Jedes Feature hat eigene Tests

## Entwicklung

### Setup

```bash
# Entwicklungsumgebung einrichten
nox -s dev_install

# Code formatieren
nox -s format

# Linting
nox -s lint

# Alle Tests
nox -s tests

# Alle CI-Checks
nox -s tests lint security docs
```



### Verfügbare nox-Sessions

#### 🧪 Testing & Quality
```bash
nox -s tests            # Vollständige Test-Suite mit pytest
nox -s tests_quick      # Schnelle Tests ohne Coverage
nox -s coverage         # Coverage-Report (HTML + Terminal)
nox -s tests_ui         # UI-Tests mit pytest-qt
```

#### 🔍 Code-Qualität
```bash
nox -s lint             # Linting mit Ruff (Fehler finden)
nox -s format           # Code formatieren mit Black + Ruff
nox -s typecheck        # Typen prüfen mit MyPy
nox -s security         # Sicherheitschecks (Bandit + Safety)
```

#### 📚 Dokumentation
```bash
nox -s docs             # Sphinx-Dokumentation bauen
nox -s docs_serve       # Live-Server für Docs (http://localhost:8000)
```

#### 🏗️ Build & Deployment
```bash
nox -s build            # Python-Packages erstellen
nox -s build_windows    # Windows-Executable mit PyInstaller
nox -s build_linux      # Linux-Binary erstellen
```

#### ⚙️ Entwicklung
```bash
nox -s dev_install      # Entwicklungsumgebung einrichten
nox -s pre_commit       # Pre-commit hooks installieren
nox -s pre_commit_all   # Pre-commit auf alle Dateien anwenden
nox -s clean            # Build-Artefakte aufräumen
nox -s ci               # Alle CI-Checks (für Continuous Integration)
```

#### 📋 Übersicht
```bash
nox -l                  # Alle verfügbaren Sessions anzeigen
```

## Projektstruktur

```
yamms/
├── yamms/                    # Hauptpaket
│   ├── features/            # Feature-Module
│   │   ├── students/        # Schülerverwaltung
│   │   ├── grades/          # Notenverwaltung
│   │   ├── classes/         # Klassenverwaltung
│   │   └── reports/         # Berichte & Export
│   ├── shared/              # Geteilte Komponenten
│   │   ├── models/          # SQLModel Datenmodelle
│   │   ├── database/        # DB-Abstraktionen
│   │   ├── ui/              # Wiederverwendbare UI-Komponenten
│   │   └── utils/           # Hilfsfunktionen
│   └── main.py              # Anwendungseinstieg
├── tests/                   # Test-Suite (spiegelt yamms/ Struktur)
├── docs/                    # Sphinx-Dokumentation
├── noxfile.py              # nox-Konfiguration
├── pyproject.toml          # Projekt-Konfiguration
└── README.md               # Diese Datei
```



## Status

🚧 **Aktuell in Entwicklung** - Version 0.1 (MVP)

- [x] Projekt-Setup und Architektur
- [x] Dokumentations-Framework
- [ ] Domain-Modelle
- [ ] Datenbank-Layer
- [ ] UI-Implementierung
- [ ] Import/Export-Funktionen
- [ ] PDF-Reports

## Lizenz

Dieses Projekt steht unter der Apache License 2.0. Siehe [LICENSE](LICENSE) für Details.

**Warum Apache 2.0?**
- ✅ Patent-Schutz für Nutzer und Contributors
- ✅ Schutz vor rechtlichen Problemen bei KI-generiertem Code
- ✅ Kompatibel mit den meisten anderen Open-Source-Lizenzen
- ✅ Industriestandard für moderne Open-Source-Projekte
