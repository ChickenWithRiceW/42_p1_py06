from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    validation_output = validate_ingredients(ingredients)
    if "- INVALID" in validation_output:
        return f"Spell rejected: {spell_name} ({validation_output})"
    return f"Spell recorded: {spell_name} ({validation_output})"
