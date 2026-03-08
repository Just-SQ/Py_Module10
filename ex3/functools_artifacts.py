from functools import reduce, partial, lru_cache, singledispatch
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


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {
        'fire_enchant': partial(base_enchantment, power=50,
                                element='fire'),
        'ice_enchant': partial(base_enchantment, power=50, element='ice'),
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


def spell_dispatcher() -> callable:
    @singledispatch
    def spell(value):
        print("value:", value)

    @spell.register
    def _(value: int):
        print("damage spell:", value)

    @spell.register
    def _(value: str):
        print("enchantment:", value)

    @spell.register
    def _(value: list):
        for i, v in enumerate(value, start=1):
            print(f"cast {i}: {v}")

    return spell


spell_powers = [40, 30, 20, 10]
operations = ['add', 'multiply', 'max']
op_name = ['Sum', 'Product', 'Max']
fibonacci_tests = [10, 9, 13]

print("\nTesting spell reducer...")
try:
    for op, name in zip(operations, op_name):
        print(f"{name}: {spell_reducer(spell_powers, op)}")
except ValueError as e:
    print(e)

print("\nTesting memorized fibonacci...")
print("Fib(10):", memoized_fibonacci(10))
print("Fib(15):", memoized_fibonacci(15))
