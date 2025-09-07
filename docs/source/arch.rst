Notenverwaltung – Moderne Feature-Architektur (2025)
====================================================

Version: 0.1

**Übergeordnetes Ziel:** Trainingsprojekt für moderne Python-Entwicklungspraktiken
**Anwendungsziel:** Lokales, DSGVO-freundliches Notenverwaltungstool für Lehrkräfte


.. contents:: Inhaltsverzeichnis
   :depth: 3
   :local:

1. Architektur-Philosophie
--------------------------

**Feature-First Design (2025)**

YAMMS folgt modernen Architekturprinzipien, die sich von der traditionellen Layer-basierten
Trennung abwenden. Statt künstlicher Schichten bevorzugen wir eine **feature-orientierte
Organisation**, die dem natürlichen Denkprozess von Entwicklern und Benutzern entspricht.

**Warum Feature-orientiert?**

- **Colocation:** Zusammengehöriger Code (UI, Logik, Tests) ist räumlich nah
- **Autonomie:** Features können unabhängig entwickelt und getestet werden
- **Klarheit:** Entwickler finden alles zu einem Feature an einem Ort
- **Skalierbarkeit:** Neue Features störenbestehende nicht
- **Team-Freundlich:** Verschiedene Entwickler können parallel an Features arbeiten

**Abkehr von klassischen Patterns**

Die traditionelle Trennung von "GUI" und "Logik" gilt heute als überholt:

- **Problem klassischer Trennung:** Künstliche Barrieren, die zusammengehörige Konzepte auseinanderreißen
- **Moderne Lösung:** Reactive Components, bei denen UI und State Management eng verzahnt sind
- **Inspiration:** React/Vue Component-Architektur, Feature Slices in Redux

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

2. Feature-Module Architektur
-----------------------------

**Core-Prinzip: Vertical Slices**

Jedes Feature ist ein "Vertical Slice" durch alle technischen Schichten:

::

  Feature "Students"
  ├── ui/
  │   ├── students_view.py          # PySide6 Widget
  │   ├── students_model.py         # QAbstractTableModel
  │   └── students_dialogs.py       # Eingabedialoge
  ├── logic/
  │   ├── students_service.py       # Geschäftslogik
  │   ├── students_validators.py    # Validierungen
  │   └── students_events.py        # Event-System
  ├── data/
  │   ├── students_repository.py    # Datenzugriff
  │   └── students_queries.py       # SQLModel Queries
  └── tests/
      ├── test_students_ui.py       # UI-Tests mit pytest-qt
      ├── test_students_logic.py    # Geschäftslogik-Tests
      └── test_students_data.py     # Repository-Tests

**Feature-Katalog**

**Students Feature**
  - Schülerverwaltung mit Import/Export
  - UI: Tabelle mit In-Place-Editing, Suchfilter
  - Logic: Validierung von Namen, Dublettencheck
  - Data: CRUD-Operationen, Bulk-Import aus CSV/Excel

**Grades Feature**
  - Noteneingabe und -berechnung
  - UI: Notenmatrix (Schüler × Aufgaben), Spalten-/Zeilensummen
  - Logic: Gewichtete Mittelwerte, Rundungsregeln, Notenschlüssel
  - Data: Effiziente Queries für große Notenmatrizen

**Classes Feature**
  - Klassen- und Fachverwaltung
  - UI: Hierarchische Ansicht, Drag&Drop für Zuordnungen
  - Logic: Klassenregeln, Schülerzuordnungen
  - Data: Relational mapping zwischen Classes/Students/Subjects

**Reports Feature**
  - PDF-Export und Druckfunktionen
  - UI: Druckvorschau, Template-Auswahl
  - Logic: Report-Engine, Datenaufbereitung
  - Data: Aggregierte Queries für Berichte

**Import/Export Feature**
  - Datenimport aus verschiedenen Quellen
  - UI: Import-Wizard, Mapping-Dialog
  - Logic: Format-Detection, Fehlerbehandlung
  - Data: Batch-Operations, Transaktionale Sicherheit

3. Shared Components Layer
---------------------------

**Gemeinsame Infrastruktur**

Während Features autonom sind, teilen sie sich bewährte Infrastruktur:

**Models (SQLModel-basiert)**
::

  shared/models/
  ├── base.py              # BaseModel mit Timestamps, ID
  ├── student.py           # Student SQLModel
  ├── grade.py             # Grade SQLModel mit Relationen
  ├── class_model.py       # Class/Subject Models
  └── calculation.py       # Berechnungsmodelle (Grade Scales)

