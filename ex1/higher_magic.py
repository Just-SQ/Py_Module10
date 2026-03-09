from typing import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combine(*args, **kwargs):
        return (
            spell1(*args, **kwargs),
            spell2(*args, **kwargs)
        )
    return combine


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def multiplication(*args, **kwargs):
        return base_spell(*args, **kwargs) * multiplier
    return multiplication


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def cast(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        else:
            return "Spell fizzled"
    return cast


def spell_sequence(spells: list[Callable]) -> Callable:
    def spell_result(*args, **kwargs):
        return [
            spell(*args, **kwargs)
            for spell in spells
        ]
    return spell_result


print("\nTesting spell combiner...")
arg1: str = "Dragon"
spell_combine: Callable = spell_combiner(
    lambda arg1: f"Fireball hits {arg1}",
    lambda arg1: f"Heals {arg1}"
)
print(f"Combined spell result: {', '.join(spell_combine(arg1))}")

print("\nTesting power amplifier...")
base_arg: int = 10
multiplicater: Callable = power_amplifier(
    lambda base_arg: base_arg,
    3
)
print(f"Original: {base_arg}, Amplified: {multiplicater(base_arg)}")

print("\nTesting conditional caster...")
cast: Callable = conditional_caster(
    lambda *args: False, lambda *args: "real spell"
)
print(cast())

print("\nTesting spell sequence...")
spells: Callable = spell_sequence(
    [lambda *args: 'this is result of the first function',
     lambda *args: 'this is result of the second function',
     lambda *args: 'this is result of the third function']
)
spell: list[str] = spells()
for sp in spell:
    print(sp)
