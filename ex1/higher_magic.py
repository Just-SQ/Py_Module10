def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combine(*args, **kwargs):
        return (
            spell1(*args, **kwargs),
            spell2(*args, **kwargs)
        )
    return combine


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def multiplication(*args, **kwargs):
        return base_spell(*args, **kwargs) * multiplier
    return multiplication


def conditional_caster(condition: callable, spell: callable) -> callable:
    def cast(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        else:
            return "Spell fizzled"
    return cast


def spell_sequence(spells: list[callable]) -> callable:
    def spell_result(*args, **kwargs):
        return [
            spell(*args, **kwargs)
            for spell in spells
        ]
    return spell_result


print("\nTesting spell combiner...")
arg1: str = "Dragon"
spell_combine: callable = spell_combiner(
    lambda arg1: f"Fireball hits {arg1}",
    lambda arg1: f"Heals {arg1}"
)
print(f"Combined spell result: {', '.join(spell_combine(arg1))}")

print("\nTesting power amplifier...")
base_arg: int = 10
multiplicater: callable = power_amplifier(
    lambda base_arg: base_arg,
    3
)
print(f"Original: {base_arg}, Amplified: {multiplicater(base_arg)}")
