from .light_validator import validate_ingredients


def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    validation_output = validate_ingredients(ingredients)
    return f"spell recorded: {spell_name} ({validation_output})"
