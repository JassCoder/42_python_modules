from .dark_spellbook import dark_spell_allowed_ingredients


def validate_dark_ingredient(ingredient: str) -> bool:
    allowed = dark_spell_allowed_ingredients()
    return any(
        element in ingredient.lower()
        for element in allowed
    )
