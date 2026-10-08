import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
        return
    print("=== Cyber Archives Recovery & Preservation ===")

    filename: str = sys.argv[1]
    print(f"Accessing file '{filename}'")
    try:
        f: typing.IO[str] = open(filename, "r")
    except OSError as error:
        print(f"[STDERR] Error opening file '{filename}': {error}",
              file=sys.stderr)
        return
    content: str = f.read()
    print("---")
    print(content, end="\n")
    print("---")
    f.close()
    print(f"File '{filename}' closed.")
    transformed: str = ""
    for line in content.splitlines(keepends=True):
        if line.endswith("\n"):
            transformed += line[:-1] + "#\n"
        else:
            transformed += line + "#"
    print("Transform data:")
    print("---")
    print(transformed, end="\n")
    print("---")

    print("Enter new file name (or empty): ", end="")
    sys.stdout.flush()
    new_name: str = sys.stdin.readline().strip()
    if new_name == "":
        print("Not saving data.")
        return
    print(f"Saving data to '{new_name}'")
    try:
        out: typing.IO[str] = open(new_name, "w")
        out.write(transformed)
        out.close()
        print(f"Data saved in file '{new_name}'.")
    except OSError as error:
        print(f"[STDERR] Error opening file '{new_name}': {error}",
              file=sys.stderr)
        print("Data not saved.")
        return


if __name__ == "__main__":
    main()
