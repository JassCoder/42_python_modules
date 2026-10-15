from importlib import import_module


def main() -> None:
    print("=== Dark Grimoire ===")

    try:
        import_module("alchemy.grimoire.dark_spellbook")
    except ImportError as error:
        print(f"Circular import detected: {error}")


if __name__ == "__main__":
    main()
