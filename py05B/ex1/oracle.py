import os
from dotenv import load_dotenv  # pyright: ignore[reportMissingImports]


def main() -> None:
    load_dotenv()
    environment: str | None = os.getenv("MATRIX_MODE", "testing")
    database_url: str | None = os.getenv("DATABASE_URL", None)
    api_key: str | None = os.getenv("API_KEY", None)
    log_level: str | None = os.getenv("LOG_LEVEL", None)
    zion_endpoint: str | None = os.getenv("ZION_ENDPOINT", None)
    print(environment)


if __name__ == "__main__":
    main()
