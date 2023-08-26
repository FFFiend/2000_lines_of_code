from robot_story.movements import *
from robot_story.classes import Entity


def test_spawn_entity():

   spawn_entity = Entity()

   spawn_entity(spawn_entity,0,0)

   assert spawn_entity.x == 0 and spawn_entity.y == 0

def test_movement_entity():

    movement_entity = Entity()

    spawn_entity(movement_entity, 5, 3)

    move_entity(movement_entity, "W")

    assert movement_entity.x == 4


    
    


