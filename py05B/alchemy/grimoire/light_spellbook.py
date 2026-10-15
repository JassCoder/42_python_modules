

def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def record_light_spell(ingredient: str) -> str:
    from .light_validator import validate_light_ingredient

    if validate_light_ingredient(ingredient):
        return f"Light spell recorded with {ingredient}"

    return f"Light spell rejected: {ingredient}"
