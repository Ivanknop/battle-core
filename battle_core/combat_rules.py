from abc import ABC, abstractmethod

class CombatRules(ABC):
    
    def initiative_score(self, entity, luck):
        return self.modified_speed(entity, luck)
        
    def is_automatic_failure(self, luck):
        return luck == 1
    
    def is_automatic_success(self, luck):
        return luck == 100
    
    def is_blocked(self, attacker, defender, attacker_luck, defender_luck):
        if self.is_automatic_failure(attacker_luck):
            return False

        if self.is_automatic_success(attacker_luck):
            return False

        attacker_speed = self.modified_speed(attacker, attacker_luck)
        defender_speed = self.modified_speed(defender, defender_luck)

        return defender_speed >= attacker_speed * 2
    
    def is_critical_hit(self, attacker, defender, attacker_luck, defender_luck):
        if self.is_automatic_failure(attacker_luck):
            return False

        if self.is_automatic_success(attacker_luck):
            return True

        attacker_speed = self.modified_speed(attacker, attacker_luck)
        defender_speed = self.modified_speed(defender, defender_luck)

        return attacker_speed >= defender_speed * 2
    
    def critical_multiplier(self, attacker, defender, attacker_luck, defender_luck):
        if self.is_automatic_success(attacker_luck):
            return 3
        if self.is_critical_hit(attacker, defender, attacker_luck, defender_luck):
            return 2
        return 1
    
    def roll_luck_pair(self, rng):
        return {
            "attacker_luck": rng.randint(1, 100),
            "defender_luck": rng.randint(1, 100),
        }

    @abstractmethod
    def calculate_base_damage(self, attacker, defender):
        pass
    
    @abstractmethod
    def calculate_turn_damage(self, attacker, defender, attacker_luck, defender_luck):
        pass
    
    @abstractmethod
    def modified_speed(self, entity, luck):
        pass