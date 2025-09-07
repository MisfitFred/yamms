Entwicklung
===========

Diese Seite beschreibt den Entwicklungsprozess und die Richtlinien für die Mitarbeit am YAMMS-Projekt.

Entwicklungsumgebung einrichten
-------------------------------

Voraussetzungen
~~~~~~~~~~~~~~~

* Python 3.12 oder höher
* Git
* Optional: Docker für DevContainer-Setup

Lokales Setup
~~~~~~~~~~~~~

.. code-block:: bash

   # Repository klonen
   git clone https://github.com/MisfitFred/yamms.git
   cd yamms

   # Virtual Environment erstellen
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   # oder: venv\Scripts\activate  # Windows

   # Entwicklungsabhängigkeiten installieren
   pip install -e ".[dev]"

DevContainer Setup (empfohlen)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Das Projekt enthält eine vorkonfigurierte DevContainer-Umgebung:

.. code-block:: bash

   # Repository klonen
   git clone https://github.com/MisfitFred/yamms.git
   cd yamms

   # In VS Code öffnen
   code .

   # DevContainer starten (Strg+Shift+P → "Dev Containers: Reopen in Container")

Build-System (nox)
------------------

Das Projekt verwendet `nox` als Task-Orchestrierung:

.. code-block:: bash

   # Alle verfügbaren Tasks anzeigen
   nox -l

   # Tests ausführen
   nox -s tests

   # Linting und Code-Formatierung
   nox -s lint
   nox -s format

   # Typ-Checks
   nox -s typecheck

   # Dokumentation generieren
   nox -s docs

   # Alle Checks auf einmal
   nox -s ci

Code-Qualität
--------------

Linting und Formatierung
~~~~~~~~~~~~~~~~~~~~~~~~

* **Black:** Code-Formatierung
* **Ruff:** Linting und Import-Sortierung
* **MyPy:** Statische Typenprüfung

.. code-block:: bash

   # Code formatieren
   nox -s format

   # Linting-Probleme finden und beheben
   nox -s lint

Pre-commit Hooks
~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Pre-commit Hooks installieren
   pre-commit install

   # Manuell ausführen
   pre-commit run --all-files

Projektstruktur
---------------

.. code-block:: text

   yamms/
   ├── app/                    # Anwendungsentry-point
   │   └── main.py
   ├── domain/                 # Domain-Logik (kerngeschäft)
   │   ├── models.py          # Domänenmodelle
   │   └── rules.py           # Geschäftsregeln
   ├── application/            # Use-Cases und Anwendungslogik
   │   ├── use_cases.py       # Anwendungsfälle
   │   └── ports.py           # Adapter-Interfaces
   ├── infrastructure/         # Externe Abhängigkeiten
   │   ├── sqlite_repo.py     # Datenbank-Adapter
   │   ├── xlsx_io.py         # Excel-Import/Export
   │   ├── pdf_reports.py     # PDF-Generierung
   │   ├── settings.py        # Konfiguration
   │   └── migrations/        # DB-Migrationen
   ├── ui_pyside/             # PySide6 UI-Layer
   │   ├── mainwindow.py      # Hauptfenster
   │   └── viewmodels.py      # MVVM ViewModels
   ├── tests/                 # Test-Suite
   │   ├── unit/              # Unit-Tests
   │   ├── integration/       # Integrations-Tests
   │   └── fixtures/          # Test-Daten
   ├── docs/                  # Sphinx-Dokumentation
   │   └── source/
   ├── noxfile.py            # nox-Konfiguration
   └── pyproject.toml        # Projekt-Konfiguration

Architektur-Prinzipien
----------------------

Hexagonal Architecture
~~~~~~~~~~~~~~~~~~~~~~

Das Projekt folgt den Prinzipien der Hexagonal Architecture:

