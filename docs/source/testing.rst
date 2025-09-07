Tests
=====

Diese Seite beschreibt die Teststrategie und die Ausführung der Tests im YAMMS-Projekt.

Testphilosophie
--------------

YAMMS folgt einer umfassenden Teststrategie basierend auf der Test-Pyramide:

* **Viele Unit-Tests:** Schnell, isoliert, testen Domain-Logik
* **Einige Integration-Tests:** Testen Zusammenspiel der Komponenten
* **Wenige E2E-Tests:** Testen kritische Benutzer-Workflows

Test-Kategorien
---------------

Unit-Tests
~~~~~~~~~~

Testen die Domain-Logik isoliert ohne externe Abhängigkeiten:

.. code-block:: python

   # tests/unit/test_grade_calculation.py
   def test_weighted_grade_calculation():
       """Test dass gewichtete Noten korrekt berechnet werden."""
       task1 = Task(weight=1.0, max_points=10)
       task2 = Task(weight=2.0, max_points=20)

       grade1 = Grade(task=task1, points=8)  # 80%
       grade2 = Grade(task=task2, points=16) # 80%

       calculator = GradeCalculator()
       result = calculator.calculate_weighted_average([grade1, grade2])

       assert result.percentage == 80.0
       assert result.grade_level == 13  # Bei 15-Punkte-System

Integration-Tests
~~~~~~~~~~~~~~~~

Testen das Zusammenspiel zwischen Application- und Infrastructure-Layer:

.. code-block:: python

   # tests/integration/test_student_import.py
   def test_csv_import_creates_students_in_database():
       """Test dass CSV-Import Schüler in DB erstellt."""
       csv_content = "Vorname,Nachname,Klasse\nMax,Mustermann,10a"

       importer = CSVStudentImporter(student_repo)
       result = importer.import_from_string(csv_content)

       students = student_repo.find_by_class("10a")
       assert len(students) == 1
       assert students[0].first_name == "Max"

E2E-Tests
~~~~~~~~~

Testen komplette Benutzer-Workflows über die UI:

.. code-block:: python

   # tests/e2e/test_grade_entry_workflow.py
   def test_complete_grade_entry_workflow(qtbot):
       """Test kompletter Workflow: Schüler hinzufügen → Note eingeben → Berechnung."""
       main_window = MainWindow()
       qtbot.addWidget(main_window)

       # Schüler hinzufügen
       main_window.add_student("Max", "Mustermann", "10a")

       # Aufgabe erstellen
       main_window.create_task("Mathe", "Klassenarbeit", 20, 2.0)

       # Note eingeben
       main_window.enter_grade("Max Mustermann", "Klassenarbeit", 16)

       # Berechnung prüfen
       grade = main_window.get_calculated_grade("Max Mustermann", "Mathe")
       assert grade == 13

Tests ausführen
--------------

Alle Tests
~~~~~~~~~~

.. code-block:: bash

   # Mit nox (empfohlen)
   nox -s tests

   # Direkt mit pytest
   pytest

Spezifische Test-Kategorien
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Nur Unit-Tests
   nox -s tests -- tests/unit

   # Nur Integration-Tests
   nox -s tests -- tests/integration

   # Nur E2E-Tests
   nox -s tests -- tests/e2e

Einzelne Tests
~~~~~~~~~~~~~

.. code-block:: bash

   # Einzelne Test-Datei
   pytest tests/unit/test_grade_calculation.py

   # Einzelner Test
   pytest tests/unit/test_grade_calculation.py::test_weighted_grade_calculation

   # Tests mit bestimmtem Pattern
   pytest -k "grade_calculation"

Test Coverage
------------

Coverage-Report generieren
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # HTML-Coverage-Report
   nox -s coverage

   # Coverage in Terminal anzeigen
   pytest --cov=yamms --cov-report=term-missing

Coverage-Ziele
~~~~~~~~~~~~~~

* **Domain-Layer:** > 95% Coverage (Kerngeschäftslogik)
* **Application-Layer:** > 90% Coverage (Use-Cases)
* **Infrastructure-Layer:** > 80% Coverage (Adapter)
* **UI-Layer:** > 60% Coverage (kritische Workflows)

Mocking und Fixtures
-------------------

Test-Fixtures
~~~~~~~~~~~~~

.. code-block:: python

   # tests/conftest.py
   @pytest.fixture
   def sample_student():
       """Erstellt einen Test-Schüler."""
       return Student(
           first_name="Max",
           last_name="Mustermann",
           class_name="10a"
       )

   @pytest.fixture
   def in_memory_db():
       """Erstellt eine In-Memory-Testdatenbank."""
       engine = create_engine("sqlite:///:memory:")
       with engine.begin() as conn:
           create_tables(conn)
           yield conn

Mocking externe Abhängigkeiten
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # tests/unit/test_pdf_export.py
   @patch('yamms.infrastructure.pdf_reports.weasyprint')
   def test_pdf_export_calls_weasyprint(mock_weasyprint):
       """Test dass PDF-Export weasyprint korrekt aufruft."""
       exporter = PDFExporter()
       exporter.export_class_overview(class_data)

       mock_weasyprint.HTML.assert_called_once()

Property-Based Testing
---------------------

