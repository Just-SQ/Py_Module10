def mage_counter() -> callable:
    x: int = 0

    def count():
        nonlocal x
        x += 1
        return x
    return count


def spell_accumulator(initial_power: int) -> callable:
    total: int = initial_power

    def accumulator(power_amount):
        nonlocal total
        total += power_amount
        return total
    return accumulator


def enchantment_factory(enchantment_type: str) -> callable:
    return lambda item_name: f"{enchantment_type} {item_name}"


def memory_vault() -> dict[str, callable]:
    result: dict = {}

    def store(key, value):
        nonlocal result
        result[key] = value

    def recall(key):
        return result.get(key, "Memory not found")

    return {
        "store": store,
        "recall": recall
    }


print("\nTesting mage counter...")
counter: callable = mage_counter()
for i in range(1, 4):
    print(f"Call {i}: {counter()}")

print("\nTesting enchantment factory...")
echant: callable = enchantment_factory("Flaming")
print(echant("Sword"))

echant: callable = enchantment_factory("Frozen")
print(echant("Shield"))