* **Domain:** Kerngeschäftslogik, keine externen Abhängigkeiten
* **Application:** Use-Cases, orchestriert Domain und Infrastructure
* **Infrastructure:** Adapter für externe Systeme (DB, Dateien, UI)
* **UI:** View-Layer mit MVVM-Pattern

Dependency Injection
~~~~~~~~~~~~~~~~~~~~

Abhängigkeiten werden über Interfaces (Ports) injiziert:

.. code-block:: python

   # Port (Interface)
   class StudentRepository(ABC):
       @abstractmethod
       def save(self, student: Student) -> None: ...

   # Adapter (Implementation)
   class SQLiteStudentRepository(StudentRepository):
       def save(self, student: Student) -> None:
           # SQLite-spezifische Implementierung
           pass

Testing-Strategie
-----------------

Test-Pyramide
~~~~~~~~~~~~~

* **Unit-Tests:** Domain-Logik, Geschäftsregeln (schnell, isoliert)
* **Integration-Tests:** Use-Cases mit echten Adaptern
* **E2E-Tests:** UI-Workflows (wenige, kritische Pfade)

Test-Kategorien
~~~~~~~~~~~~~~~

.. code-block:: bash

   # Nur Unit-Tests
   nox -s tests -- tests/unit

   # Nur Integration-Tests
   nox -s tests -- tests/integration

   # Tests mit Coverage
   nox -s coverage

Git-Workflow
------------

Branch-Strategie
~~~~~~~~~~~~~~~~

* **main:** Produktionsreife Releases
* **develop:** Entwicklungsbranch für Features
* **feature/***:** Feature-Branches von develop
* **hotfix/***:** Kritische Bugfixes von main

Commit-Nachrichten
~~~~~~~~~~~~~~~~~

Folgen Sie der Conventional Commits Spezifikation:

.. code-block:: text

   feat: add student import from CSV
   fix: calculate weighted grades correctly
   docs: update architecture documentation
   test: add unit tests for grade calculation
   refactor: extract note calculation to domain

Pull Request Prozess
~~~~~~~~~~~~~~~~~~~

1. Feature-Branch von `develop` erstellen
2. Implementierung mit Tests
3. Alle CI-Checks müssen grün sein
4. Code Review durch Maintainer
5. Merge nach `develop`

Continuous Integration
---------------------

GitHub Actions Pipeline
~~~~~~~~~~~~~~~~~~~~~~~

Die CI/CD-Pipeline läuft auf jedem Push und PR:

.. code-block:: yaml

   # .github/workflows/ci.yml
   - Linting und Code-Formatierung
   - Unit- und Integration-Tests
   - Typ-Checks mit MyPy
   - Dokumentation-Build
   - Security-Scans
   - Packaging (auf Tags)

Release-Prozess
~~~~~~~~~~~~~~

1. Version in `pyproject.toml` aktualisieren
2. Changelog aktualisieren
3. Tag erstellen: `git tag v0.1.0`
4. Tag pushen: `git push origin v0.1.0`
5. GitHub Actions erstellt automatisch Release-Artefakte

Debugging und Profiling
-----------------------

Logging
~~~~~~~

.. code-block:: python

   import logging

   logger = logging.getLogger(__name__)
   logger.info("Processing student grades...")

Performance-Monitoring
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Profiling mit py-spy
   py-spy top --pid <process-id>

   # Memory-Profiling
   memory_profiler -l app/main.py

Troubleshooting
--------------

Häufige Probleme
~~~~~~~~~~~~~~~

**UI startet nicht unter WSL2:**

.. code-block:: bash

   # WSLg konfigurieren
   export DISPLAY=:0

   # X11-Forwarding testen
   xclock

**SQLite-Datei gesperrt:**

.. code-block:: bash

   # Prozesse prüfen, die auf DB zugreifen
   lsof yamms.db

**Import-Fehler:**

.. code-block:: bash

   # PYTHONPATH prüfen
   python -c "import sys; print(sys.path)"

   # Editable Install neu machen
   pip install -e .
