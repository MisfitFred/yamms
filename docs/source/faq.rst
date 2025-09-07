Häufig gestellte Fragen (FAQ)
============================

Diese Seite beantwortet die häufigsten Fragen zur Nutzung von YAMMS.

Allgemeine Fragen
----------------

Was ist YAMMS?
~~~~~~~~~~~~~

YAMMS (Yet Another Mark Management System) ist ein lokales Notenverwaltungstool für Lehrkräfte. Es läuft vollständig offline auf Ihrem Computer und ermöglicht die sichere, DSGVO-konforme Verwaltung von Schülernoten und Bewertungen.

Warum ein weiteres Notenprogramm?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

YAMMS wurde entwickelt, weil viele bestehende Lösungen entweder:

* Cloud-basiert sind und Datenschutz-Bedenken aufwerfen
* Zu komplex und überladen für den Alltag sind
* Nicht transparent in der Notenberechnung sind
* Nicht auf verschiedenen Betriebssystemen laufen

YAMMS fokussiert sich auf Einfachheit, Datenschutz und Transparenz.

Ist YAMMS kostenlos?
~~~~~~~~~~~~~~~~~~~

Ja, YAMMS ist Open-Source-Software und komplett kostenlos. Der Quellcode ist auf GitHub verfügbar und kann frei eingesehen und modifiziert werden.

Installation und Setup
---------------------

Welche Systemanforderungen hat YAMMS?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Mindestanforderungen:**

* **Windows:** Windows 10 oder neuer
* **Linux:** Ubuntu 18.04+ oder äquivalent
* **macOS:** macOS 10.15+ (experimentell)
* **RAM:** 4 GB (8 GB empfohlen)
* **Speicherplatz:** 100 MB für Installation + Speicherplatz für Daten

Kann ich YAMMS ohne Installation nutzen?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ja! YAMMS ist als portable Anwendung verfügbar:

* **Windows:** `yamms.exe` direkt ausführen
* **Linux:** Binary `yamms` mit `chmod +x` ausführbar machen
* Alle Daten werden im Benutzerverzeichnis gespeichert

Wo werden meine Daten gespeichert?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Standard-Speicherorte:**

