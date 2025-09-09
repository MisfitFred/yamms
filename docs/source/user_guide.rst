Benutzerhandbuch
================

Willkommen bei YAMMS - Ihrem lokalen Notenverwaltungstool! Diese Anleitung führt Sie durch alle wichtigen Funktionen.

Erste Schritte
--------------

Installation
~~~~~~~~~~~~

1. **Windows:** Laden Sie `yamms.exe` herunter und führen Sie es aus
2. **Linux:** Laden Sie das `yamms` Binary herunter, machen Sie es ausführbar (`chmod +x yamms`) und starten Sie es
3. **macOS:** Öffnen Sie `yamms.app` (ggf. Sicherheitseinstellungen anpassen)

Erster Start
~~~~~~~~~~~~

Beim ersten Start werden Sie aufgefordert:

1. **Datenbank-Speicherort wählen:** Standard ist `~/Noten/yamms.db`
2. **Verschlüsselung aktivieren:** Optional, für sensible Daten empfohlen
3. **Backup-Einstellungen:** Automatische Backups konfigurieren

.. note::
   YAMMS speichert alle Daten lokal auf Ihrem Computer. Es werden keine Daten in die Cloud übertragen.

Grundlegende Bedienung
----------------------

Hauptfenster-Aufbau
~~~~~~~~~~~~~~~~~~~

.. code-block:: text

   ┌─────────────────────────────────────────────────────────────┐
   │ Datei  Bearbeiten  Ansicht  Extras  Hilfe                   │
   ├─────────────┬───────────────────────────────────────────────┤
   │ Klassen     │                                               │
   │ ├─ 10a      │          Notenmatrix                          │
   │ ├─ 10b      │     (Schüler × Aufgaben)                     │
   │ └─ 11a      │                                               │
   │             │                                               │
   │ Fächer      │                                               │
   │ ├─ Mathe    │                                               │
   │ ├─ Deutsch  │                                               │
   │ └─ Englisch │                                               │
   │             │                                               │
   │ Aufgaben    │                                               │
   │ ├─ KA 1     ├───────────────────────────────────────────────┤
   │ ├─ Test 2   │           Details & Bemerkungen              │
   │ └─ Projekt  │                                               │
   └─────────────┴───────────────────────────────────────────────┘

Navigation
~~~~~~~~~~

* **Klassen-Auswahl:** Klicken Sie links auf eine Klasse
* **Fach-Auswahl:** Wählen Sie das gewünschte Fach aus der Liste
* **Notenerfassung:** Doppelklick in eine Zelle der Notenmatrix
* **Schnelltasten:**
  - `Strg+N`: Neue Aufgabe
  - `Strg+S`: Speichern
  - `Strg+Z`: Rückgängig
  - `F11`: Vollbild

Klassen- und Schülerverwaltung
------------------------------

Neue Klasse anlegen
~~~~~~~~~~~~~~~~~~~

1. Rechtsklick im Klassen-Bereich → "Neue Klasse"
2. Klassennamen eingeben (z.B. "10a")
3. Schuljahr auswählen (z.B. "2024/2025")
4. Mit "OK" bestätigen

Schüler hinzufügen
~~~~~~~~~~~~~~~~~~

**Einzeln:**

1. Klasse auswählen
2. Rechtsklick in Schülerliste → "Schüler hinzufügen"
3. Vor- und Nachname eingeben
4. Optional: Bemerkungen hinzufügen

**Import aus CSV/Excel:**

1. Menü → "Datei" → "Schüler importieren"
2. CSV- oder Excel-Datei auswählen
3. Spalten zuordnen (Vorname, Nachname, Klasse)
4. Import bestätigen

.. tip::
   **CSV-Format-Beispiel:**

   .. code-block:: text

      Vorname,Nachname,Klasse,Bemerkung
      Max,Mustermann,10a,
      Anna,Schmidt,10a,Nachteilsausgleich
      Tom,Weber,10a,

Schüler bearbeiten/löschen
~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Bearbeiten:** Doppelklick auf Schülername
* **Löschen:** Rechtsklick → "Löschen" (Warnung erscheint)
* **Klasse wechseln:** Drag & Drop zwischen Klassen

Aufgaben- und Notenverwaltung
-----------------------------

