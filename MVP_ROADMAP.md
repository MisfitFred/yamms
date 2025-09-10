# YAMMS MVP Roadmap

## Projektstruktur

```
yamms/
├── core/                   # Kernlogik
│   ├── models/            # Datenmodelle
│   ├── database/          # DB-Layer mit SQLCipher
│   └── services/          # Business Logic
├── gui/                   # Qt GUI
│   ├── widgets/           # Wiederverwendbare UI-Komponenten
│   ├── dialogs/           # Dialog-Fenster
│   └── main_window/       # Hauptfenster
├── utils/                 # Hilfsfunktionen
└── resources/             # UI-Dateien, Icons, etc.
```

## MVP Features (Priorität 1)

### 1. **Grunddatenstruktur** 📊
**Aufwand:** 2-3 Tage
**Tasks:**
- [ ] SQLCipher Datenbank Setup
- [ ] Schüler-Model (Name, ID, Klasse)
- [ ] Fächer-Model (Name, Gewichtung)
- [ ] Noten-Model (Wert, Datum, Typ, Gewichtung)
- [ ] Klassen-Model (Name, Schuljahr)

**Technisch:**
```python
# models/student.py
@dataclass
class Student:
    id: str
    first_name: str
    last_name: str
    class_id: str

# models/grade.py
@dataclass
class Grade:
    student_id: str
    subject_id: str
    value: float
    date: datetime
    weight: float = 1.0
```

### 2. **Basis-GUI** 🖥️
**Aufwand:** 3-4 Tage
**Tasks:**
- [ ] Hauptfenster mit Menüleiste
- [ ] Schüler-Liste (TableView)
- [ ] Einfache Noten-Eingabe Dialog
- [ ] Basis-Navigation zwischen Views

**Technisch:**
```python
# gui/main_window/main_window.py
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.setup_menus()

# gui/widgets/student_table.py
class StudentTableWidget(QTableWidget):
    # Schüler-Tabelle mit Sortierung
```

### 3. **CRUD Operationen** ✏️
**Aufwand:** 2-3 Tage
**Tasks:**
- [ ] Schüler hinzufügen/bearbeiten/löschen
- [ ] Noten hinzufügen/bearbeiten/löschen
- [ ] Fächer verwalten
- [ ] Klassen verwalten

### 4. **Einfache Berechnungen** 🧮
**Aufwand:** 1-2 Tage
**Tasks:**
- [ ] Notendurchschnitt pro Schüler
- [ ] Notendurchschnitt pro Fach
- [ ] Gewichtete Durchschnitte
- [ ] Einfache Statistiken

**Technisch:**
```python
# services/grade_calculator.py
class GradeCalculator:
    def calculate_average(self, grades: List[Grade]) -> float:
        if not grades:
            return 0.0
        total_weight = sum(g.weight for g in grades)
        weighted_sum = sum(g.value * g.weight for g in grades)
        return weighted_sum / total_weight
```

## MVP+ Features (Priorität 2)

### 5. **Export/Import** 📤
**Aufwand:** 2-3 Tage
**Tasks:**
- [ ] CSV Export
- [ ] PDF Zeugnisse (einfach)
- [ ] Backup/Restore
- [ ] Excel Import

### 6. **Erweiterte UI** 🎨
**Aufwand:** 2-3 Tage
**Tasks:**
- [ ] Besseres Styling mit QSS
- [ ] Icons und Themes
- [ ] Keyboard Shortcuts
- [ ] Statusbar mit Infos

### 7. **Sicherheit & Settings** 🔒
**Aufwand:** 1-2 Tage
**Tasks:**
- [ ] Passwort-Setup für DB
- [ ] Einstellungen Dialog
- [ ] Automatische Backups
- [ ] Update-Check

## Future Features (Priorität 3)

### 8. **Erweiterte Analysen** 📈
- Notenverteilung Diagramme
- Entwicklung über Zeit
- Vergleiche zwischen Klassen
- Export für Schulverwaltung

### 9. **Collaboration** 👥
- Multi-User Support
- Lehrer-Accounts
- Berechtigung-System
- Sync zwischen Geräten

## Technologie-Stack Entscheidungen

### **Database:** SQLCipher
```python
# Verschlüsselte SQLite für DSGVO-Konformität
# Lokale Datenspeicherung, keine Cloud
```

### **GUI:** PySide6 (Qt)
```python
# Moderne, native UI
# Cross-platform (Windows/Mac/Linux)
# Professionelles Aussehen
```

### **Architecture:** MVC Pattern
```python
yamms/
├── models/     # Datenlogik
├── views/      # UI Components
└── controllers/# Business Logic
```

## MVP Zeitplan (ca. 2-3 Wochen)

**Woche 1:** Features 1-2 (Datenstruktur + Basis-GUI)
**Woche 2:** Features 3-4 (CRUD + Berechnungen)
**Woche 3:** Testing, Polish, erste MVP-Version

## Erste Schritte

1. **Start hier:** Models und Database Setup
2. **Dann:** Einfachstes GUI mit einer Schüler-Tabelle
3. **Iterativ ausbauen:** Feature für Feature

Soll ich mit der Implementation von Feature 1 (Datenmodelle) anfangen?
