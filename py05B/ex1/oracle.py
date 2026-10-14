import os
from dotenv import load_dotenv  # pyright: ignore[reportMissingImports]


def main() -> None:
    r = "\033[0m"
    y = "\033[33m"
    c = "\033[32m"
    load_dotenv()
    environment: str = os.getenv("MATRIX_MODE", "development")
    database_url: str | None = os.getenv("DATABASE_URL", None)
    api_key: str | None = os.getenv("API_KEY", None)
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    zion_endpoint: str | None = os.getenv("ZION_ENDPOINT", None)
    print(f"Mode                   : {c}{environment}{r}")
    print(f"Database_url configured: {c}{database_url is not None}{r}")
    print(f"Api_key      configured: {c}{api_key is not None}{r}")
    print(f"Log Level              : {c}{log_level}{r}")
    print(f"Zion_endpoint          : {c}{zion_endpoint is not None}{r}")

    print()
    if environment == "development":
        print(f"Oracle running in {c}{environment}{r} mode")
    elif environment == "production":
        print(f"Oracle running in {c}{environment}{r} mode")
    else:
        print(f"{y}WARNING: Unknown or missing environment mode{r}")
    print()
    if database_url is None:
        print(f"{y}WARNING: DATABASE_URL is missing{r}")
    if api_key is None:
        print(f"{y}WARNING: API_KEY is missing{r}")
    if zion_endpoint is None:
        print(f"{y}WARNING: ZION_ENDPOINT is missing{r}")


if __name__ == "__main__":
    main()
