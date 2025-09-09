YAMMS - Yet Another Mark Management System
==========================================

Willkommen zur Dokumentation des **YAMMS** (Yet Another Mark Management System) - einem lokalen, DSGVO-freundlichen Notenverwaltungstool für Lehrkräfte.

.. note::
   Dies ist ein Trainingsprojekt für Schüler im Bereich Software-Entwicklung mit dem Ziel, ein robustes, offline funktionierendes Tool zu entwickeln.

Überblick
---------

YAMMS ist ein Desktop-Tool zur schnellen und transparenten Notenverwaltung, das speziell für einzelne Lehrkräfte entwickelt wurde. Es läuft vollständig offline und bietet folgende Kernfunktionen:

* **Klassen- und Schülerverwaltung** mit flexibler Fächerorganisation
* **Aufgabenverwaltung** mit konfigurierbaren Gewichtungen und Bewertungsschemata
* **Automatische Notenberechnung** mit transparenten Algorithmen
* **Import/Export-Funktionen** für CSV und XLSX-Dateien
* **PDF-Reports** für Klassenübersichten und Einzelschülerberichte
* **Sichere lokale Datenhaltung** mit optionaler Verschlüsselung
* **Automatische Backups** mit Rotation

Technische Highlights
---------------------

* **Architektur:** Hexagonal Architecture (Ports & Adapters) mit MVVM im UI
* **Framework:** Python 3.12 + PySide6 (Qt) für native Desktop-Performance
* **Datenbank:** SQLite mit optionaler SQLCipher-Verschlüsselung
* **Qualitätssicherung:** Umfassende Test-Suite mit pytest
* **Dokumentation:** Sphinx-basiert mit automatischer CI/CD-Integration

Schnellstart
------------

.. code-block:: bash

   # Repository klonen
   git clone https://github.com/MisfitFred/yamms.git
   cd yamms

   # Entwicklungsumgebung einrichten
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   # oder: venv\Scripts\activate  # Windows

   # Abhängigkeiten installieren
   pip install -r requirements.txt

   # Tests ausführen
   nox -s tests

   # Dokumentation generieren
   nox -s docs

Inhaltsverzeichnis
------------------

.. toctree::
   :maxdepth: 2
   :caption: Architektur & Design:

   arch

.. toctree::
   :maxdepth: 2
   :caption: Entwicklung:

   development
   testing
   deployment
   sqlcipher_setup


.. toctree::
   :maxdepth: 2
   :caption: Benutzerhandbuch:

   user_guide
   faq

.. toctree::
   :maxdepth: 2
   :caption: API Referenz:

   api/index

Projektstatus
-------------

.. list-table:: Entwicklungsfortschritt
   :header-rows: 1
   :widths: 20 20 60

   * - Version
     - Status
     - Features
   * - v0.1 (MVP)
     - 🚧 In Entwicklung
     - Domain-Modell, Notenmatrix, CSV/XLSX Import/Export, PDF-Reports
   * - v0.2
     - 📋 Geplant
     - SQLCipher-Verschlüsselung, Ereignisprotokoll, Einzelschüler-Reports
   * - v0.3
     - 📋 Geplant
     - Custom Notenschlüssel pro Fach, Backup-Rotation UI

Lizenz & Datenschutz
--------------------

YAMMS wurde mit besonderem Fokus auf Datenschutz entwickelt:

* **Offline-First:** Keine Cloud-Anbindung erforderlich
* **DSGVO-konform:** Minimale Datenspeicherung, lokale Verschlüsselung möglich
* **Transparenz:** Offener Quellcode, nachvollziehbare Algorithmen
* **Kontrolle:** Benutzer behält vollständige Kontrolle über alle Daten

Indizes und Tabellen
====================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
