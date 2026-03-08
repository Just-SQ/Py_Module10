def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    result: list[dict] = sorted(
        artifacts,
        key=lambda artifact: artifact.get('power', 0),
        reverse=True
        )

    return result


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    result: list[dict] = list(filter(
        lambda mage: mage.get('power', 0) >= min_power,
        mages
    ))

    return result


def spell_transformer(spells: list[str]) -> list[str]:
    result: list[str] = list(map(
        lambda spell: "* " + spell + " *",
        spells
    ))

    return result


def mage_stats(mages: list[dict]) -> dict:
    max_power: int = max(
        map(lambda mage: mage.get('power', 0), mages)
    )
    min_power: int = min(
        map(lambda mage: mage.get('power', 0), mages)
    )
    avg_power: float = sum(
        map(lambda mage: mage.get('power', 0), mages)
    )
    return {
        'max_power': max_power,
        'min_power': min_power,
        'avg_power': avg_power / len(mages)
    }


artifacts: list[dict] = [
    {'name': 'Crystal Orb', 'power': 85, 'type': 'weapon'},
    {'name': 'Fire Staff', 'power': 92, 'type': 'focus'}
]
spells: list[str] = ['fireball', 'heal', 'shield']

artifacts = artifact_sorter(artifacts)
print("\nTesting artifact sorter...")
print(f"{artifacts[0]['name']} ({artifacts[0]['power']} power) comes "
      f"before {artifacts[1]['name']} ({artifacts[1]['power']} power)")

spells = spell_transformer(spells)
print("\nTesting spell transformer...")
print(*spells)
