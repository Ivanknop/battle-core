# battle-core

Core package for turn-based battle simulations. Provides abstract base classes for entities, combat rules, and fights. Domain-pure: no web framework dependencies.

## Installation

```bash
pip install git+https://github.com/Ivanknop/battle-core.git
```

## Contents

### `Entity` (abstract)

Base class for any combatant. Requires Python 3.12+.

```python
from battle_core.entity import Entity

class MyEntity(Entity):
    def __init__(self, name, vitality, characteristics):
        super().__init__(name, vitality, characteristics)

    def offensive_power(self):
        return self.characteristics["attack"]

    def defensive_power(self):
        return self.characteristics["defense"]

    def initiative(self):
        return self.characteristics["speed"]

    @classmethod
    def from_dict(cls, data):
        entity = cls(data["name"], data["vitality"], data["characteristics"])
        entity.set_vitality(data["vitality"])
        return entity
```

**Concrete methods provided:**

| Method | Description |
|---|---|
| `take_hit(damage)` | Reduces vitality by damage (floor: 0) |
| `is_alive()` | Returns `True` if vitality > 0 |
| `get_vitality()` | Current vitality |
| `get_initial_vitality()` | Vitality at construction time |
| `set_vitality(value)` | Sets vitality (floor: 0) |
| `update_vitality(energy)` | Adds energy to current vitality |
| `to_dict()` | Serializes to `{"name", "vitality", "initial_vitality", "characteristics"}` |

**Abstract methods to implement:**

| Method | Description |
|---|---|
| `offensive_power()` | Returns attack value |
| `defensive_power()` | Returns defense value |
| `initiative()` | Returns speed/priority value |
| `from_dict(cls, data)` | Classmethod — reconstructs entity from dict |

**Constructor validation** — raises `ValueError` if `name` is empty, `TypeError` if `vitality` is not numeric or `characteristics` is not a dict.

---

### `CombatRules`

Concrete class. Can be used directly or subclassed for domain-specific rules (e.g. type multipliers).

```python
from battle_core.combat_rules import CombatRules

rules = CombatRules()
```

**Methods:**

| Method | Description |
|---|---|
| `calculate_base_damage(attacker, defender)` | `max(1, attacker.offensive_power() - defender.defensive_power())` |
| `calculate_turn_damage(attacker, defender, attacker_luck, defender_luck)` | Applies block and critical modifiers |
| `is_blocked(attacker, defender, attacker_luck, defender_luck)` | True if defender speed ≥ attacker speed × 2 |
| `is_critical_hit(attacker, defender, attacker_luck, defender_luck)` | True if attacker speed ≥ defender speed × 2 |
| `critical_multiplier(...)` | Returns 3 on automatic success, 2 on critical, 1 otherwise |
| `roll_luck_pair(rng)` | Returns `{"attacker_luck": int, "defender_luck": int}` (1–100) |
| `initiative_score(entity, luck)` | `entity.initiative() + luck` |
| `modified_speed(entity, luck)` | `entity.initiative() + luck` |

Luck values of `1` = automatic failure, `100` = automatic success.

---

### `Fight` (abstract)

Manages turn execution between two `Entity` instances.

```python
from battle_core.fight import Fight

class MyFight(Fight):
    def __init__(self, fighter_one, fighter_two, rng=None):
        super().__init__(fighter_one, fighter_two, CombatRules(), rng)

    def turn_text(self, attacker, defender, damage, attacker_luck, defender_luck, defender_initial_vitality):
        return f"{attacker.get_name()} dealt {damage} to {defender.get_name()}"
```

**Concrete methods provided:**

| Method | Description |
|---|---|
| `play_turn(player_luck, opponent_luck)` | Executes one full turn, returns list of event strings |
| `attack_once(attacker, defender, ...)` | Executes one attack |
| `order_to_hit(player_luck, opponent_luck)` | Returns `(first, second)` based on initiative |
| `both_fighters_are_alive()` | True if both entities have vitality > 0 |
| `winner()` | Returns winning entity or `None` if fight ongoing |

**Abstract methods to implement:**

| Method | Description |
|---|---|
| `turn_text(attacker, defender, damage, attacker_luck, defender_luck, defender_initial_vitality)` | Returns a string describing the attack |

The `rng` parameter accepts any object with a `randint(a, b)` method. Defaults to Python's `random` module. Pass a seeded `random.Random` instance for deterministic tests.

---

## Running tests

```bash
pip install pytest
pytest tests/
```

## Used by

- [pokemonBattle-py](https://github.com/Ivanknop/pokemonBattle-py)
- [superHeroBattle](https://github.com/Ivanknop/superHeroBattle)
- [country-battle](https://github.com/Ivanknop/country-battle)