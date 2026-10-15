from alchemy.grimoire.light_spellbook import record_light_spell


def main() -> None:
    print("=== Light Grimoire ===")
    print(record_light_spell("fire"))
    print(record_light_spell("earth crystal"))
    print(record_light_spell("dragon blood"))


if __name__ == "__main__":
    main()
