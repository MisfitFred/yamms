# GitHub Issues für YAMMS MVP

## Epic: Core Data Layer
**Label:** `epic`, `priority:high`, `mvp`

### Issue 1: Setup SQLCipher Database
**Labels:** `feature`, `database`, `security`, `mvp`
**Assignee:** MisfitFred
**Milestone:** MVP v0.1.0

**Description:**
Implement encrypted local database using SQLCipher for GDPR-compliant data storage.

**Acceptance Criteria:**
- [ ] SQLCipher integration with Python
- [ ] Database schema creation and migration system
- [ ] Password-protected database encryption
- [ ] Connection pooling and error handling
- [ ] Unit tests for database operations

**Technical Requirements:**
```python
# Expected API
from yamms.database import DatabaseManager

db = DatabaseManager("yamms.db", password="user_password")
db.create_tables()
```

**Definition of Done:**
- Database creates encrypted .db file
- All tables created with proper schemas
- Password protection working
- Tests pass with 100% coverage

---

### Issue 2: Create Core Data Models
**Labels:** `feature`, `models`, `mvp`
**Assignee:** MisfitFred
**Milestone:** MVP v0.1.0

**Description:**
Define dataclass models for Student, Grade, Subject, and Class entities with validation.

**Acceptance Criteria:**
- [ ] Student model with ID, name, class assignment
- [ ] Grade model with value, date, weight, type
- [ ] Subject model with name, weight, description
- [ ] Class model with name, year, student list
- [ ] Pydantic validation for all fields
- [ ] Type hints and documentation

**Technical Requirements:**
```python
@dataclass
class Student:
    id: UUID
    first_name: str
    last_name: str
    class_id: UUID
    created_at: datetime

    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
```

---

### Issue 3: Implement Database Repository Pattern
**Labels:** `feature`, `repository`, `mvp`
**Assignee:** MisfitFred
**Milestone:** MVP v0.1.0

**Description:**
Create repository classes for CRUD operations on all entities.

**Acceptance Criteria:**
- [ ] StudentRepository with full CRUD
- [ ] GradeRepository with full CRUD
- [ ] SubjectRepository with full CRUD
- [ ] ClassRepository with full CRUD
- [ ] Async/await support for operations
- [ ] Transaction support for bulk operations

**Technical Requirements:**
```python
class StudentRepository:
    async def create(self, student: Student) -> Student:
    async def get_by_id(self, id: UUID) -> Optional[Student]:
    async def get_by_class(self, class_id: UUID) -> List[Student]:
    async def update(self, student: Student) -> Student:
    async def delete(self, id: UUID) -> bool:
```

---

## Epic: GUI Foundation
**Label:** `epic`, `priority:high`, `mvp`, `gui`

### Issue 4: Create Main Window with PySide6
**Labels:** `feature`, `gui`, `mvp`
**Assignee:** MisfitFred
**Milestone:** MVP v0.1.0

**Description:**
Implement main application window with menu bar, toolbar, and navigation.

**Acceptance Criteria:**
- [ ] Main window with proper layout
- [ ] Menu bar (File, Edit, View, Help)
- [ ] Toolbar with common actions
- [ ] Status bar with application info
- [ ] Window state persistence (size, position)
- [ ] Application icon and branding

**Technical Requirements:**
```python
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YAMMS - Yet Another Mark Management System")
        self.setup_ui()
        self.setup_menus()
        self.setup_toolbar()
```

---

### Issue 5: Student Management Widget
**Labels:** `feature`, `gui`, `students`, `mvp`
**Assignee:** MisfitFred
**Milestone:** MVP v0.1.0

**Description:**
Create widget for displaying and managing student list with table view.

**Acceptance Criteria:**
- [ ] QTableView for student display
- [ ] Add/Edit/Delete student dialogs
- [ ] Search and filter functionality
- [ ] Sort by name, class, ID
- [ ] Context menu for quick actions
- [ ] Keyboard shortcuts (Ctrl+N, Del, etc.)

**Mockup:**
```
┌─ Students ─────────────────────────┐
│ [Add] [Edit] [Delete] [🔍Search]   │
├────────────────────────────────────┤
│ Name        │ Class │ ID     │ Avg │
│ Max Müller  │ 10A   │ 001    │ 2.3 │
│ Anna Schmidt│ 10A   │ 002    │ 1.8 │
│ ...         │       │        │     │
└────────────────────────────────────┘
```

---

### Issue 6: Grade Entry Dialog
**Labels:** `feature`, `gui`, `grades`, `mvp`
**Assignee:** MisfitFred
**Milestone:** MVP v0.1.0

**Description:**
Dialog for entering and editing grades with validation and calculation preview.

