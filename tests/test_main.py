"""Tests für YAMMS Hauptmodul."""

from yamms.main import main


def test_main_returns_zero():
    """Test dass main() erfolgreich (Exit-Code 0) zurückgibt."""
    result = main([])
    assert result == 0


def test_main_with_args():
    """Test main() mit Argumenten."""
    result = main(["--help"])  # Wird ignoriert in aktueller Implementierung
    assert result == 0
