def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    allowed: list[str] = light_spell_allowed_ingredients()
    ingredients_list: list[str] = [
        i.strip().lower() for i in ingredients.split(",")
    ]
    is_valid: bool = any(item in allowed for item in ingredients_list)
    status: str = "VALID" if is_valid else "INVALID"
    return f"{ingredients} - {status}"
