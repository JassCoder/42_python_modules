def secure_archive(
    filename: str,
    action: int = 0,
    content: str = ""
) -> tuple[bool, str]:
    """Read or write a file safely using the 'with' statement.

    Returns (True, <contents or success message>) on success,
    or (False, <error message>) on failure.
    """
    if action == 0:
        try:
            with open(filename, "r") as f:
                data: str = f.read()
            return (True, data)
        except OSError as error:
            return (False, str(error))

    try:
        with open(filename, "w") as f:
            f.write(content)
        return (True, "Content successfully written to file")
    except OSError as error:
        return (False, str(error))


def main() -> None:
    print("=== Cyber Archives Security ===")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))

    print("Using 'secure_archive' to read from a regular file:")
    result = secure_archive("ancient_fragment.txt")
    print(result)

    print("Using 'secure_archive' to write previous content to a new file:")
    if result[0]:
        print(secure_archive("vault_copy.txt", 1, result[1]))
    else:
        print(secure_archive("vault_copy.txt", 1, ""))


if __name__ == "__main__":
    main()
