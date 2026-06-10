from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed_ingredients = light_spell_allowed_ingredients()
    if ingredients.lower().find(allowed_ingredients):
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"
