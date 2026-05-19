import functools
import operator
from typing import Callable, Any


def spell_reducer(spells: list[int], operation: str) -> int:

    if not isinstance(spells, list):
        raise TypeError("Spells must be a list of integers.")

    if not spells:
        return 0

    ops_map: dict[str, Callable[[int, int], int]] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min,
    }

    if operation not in ops_map:
        raise ValueError(f"Unknown operation: '{operation}'. "
                         f"Valid ops: {list(ops_map.keys())}")

    try:
        return functools.reduce(ops_map[operation], spells)
    except TypeError as e:
        raise TypeError(f"All elements in spells must be compatible"
                        f" with '{operation}': {e}")


def partial_enchanter(
        base_enchantment: Callable[[int, str, str], str]
) -> dict[str, Callable[[str], str]]:

    if not callable(base_enchantment):
        raise TypeError("base_enchantment must be a callable function.")

    return {
        "fire_50": functools.partial(base_enchantment, 50, "Fire"),
        "ice_50": functools.partial(base_enchantment, 50, "Ice"),
        "lightning_50": functools.partial(base_enchantment, 50, "Lightning")
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:

    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers.")
    if n > 500:
        raise ValueError("n is too large for recursive Fibonacci "
                         "due to stack limits.")

    if n in (0, 1):
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:

    @functools.singledispatch
    def process_spell(_spell: Any) -> str:
        return "Unknown spell type"

    @process_spell.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @process_spell.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @process_spell.register(list)
    def _(spell: list[Any]) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return process_spell


if __name__ == "__main__":

    print("Testing spell reducer...")
    spells_list = [10, 20, 30, 40]
    try:
        print(f"Sum: {spell_reducer(spells_list, 'add')}")
        print(f"Product: {spell_reducer(spells_list, 'multiply')}")
        print(f"Max: {spell_reducer(spells_list, 'max')}")
    except Exception as e:
        print(f"Reducer Error: {e}")

    print("\nTesting memoized fibonacci...")
    try:
        print(f"Fib(0): {memoized_fibonacci(0)}")
        print(f"Fib(1): {memoized_fibonacci(1)}")
        print(f"Fib(10): {memoized_fibonacci(10)}")
        print(f"Fib(15): {memoized_fibonacci(15)}")
        print(f"Cache Info: {memoized_fibonacci.cache_info()}")
    except Exception as e:
        print(f"Fibonacci Error: {e}")

    print("\nTesting spell dispatcher...")
    cast_spell = spell_dispatcher()
    try:
        print(cast_spell(42))
        print(cast_spell("fireball"))
        print(cast_spell([1, 2, 3]))
        print(cast_spell({"type": "shadow"}))
    except Exception as e:
        print(f"Dispatcher Error: {e}")
