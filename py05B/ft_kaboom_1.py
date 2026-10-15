def main() -> None:
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")

    try:
        from alchemy.grimoire.dark_spellbook import dark_spell_record
        print(dark_spell_record("Dark Ritual", "bats"))  # noqa: F401
    except ImportError as error:
        print(f"Laboratory exploded: {error}")


if __name__ == "__main__":
    main()
