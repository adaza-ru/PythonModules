from typing import Callable


def fireball(target: str, power: int) -> str:
    return f"Fireball scorches {target} for {power} damage"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def shield(target: str, power: int) -> str:
    return f"Shield protects {target} blocking {power} damage"


def is_boss(target: str, power: int) -> bool:
    return target.lower() == "dragon" and power >= 50


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    if not (callable(spell1) and callable(spell2)):
        raise TypeError("Both arguments must be callable functions.")

    def combined_spell(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))

    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    if not callable(base_spell):
        raise TypeError("base_spell must be a callable function.")
    if not isinstance(multiplier, (int, float)):
        raise TypeError("multiplier must be a numeric value.")

    def amplified_spell(target: str, power: int) -> str:
        return base_spell(target, int(power * multiplier))

    return amplified_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    if not (callable(condition) and callable(spell)):
        raise TypeError("Both condition and spell must be callable functions.")

    def conditional_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"

    return conditional_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    if not isinstance(spells, list) or not all(callable(s) for s in spells):
        raise TypeError("spells must be a list of callable functions.")

    def sequenced_spells(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]

    return sequenced_spells


if __name__ == "__main__":

    print("\nTesting spell combiner...")
    try:
        combined = spell_combiner(fireball, heal)
        result_combo = combined("Dragon", 50)
        print(f"Combined spell result: {result_combo[0]}, {result_combo[1]}")
    except Exception as e:
        print(f"Error in spell_combiner: {e}")

    print("\nTesting power amplifier...")
    try:
        original_power = 10
        multiplier = 3
        mega_fireball = power_amplifier(fireball, multiplier)
        print(f"Original: {fireball('Goblin', original_power)}")
        print(f"Amplified: {mega_fireball('Goblin', original_power)}")
    except Exception as e:
        print(f"Error in power_amplifier: {e}")

    print("\nTesting conditional caster...")
    try:
        boss_slayer = conditional_caster(is_boss, fireball)
        print(f"Against Boss: {boss_slayer('Dragon', 100)}")
        print(f"Against Minion: {boss_slayer('Goblin', 100)}")
        print(f"Against Boss (weak): {boss_slayer('Dragon', 20)}")
    except Exception as e:
        print(f"Error in conditional_caster: {e}")

    print("\nTesting spell sequence...")
    try:
        ultimate_combo = spell_sequence([shield, fireball, heal])
        results = ultimate_combo("Hero", 30)
        for i, res in enumerate(results, 1):
            print(f"Action {i}: {res}")
    except Exception as e:
        print(f"Error in spell_sequence: {e}")
