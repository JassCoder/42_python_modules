def validate_light_ingredient(ingredient: str) -> bool:
    ingredient = ingredient.lower()

    from .light_spellbook import light_spell_allowed_ingredients

    allowed = light_spell_allowed_ingredients()
    return any(element in ingredient for element in allowed)