Neue Aufgabe erstellen
~~~~~~~~~~~~~~~~~~~~~~

1. Fach auswählen
2. Button "Neue Aufgabe" oder `Strg+N`
3. Aufgabendaten eingeben:

   * **Name:** z.B. "Klassenarbeit 1"
   * **Typ:** Klassenarbeit, Test, Mündlich, Projekt
   * **Datum:** Bewertungsdatum
   * **Maximale Punkte:** z.B. 20
   * **Gewichtung:** z.B. 2.0 für Klassenarbeiten, 1.0 für Tests
   * **Bemerkung:** Optional

Noten eingeben
~~~~~~~~~~~~~~

**Direkte Eingabe:**

1. Doppelklick in Notenmatrix-Zelle
2. Punkte eingeben (z.B. "16" für 16 von 20 Punkten)
3. `Enter` drücken oder Tab zur nächsten Zelle

**Tastatur-Navigation:**

* `Tab`: Nächste Zelle (rechts)
* `Shift+Tab`: Vorherige Zelle (links)
* `Enter`: Nächste Zeile (runter)
* `Shift+Enter`: Vorherige Zeile (hoch)
* `Esc`: Eingabe abbrechen

**Schnelleingabe:**

* **Fehlend:** `f` oder `-` für nicht bewertete Leistung
* **Entschuldigt:** `e` für entschuldigtes Fehlen
* **Attest:** `a` für ärztliches Attest

Notenberechnung verstehen
~~~~~~~~~~~~~~~~~~~~~~~~~

YAMMS berechnet Noten transparent in mehreren Schritten:

1. **Punkte → Prozent:** `16/20 = 80%`
2. **Prozent → Note:** Nach Notenschlüssel (z.B. 80% = Note 13)
3. **Gewichtung:** Klassenarbeiten zählen doppelt
4. **Gesamtnote:** Gewichteter Durchschnitt aller Aufgaben

**Beispiel-Berechnung:**

.. code-block:: text

   Schüler: Max Mustermann, Fach: Mathematik

   KA 1:    16/20 Punkte = 80% = Note 13 (Gewicht: 2.0)
   Test 1:  12/15 Punkte = 80% = Note 13 (Gewicht: 1.0)
   KA 2:    18/24 Punkte = 75% = Note 12 (Gewicht: 2.0)

   Gewichteter Durchschnitt:
   (13×2.0 + 13×1.0 + 12×2.0) ÷ (2.0 + 1.0 + 2.0) = 64 ÷ 5 = 12.8

   Gesamtnote: 13 (gerundet)

Notenschlüssel anpassen
~~~~~~~~~~~~~~~~~~~~~~~

1. Menü → "Extras" → "Notenschlüssel"
2. Fach auswählen oder "Standard" für alle Fächer
3. Prozent-Grenzen anpassen:

.. code-block:: text

   15 Punkte: ≥95%    |  8 Punkte: ≥55%   |  1 Punkt:  ≥20%
   14 Punkte: ≥90%    |  7 Punkte: ≥50%   |  0 Punkte: <20%
   13 Punkte: ≥85%    |  6 Punkte: ≥45%   |
   12 Punkte: ≥80%    |  5 Punkte: ≥40%   |
   11 Punkte: ≥75%    |  4 Punkte: ≥33%   |
   10 Punkte: ≥70%    |  3 Punkte: ≥27%   |
   9 Punkte:  ≥65%    |  2 Punkte: ≥23%   |

Import und Export
-----------------

Schülerdaten importieren
~~~~~~~~~~~~~~~~~~~~~~~~

**Unterstützte Formate:** CSV, Excel (.xlsx)

**CSV-Import:**

1. Datei → "Import" → "Schüler aus CSV"
2. Datei auswählen
3. Trennzeichen prüfen (Standard: Komma)
4. Spalten zuordnen
5. Import starten

**Excel-Import:**

1. Datei → "Import" → "Schüler aus Excel"
2. .xlsx-Datei auswählen
3. Arbeitsblatt auswählen
4. Erste Zeile als Überschrift markieren
5. Spalten zuordnen

Noten exportieren
~~~~~~~~~~~~~~~~~

**Excel-Export:**

