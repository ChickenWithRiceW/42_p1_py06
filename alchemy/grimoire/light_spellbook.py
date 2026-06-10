

def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    from .light_validator import validate_ingredients
    validation_output = validate_ingredients(ingredients)
    if "- INVALID" in validation_output:
        return f"Spell rejected: {spell_name} ({validation_output})"
    return f"Spell recorded: {spell_name} ({validation_output})"
