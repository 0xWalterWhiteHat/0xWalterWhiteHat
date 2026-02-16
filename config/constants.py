"""Application configuration constants."""


class AppConfig:
    """Application configuration constants."""

    VERSION = '1.0.0'
    APP_NAME = 'Walter'
    MAX_RETRIES = 3


def get_config():
    """Return an AppConfig instance."""
    return AppConfig()