**Acceptance Criteria:**
- [ ] Student selection dropdown
- [ ] Subject selection dropdown
- [ ] Grade value input (1.0 - 6.0 German system)
- [ ] Date picker (default: today)
- [ ] Weight factor input
- [ ] Grade type selection (exam, homework, oral)
- [ ] Live average calculation preview
- [ ] Input validation and error messages

---

## Epic: Business Logic
**Label:** `epic`, `priority:medium`, `mvp`

### Issue 7: Grade Calculation Service
**Labels:** `feature`, `calculation`, `mvp`
**Assignee:** MisfitFred
**Milestone:** MVP v0.1.0

**Description:**
Service for calculating weighted averages and grade statistics.

**Acceptance Criteria:**
- [ ] Calculate student average per subject
- [ ] Calculate student overall average
- [ ] Calculate class average per subject
- [ ] Weighted grade calculations
- [ ] Handle different grading systems
- [ ] Performance optimization for large datasets

**Technical Requirements:**
```python
class GradeCalculator:
    def calculate_student_average(self, student_id: UUID, subject_id: UUID) -> float:
    def calculate_student_overall(self, student_id: UUID) -> float:
    def calculate_class_average(self, class_id: UUID, subject_id: UUID) -> float:
```

---

### Issue 8: Data Validation Service
**Labels:** `feature`, `validation`, `mvp`
**Assignee:** MisfitFred
**Milestone:** MVP v0.1.0

**Description:**
Comprehensive validation for all user inputs and data consistency.

**Acceptance Criteria:**
- [ ] Grade value validation (1.0-6.0)
- [ ] Name validation (no special chars)
- [ ] Date validation (not future dates)
- [ ] Duplicate prevention (same student/subject/date)
- [ ] Data consistency checks
- [ ] User-friendly error messages

---

## Epic: Data Export/Import
**Label:** `epic`, `priority:low`, `mvp+`

### Issue 9: CSV Export Functionality
**Labels:** `feature`, `export`, `mvp+`
**Assignee:** MisfitFred
**Milestone:** MVP v0.2.0

**Description:**
Export student grades and statistics to CSV format.

**Acceptance Criteria:**
- [ ] Export individual student grades
- [ ] Export class overview
- [ ] Export grade statistics
- [ ] Configurable CSV format
- [ ] Progress indicator for large exports
- [ ] Error handling for file operations

---

### Issue 10: Basic PDF Reports
**Labels:** `feature`, `export`, `pdf`, `mvp+`
**Assignee:** MisfitFred
**Milestone:** MVP v0.2.0

**Description:**
Generate simple PDF reports for individual students and classes.

**Acceptance Criteria:**
- [ ] Student grade report (transcript style)
- [ ] Class overview report
- [ ] Configurable report templates
- [ ] School logo/header support
- [ ] Print-friendly formatting

---

## Epic: Settings & Security
**Label:** `epic`, `priority:medium`, `security`

### Issue 11: Application Settings
**Labels:** `feature`, `settings`, `mvp+`
**Assignee:** MisfitFred
**Milestone:** MVP v0.2.0

**Description:**
Settings dialog for application configuration and preferences.

**Acceptance Criteria:**
- [ ] Database password change
- [ ] Grading system selection (1-6, A-F, etc.)
- [ ] UI theme selection
- [ ] Auto-backup settings
- [ ] Language selection (DE/EN)
- [ ] Settings persistence

---

### Issue 12: Backup & Restore
**Labels:** `feature`, `backup`, `security`, `mvp+`
**Assignee:** MisfitFred
**Milestone:** MVP v0.2.0

**Description:**
Automated and manual backup functionality with restore capabilities.

**Acceptance Criteria:**
- [ ] Manual backup creation
- [ ] Automatic backup scheduling
- [ ] Encrypted backup files
- [ ] Backup verification
- [ ] One-click restore functionality
- [ ] Backup location configuration

---

## Development Guidelines

### Branch Strategy:
- `main` - Production ready code
- `develop` - Integration branch
- `feature/issue-{number}-{short-description}` - Feature branches

### Commit Convention:
```
feat(database): add SQLCipher integration (#1)
fix(gui): resolve student table sorting issue (#5)
docs(readme): update installation instructions
test(models): add validation tests for Grade model
```

### Review Requirements:
- [ ] All tests pass
- [ ] Code coverage > 80%
- [ ] Type hints complete
- [ ] Documentation updated
- [ ] Security review for data handling

### Milestones:
- **MVP v0.1.0** (3 weeks) - Core functionality
- **MVP v0.2.0** (2 weeks) - Export & Settings
- **MVP v1.0.0** (1 week) - Polish & Release