1. Klasse und Fach auswählen
2. Datei → "Export" → "Noten als Excel"
3. Speicherort wählen
4. Export-Optionen:
   - Nur Noten oder mit Schülerdaten
   - Berechnete Gesamtnoten einschließen
   - Statistiken hinzufügen

**CSV-Export:**

1. Ähnlich wie Excel-Export
2. Trennzeichen wählen (Komma, Semikolon, Tab)
3. Zeichenkodierung (UTF-8 empfohlen)

Berichte und Ausdruck
---------------------

Klassenübersicht drucken
~~~~~~~~~~~~~~~~~~~~~~~~

1. Klasse und Fach auswählen
2. Datei → "Drucken" → "Klassenübersicht"
3. Druckoptionen:
   - Alle Aufgaben oder Zeitraum wählen
   - Mit/ohne Gesamtnoten
   - Unterschriftenfeld hinzufügen
4. Vorschau prüfen
5. Drucken oder als PDF speichern

Einzelschüler-Report
~~~~~~~~~~~~~~~~~~~~

1. Schüler auswählen
2. Datei → "Drucken" → "Schüler-Zeugnis"
3. Fächer auswählen
4. Report-Stil wählen:
   - Detailliert (alle Einzelnoten)
   - Kompakt (nur Gesamtnoten)
   - Notenentwicklung (Diagramm)

Notenlisten erstellen
~~~~~~~~~~~~~~~~~~~~~

1. Datei → "Berichte" → "Notenliste"
2. Filter setzen:
   - Klasse(n)
   - Fach/Fächer
   - Zeitraum
   - Notentyp (alle, nur KA, nur Tests)
3. Sortierung wählen
4. Exportieren oder drucken

Backup und Sicherheit
---------------------

Automatische Backups
~~~~~~~~~~~~~~~~~~~~

YAMMS erstellt automatisch Backups:

* **Häufigkeit:** Täglich beim Programmstart
* **Speicherort:** `~/Noten/Backups/`
* **Format:** Verschlüsselte ZIP-Archive
* **Aufbewahrung:** 30 Tage (konfigurierbar)

Manuelles Backup
~~~~~~~~~~~~~~~~

1. Datei → "Backup" → "Backup erstellen"
2. Speicherort wählen
3. Verschlüsselung aktivieren (empfohlen)
4. Passwort setzen
5. Backup erstellen

Wiederherstellung
~~~~~~~~~~~~~~~~~

1. Datei → "Backup" → "Wiederherstellen"
2. Backup-Datei auswählen
3. Passwort eingeben (falls verschlüsselt)
4. **Achtung:** Aktuelle Daten werden überschrieben!
5. Wiederherstellung bestätigen

Daten-Verschlüsselung
~~~~~~~~~~~~~~~~~~~~~

**Beim ersten Start:**

1. "Verschlüsselung aktivieren" wählen
2. Starkes Passwort setzen
3. Passwort bestätigen

**Nachträglich aktivieren:**

1. Extras → "Einstellungen" → "Sicherheit"
2. "Datenbank verschlüsseln" aktivieren
3. Passwort setzen
4. Neustart erforderlich

.. warning::
   **Passwort vergessen = Datenverlust!**

   * Notieren Sie Ihr Passwort sicher
   * Erstellen Sie regelmäßig unverschlüsselte Backups
   * Es gibt keine Passwort-Wiederherstellung!

Erweiterte Funktionen
---------------------

Bemerkungen und Kommentare
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Schüler-Bemerkungen:**

* Rechtsklick auf Schüler → "Bemerkung hinzufügen"
* Sichtbar in allen Berichten
* Kategorien: Allgemein, Pädagogisch, Organisatorisch

**Noten-Kommentare:**

* Rechtsklick auf Note → "Kommentar"
* Erklärung für besondere Bewertungen
* Nur für Lehrkraft sichtbar

Statistiken und Analysen
~~~~~~~~~~~~~~~~~~~~~~~~

**Klassenstatistiken:**

1. Ansicht → "Statistiken" → "Klasse"
2. Zeigt Durchschnitt, Median, Standardabweichung
3. Notenverteilung als Diagramm

**Fach-Analysen:**

1. Fach auswählen
2. Ansicht → "Statistiken" → "Fach"
3. Aufgaben-Vergleich
4. Schwierigkeitsgrad-Analyse

