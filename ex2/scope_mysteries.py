from typing import Callable


def mage_counter() -> Callable:
    x: int = 0

    def count():
        nonlocal x
        x += 1
        return x
    return count


def spell_accumulator(initial_power: int) -> Callable:
    total: int = initial_power

    def accumulator(power_amount):
        nonlocal total
        total += power_amount
        return total
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    return lambda item_name: f"{enchantment_type} {item_name}"


def memory_vault() -> dict[str, Callable]:
    result: dict = {}

    def store(key, value):
        result[key] = value

    def recall(key):
        return result.get(key, "Memory not found")

    return {
        "store": store,
        "recall": recall
    }


print("\nTesting mage counter...")
counter: Callable = mage_counter()
for i in range(1, 4):
    print(f"Call {i}: {counter()}")

print("\nTesting enchantment factory...")
echant: Callable = enchantment_factory("Flaming")
print(echant("Sword"))

echant = enchantment_factory("Frozen")
print(echant("Shield"))

print("\nTesting spell accumulator...")
initial_power: int = 10
sp_acc: Callable = spell_accumulator(initial_power)
print(f"This the initial power: {initial_power}\n"
      f"Power after accumulating 5: {sp_acc(5)}")

print("\nTesting memory vault...")
call_or_store: dict[str, Callable] = memory_vault()
store: Callable = call_or_store["store"]
call: Callable = call_or_store["recall"]
print("storing age in memory vault")
store('age', 23)
print("getting age:", call('age'))