**Database Layer**
::

  shared/database/
  ├── connection.py        # SQLite Connection Management
  ├── migrations.py        # Schema-Migrationen
  ├── base_repository.py   # Generic Repository Pattern
  └── query_builder.py     # Type-safe Query Builder

**UI Framework**
::

  shared/ui/
  ├── reactive/
  │   ├── signals.py       # Globales Event-System
  │   ├── state.py         # Application State Management
  │   └── observers.py     # Observer Pattern für UI-Updates
  ├── components/
  │   ├── data_table.py    # Wiederverwendbare Tabellen-Widgets
  │   ├── search_bar.py    # Suchkomponenten
  │   └── dialogs.py       # Standard-Dialoge
  └── themes/
      ├── modern_dark.py   # Dunkles Theme
      └── classic.py       # Klassisches Theme

**Utilities**
::

  shared/utils/
  ├── validation.py        # Validators (Email, Namen, etc.)
  ├── formatting.py        # Number/Date Formatierung
  ├── io_helpers.py        # File I/O Utilities
  └── logging.py           # Structured Logging Setup
4. Reactive Programming Model
-----------------------------

**Event-Driven UI Updates**

YAMMS nutzt ein **Reactive Programming**-Modell für konsistente UI-Updates:

**Signal/Slot System (Qt-erweitert)**
::

  # Feature-übergreifende Events
  from shared.reactive.signals import app_signals

  # Student wurde aktualisiert
  app_signals.student_updated.emit(student_id, student_data)

  # Alle interessierten UI-Komponenten reagieren automatisch
  grades_widget.on_student_updated(student_id, student_data)
  reports_widget.refresh_student_data(student_id)

**State Management**
::

  shared/reactive/state.py:

  class ApplicationState:
      """Zentraler Application State mit Reactive Updates"""

      def __init__(self):
          self.current_class = ReactiveProperty(None)
          self.selected_students = ReactiveList([])
          self.filter_settings = ReactiveDict({})

      def set_current_class(self, class_id):
          """Automatische UI-Updates bei Klassenänderung"""
          self.current_class.value = class_id
          # Alle subscribers werden automatisch benachrichtigt

**Vorteile des Reactive Models:**

- **Konsistenz:** UI bleibt automatisch synchron
- **Entkopplung:** Features wissen nicht voneinander, kommunizieren über Events
- **Testbarkeit:** State-Änderungen sind nachvollziehbar und testbar
- **Performance:** Nur betroffene UI-Komponenten werden aktualisiert

5. Technologie-Stack (2025)
----------------------------

**Moderne Python-Entwicklung**

**Core Framework**
  - **Python 3.12:** Moderne Features (match/case, TypeVars, Performance)
  - **PySide6 6.9+:** Qt6 mit verbessertem High-DPI Support
  - **SQLModel:** Type-safe ORM mit Pydantic Integration
  - **SQLite 3.45+:** Mit JSON-Support und besserer Performance

**Development Experience**
  - **nox:** Task Orchestration (ersetzt Make/tox)
  - **Ruff:** Ultra-fast Linting (ersetzt flake8/isort/pyupgrade)
  - **Black:** Code Formatting (unverändert der Standard)
  - **MyPy:** Static Type Checking mit strikter Konfiguration
  - **pytest:** Testing mit pytest-qt für UI-Tests

**Build & Deployment**
  - **PyInstaller 6.0+:** Single-file Binaries für alle Plattformen
  - **GitHub Actions:** CI/CD mit Matrix-Builds
  - **pre-commit:** Git Hooks für Code Quality
  - **Sphinx:** Dokumentation mit modern Theme

**Warum diese Choices?**

**PySide6 vs. Web-Framework**
  - ✅ Native Performance für Tabellen-intensive UIs
  - ✅ Offline-First, kein Server notwendig
  - ✅ Plattform-native Look & Feel
  - ✅ Direkte Datei-Zugriffe ohne Security-Restrictions

**SQLModel vs. Django ORM**
  - ✅ Type Safety mit Pydantic Models
  - ✅ Weniger Boilerplate als Django
  - ✅ SQLAlchemy-Power ohne Komplexität
  - ✅ Automatische API-Serialization (falls später Web-API)

