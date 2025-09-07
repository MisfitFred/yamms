SQLCipher Installation
======================

SQLCipher ist eine optionale Abhängigkeit für YAMMS, die Datenbankverschlüsselung ermöglicht.
Die Installation erfordert zusätzliche Systemabhängigkeiten.

Installation auf Ubuntu/Debian
-------------------------------

.. code-block:: bash

   # Systemabhängigkeiten installieren
   sudo apt-get update
   sudo apt-get install -y libsqlcipher-dev

   # SQLCipher Python-Paket installieren
   pip install sqlcipher3>=0.5.2

Installation auf anderen Systemen
----------------------------------

**macOS (mit Homebrew):**

.. code-block:: bash

   brew install sqlcipher
   pip install sqlcipher3>=0.5.2

**Windows:**

SQLCipher erfordert eine manuelle Kompilierung unter Windows oder die Verwendung
vorkompilierter Binärdateien. Für Entwicklungszwecke kann SQLite ohne Verschlüsselung
verwendet werden.

Konfiguration
-------------

Nach der Installation von SQLCipher kann die Verschlüsselung in der Anwendung
aktiviert werden:

.. code-block:: python

   from yamms.config import Settings

   settings = Settings(
       database_encrypt=True,
       database_password="sicheres_passwort"
   )

.. note::
   Ohne SQLCipher verwendet YAMMS reguläres SQLite ohne Verschlüsselung.
   Dies ist für Entwicklungs- und Testzwecke ausreichend.
