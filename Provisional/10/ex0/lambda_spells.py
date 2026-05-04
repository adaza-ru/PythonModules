def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return (sorted(artifacts, key=lambda x: x['power'], reverse=True))


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return (filter(lambda x: x['power'] > min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return (list(map(lambda s: '* ' + s + ' *', spells)))


def mage_stats(mages: list[dict]) -> dict:
    max_p = max(mages, key=lambda p: p['power'])['power']
    min_p = min(mages, key=lambda p: p['power'])['power']
    avg_p = round(sum(map(lambda p: p['power'], mages))/len(mages), 2)

    return {
        'max_power': max_p,
        'min_power': min_p,
        'avg_power': avg_p
    }


if __name__ == "__main__":

    print("\nTesting artifact sorter...")
    test_sort: list[dict] = [
        {'name': "Crystal Orb", 'power': 85, 'type': "Divination"},
        {'name': "Fire Staff", 'power': 92, 'type': "Evocation"}
    ]
    new_sort: list[dict] = artifact_sorter(test_sort)
    print(f"{new_sort[0]['name']} ({new_sort[0]['power']})"
          " comes before "
          f"{new_sort[1]['name']} ({new_sort[1]['power']})")

    print("\nTesting artifact sorter...")
    test_transform: list[str] = ["fireball", "heal", "shield"]
    new_transform: list[str] = spell_transformer(test_transform)
    for spell in new_transform:
        print(f"{spell}", end=" ")
    print("")

    print("\nTesting power filter ...")
    test_filter: list[dict] = [
        {'name': "Gandalf", 'power': 80, 'element': "Light"},
        {'name': "Rincewind", 'power': 999, 'element': "Survival"},
        {'name': "Alphonse Elric", 'power': 50, 'element': "Alchemy"},
        {'name': "Harry Potter", 'power': 1, 'element': "Plot Armor"},
    ]
    new_filter: list[dict] = power_filter(test_filter, 70)
    for mage in new_filter:
        print(f"{mage['name']}: {mage['power']} {mage['element']} power")

    print("\nTesting mage stats...")
    new_stats: dict = mage_stats(test_filter)
    print(
        f"Max Power: {new_stats['max_power']}\n"
        f"Min Power: {new_stats['min_power']}\n"
        f"Average Power: {new_stats['avg_power']}"
    )
