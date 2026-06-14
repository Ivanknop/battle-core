
from abc import ABC, abstractmethod


class Entity(ABC):
    def __init__(self, name, vitality, characteristics):
        self._validate_inputs(name,vitality,characteristics)

        self.name = name
        self.vitality = vitality
        self.initial_vitality = vitality
        self.characteristics = characteristics

    def _validate_inputs(self,name,vitality,characteristics):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("name should be a not empty string")
        if not isinstance(vitality, (int, float)):
            raise TypeError("vitality should be a number")
        if not isinstance(characteristics, dict):
            raise TypeError("characteristics should be a dict")
        
    def get_name(self):
        return self.name

    def get_characteristics(self):
        return  self.characteristics

    def get_vitality(self):
        return self.vitality
    
    def get_initial_vitality(self):
        return self.initial_vitality

    def take_hit(self, damage):
        self.vitality = max(0, self.vitality - float(damage))

    def is_alive(self):
        return self.vitality > 0
    
    def update_vitality(self, energy):
        self.vitality +=  energy
    
    def set_vitality(self, new_vitality):
        self.vitality = max(0, float(new_vitality))

    def __str__(self): 
         return str(f'{self.name}: {self.vitality} vitality. Characteristics: {self.characteristics}')
    
    def to_dict(self):
        return {
        "name": self.get_name(),
        "vitality": self.get_vitality(),
        "initial_vitality": self.get_initial_vitality(),
        "characteristics": self.get_characteristics()
    }
    
    @abstractmethod
    def offensive_power(self):
        pass

    @abstractmethod
    def defensive_power(self):
        pass
    @abstractmethod
    def initiative(self):
        pass

    @classmethod
    @abstractmethod
    def from_dict(cls, data):
        pass