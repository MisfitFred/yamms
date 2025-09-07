"""YAMMS Konfiguration basierend auf Pydantic Settings."""

from functools import lru_cache
from pathlib import Path

from platformdirs import user_config_dir, user_data_dir
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """YAMMS Anwendungseinstellungen."""

    # Anwendungseinstellungen
    debug: bool = Field(default=False, description="Debug-Modus aktivieren")
    log_level: str = Field(default="INFO", description="Log-Level")

    # Datenbankeinstellungen
    database_url: str = Field(
        default_factory=lambda: f"sqlite:///{user_data_dir('yamms')}/yamms.db",
        description="Datenbank-URL",
    )
    database_encrypt: bool = Field(default=False, description="Datenbank verschlüsseln")
    database_password: str | None = Field(
        default=None, description="Datenbank-Passwort"
    )

    # UI-Einstellungen
    theme: str = Field(default="system", description="UI-Theme (light/dark/system)")
    language: str = Field(default="de", description="Sprache")

    # Verzeichnisse
    config_dir: Path = Field(
        default_factory=lambda: Path(user_config_dir("yamms")),
        description="Konfigurationsverzeichnis",
    )
    data_dir: Path = Field(
        default_factory=lambda: Path(user_data_dir("yamms")),
        description="Datenverzeichnis",
    )

    model_config = SettingsConfigDict(
        env_prefix="YAMMS_",
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )


@lru_cache
def get_settings() -> Settings:
    """Hole gecachte Settings-Instanz."""
    return Settings()