**Feature-Architecture vs. Django Apps**
  - ✅ Weniger Framework-Overhead
  - ✅ Flexible Strukturierung
  - ✅ Bessere Testbarkeit
  - ✅ Moderne Patterns ohne Legacy-Ballast
6. Detaillierte Verzeichnisstruktur
------------------------------------

**Feature-orientierte Organisation**

::

  yamms/
  ├── main.py                          # Application Entry Point
  ├── features/                        # Feature Modules (Vertical Slices)
  │   ├── students/
  │   │   ├── __init__.py
  │   │   ├── ui/
  │   │   │   ├── students_widget.py   # Haupt-Widget für Schülerliste
  │   │   │   ├── student_dialog.py    # Eingabe-Dialog für neue Schüler
  │   │   │   └── import_wizard.py     # CSV/Excel Import Wizard
  │   │   ├── logic/
  │   │   │   ├── students_service.py  # Geschäftslogik (CRUD, Validation)
  │   │   │   ├── import_service.py    # Import-Logik mit Error Handling
  │   │   │   └── validators.py        # Name/Email/etc. Validierung
  │   │   ├── data/
  │   │   │   ├── repository.py        # SQLModel Repository
  │   │   │   └── queries.py           # Optimierte Datenbankabfragen
  │   │   └── tests/
  │   │       ├── test_students_ui.py  # pytest-qt UI Tests
  │   │       ├── test_service.py      # Unit Tests für Geschäftslogik
  │   │       └── test_repository.py   # Integration Tests für DB
  │   ├── grades/
  │   │   ├── ui/
  │   │   │   ├── grades_matrix.py     # Hauptansicht: Notenmatrix
  │   │   │   ├── grade_calculator.py  # UI für Notenberechnung
  │   │   │   └── assignment_dialog.py # Dialog für neue Aufgaben
  │   │   ├── logic/
  │   │   │   ├── calculation_engine.py # Notenberechnung (gewichtet)
  │   │   │   ├── grade_scales.py      # Notenschlüssel-Management
  │   │   │   └── statistics.py        # Klassen-/Schülerstatistiken
  │   │   ├── data/
  │   │   │   ├── grades_repository.py # Effiziente Matrix-Queries
  │   │   │   └── assignments_repo.py  # Aufgaben-Management
  │   │   └── tests/
  │   │       ├── test_calculation.py  # Tests für Notenberechnung
  │   │       └── test_grades_ui.py    # UI Tests für Matrix-Editing
  │   ├── classes/
  │   │   ├── ui/
  │   │   │   ├── class_tree.py        # Hierarchische Klassen-Ansicht
  │   │   │   └── subject_manager.py   # Fach-Verwaltung
  │   │   ├── logic/
  │   │   │   ├── class_service.py     # Klassen-Geschäftslogik
  │   │   │   └── subject_service.py   # Fach-Management
  │   │   └── data/
  │   │       └── class_repository.py  # Klassen/Fächer DB-Zugriff
  │   └── reports/
  │       ├── ui/
  │       │   ├── report_preview.py    # PDF-Vorschau
  │       │   └── export_dialog.py     # Export-Optionen
  │       ├── logic/
  │       │   ├── pdf_generator.py     # WeasyPrint PDF-Erstellung
  │       │   ├── excel_exporter.py    # XLSX-Export mit Pandas
  │       │   └── report_templates.py  # Template-System für Berichte
  │       └── data/
  │           └── report_queries.py    # Aggregierte Daten für Reports
  ├── shared/                          # Geteilte Infrastruktur
  │   ├── models/                      # SQLModel Definitionen
  │   │   ├── base.py                  # BaseModel mit Common Fields
  │   │   ├── student.py               # Student Model mit Relationen
  │   │   ├── grade.py                 # Grade/Assignment Models
  │   │   └── class_model.py           # Class/Subject Models
  │   ├── database/
  │   │   ├── connection.py            # DB Connection & Session Management
  │   │   ├── migrations.py            # Alembic Integration
  │   │   └── base_repository.py       # Generic Repository Pattern
  │   ├── ui/
  │   │   ├── reactive/                # Reactive Programming Layer
  │   │   │   ├── signals.py           # Application-wide Signals
  │   │   │   ├── state.py             # Global State Management
  │   │   │   └── observers.py         # Observer Pattern Implementation
  │   │   ├── components/              # Reusable UI Components
  │   │   │   ├── data_table.py        # Enhanced QTableWidget
  │   │   │   ├── search_widget.py     # Reusable Search Component
  │   │   │   └── progress_dialog.py   # Progress Dialogs für Long Operations
  │   │   └── themes/
  │   │       ├── modern_dark.qss      # Dark Theme Stylesheet
  │   │       └── light.qss            # Light Theme Stylesheet
  │   └── utils/
  │       ├── validation.py            # Common Validators
  │       ├── formatting.py            # Number/Date Formatting
  │       ├── io_helpers.py            # File I/O Utilities
  │       └── config.py                # Application Settings
  ├── tests/                           # Integration & System Tests
  │   ├── integration/                 # Cross-Feature Tests
  │   ├── fixtures/                    # Test Data & Fixtures
  │   └── conftest.py                  # pytest Configuration
  ├── docs/                            # Sphinx Documentation
  │   ├── source/
  │   │   ├── features/                # Feature-spezifische Docs
  │   │   ├── architecture/            # Architecture Decision Records
  │   │   └── api/                     # Auto-generated API Docs
  │   └── build/                       # Generated Documentation
  ├── noxfile.py                       # Task Orchestration
  ├── pyproject.toml                   # Project Configuration
  └── README.md                        # Project Overview

