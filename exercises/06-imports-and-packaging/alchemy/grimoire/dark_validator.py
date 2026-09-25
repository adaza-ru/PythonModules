from .dark_spellbook import dark_spell_allowed_ingredients


def validate_dark_ingredients(ingredients: str) -> str:
    allowed: list[str] = dark_spell_allowed_ingredients()
    ingredients_list: list[str] = [
        i.strip().lower() for i in ingredients.split(",")
    ]
    is_valid: bool = any(item in allowed for item in ingredients_list)
    status: str = "VALID" if is_valid else "INVALID"
    return f"{ingredients} - {status}"