Für komplexe Geschäftslogik verwenden wir Hypothesis:

.. code-block:: python

   # tests/unit/test_grade_calculation_properties.py
   from hypothesis import given, strategies as st

   @given(
       points=st.integers(min_value=0, max_value=100),
       max_points=st.integers(min_value=1, max_value=100)
   )
   def test_percentage_calculation_properties(points, max_points):
       """Test dass Prozent-Berechnung immer gültige Werte liefert."""
       if points <= max_points:
           percentage = calculate_percentage(points, max_points)
           assert 0 <= percentage <= 100

Performance-Tests
----------------

Load-Tests für kritische Operationen:

.. code-block:: python

   # tests/performance/test_grade_calculation_performance.py
   def test_grade_calculation_with_large_dataset():
       """Test dass Notenberechnung auch bei vielen Schülern performant ist."""
       students = create_students(1000)
       tasks = create_tasks(50)
       grades = create_random_grades(students, tasks)

       start_time = time.time()
       calculator = GradeCalculator()
       results = calculator.calculate_all_grades(grades)
       execution_time = time.time() - start_time

       assert execution_time < 1.0  # Sollte unter 1 Sekunde dauern
       assert len(results) == 1000

UI-Tests mit Qt
--------------

PySide6/Qt-Tests benötigen spezielle Behandlung:

.. code-block:: python

   # tests/ui/test_main_window.py
   import pytest
   from pytestqt.qtbot import QtBot

   @pytest.fixture
   def main_window(qtbot):
       """Erstellt Hauptfenster für Tests."""
       window = MainWindow()
       qtbot.addWidget(window)
       return window

   def test_student_table_displays_data(qtbot, main_window):
       """Test dass Schülertabelle Daten korrekt anzeigt."""
       # Daten hinzufügen
       main_window.student_model.add_student("Max", "Mustermann")

       # UI aktualisieren
       qtbot.wait(100)

       # Tabelle prüfen
       table = main_window.student_table
       assert table.rowCount() == 1
       assert table.item(0, 0).text() == "Max"

Test-Daten und Factories
------------------------

Test-Factories für konsistente Testdaten:

.. code-block:: python

   # tests/factories.py
   import factory
   from yamms.domain.models import Student, Task, Grade

   class StudentFactory(factory.Factory):
       class Meta:
           model = Student

       first_name = factory.Faker('first_name')
       last_name = factory.Faker('last_name')
       class_name = factory.Faker('random_element', elements=['10a', '10b', '11a'])

   class TaskFactory(factory.Factory):
       class Meta:
           model = Task

       subject = factory.Faker('random_element', elements=['Mathe', 'Deutsch', 'Englisch'])
       task_type = factory.Faker('random_element', elements=['Klassenarbeit', 'Test'])
       max_points = factory.Faker('random_int', min=10, max=50)
       weight = factory.Faker('random_element', elements=[1.0, 1.5, 2.0])

Continuous Testing
-----------------

Test-Automation in CI/CD
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml

   # .github/workflows/tests.yml
   name: Tests
   on: [push, pull_request]

   jobs:
     test:
       runs-on: ubuntu-latest
       strategy:
         matrix:
           python-version: [3.12, 3.13]

       steps:
         - uses: actions/checkout@v4
         - name: Set up Python
           uses: actions/setup-python@v4
           with:
             python-version: ${{ matrix.python-version }}

         - name: Install dependencies
           run: |
             pip install nox

         - name: Run tests
           run: nox -s tests

Pre-commit Testing
~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # .pre-commit-config.yaml
   repos:
     - repo: local
       hooks:
         - id: tests
           name: Run tests
           entry: nox -s tests-quick
           language: system
           pass_filenames: false

Test-Debugging
--------------

Debugging fehlschlagender Tests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Verbose-Modus
   pytest -v

   # Bei erstem Fehler stoppen
   pytest -x

   # Debugger bei Fehler starten
   pytest --pdb

   # Nur fehlgeschlagene Tests wiederholen
   pytest --lf

Test-Output analysieren
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # JUnit-XML für CI
   pytest --junit-xml=test-results.xml

   # HTML-Report
   pytest --html=test-report.html --self-contained-html

Best Practices
--------------

Test-Naming
~~~~~~~~~~

* Verwenden Sie beschreibende Namen: `test_should_calculate_weighted_average_when_multiple_tasks_exist`
* Folgen Sie dem AAA-Pattern: Arrange, Act, Assert
* Ein Test pro Verhalten/Szenario

Test-Organisation
~~~~~~~~~~~~~~~~

* Gruppieren Sie Tests in logische Module
* Verwenden Sie aussagekräftige Docstrings
* Halten Sie Tests einfach und fokussiert

Test-Isolation
~~~~~~~~~~~~~~

* Jeder Test sollte unabhängig laufen können
* Vermeiden Sie geteilten Zustand zwischen Tests
* Räumen Sie nach Tests auf (Teardown)

.. code-block:: python

   def test_with_proper_cleanup():
       # Arrange
       temp_file = create_temp_file()

       try:
           # Act & Assert
           result = process_file(temp_file)
           assert result is not None
       finally:
           # Cleanup
           os.unlink(temp_file)
