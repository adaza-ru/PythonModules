from typing import Callable, Any


def mage_counter() -> Callable[[], int]:

    count: int = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:

    if not isinstance(initial_power, int):
        raise TypeError("Initial power must be an integer.")
    total_power: int = initial_power

    def accumulate(amplification: int) -> int:
        if not isinstance(amplification, int):
            raise TypeError("Amplification must be an integer.")
        nonlocal total_power
        total_power += amplification
        return total_power

    return accumulate


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:

    if not isinstance(enchantment_type, str):
        raise TypeError("Enchantment type must be a string.")

    def enchant(item_name: str) -> str:
        if not isinstance(item_name, str):
            raise TypeError("Item name must be a string.")
        return f"{enchantment_type} {item_name}"

    return enchant


def memory_vault() -> dict[str, Callable[..., Any]]:

    vault: dict[str, Any] = {}

    def store(key: str, value: Any) -> str:
        if not isinstance(key, str):
            raise TypeError("Memory key must be a string.")
        vault[key] = value
        return f"Stored '{key}'"

    def recall(key: str) -> Any:
        return vault.get(key, "Memory not found")

    return {
        "store": store,
        "recall": recall
    }


if __name__ == "__main__":

    print("\nTesting mage counter...")
    try:
        counter_a = mage_counter()
        counter_b = mage_counter()
        print(f"counter_a call 1: {counter_a()}")
        print(f"counter_a call 2: {counter_a()}")
        print(f"counter_b call 1: {counter_b()}")
    except Exception as e:
        print(f"Error in mage_counter: {e}")

    print("\nTesting spell accumulator...")
    try:
        accumulator = spell_accumulator(100)

        print(f"Base 100, add 20: {accumulator(20)}")
        print(f"Base 100, add 30: {accumulator(30)}")
    except Exception as e:
        print(f"Error in spell_accumulator: {e}")

    print("\nTesting enchantment factory...")
    try:
        flame_enchant = enchantment_factory("Flaming")
        frost_enchant = enchantment_factory("Frozen")
        print(flame_enchant("Sword"))
        print(frost_enchant("Shield"))
    except Exception as e:
        print(f"Error in enchantment_factory: {e}")

    print("\nTesting memory vault...")
    try:
        vault_funcs = memory_vault()
        store_spell = vault_funcs["store"]
        recall_spell = vault_funcs["recall"]
        print(f"Store 'secret' = 42 -> {store_spell('secret', 42)}")
        print(f"Recall 'secret': {recall_spell('secret')}")
        print(f"Recall 'unknown': {recall_spell('unknown')}")
    except Exception as e:
        print(f"Error in memory_vault: {e}")