**Schüler-Verlauf:**

1. Schüler auswählen
2. Ansicht → "Notenentwicklung"
3. Zeitlicher Verlauf aller Fächer
4. Trend-Analyse

Mehrere Klassen/Fächer
~~~~~~~~~~~~~~~~~~~~~~

**Fach-übergreifende Ansicht:**

1. Ansicht → "Alle Fächer"
2. Zeigt Gesamtdurchschnitt pro Schüler
3. Vergleich zwischen Fächern

**Klassen-Vergleich:**

1. Mehrere Klassen auswählen (Strg+Klick)
2. Ansicht → "Klassenvergleich"
3. Statistischer Vergleich
4. Anonymisierte Darstellung

Tastaturkürzel
~~~~~~~~~~~~~~

.. list-table:: Wichtige Shortcuts
   :header-rows: 1
   :widths: 30 70

   * - Tastenkombination
     - Funktion
   * - `Strg+N`
     - Neue Aufgabe
   * - `Strg+S`
     - Speichern
   * - `Strg+Z`
     - Rückgängig
   * - `Strg+Y`
     - Wiederholen
   * - `Strg+F`
     - Suchen
   * - `Strg+P`
     - Drucken
   * - `F5`
     - Aktualisieren
   * - `F11`
     - Vollbild
   * - `Esc`
     - Abbrechen
   * - `Del`
     - Note löschen

Problemlösung
-------------

Häufige Probleme
~~~~~~~~~~~~~~~~

**Problem: "Datenbank kann nicht geöffnet werden"**

* **Lösung:**
  1. Prüfen Sie, ob die Datei existiert
  2. Bei Verschlüsselung: Korrektes Passwort eingeben
  3. Backup wiederherstellen

**Problem: "Noten werden nicht berechnet"**

* **Lösung:**
  1. Prüfen Sie Gewichtungen (müssen > 0 sein)
  2. Kontrollieren Sie Notenschlüssel
  3. Ansicht → "Neu berechnen" (F5)

**Problem: "Import schlägt fehl"**

* **Lösung:**
  1. Datei-Format prüfen (CSV, XLSX)
  2. Zeichenkodierung (UTF-8 verwenden)
  3. Keine Sonderzeichen in Spaltennamen
  4. Spalten korrekt zuordnen

**Problem: "Drucken funktioniert nicht"**

* **Lösung:**
  1. Drucker-Installation prüfen
  2. Als PDF speichern und dann drucken
  3. Seitenränder anpassen

Daten-Reparatur
~~~~~~~~~~~~~~~

**Backup-Wiederherstellung:**

1. Programm beenden
2. Datenbank-Datei sichern
3. YAMMS starten → "Backup wiederherstellen"
4. Letztes funktionierendes Backup wählen

**Datenbank-Reparatur:**

1. Extras → "Datenbank" → "Reparieren"
2. Inkonsistenzen werden automatisch behoben
3. Backup wird vor Reparatur erstellt

Support und Updates
-------------------

Hilfe erhalten
~~~~~~~~~~~~~~

1. **Eingebaute Hilfe:** F1 drücken
2. **Online-Dokumentation:** yamms.readthedocs.io
3. **GitHub Issues:** github.com/MisfitFred/yamms/issues
4. **E-Mail-Support:** support@yamms.de

Updates installieren
~~~~~~~~~~~~~~~~~~~~

**Automatische Prüfung:**

* YAMMS prüft beim Start auf Updates
* Benachrichtigung bei verfügbaren Updates
* Optional: Automatisches Herunterladen

**Manuelle Aktualisierung:**

1. Hilfe → "Nach Updates suchen"
2. Update herunterladen
3. YAMMS beenden
4. Neue Version installieren
5. Daten werden automatisch migriert

Datenschutz-Hinweise
~~~~~~~~~~~~~~~~~~~~

* **Lokale Speicherung:** Alle Daten bleiben auf Ihrem Computer
* **Keine Cloud:** Keine automatische Synchronisation
* **Verschlüsselung:** Optional für sensitive Daten
* **Backup-Sicherheit:** Backups sollten sicher aufbewahrt werden
* **Export-Warnung:** Exportierte Dateien enthalten personenbezogene Daten
