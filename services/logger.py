"""Logger service module."""

from datetime import datetime, timezone


class Logger:
    """A simple logger that prints formatted log messages with timestamps."""

    def _format(self, level: str, message: str) -> str:
        ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
        return f"[{ts}] [{level}] {message}"

    def info(self, message: str) -> None:
        """Print an informational log message with timestamp."""
        print(self._format("INFO", message))

    def warn(self, message: str) -> None:
        """Print a warning log message with timestamp."""
        print(self._format("WARN", message))

    def error(self, message: str) -> None:
        """Print an error log message with timestamp."""
        print(self._format("ERROR", message))
