import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    filename: str = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    try:
        f: typing.IO[str] = open(filename, "r")
    except OSError as error:
        print(f"Error opening file '{filename}': {error}")
        return
    print("---")
    print(f.read(), end="")
    print("---")
    f.close()
    print(f"File '{filename}' closed.")


if __name__ == "__main__":
    main()
