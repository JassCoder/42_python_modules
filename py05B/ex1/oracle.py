import os
from dotenv import load_dotenv # pyright: ignore[reportMissingImports]

def main() -> None:
    load_dotenv()
    environment = os.getenv("MATRIX_MODE", "development")
    print(environment)


if __name__ == "__main__":
    main()