* **Windows:** `C:\Users\[Name]\Dokumente\Noten\`
* **Linux:** `~/Noten/`
* **macOS:** `~/Documents/Noten/`

Sie können den Speicherort beim ersten Start oder später ändern.

Datenschutz und Sicherheit
-------------------------

Ist YAMMS DSGVO-konform?
~~~~~~~~~~~~~~~~~~~~~~~

Ja, YAMMS wurde speziell unter Berücksichtigung der DSGVO entwickelt:

* **Datenminimierung:** Nur notwendige Daten werden gespeichert
* **Lokale Speicherung:** Keine Cloud-Übertragung
* **Verschlüsselung:** Optional verfügbar
* **Transparenz:** Offener Quellcode
* **Kontrolle:** Vollständige Benutzerkontrolle über Daten

Wie sicher sind meine Daten?
~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Lokale Speicherung:** Daten verlassen Ihren Computer nicht
* **Verschlüsselung:** Optional mit SQLCipher (AES-256)
* **Automatische Backups:** Regelmäßige, sichere Sicherungen
* **Zugriffsschutz:** Nur Sie haben Zugriff auf Ihre Daten

Kann ich meine Daten verschlüsseln?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ja, YAMMS bietet optionale Verschlüsselung:

1. Beim ersten Start "Verschlüsselung aktivieren" wählen
2. Oder später: Extras → Einstellungen → Sicherheit
3. Starkes Passwort wählen
4. **Wichtig:** Passwort sicher aufbewahren!

.. warning::
   Bei Verlust des Verschlüsselungs-Passworts sind die Daten unwiderruflich verloren!

Notenverwaltung
--------------

Welche Notensysteme werden unterstützt?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

YAMMS unterstützt verschiedene Bewertungssysteme:

* **15-Punkte-System** (Oberstufe): 0-15 Punkte
* **6-Noten-System** (Standard): 1-6 mit + und -
* **Punkte-System:** Beliebige Punktzahlen mit konfigurierbaren Grenzen
* **Prozent-System:** 0-100% mit konfigurierbarer Umrechnung

Sie können eigene Notenschlüssel pro Fach definieren.

Wie funktioniert die Gewichtung?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Aufgaben können unterschiedlich gewichtet werden:

* **Klassenarbeiten:** Gewicht 2.0 (zählen doppelt)
* **Tests:** Gewicht 1.0 (normales Gewicht)
* **Mündliche Noten:** Gewicht 0.5 (halbes Gewicht)
* **Projekte:** Gewicht 1.5 (individuell anpassbar)

Die Gesamtnote wird als gewichteter Durchschnitt berechnet.

Kann ich Noten nachträglich ändern?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ja, Noten können jederzeit geändert werden:

* Doppelklick auf die Note in der Matrix
* Neuen Wert eingeben
* Änderung wird automatisch gespeichert
* Optional: Änderungsprotokoll aktivieren

Wie gehe ich mit fehlenden Schülern um?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

YAMMS bietet verschiedene Optionen:

* **`f`** oder **`-`**: Fehlend (nicht bewertet)
* **`e`**: Entschuldigt gefehlt
* **`a`**: Attest (ärztlich entschuldigt)

Diese Werte fließen nicht in die Notenberechnung ein.

Import und Export
----------------

Welche Dateiformate werden unterstützt?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Import:**

* CSV (Komma-, Semikolon-, Tab-getrennt)
* Excel (.xlsx)
* OpenDocument Calc (.ods) - geplant

**Export:**

* CSV (konfigurierbare Trennung)
* Excel (.xlsx)
* PDF (Berichte)
* HTML (Berichte)

Wie importiere ich Schülerlisten?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **CSV-Format vorbereiten:**

   .. code-block:: text

      Vorname,Nachname,Klasse
      Max,Mustermann,10a
      Anna,Schmidt,10a

2. **Import durchführen:**

   * Datei → Import → Schüler aus CSV
   * Datei auswählen
   * Spalten zuordnen
   * Import starten

Kann ich Daten aus anderen Programmen übernehmen?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Teilweise, je nach Exportmöglichkeiten des anderen Programms:

* **Excel-Listen:** Direkt importierbar
* **Schulverwaltungssoftware:** Meist über CSV-Export
* **Andere Notenprogramme:** Manueller Export/Import nötig

Bei Problemen können Sie uns eine Beispieldatei zur Verfügung stellen.

Berichte und Ausdruck
--------------------

Welche Berichte kann ich erstellen?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Klassenübersicht:** Alle Schüler mit Noten einer Klasse/Fach
* **Einzelschüler-Zeugnis:** Detaillierte Übersicht für einen Schüler
* **Notenlisten:** Sortierte Listen nach verschiedenen Kriterien
* **Statistiken:** Durchschnitte, Notenverteilung, Trends
* **Anwesenheitslisten:** Leere Listen zum Ausfüllen

Kann ich eigene Report-Vorlagen erstellen?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Aktuell sind die Report-Vorlagen fest vorgegeben. Für v0.3 ist ein Template-System geplant, mit dem Sie eigene Vorlagen erstellen können.

**Aktueller Workaround:**

1. Export als Excel/CSV
2. Eigene Formatierung in Excel/LibreOffice
3. Als Vorlage speichern

Wie drucke ich Zeugnisse?
~~~~~~~~~~~~~~~~~~~~~~~

1. Schüler auswählen
2. Datei → Drucken → Schüler-Zeugnis
3. Fächer und Zeitraum wählen
4. Zeugnis-Template auswählen
5. Vorschau prüfen
6. Drucken oder als PDF speichern

Technische Probleme
-------------------

YAMMS startet nicht - was tun?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Windows:**

1. Rechtsklick auf `yamms.exe` → "Als Administrator ausführen"
2. Windows Defender/Antivirus prüfen
3. Visual C++ Redistributable installieren

**Linux:**

.. code-block:: bash

   # Ausführungsrechte setzen
   chmod +x yamms

   # Dependencies prüfen
   ldd yamms

   # Von Terminal starten für Fehlermeldungen
   ./yamms

**Allgemein:**

* Neustart des Computers
* Temporäre Dateien löschen
* Antivirus-Software temporär deaktivieren

"Datenbank ist beschädigt" - Fehlermeldung
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Sofort:** Programm beenden, nichts speichern
2. **Backup wiederherstellen:**

   * YAMMS starten
   * Datei → Backup → Wiederherstellen
   * Letztes funktionierendes Backup wählen

3. **Datenbank reparieren:**

   * Extras → Datenbank → Reparieren
   * Automatische Reparatur durchführen

4. **Präventiv:** Regelmäßige manuelle Backups erstellen

Import schlägt fehl
~~~~~~~~~~~~~~~~~~

**Häufige Ursachen und Lösungen:**

* **Falsche Kodierung:** UTF-8 verwenden
* **Sonderzeichen:** Umlaute in Spaltennamen vermeiden
* **Leere Zeilen:** Am Ende der Datei entfernen
* **Falsches Format:** CSV vs. Excel prüfen

**Debug-Schritte:**

1. Datei in Texteditor öffnen
2. Erste Zeilen prüfen
3. Trennzeichen identifizieren
4. Bei Excel: Als CSV exportieren und nochmal versuchen

Noten werden falsch berechnet
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Gewichtungen prüfen:**

   * Alle Aufgaben haben Gewicht > 0?
   * Gewichtungen sinnvoll verteilt?

2. **Notenschlüssel kontrollieren:**

   * Extras → Notenschlüssel
   * Prozent-Grenzen prüfen
   * Rundungsregeln beachten

3. **Manuelle Nachrechnung:**

   * Beispiel mit Taschenrechner nachrechnen
   * Bei Abweichung: Bug-Report erstellen

Performance-Probleme
~~~~~~~~~~~~~~~~~~~

**YAMMS läuft langsam:**

* **Datenbank-Größe:** Sehr viele Schüler (>10.000)?
* **Backup-Größe:** Alte Backups löschen
* **System-Ressourcen:** Anderen Programme beenden
* **Festplatte:** SSD vs. HDD, freier Speicherplatz

**Optimierung:**

1. Extras → Datenbank → Optimieren
2. Alte, nicht benötigte Klassen archivieren
3. Backup-Aufbewahrungszeit reduzieren

Updates und Versionen
---------------------

Wie aktualisiere ich YAMMS?
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Automatisch (empfohlen):**

1. YAMMS benachrichtigt bei verfügbaren Updates
2. "Update herunterladen" klicken
3. YAMMS schließen
4. Update installiert sich automatisch

**Manuell:**

1. Hilfe → "Nach Updates suchen"
2. Oder: Neue Version von GitHub herunterladen
3. Alte Version durch neue ersetzen
4. Daten werden automatisch migriert

Gehen meine Daten bei Updates verloren?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nein! YAMMS erstellt vor jedem Update automatisch ein Backup. Die Datenbank wird bei Bedarf automatisch auf das neue Format migriert.

**Sicherheitshalber:**

* Manuelles Backup vor großen Updates (z.B. v0.1 → v0.2)
* Backup auf externem Speicher
* Update zunächst auf Testsystem probieren

Welche Version habe ich installiert?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Hilfe → "Über YAMMS"
* Oder beim Programmstart in der Titelleiste
* Kommandozeile: `yamms --version`

Datenportabilität
-----------------

Kann ich meine Daten auf einen anderen Computer übertragen?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ja, sehr einfach:

**Methode 1: Backup/Restore**

1. Alter Computer: Datei → Backup erstellen
2. Backup-Datei kopieren (USB-Stick, Cloud)
3. Neuer Computer: YAMMS installieren
4. Datei → Backup wiederherstellen

**Methode 2: Datenbank-Datei kopieren**

1. Datenbank-Datei finden (meist `~/Noten/yamms.db`)
2. Datei auf neuen Computer kopieren
3. YAMMS starten, Datei öffnen

Funktioniert YAMMS im Netzwerk?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

YAMMS ist für Einzelarbeitsplätze konzipiert. Mehrbenutzer-Zugriff ist nicht vorgesehen und kann zu Datenverlust führen.

**Mögliche Workarounds:**

* Datenbank auf Netzlaufwerk (nur ein Benutzer gleichzeitig!)
* Regelmäßiger Export/Import zwischen Lehrern
* Geplant für v0.3: Sync-Funktion für Lehrerteams

Kann ich YAMMS portable nutzen?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ja! YAMMS kann vollständig portable betrieben werden:

1. `yamms.exe` auf USB-Stick kopieren
2. Beim ersten Start "Portable Modus" wählen
3. Alle Daten werden auf dem USB-Stick gespeichert
4. Auf jedem Computer verwendbar

Erweiterte Funktionen
--------------------

Kann ich eigene Notenschlüssel erstellen?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ja, YAMMS unterstützt benutzerdefinierte Notenschlüssel:

1. Extras → Notenschlüssel → "Neu erstellen"
2. Prozent-Grenzen für jede Note definieren
3. Pro Fach oder global anwendbar
4. Import/Export von Notenschlüsseln möglich

Gibt es eine API für Entwickler?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Aktuell nein, aber geplant für v0.3:

* REST-API für externe Tools
* Plugin-System für Erweiterungen
* Dokumentierte Datenbank-Struktur

Kann ich YAMMS an unser Schulnetzwerk anbinden?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

YAMMS ist bewusst standalone konzipiert. Für Schulnetzwerk-Integration müssten Sie:

* Export/Import-Scripte entwickeln
* Regelmäßige Synchronisation einrichten
* IT-Administration kontaktieren

Geplant ist eine "School Edition" mit Netzwerk-Features.

Support und Community
--------------------

Wo bekomme ich Hilfe?
~~~~~~~~~~~~~~~~~~~

1. **Diese FAQ:** Häufige Probleme und Lösungen
2. **Benutzerhandbuch:** Detaillierte Anleitung
3. **GitHub Issues:** Bug-Reports und Feature-Requests
4. **E-Mail:** support@yamms.de für persönlichen Support
5. **Forum:** Geplant für größere Community

Wie melde ich einen Bug?
~~~~~~~~~~~~~~~~~~~~~~~

1. **GitHub Issues:** https://github.com/MisfitFred/yamms/issues
2. **Information sammeln:**

   * YAMMS-Version (Hilfe → Über)
   * Betriebssystem und Version
   * Genaue Fehlerbeschreibung
   * Schritte zum Reproduzieren
   * Screenshots falls hilfreich

3. **Logs anhängen:** `~/Noten/logs/yamms.log`

Kann ich bei der Entwicklung helfen?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ja! YAMMS ist Open Source:

* **Code beitragen:** GitHub Pull Requests
* **Übersetzungen:** Lokalisierung in andere Sprachen
* **Testing:** Beta-Versionen testen
* **Dokumentation:** Verbesserungen und Ergänzungen
* **Design:** UI/UX-Vorschläge

Siehe `CONTRIBUTING.md` im GitHub-Repository.

Gibt es Schulungen oder Workshops?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Aktuell nicht, aber geplant:

* Online-Tutorials (YouTube)
* Webinare für Schulen
* Workshop-Materialien für IT-Koordinatoren
* Train-the-Trainer-Programme

Kontaktieren Sie uns bei Interesse!
