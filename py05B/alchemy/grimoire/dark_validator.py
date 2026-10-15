from .dark_spellbook import dark_spell_allowed_ingredients


def dark_validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    valid = any(
        element in ingredients.lower()
        for element in allowed
    )

    if valid:
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
