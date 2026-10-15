def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients

    allowed = light_spell_allowed_ingredients()
    valid = any(
        element in ingredients.lower()
        for element in allowed
    )

    if valid:
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
