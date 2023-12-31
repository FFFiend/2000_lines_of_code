from collections import deque
import numpy as np


class Entity:
    """ Entity class for the world. """
    def __init__(self):
        # add more attributes?
        self.x, self.y = None, None
        self.health = 100
        self.stamina = 250
        self.damage = 0
        self.inventory = {}

        self.repr = None

    def __repr__(self):
        return self.repr

class Robot(Entity):
    """Class for the robot entity. """
    def __init__(self):
        super().__init__()
        self.damage = 20
        self.repr = ".||."
    

class Block(Entity):
    """Blocker class"""
    def __init__(self):
        super().__init__()
        self.repr = "[]"

class MiniAdversary(Entity):
    """Class for obstacles in the world."""
    def __init__(self):
        super().__init__()
        self.damage = 5
        self.health = 3
        self.repr = "*"

class Item:
    """Item class."""

class Consumable(Item):
    """Consumable class."""
    def __init__(self):
        self.status = "Active"
        self.repr = None
    
    def __repr__(self):
        return self.repr

class TimedConsumable(Consumable):
    """ TimedConsumable class. """
    def __init__(self):
        self.duration = 30

class StaminaPotion(TimedConsumable):
    def __init__(self, boost_val: int):
        super().__init__()
        self.stamina_grant = boost_val
        self.repr = "SP"


class ShieldPotion(TimedConsumable):
    def __init__(self, shield_val: int):
        super().__init__()
        self.shield_val = shield_val
        self.repr = "<>"


class Game:
    def __init__(self):
        self.world = [["."] * 25 for i in range(25)]
        self.player_score = 0
        self.player = Robot()
        self._action_sequence = deque
        
    def _update(self):
        raise NotImplementedError