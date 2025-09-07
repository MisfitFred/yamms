Deployment
==========

Diese Seite beschreibt den Build- und Deployment-Prozess für YAMMS.

Build-System
-----------

nox-basierte Builds
~~~~~~~~~~~~~~~~~~

Das Projekt verwendet `nox` als primäres Build-Tool:

.. code-block:: bash

   # Alle verfügbaren Build-Tasks anzeigen
   nox -l

   # Kompletter CI-Build
   nox -s ci

   # Nur Packaging
   nox -s build

   # Distribution erstellen
   nox -s dist

PyInstaller-Packaging
~~~~~~~~~~~~~~~~~~~~

Für End-User-Distributionen verwenden wir PyInstaller:

.. code-block:: bash

   # Windows-Executable erstellen
   nox -s build-windows

   # Linux-Binary erstellen
   nox -s build-linux

   # macOS-App Bundle erstellen
   nox -s build-macos

Target-Platforms
----------------

Unterstützte Betriebssysteme
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Platform-Support
   :header-rows: 1
   :widths: 20 20 30 30

   * - Platform
     - Status
     - Packaging
     - Besonderheiten
   * - Windows 10/11
     - ✅ Vollständig
     - PyInstaller .exe
     - Native Windows-Dialoge
   * - Ubuntu 20.04+
     - ✅ Vollständig
     - PyInstaller Binary
     - AppImage geplant
   * - macOS 11+
     - 🧪 Experimentell
     - PyInstaller .app
     - Code-Signing erforderlich
   * - RHEL/CentOS 8+
     - 🧪 Experimentell
     - PyInstaller Binary
     - Manual Testing

Abhängigkeiten
~~~~~~~~~~~~~

.. code-block:: toml

   # pyproject.toml
   [project]
   dependencies = [
       "pyside6>=6.5.0",
       "sqlmodel>=0.0.14",
       "pandas>=2.0.0",
       "openpyxl>=3.1.0",
       "weasyprint>=60.0",
       "cryptography>=41.0.0",  # für SQLCipher
   ]

Release-Pipeline
---------------

GitHub Actions Workflow
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml

   # .github/workflows/release.yml
   name: Release
   on:
     push:
       tags: ['v*']

   jobs:
     build-windows:
       runs-on: windows-latest
       steps:
         - uses: actions/checkout@v4
         - name: Setup Python
           uses: actions/setup-python@v4
           with:
             python-version: '3.12'
         - name: Build Windows executable
           run: nox -s build-windows
         - name: Upload artifact
           uses: actions/upload-artifact@v4
           with:
             name: yamms-windows
             path: dist/yamms.exe

     build-linux:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v4
         - name: Setup Python
           uses: actions/setup-python@v4
           with:
             python-version: '3.12'
         - name: Build Linux binary
           run: nox -s build-linux
         - name: Upload artifact
           uses: actions/upload-artifact@v4
           with:
             name: yamms-linux
             path: dist/yamms

     create-release:
       needs: [build-windows, build-linux]
       runs-on: ubuntu-latest
       steps:
         - name: Download artifacts
           uses: actions/download-artifact@v4
         - name: Create Release
           uses: softprops/action-gh-release@v1
           with:
             files: |
               yamms-windows/yamms.exe
               yamms-linux/yamms
             generate_release_notes: true

Versionierung
~~~~~~~~~~~~

Wir folgen Semantic Versioning (SemVer):

* **Major (X.0.0):** Breaking Changes in der API
* **Minor (0.X.0):** Neue Features, rückwärtskompatibel
* **Patch (0.0.X):** Bugfixes, rückwärtskompatibel

.. code-block:: bash

   # Version bumpen
   bump2version patch  # 0.1.0 → 0.1.1
   bump2version minor  # 0.1.1 → 0.2.0
   bump2version major  # 0.2.0 → 1.0.0

Packaging-Konfiguration
----------------------

PyInstaller-Specs
~~~~~~~~~~~~~~~~

