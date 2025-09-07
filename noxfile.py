"""Nox-Konfiguration für YAMMS Development Tasks."""

import nox

# Python-Versionen für Tests
PYTHON_VERSIONS = ["3.12"]
# Haupt-Python-Version für andere Tasks
MAIN_PYTHON = "3.12"


@nox.session(python=MAIN_PYTHON)
def format(session):
    """Code formatieren mit Black und Ruff."""
    session.install("black", "ruff")
    session.run("black", "yamms", "tests", "noxfile.py")
    session.run("ruff", "check", "--fix", "yamms", "tests", "noxfile.py")


@nox.session(python=MAIN_PYTHON)
def lint(session):
    """Linting mit Ruff."""
    session.install("ruff")
    session.run("ruff", "check", "yamms", "tests", "noxfile.py")


@nox.session(python=MAIN_PYTHON)
def typecheck(session):
    """Typen-Checks mit MyPy."""
    session.install("-e", ".[dev]")
    session.run("mypy", "yamms")


@nox.session(python=PYTHON_VERSIONS)
def tests(session):
    """Tests mit pytest ausführen."""
    session.install("-e", ".[test]")
    session.run("pytest", "-v", "--cov=yamms", "--cov-report=term-missing")


@nox.session(python=MAIN_PYTHON)
def tests_ui(session):
    """UI-Tests mit pytest-qt."""
    session.install("-e", ".[test]")
    session.run("pytest", "-v", "-m", "ui", "--cov=yamms")


@nox.session(python=MAIN_PYTHON)
def coverage(session):
    """Coverage-Report generieren."""
    session.install("-e", ".[test]")
    session.run("coverage", "run", "-m", "pytest")
    session.run("coverage", "report")
    session.run("coverage", "html")


@nox.session(python=MAIN_PYTHON)
def docs(session):
    """Dokumentation mit Sphinx generieren."""
    session.install("-e", ".[docs]")
    session.cd("docs")
    session.run("sphinx-build", "-b", "html", "source", "build/html", "-W")


@nox.session(python=MAIN_PYTHON)
def docs_serve(session):
    """Dokumentation mit Live-Reload."""
    session.install("-e", ".[docs]", "sphinx-autobuild")
    session.cd("docs")
    session.run(
        "sphinx-autobuild",
        "source",
        "build/html",
        "--host",
        "0.0.0.0",
        "--port",
        "8000",
    )


@nox.session(python=MAIN_PYTHON)
def security(session):
    """Security-Checks."""
    session.install("safety", "bandit", "pip-audit")
    session.run("safety", "check")
    session.run("bandit", "-r", "yamms")
    session.run("pip-audit")


@nox.session(python=MAIN_PYTHON)
def pre_commit(session):
    """Pre-commit-Hooks installieren."""
    session.install("pre-commit")
    session.run("pre-commit", "install")


@nox.session(python=MAIN_PYTHON)
def pre_commit_all(session):
    """Pre-commit-Hooks auf alle Dateien anwenden."""
    session.install("pre-commit")
    session.run("pre-commit", "run", "--all-files")


@nox.session(python=MAIN_PYTHON)
def clean(session):
    """Build-Artefakte löschen."""
    import shutil
    from pathlib import Path

    artifacts = [
        "build",
        "dist",
        "*.egg-info",
        ".coverage",
        "htmlcov",
        ".pytest_cache",
        ".mypy_cache",
        "__pycache__",
        "docs/build",
    ]

    for pattern in artifacts:
        for path in Path().glob(pattern):
            if path.is_dir():
                shutil.rmtree(path)
                print(f"Entfernt: {path}")
            elif path.is_file():
                path.unlink()
                print(f"Entfernt: {path}")


@nox.session(python=MAIN_PYTHON)
def build(session):
    """Baut Wheel und Source Distribution."""
    session.install("build")
    session.run("python", "-m", "build")


@nox.session(python=MAIN_PYTHON)
def dev_install(session):
    """Entwicklungsumgebung installieren."""
    session.install("-e", ".[dev]")
    session.run("pre-commit", "install")


@nox.session(python=MAIN_PYTHON)
def ci(session):
    """Alle CI-Checks ausführen."""
    session.notify("format")
    session.notify("lint")
    session.notify("typecheck")
    session.notify("tests")
    session.notify("security")
    session.notify("docs")
