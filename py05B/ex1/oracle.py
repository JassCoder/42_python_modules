import os
from dotenv import load_dotenv  # pyright: ignore[reportMissingImports]


def main() -> None:
    r = "\033[0m"
    y = "\033[33m"
    c = "\033[32m"
    load_dotenv()
    environment: str | None = os.getenv("MATRIX_MODE", None)
    database_url: str | None = os.getenv("DATABASE_URL", None)
    api_key: str | None = os.getenv("API_KEY", None)
    log_level: str | None = os.getenv("LOG_LEVEL", None)
    zion_endpoint: str | None = os.getenv("ZION_ENDPOINT", None)
    print(f"Environment  configured: {c}{environment is not None}{r}")
    print(f"Database_url configured: {c}{database_url is not None}{r}")
    print(f"Api_key      configured: {c}{api_key is not None}{r}")
    print(f"Log_level              : {c}{log_level is not None}{r}")
    print(f"Zion_endpoint          : {c}{zion_endpoint is not None}{r}")

    print()
    if environment == "development":
        print(f"Oracle running in {c}{environment}{r} mode")
    elif environment == "production":
        print(f"Oracle running in {c}{environment}{r} mode")
    else:
        print(f"{y}WARNING: Unknown or missing environment mode{r}")


if __name__ == "__main__":
    main()
