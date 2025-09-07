```rst
Notenverwaltung – Architektur & Doku (MVP)
==========================================

Version: 0.1

Übergeordnetes Ziel: Trainingsprojekt für Schüler im Bereich Software-Entwicklung
Ziel: kleines, lokales Tool für Lehrkräfte, offline, DSGVO-freundlich, robust.


.. contents:: Inhaltsverzeichnis
   :depth: 2
   :local:

1. Ziel & Scope
---------------

**Zielgruppe:** einzelne Lehrkraft, Einzelplatz, Windows/macOS/Linux.

**Ziel:** schnelle Erfassung von Noten und Bemerkungen pro Klasse/Fach, transparente Berechnung, Export/Druck.

**Nicht-Ziele (vorerst):** Cloud, Mehrbenutzer, Synchronisation, mobile App, Schulverwaltungs-Integration.

**MVP-Funktionen**

#. Klassen/Fächer/Schüler verwalten
#. Aufgaben (Klassenarbeit/Test/Mündlich/Projekt) mit Gewicht & max. Punkte
#. Noten erfassen (Punkte oder 15-Punkte-Skala)
#. Berechnung Fachnote je Schüler mit konfigurierbarem Notenschlüssel
#. Import/Export CSV/XLSX
#. Druck/PDF: Klassenübersicht, Einzelschüler
#. Lokale DB (SQLite), optional Verschlüsselung (SQLCipher)
#. Auto-Backups (rotierend)

2. Architektur-Überblick
------------------------

**Ansatz:** Ports & Adapters / Hexagonal light mit MVVM im UI.

- **Domain:** reine Fachlogik (Modelle, Validierungen, Notenberechnung, Rundung)
- **Application:** Use-Cases (Import/Export, Add/Update Note, Backup), orchestriert Repositories
- **Infrastructure:** SQLite-Repository, XLSX/CSV-Adapter, PDF/Druck, Settings
- **UI (MVP):** Desktop mit PySide6 (Qt). Später optional Web/Tauri, ohne die Domain zu ändern.

**Begründung:** offline, schnell, testbar; später portierbar. Kein Over-Engineering, aber klare Kanten.

3. Technologie- und Framework-Entscheidungen
--------------------------------------------

- **Programmiersprache:** Python 3.12
- **UI-Framework:** PySide6 (Qt)
  *Grund: native Tabellen, stabil, Packaging möglich; GUI wird per WSLg auch unter WSL2 angezeigt.*
- **ORM/Mapping:** SQLModel (Pydantic + SQLAlchemy)
  *Grund: Typsicherheit, einfache DB-Migrationen, vertraut aus der Python-Welt.*
- **DB:** SQLite; optional SQLCipher für Verschlüsselung
  *Grund: Zero-Admin, robust, file-based, ideal für Einzelplatz.*
- **Import/Export:** Pandas + Openpyxl
  *Grund: schnelle Anbindung an CSV/XLSX.*
- **Docs:** Sphinx (RST)
  *Grund: Standard in Python, Integration mit GitHub Actions, CI-freundlich.*
- **Testing:** Pytest, Ruff, Black, MyPy
  *Grund: etablierter Python-Stack für Codequalität.*
- **Build/Packaging:**
  - **PyInstaller** für Linux/Windows-Binaries (MVP)
  - **nox** als Task-Orchestrierung für Tests, Lint, Docs, Packaging
  *Grund: Python-idiomatischer als CMake/Ninja für reine Python-Projekte.*
- **CI/CD:** GitHub Actions
  *Grund: automatische Tests, Doku-Generierung, Packaging, Artefakt-Upload.*
- **Dev-Umgebung:** WSL2 + DevContainer
  *Grund: reproduzierbare Linux-Umgebung, WSLg für UI, saubere Toolchain.*

4. Verzeichnisstruktur
----------------------

::

  notenverwaltung/
    app/
      main.py
    domain/
      models.py
      rules.py
    application/
      use_cases.py
      ports.py
    infrastructure/
      sqlite_repo.py
      xlsx_io.py
      pdf_reports.py
      settings.py
      migrations/
        001_init.sql
    ui_pyside/
      mainwindow.py
      viewmodels.py
    tests/
      test_rules.py
      test_use_cases.py
    docs/
      conf.py
      index.rst
      architektur.rst
    noxfile.py
    pyproject.toml

5. Domänenmodell
----------------

**Kernobjekte**

- **Klasse** (id, name, schuljahr)
- **Schueler** (id, vorname, nachname, klasse_id)
- **Fach** (id, name)
- **Aufgabe** (id, fach_id, datum, typ, gewicht, max_punkte)
- **Note** (id, schueler_id, aufgabe_id, punkte)
- **Notenschluessel** (id, fach_id|null, schema_json)
- **EreignisLog** (id, zeit, entity, entity_id, alt, neu)

ER-Diagramm (ASCII)
~~~~~~~~~~~~~~~~~~~

::

  Klasse 1---* Schueler
  Fach   1---* Aufgabe 1---* Note *---1 Schueler
  Notenschluessel (optional je Fach oder global)

6. Notenberechnung (Regeln)
---------------------------

1. **Punkte → Prozent:** ``proz = punkte / max_punkte``
2. **Prozent → Stufe:** via konfigurierbare Tabelle (z. B. Gym 15-Punkte oder 1–6)
3. **Gewichtung:** gewichteter Mittelwert über Aufgaben eines Fachs
4. **Rundung:** konfigurierbar (kaufmännisch, .5 auf)
5. **Transparenz:** Report zeigt Summanden und Gewichte je Schüler/Fach

Beispiel-Notenschluessel (15-Punkte)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  >=95%: 15 | >=90: 14 | >=85: 13 | ... | <20: 0

7. Use-Cases (Application)
--------------------------

- **UC-01: Schülerliste importieren (CSV/XLSX)**
- **UC-02: Aufgabe anlegen**
- **UC-03: Noten erfassen (In-Cell Edit, Tastatur-Navigation, Undo/Redo)**
- **UC-04: Fachnote berechnen**
- **UC-05: Export/Druck (PDF, XLSX)**
- **UC-06: Backup/Restore**

8. UI-Skizze (MVP)
------------------

- **Navigation links:** Klassen → Fächer
- **Zentrum:** Notenmatrix (Schüler × Aufgaben) mit In-Cell-Edit, Summenzeile
- **Rechts:** Details/Verlauf, Bemerkungen, Gewichtungen
- **Menü:** Datei (Neu/Öffnen/Backup/Restore), Import/Export, Drucken, Einstellungen

**MVVM:** ``QAbstractTableModel`` für Matrix, ViewModel ruft Use-Cases, Domain bleibt UI-frei.

9. Datenschutz & Sicherheit
---------------------------

- Standard: lokale Datei ``~/Noten/noten.sqlite``
- Optional: **SQLCipher** mit Passwort
- Auto-Backups: lokale verschlüsselte ZIPs, 30 Tage Aufbewahrung
- Kein Cloud-Zwang; wenn Sync, dann vom Benutzer verwaltet (z. B. Netzlaufwerk)
- Exportierte Dateien sind personenbezogen → Warnhinweise
- Minimalprinzip: nur notwendige Daten speichern

10. Teststrategie
-----------------

- **Unit-Tests (Domain):** Notenberechnung, Rundung, Grenzwerte
- **Use-Case-Tests:** Import-/Export-Validierung, Undo/Redo
- **Smoke-Tests UI:** Laden, Editieren, Speichern
- **DB-Migrationstests:** Daten bleiben gültig nach Migration

11. CI/CD-Pipeline
------------------

- **GitHub Actions** auf `ubuntu-latest` und `windows-latest`
- Jobs:
  - Lint & Tests (`nox -s lint tests typecheck`)
  - Docs (`sphinx-build` via nox)
  - Packaging mit PyInstaller (Linux/Windows)
  - Artefakte hochladen
  - Release bei Tag push

12. Release & Migration
-----------------------

- **v0.1:** Domain, Notenmatrix, CSV/XLSX Import/Export, PDF Klassenübersicht
- **v0.2:** SQLCipher, EreignisLog, Einzelschüler-Report
- **v0.3:** Custom Notenschlüssel pro Fach, Backup-Rotation UI

Migrationen: nummerierte SQL-Skripte, App startet mit Auto-Apply bei Backup-Erstellung.

13. ADRs (Kurzform)
-------------------

**ADR-001 Trennung Domain/UI**
Entscheidung: Ports & Adapters mit MVVM.
Alternative: Logik in UI.
Konsequenz: bessere Testbarkeit, späterer UI-Tausch möglich.

**ADR-002 SQLite als DB**
Entscheidung: SQLite + SQLCipher optional.
Alternative: Dateien/CSV, Postgres.
Konsequenz: robust, zero-admin, einfache Backups.

**ADR-003 Build/Tasks**
Entscheidung: nox + pytest + sphinx + pyinstaller.
Alternative: CMake+Ninja.
Konsequenz: Python-idiomatisch, weniger Overhead, später erweiterbar.

**ADR-004 Dev-Umgebung**
Entscheidung: WSL2 + DevContainer.
Alternative: native Windows-Setup.
Konsequenz: reproduzierbar, saubere Toolchain, GUI über WSLg.

14. Glossar
-----------

- **Aufgabe:** bewertete Leistung (KA/Test/Mündlich/Projekt) mit Datum und Gewicht
- **Notenschlüssel:** Mapping Prozent → Note (15-Punkte oder 1–6)
- **Fachnote:** gewichtete, gerundete Gesamtnote je Fach/Schüler
```