.. code-block:: python

   # build/yamms.spec
   # -*- mode: python ; coding: utf-8 -*-

   block_cipher = None

   a = Analysis(
       ['app/main.py'],
       pathex=[],
       binaries=[],
       datas=[
           ('yamms/ui_pyside/resources', 'yamms/ui_pyside/resources'),
           ('yamms/infrastructure/migrations', 'yamms/infrastructure/migrations'),
       ],
       hiddenimports=[
           'PySide6.QtCore',
           'PySide6.QtWidgets',
           'PySide6.QtGui',
           'sqlalchemy.dialects.sqlite',
       ],
       hookspath=[],
       hooksconfig={},
       runtime_hooks=[],
       excludes=[],
       win_no_prefer_redirects=False,
       win_private_assemblies=False,
       cipher=block_cipher,
       noarchive=False,
   )

   pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

   exe = EXE(
       pyz,
       a.scripts,
       a.binaries,
       a.zipfiles,
       a.datas,
       [],
       name='yamms',
       debug=False,
       bootloader_ignore_signals=False,
       strip=False,
       upx=True,
       upx_exclude=[],
       runtime_tmpdir=None,
       console=False,  # Windows: GUI-App ohne Konsole
       disable_windowed_traceback=False,
       argv_emulation=False,
       target_arch=None,
       codesign_identity=None,
       entitlements_file=None,
       icon='yamms/ui_pyside/resources/icon.ico',  # Windows-Icon
   )

Build-Optimierung
~~~~~~~~~~~~~~~

.. code-block:: bash

   # PyInstaller-Optimierungen
   pyinstaller \
     --onefile \                    # Single executable
     --windowed \                   # GUI-App (kein Terminal)
     --optimize=2 \                 # Python-Bytecode optimieren
     --strip \                      # Debug-Symbole entfernen
     --upx-dir=/usr/bin \          # UPX-Kompression
     --exclude-module=tkinter \     # Unnötige Module ausschließen
     --exclude-module=matplotlib \
     app/main.py

Installation & Distribution
--------------------------

Windows-Installation
~~~~~~~~~~~~~~~~~~

.. code-block:: batch

   REM Portable Installation
   yamms.exe --portable

   REM System-Installation (geplant für v0.2)
   yamms-installer.msi

Linux-Installation
~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Portable Binary
   chmod +x yamms
   ./yamms

   # System-Installation via Package Manager (geplant)
   sudo apt install yamms        # Ubuntu/Debian
   sudo dnf install yamms        # Fedora
   sudo pacman -S yamms          # Arch

   # AppImage (geplant für v0.2)
   chmod +x yamms.AppImage
   ./yamms.AppImage

macOS-Installation
~~~~~~~~~~~~~~~~

.. code-block:: bash

   # App Bundle
   open yamms.app

   # Homebrew (geplant)
   brew install --cask yamms

Auto-Update (Zukunft)
~~~~~~~~~~~~~~~~~~~

Für v0.3 geplant:

.. code-block:: python

   # Auto-Update-Mechanismus
   class UpdateChecker:
       def check_for_updates(self) -> Optional[UpdateInfo]:
           """Prüft GitHub Releases auf neue Versionen."""
           pass

       def download_update(self, update_info: UpdateInfo) -> Path:
           """Lädt Update herunter und verifiziert Signatur."""
           pass

Container-Deployment
-------------------

Docker-Support (Optional)
~~~~~~~~~~~~~~~~~~~~~~~~

Für Server-Deployments oder Development:

