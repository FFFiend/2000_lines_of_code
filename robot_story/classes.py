class Entity:
    """ Entity class for the world. """
    def __init__(self):
        # add more attributes?
        self.x, self.y = None, None
        self.health = 100
        self.stamina = 250
        self.damage = 0
        self.inventory = {}

class Robot(Entity):
    """Class for the robot entity. """
    def __init__(self):
        super().__init__()
        self.damage = 20

class MiniAdversary(Entity):
    """Class for obstacles in the world."""
    def __init__(self):
        super().__init__()
        self.damage = 5
        self.health = 3

class Item:
    """Item class."""

class Consumable(Item):
    """Consumable class."""
    def __init__(self):
        self.status = "Active"

class TimedConsumable(Consumable):
    """ TimedConsumable class. """
    def __init__(self):
        self.duration = 30

class StaminaPotion(TimedConsumable):
    def __init__(self, boost_val: int):
        super().__init__()
        self.stamina_grant = boost_val

class ShieldPotion(TimedConsumable):
    def __init__(self, shield_val: int):
        super().__init__()
        self.shield_val = shield_val




