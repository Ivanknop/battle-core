
from abc import ABC, abstractmethod


class Entity(ABC):
    def __init__(self, name, vitality, characteristics):
        self.name = name
        self.vitality = vitality
        self.initial_vitality = vitality
        self.characteristics = characteristics

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

    def __str__(self): 
         return str(f'{self.name}: {self.vitality} vitality. Characteristics: {self.characteristics}')
    
    @abstractmethod
    def offensive_power(self):
        pass

    @abstractmethod
    def defensive_power(self):
        pass
    @abstractmethod
    def initiative(self):
        pass