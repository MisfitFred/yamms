"""Tests für YAMMS Konfiguration."""

from pathlib import Path

from yamms.config import Settings, get_settings


def test_settings_default_values():
    """Test dass Settings standardwerte hat."""
    settings = Settings()

    assert settings.debug is False
    assert settings.log_level == "INFO"
    assert settings.database_encrypt is False
    assert settings.theme == "system"
    assert settings.language == "de"


def test_settings_database_url():
    """Test dass Database-URL korrekt generiert wird."""
    settings = Settings()

    assert "yamms.db" in settings.database_url
    assert settings.database_url.startswith("sqlite://")


def test_settings_directories():
    """Test dass Verzeichnisse als Path-Objekte verfügbar sind."""
    settings = Settings()

    assert isinstance(settings.config_dir, Path)
    assert isinstance(settings.data_dir, Path)
    assert "yamms" in str(settings.config_dir)
    assert "yamms" in str(settings.data_dir)


def test_get_settings_cached():
    """Test dass get_settings() gecacht wird."""
    settings1 = get_settings()
    settings2 = get_settings()

    assert settings1 is settings2  # Identisches Objekt durch Cache
