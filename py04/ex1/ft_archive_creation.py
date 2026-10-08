import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return

    filename: str = sys.argv[1]

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")
    try:
        f: typing.IO[str] = open(filename, "r")
    except OSError as error:
        print(f"Error opening file '{filename}': {error}")
        return
    content: str = f.read()
    print("---")
    print(content, end="")
    print("---")
    f.close()
    print(f"File '{filename}' closed.")
    transformed: str = ""
    for line in content.splitlines(keepends=True):
        if line.endswith("\n"):
            transformed = transformed + line[:-1] + "#\n"
        else:
            transformed += line + "#"
    print("Transform data:")
    print("---")
    print(transformed, end="")
    print("---")

    new_name: str = input("Enter new file name (or empty): ")
    if new_name == "":
        print("Not saving data.")
        return
    print(f"Saving data to '{new_name}'")
    out: typing.IO[str] = open(new_name, "w")
    out.write(transformed)
    out.close()
    print(f"Data saved in file '{new_name}'.")


if __name__ == "__main__":
    main()
