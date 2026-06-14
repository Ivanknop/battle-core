from battle_core.entity import Entity
import pytest

class ConcreteEntity(Entity):
    def __init__(self, name, vitality,characteristics):
        super().__init__(name, vitality, characteristics)
    def offensive_power(self):
        return self.characteristics["strength"]
    def defensive_power(self):
        return self.characteristics["defense"]
    def initiative(self):
        return 0
    @classmethod
    def from_dict(cls, data):
        concrete_entity = cls(data["name"], data["characteristics"])
        concrete_entity.set_vitality(data["vitality"])
        return concrete_entity

def test_entity_has_expected_characteristics():
    entity = ConcreteEntity("Test Entity", 100,{"strength": 50, "defense": 30})

    assert entity.name == "Test Entity"
    assert entity.vitality == 100
    assert entity.offensive_power() == 50
    assert entity.defensive_power() == 30

def test_entity_take_hit_reduces_vitality():
    entity = ConcreteEntity("Test Entity", 100,{"strength": 50, "defense": 30})
    entity.take_hit(20)
    assert entity.vitality == 80

def test_entity_is_alive():
    entity = ConcreteEntity("Test Entity", 100,{"strength": 50, "defense": 30})
    assert entity.is_alive()
    entity.take_hit(100)
    assert not entity.is_alive()

def test_entity_update_vitality():
    entity = ConcreteEntity("Test Entity", 100,{"strength": 50, "defense": 30})
    entity.update_vitality(20)
    assert entity.vitality == 120
    entity.update_vitality(-50)
    assert entity.vitality == 70

def test_entity_str_representation():
    entity = ConcreteEntity("Test Entity", 100,{"strength": 50, "defense": 30})
    expected_str = "Test Entity: 100 vitality. Characteristics: {'strength': 50, 'defense': 30}"
    assert str(entity) == expected_str

def test_entity_rejects_non_numeric_vitality():
    with pytest.raises(TypeError):
        ConcreteEntity("Pikachu", "cien", {"strength": 50, "defense": 30})

def test_entity_rejects_empty_name():
    with pytest.raises(ValueError):
        ConcreteEntity("", 100, {"strength": 50, "defense": 30})

def test_entity_rejects_non_dict_characteristics():
    with pytest.raises(TypeError):
        ConcreteEntity("Pikachu", 100, "fuerte")