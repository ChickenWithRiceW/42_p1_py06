from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed_ingredients = dark_spell_allowed_ingredients()
    if ingredients.lower().find(allowed_ingredients):
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"
