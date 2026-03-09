from functools import reduce, partial, lru_cache, singledispatch
from typing import Callable
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    if spells:
        if operation == "add":
            return reduce(lambda a, b: operator.add(a, b), spells)

        elif operation == "multiply":
            return reduce(lambda a, b: operator.mul(a, b), spells)

        elif operation == "max":
            return reduce(lambda a, b: max(a, b), spells)

        elif operation == "min":
            return reduce(lambda a, b: min(a, b), spells)

        else:
            raise ValueError(
                'you can only use "add", "multiply", "max", "min" as operation'
                )
    else:
        raise ValueError('list is empty')


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        'fire_enchant': partial(base_enchantment, power=50,
                                element='fire'),

        'ice_enchant': partial(base_enchantment, power=50,
                               element='ice'),

        'lightning_enchant': partial(base_enchantment, power=50,
                                     element='lightning')
    }


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Fibonacci is only positive")
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable:
    @singledispatch
    def spell(value):
        print("value:", value)

    @spell.register
    def _(value: int):
        print("This is an int:", value)

    @spell.register
    def _(value: str):
        print("This is a str:", value)

    @spell.register
    def _(value: list):
        print("This is a list:", value)

    return spell


spell_powers: list[int] = [40, 30, 20, 10]
operations: list[str] = ['add', 'multiply', 'max']
op_name: list[str] = ['Sum', 'Product', 'Max']
fibonacci_tests: list[int] = [10, 9, 13]

print("\nTesting spell reducer...")
try:
    for op, name in zip(operations, op_name):
        print(f"{name}: {spell_reducer(spell_powers, op)}")
except ValueError as e:
    print(e)

print("\nTesting memorized fibonacci...")
print("Fib(10):", memoized_fibonacci(10))
print("Fib(15):", memoized_fibonacci(15))

print("\nTesting partial enchanter...")
enchanters_dict: dict[str, Callable] = partial_enchanter(
    lambda power, element: f"power: {power}\nelement: {element}\n"
)

fire: Callable = enchanters_dict['fire_enchant']
ice: Callable = enchanters_dict['ice_enchant']
lightning: Callable = enchanters_dict['lightning_enchant']

print(fire())
print(ice())
print(lightning())

print("Testing spell dispatcher...")
dispatcher: Callable = spell_dispatcher()
dispatcher(10)
dispatcher("omg it's magical")
dispatcher([10, 20])
