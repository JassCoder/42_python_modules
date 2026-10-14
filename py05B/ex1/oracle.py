"""
The Oracle: Environment Configuration Checker.

This module uses python-dotenv to load configuration
variables from a .env file.

It checks whether the required environment variables
are configured, provides default values, and displays
warnings when configuration is missing.

It also supports development and production modes. 
"""
import os
from dotenv import load_dotenv


def main() -> None:
    r = "\033[0m"
    y = "\033[33m"
    c = "\033[32m"
    print()
    print(f"ORACLE STATUS: {c}Consulting the configuration...{r}")
    loaded: bool = load_dotenv()
    if loaded:
        print(f"{c}[OK] Configuration loaded from .env{r}")
    else:
        print(f"{y}[WARNING] No configuration loaded from .env{r}")
        print(f"{y}Using environment variables or default values.{r}")
    print()
    environment: str = os.getenv("MATRIX_MODE", "development")
    database_url: str | None = os.getenv("DATABASE_URL", None)
    api_key: str | None = os.getenv("API_KEY", None)
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    zion_endpoint: str | None = os.getenv("ZION_ENDPOINT", None)
    print()
    print(f"Mode: {c}{environment}{r}")
    print(f"Database: {c}{'Configured' if database_url else 'Not configured'}{r}")
    print(f"API Access: {c}{'Key configured' if api_key else 'Key missing'}{r}")
    print(f"Log Level:{c}{log_level}{r}")
    print(f"Remote Network:{c}{'Endpoint configured' if zion_endpoint else 'Not configured'}{r}")
    print()
    print()
    if environment == "development":
        print(f"Oracle running in {c}{environment}{r} mode")
    elif environment == "production":
        print(f"Oracle running in {c}{environment}{r} mode")
    else:
        print(f"{y}WARNING: Unknown or missing environment mode{r}")
    print()
    print()
    if database_url is None:
        print(f"{y}WARNING: DATABASE_URL is missing{r}")
    if api_key is None:
        print(f"{y}WARNING: API_KEY is missing{r}")
    if zion_endpoint is None:
        print(f"{y}WARNING: ZION_ENDPOINT is missing{r}")


if __name__ == "__main__":
    main()
