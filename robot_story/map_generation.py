from classes import *
import numpy as np

"""Random Map Generation module."""
DEFAULT_STAMINA_VAL = 20
DEFAULT_SHIELD_VAL = 10

def _generate_map(curr_world: list[list[str]], world_dict) -> list[list[Entity, int]]:
    for i in range(len(curr_world)):
        for j in range(len(curr_world[0])):
            rand_num = np.random.randint(1,53)
            if rand_num % 3 == 0:
                curr_world[i][j] = MiniAdversary()

            elif rand_num % 7 == 0:
                curr_world[i][j] = StaminaPotion(DEFAULT_STAMINA_VAL)
            
            elif rand_num % 2 == 0:
                curr_world[i][j] = ShieldPotion(DEFAULT_SHIELD_VAL)
    
            elif rand_num % 11 == 0:
                curr_world[i][j] = Block()

            else:
                curr_world[i][j] = rand_num
            world_dict[(i,j)] = curr_world[i][j]

    return curr_world