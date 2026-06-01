from core.entity import Entity

class ConcreteEntity(Entity):
    def __init__(self, name, vitality):
        characteristics = {"strength": 50, "defense": 30}
        super().__init__(name, vitality, characteristics)
    def offensive_power(self):
        return self.characteristics["strength"]
    def defensive_power(self):
        return self.characteristics["defense"]

def test_entity_has_expected_characteristics():
    entity = ConcreteEntity("Test Entity", 100)

    assert entity.name == "Test Entity"
    assert entity.vitality == 100
    assert entity.offensive_power() == 50
    assert entity.defensive_power() == 30

def test_entity_take_hit_reduces_vitality():
    entity = ConcreteEntity("Test Entity", 100)
    entity.take_hit(20)
    assert entity.vitality == 80

def test_entity_is_alive():
    entity = ConcreteEntity("Test Entity", 100)
    assert entity.is_alive()
    entity.take_hit(100)
    assert not entity.is_alive()

def test_entity_update_vitality():
    entity = ConcreteEntity("Test Entity", 100)
    entity.update_vitality(20)
    assert entity.vitality == 120
    entity.update_vitality(-50)
    assert entity.vitality == 70

def test_entity_str_representation():
    entity = ConcreteEntity("Test Entity", 100)
    expected_str = "Test Entity: 100 vitality. Characteristics: {'strength': 50, 'defense': 30}"
    assert str(entity) == expected_str