**Organisationsprinzipien**

1. **Feature Autonomy:** Jedes Feature kann unabhängig entwickelt werden
2. **Shared Abstraction:** Gemeinsame Infrastruktur ohne Feature-spezifische Details
3. **Test Colocation:** Tests leben nah am Code, den sie testen
4. **Documentation by Feature:** Docs sind nach Features organisiert
5. **Type Safety:** Alle Module haben vollständige Type Hints

7. Feature-übergreifende Patterns
----------------------------------

**Repository Pattern (Modern)**

Jedes Feature implementiert sein eigenes Repository, aber alle erben von einer gemeinsamen Basis:

::

  # shared/database/base_repository.py

  class BaseRepository[T](Generic[T]):
      """Type-safe Base Repository mit modernen Python Features"""

      def __init__(self, model_class: Type[T], session: Session):
          self.model_class = model_class
          self.session = session

      async def find_by_id(self, id: int) -> T | None:
          """Type-safe Find mit Optional Return"""
          return await self.session.get(self.model_class, id)

      async def find_many(self, **filters) -> list[T]:
          """Filtered Query mit Type Safety"""
          query = select(self.model_class)
          for key, value in filters.items():
              query = query.where(getattr(self.model_class, key) == value)
          return (await self.session.execute(query)).scalars().all()

**Event System (Reactive)**

Features kommunizieren über ein typsicheres Event-System:

::

  # shared/reactive/signals.py

  from dataclasses import dataclass
  from typing import Protocol

  @dataclass
  class StudentUpdatedEvent:
      student_id: int
      student_data: StudentModel
      changed_fields: set[str]

  class EventBus:
      """Type-safe Event Bus für Feature-Kommunikation"""

      def __init__(self):
          self._subscribers: dict[type, list[callable]] = {}

      def subscribe[T](self, event_type: type[T], handler: callable[[T], None]):
          """Type-safe Event Subscription"""
          if event_type not in self._subscribers:
              self._subscribers[event_type] = []
          self._subscribers[event_type].append(handler)

      def emit[T](self, event: T):
          """Emit Event to all Subscribers"""
          event_type = type(event)
          for handler in self._subscribers.get(event_type, []):
              handler(event)

**Validation Layer**

Zentrale Validierung mit Pydantic Integration:

::

  # shared/utils/validation.py

  from pydantic import BaseModel, validator

  class StudentCreateRequest(BaseModel):
      """Request Model für Student Creation mit Validation"""

      first_name: str
      last_name: str
      email: str | None = None
      class_id: int

      @validator('first_name', 'last_name')
      def validate_names(cls, v):
          if not v or len(v.strip()) < 2:
              raise ValueError('Name muss mindestens 2 Zeichen haben')
          return v.strip().title()

      @validator('email')
      def validate_email(cls, v):
          if v and '@' not in v:
              raise ValueError('Ungültige E-Mail-Adresse')
          return v

8. Type Safety & Modern Python
-------------------------------

**SQLModel Integration**

Vollständige Type Safety von der Datenbank bis zur UI:

