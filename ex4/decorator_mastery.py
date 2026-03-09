from functools import wraps
from time import time, sleep
from typing import Callable
from random import choice


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def timer(*args):
        print(f"Casting {func.__name__}...")
        start: float = time()
        res = func(*args)
        end: float = time()
        print(f"Spell completed in {end - start: .3f} seconds")
        return res
    return timer


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable):
        @wraps(func)
        def validator(*args, **kwargs):
            try:
                power: int = kwargs['power']
            except KeyError:
                raise KeyError(
                    "you need to enter power arg in this format power=any_int"
                    )

            if power >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return validator
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func):
        @wraps(func)
        def spell(*args, **kwargs):
            for _ in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print("Spell failed,retrying...")
            return f"Spell casting failed after {max_attempts} attempts"
        return spell
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def fireball() -> str:
    sleep(0.101)
    return "fireball cast!"


print("\nTesting spell timer...")
print("Result:", fireball())

print("\nTesting MageGuild...")
mage = MageGuild()
spell_name: str = "Lightning"
print(mage.validate_mage_name(spell_name))
print(mage.validate_mage_name("*"))
try:
    print(mage.cast_spell(spell_name, power=15))
    print(mage.cast_spell(spell_name, power=9))
except Exception as e:
    print(e)

print("\nTesting power validator...")
min_power: int = 10


@power_validator(min_power)
def spell(power: int) -> int:
    return power


try:
    print("This is what happen if argument (power) is < min_power:",
          spell(power=9))
except ValueError as e:
    print(e)
    exit(1)

print("\nTesting retry spell...")

rand_list: list[None | str] = [None, None, "it work"]
max_attempts: int = 5


@retry_spell(max_attempts)
def spell_tester(random_list):
    var: str | None = choice(random_list)
    if var:
        return var
    else:
        raise ValueError


print(spell_tester(rand_list))
