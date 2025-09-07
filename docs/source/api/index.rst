API-Referenz
=============

Diese Seite enthält die automatisch generierte API-Dokumentation für YAMMS.

.. note::
   Die API-Dokumentation wird automatisch aus den Docstrings im Code generiert.
   Diese Sektion wird erweitert, sobald die ersten Module implementiert sind.

Module-Übersicht
---------------

.. toctree::
   :maxdepth: 2

   modules

Geplante Module
--------------

**Domain Layer:**

* `yamms.domain.models` - Domänenmodelle (Student, Task, Grade, etc.)
* `yamms.domain.rules` - Geschäftsregeln und Berechnungslogik

**Application Layer:**

* `yamms.application.use_cases` - Anwendungsfälle und Orchestrierung
* `yamms.application.ports` - Interface-Definitionen für Adapter

**Infrastructure Layer:**

* `yamms.infrastructure.sqlite_repo` - SQLite-Datenbank-Adapter
* `yamms.infrastructure.xlsx_io` - Excel-Import/Export
* `yamms.infrastructure.pdf_reports` - PDF-Generierung

**UI Layer:**

* `yamms.ui_pyside.mainwindow` - Hauptfenster-Implementierung
* `yamms.ui_pyside.viewmodels` - MVVM ViewModels

Automatische Dokumentation
--------------------------

Die vollständige API-Dokumentation wird automatisch mit Sphinx Autodoc generiert:

.. code-block:: bash

   # API-Dokumentation neu generieren
   sphinx-apidoc -f -o docs/source/api yamms/

   # Dokumentation bauen
   sphinx-build -b html docs/source docs/build/html