.. code-block:: dockerfile

   # Dockerfile
   FROM python:3.12-slim

   # System-Abhängigkeiten für GUI
   RUN apt-get update && apt-get install -y \
       libgl1-mesa-glx \
       libglib2.0-0 \
       libxcb1 \
       && rm -rf /var/lib/apt/lists/*

   WORKDIR /app
   COPY . .

   RUN pip install -e .

   # X11-Forwarding für GUI
   ENV DISPLAY=:0

   CMD ["python", "app/main.py"]

DevContainer
~~~~~~~~~~~

.. code-block:: json

   // .devcontainer/devcontainer.json
   {
       "name": "YAMMS Development",
       "image": "mcr.microsoft.com/devcontainers/python:3.12",
       "features": {
           "ghcr.io/devcontainers/features/git:1": {},
           "ghcr.io/devcontainers/features/github-cli:1": {}
       },
       "customizations": {
           "vscode": {
               "extensions": [
                   "ms-python.python",
                   "ms-python.black-formatter",
                   "charliermarsh.ruff"
               ]
           }
       },
       "postCreateCommand": "pip install -e '.[dev]'",
       "remoteUser": "vscode"
   }

Monitoring & Telemetrie
---------------------

Crash-Reporting
~~~~~~~~~~~~~~

.. code-block:: python

   # Optional: Sentry für Crash-Reports
   import sentry_sdk

   def setup_error_reporting():
       if user_consents_to_telemetry():
           sentry_sdk.init(
               dsn="...",
               environment="production",
               before_send=anonymize_user_data
           )

Performance-Monitoring
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Performance-Metriken sammeln
   class PerformanceMonitor:
       def track_startup_time(self) -> None:
           """Misst Anwendungsstart-Zeit."""
           pass

       def track_operation_time(self, operation: str) -> ContextManager:
           """Misst Zeit für spezifische Operationen."""
           pass

Security & Code-Signing
----------------------

Windows Code-Signing
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Code-Signing mit signtool (Windows)
   signtool sign /f certificate.p12 /p password /t http://timestamp.url yamms.exe

macOS Code-Signing
~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # macOS Code-Signing
   codesign --force --sign "Developer ID Application: Your Name" yamms.app

   # Notarisierung
   xcrun notarytool submit yamms.app --keychain-profile "notary"

Vulnerability-Scanning
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Abhängigkeiten auf Sicherheitslücken prüfen
   safety check

   # SBOM generieren
   cyclonedx-bom -o sbom.json

Backup & Recovery
----------------

Backup-Strategien
~~~~~~~~~~~~~~~

.. code-block:: python

   # Automatische Backups vor Updates
   class BackupManager:
       def create_pre_update_backup(self) -> Path:
           """Erstellt Backup vor App-Update."""
           pass

       def restore_from_backup(self, backup_path: Path) -> bool:
           """Stellt Daten aus Backup wieder her."""
           pass

User-Data-Migration
~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Daten-Migration zwischen Versionen
   class DataMigrator:
       def migrate_user_data(self, from_version: str, to_version: str) -> bool:
           """Migriert Benutzerdaten zwischen Versionen."""
           pass

Troubleshooting
--------------

Build-Probleme
~~~~~~~~~~~~~

**PyInstaller findet Module nicht:**

.. code-block:: bash

   # Hidden imports explizit angeben
   pyinstaller --hidden-import=PySide6.QtCore app/main.py

**Große Executable-Dateien:**

.. code-block:: bash

   # Unnötige Module ausschließen
   pyinstaller --exclude-module=matplotlib --exclude-module=scipy app/main.py

**UI-Elemente fehlen:**

.. code-block:: bash

   # Resource-Dateien explizit einbinden
   pyinstaller --add-data "resources:resources" app/main.py

Platform-spezifische Probleme
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Windows: "MSVCP140.dll fehlt"**

.. code-block:: bash

   # Visual C++ Redistributable mitliefern
   pyinstaller --collect-all=msvcrt app/main.py

**Linux: "Qt platform plugin not found"**

.. code-block:: bash

   # Qt-Plugins explizit einbinden
   pyinstaller --collect-submodules=PySide6 app/main.py

**macOS: "App kann nicht geöffnet werden"**

.. code-block:: bash

   # Gatekeeper-Probleme beheben
   xattr -cr yamms.app
   spctl --assess --verbose yamms.app