::

  # shared/models/student.py

  from sqlmodel import SQLModel, Field, Relationship
  from datetime import datetime

  class StudentBase(SQLModel):
      """Base Model für Student (shared zwischen DB und API)"""
      first_name: str = Field(min_length=2, max_length=50)
      last_name: str = Field(min_length=2, max_length=50)
      email: str | None = Field(default=None, regex=r'^[^@]+@[^@]+\.[^@]+$')
      birth_date: datetime | None = None

  class Student(StudentBase, table=True):
      """Database Model für Student"""
      id: int | None = Field(default=None, primary_key=True)
      class_id: int = Field(foreign_key="class.id")
      created_at: datetime = Field(default_factory=datetime.now)

      # Relationships
      class_: "Class" = Relationship(back_populates="students")
      grades: list["Grade"] = Relationship(back_populates="student")

  class StudentCreate(StudentBase):
      """Request Model für Student Creation"""
      class_id: int

  class StudentRead(StudentBase):
      """Response Model für Student Queries"""
      id: int
      class_id: int
      created_at: datetime

**Modern Python Features**

::

  # Python 3.12 Features in Action

  from typing import TypeVar, Generic, Protocol

  T = TypeVar('T', bound=SQLModel)

  class Repository[T](Protocol):
      """Protocol für Repository mit Generics"""

      async def create(self, item: T) -> T: ...
      async def get_by_id(self, id: int) -> T | None: ...
      async def update(self, id: int, data: dict) -> T | None: ...

  # Match/Case für Grade Calculation
  def calculate_grade_level(percentage: float) -> str:
      match percentage:
          case p if p >= 95: return "Sehr gut (1+)"
          case p if p >= 90: return "Sehr gut (1)"
          case p if p >= 85: return "Gut (2+)"
          case p if p >= 80: return "Gut (2)"
          case _: return "Ungenügend"

9. Testing Strategy (Modern)
----------------------------

**Multi-Layer Testing**

Jedes Feature hat eine vollständige Test-Pyramide:

**Unit Tests (Logic Layer)**
::

  # features/grades/tests/test_calculation.py

  import pytest
  from features.grades.logic.calculation_engine import GradeCalculator

  class TestGradeCalculation:

      def test_weighted_average_calculation(self):
          """Test gewichtete Durchschnitte"""
          calculator = GradeCalculator()

          grades = [
              {"points": 45, "max_points": 50, "weight": 2},  # 90% * 2
              {"points": 40, "max_points": 50, "weight": 1},  # 80% * 1
          ]

          result = calculator.calculate_weighted_average(grades)
          expected = (90 * 2 + 80 * 1) / (2 + 1)  # 86.67%

          assert result == pytest.approx(expected, rel=1e-2)

**Integration Tests (Data Layer)**
::

  # features/students/tests/test_repository.py

  import pytest
  from sqlmodel import Session
  from features.students.data.repository import StudentRepository

  @pytest.fixture
  async def student_repo(db_session: Session):
      return StudentRepository(db_session)

  class TestStudentRepository:

      async def test_create_and_find_student(self, student_repo):
          """Test vollständiger CRUD Cycle"""
          student_data = StudentCreate(
              first_name="Max",
              last_name="Mustermann",
              class_id=1
          )

          # Create
          created = await student_repo.create(student_data)
          assert created.id is not None

          # Read
          found = await student_repo.get_by_id(created.id)
          assert found.first_name == "Max"

**UI Tests (pytest-qt)**
::

  # features/students/tests/test_students_ui.py

  import pytest
  from PySide6.QtWidgets import QApplication
  from features.students.ui.students_widget import StudentsWidget

  @pytest.fixture
  def students_widget(qtbot):
      widget = StudentsWidget()
      qtbot.addWidget(widget)
      return widget

  class TestStudentsUI:

      def test_add_student_dialog(self, students_widget, qtbot):
          """Test Student hinzufügen über UI"""

          # Simulate button click
          qtbot.mouseClick(students_widget.add_button, Qt.LeftButton)

          # Dialog should appear
          dialog = students_widget.findChild(QDialog, "add_student_dialog")
          assert dialog is not None
          assert dialog.isVisible()

**Property-Based Testing**
::

  # features/grades/tests/test_calculation_properties.py

  from hypothesis import given, strategies as st

  class TestGradeCalculationProperties:

      @given(
          points=st.floats(min_value=0, max_value=100),
          max_points=st.floats(min_value=1, max_value=100)
      )
      def test_percentage_always_between_0_and_100(self, points, max_points):
          """Percentage sollte immer zwischen 0 und 100 sein"""
          calculator = GradeCalculator()

          percentage = calculator.points_to_percentage(points, max_points)

          assert 0 <= percentage <= 100

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
