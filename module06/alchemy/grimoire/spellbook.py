def record_spell(spell_name: str, ingredients: str) -> str:
    # Late import inside the function to avoid circular dependency.
    # If we imported at the top of the file AND validator imported spellbook,
    # Python would get stuck in an infinite import loop. By importing here,
    # we delay the import until the function is actually called
    # , breaking the cycle.
    from .validator import validate_ingredients

    validation_result = validate_ingredients(ingredients)
    if "VALID" in validation_result and "INVALID" not in validation_result:
        return f"Spell recorded: {spell_name} ({validation_result})"
    return f"Spell rejected: {spell_name} ({validation_result})"
