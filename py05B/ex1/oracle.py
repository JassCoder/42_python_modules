"""
The Oracle: Environment Configuration Checker.

This module uses python-dotenv to load configuration
variables from a .env file.

It checks whether the required environment
variables are configured,
provides default values, and displays
warnings when configuration is missing.
It also supports development and production modes.
"""
import os
import dotenv


def main() -> None:
    print()
    print("ORACLE STATUS: Consulting the configuration...")
    loaded: bool = dotenv.load_dotenv()
    if loaded:
        print("[OK] Configuration loaded from .env")
    else:
        print("[WARNING] No configuration loaded from .env")
        print("Using environment variables or default values.")
    print()
    environment: str = os.getenv("MATRIX_MODE", "development")
    database_url: str | None = os.getenv("DATABASE_URL", None)
    api_key: str | None = os.getenv("API_KEY", None)
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    zion_endpoint: str | None = os.getenv("ZION_ENDPOINT", None)
    print()
    print(f"Mode: {environment}")
    print(f"Database: "
          f"{'Configured' if database_url else 'Not configured'}")
    print(f"API Access: "
          f"{'Key configured' if api_key else 'Key missing'}")
    print(f"Log Level: {log_level}")
    print(f"Remote Network: "
          f"{'Endpoint configured' if zion_endpoint else 'Not configured'}")
    print()
    print()
    if environment == "development":
        print(f"Oracle running in {environment} mode")
    elif environment == "production":
        print(f"Oracle running in {environment} mode")
    else:
        print("WARNING: Unknown or missing environment mode")
    print()
    print()
    if database_url is None:
        print("WARNING: DATABASE_URL is missing")
    if api_key is None:
        print("WARNING: API_KEY is missing")
    if zion_endpoint is None:
        print("WARNING: ZION_ENDPOINT is missing")

    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
