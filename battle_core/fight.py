from abc import ABC, abstractmethod

import random

class Fight(ABC):
    def __init__(self, fighter_one, fighter_two, combat_rules=None, rng=None):
        self.__fighter_one = fighter_one
        self.__fighter_two = fighter_two
        self.__rng = rng or random
        self.__combat_rules = combat_rules 

    def get_fighter_one(self):
        return self.__fighter_one

    def get_fighter_two(self):
        return self.__fighter_two

    def get_combat_rules(self):
        return self.__combat_rules

    def order_to_hit(self, player_luck=0, opponent_luck=0):
        fighter_one_initiative = self.__combat_rules.initiative_score(
            self.get_fighter_one(),
            player_luck,
        )
        fighter_two_initiative = self.__combat_rules.initiative_score(
            self.get_fighter_two(),
            opponent_luck,
        )
        if fighter_one_initiative >= fighter_two_initiative:
            return self.get_fighter_one(), self.get_fighter_two()
        return self.get_fighter_two(), self.get_fighter_one()

    def play_turn(self, player_luck=0, opponent_luck=0):
        player_luck = int(player_luck)
        opponent_luck = int(opponent_luck)

        if not self.both_fighters_are_alive():
            winner = self.winner()
            if winner is None:
                return ["La batalla terminó sin vencedor."]
            return ["La batalla ya terminó. Vencedor " + winner.get_name()]

        first_attacker, second_attacker = self.order_to_hit(
            player_luck,
            opponent_luck,
        )
        events = []
        events.append(
            self.attack_once(
                first_attacker,
                second_attacker,
                player_luck,
                opponent_luck,
            )
        )
        if second_attacker.is_alive():
            events.append(
                self.attack_once(
                    second_attacker,
                    first_attacker,
                    player_luck,
                    opponent_luck,
                )
            )

        return events
    
    def both_fighters_are_alive(self):
        return self.get_fighter_two().is_alive() and self.get_fighter_one().is_alive()

    def winner(self):
        if self.get_fighter_one().is_alive() and not self.get_fighter_two().is_alive():
            return self.get_fighter_one()
        if self.get_fighter_two().is_alive() and not self.get_fighter_one().is_alive():
            return self.get_fighter_two()
        return None
    
    def attack_once(self, attacker, defender, player_luck, opponent_luck):
        attacker_luck, defender_luck = self.luck_for(
            attacker,
            player_luck,
            opponent_luck,
        )
        defender_initial_vitality = defender.get_vitality()
        damage = self.get_combat_rules().calculate_turn_damage(
            attacker,
            defender,
            attacker_luck,
            defender_luck,
        )
        if damage > 0:
            defender.take_hit(damage)
        return self.turn_text(
            attacker,
            defender,
            damage,
            attacker_luck,
            defender_luck,
            defender_initial_vitality,
        )
    
    def luck_for(self, attacker,  player_luck, opponent_luck):
        if attacker == self.get_fighter_one():
            return player_luck, opponent_luck
        return opponent_luck, player_luck
    
    @abstractmethod
    def turn_text(self, attacker, defender, damage, attacker_luck, defender_luck, defender_initial_vitality):
        pass