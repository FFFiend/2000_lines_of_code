from classes import Entity, Item, ShieldPotion, StaminaPotion

KEY_TO_DIRECTION_MAP = {"W": (-1, 0), "A": (0, -1), "S": (1, 0), "D": (0, 1)}


def move_entity(entity: Entity, direction: str):
    """
    want one key press to correspond to one co-ordinate movement
    """
    assert (
        direction in KEY_TO_DIRECTION_MAP
    ), "Please enter one of W, A, S or D to move the entity in the world."

    assert (
        entity.x is not None and entity.y is not None
    ), "The entity does not exist on the board."

    entity.x += KEY_TO_DIRECTION_MAP[direction][0]
    entity.y += KEY_TO_DIRECTION_MAP[direction][1]


def spawn_entity(entity: Entity, spawn_x, spawn_y):
    assert (
        spawn_x is None and spawn_y is None
    ), "You can't spawn an entity that alreaady exists on the board."

    entity.x, entity.y = spawn_x, spawn_y


def deal_damage(entity: Entity, damage_dealer: Entity, damage_amount: int):
    assert damage_amount >= 0, "Damage can only be non-negative values."
    assert (
        damage_dealer.damage >= damage_amount
    ), "Entity cannot deal more damage than its base damage."

    if entity.health - damage_amount <= 0:
        # entity is dead. Game over.
        # Kill game instance.
        # TODO
        pass

    else:
        entity.health -= damage_amount

def stamina_boost(entity: Entity, stam_potion = StaminaPotion):
    """ Initiated after an object has picked up a stamina boosting consumable. """
    assert stam_potion.stamina_grant > 0, "You cannot slow the entity down with a boost."

    entity.stamina = entity.stamina + (0.43 * stam_potion.stamina_grant * entity.stamina)

    stam_potion.status = "Inactive"

    # TODO: ERASE THE CONSUMABLE ENTITY FROM THE WORLD WHEN THIS HAPPENS.

def shield(entity: Entity, shield_potion: ShieldPotion):
    assert shield_potion.shield_val >= 0, "Shield value must be non-negative."

    entity.health += shield_potion.shield_val

    shield_potion.status = "Inactive"

def pick_up_item(entity: Entity, item: Item):
    """ Entity picks the item up. """
    if item in entity.inventory:
        entity.inventory[item] += 1
    else:
        entity.inventory[item] = 1



