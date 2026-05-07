from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = light_spell_allowed_ingredients()
    ingredients_list = [i.strip().lower() for i in ingredients.split(",")]
    is_valid = any(item in allowed for item in ingredients_list)
    status = "VALID" if is_valid else "INVALID"
    return f"{ingredients} - {status}"
