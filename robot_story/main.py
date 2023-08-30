from classes import *
from movements import *
import numpy as np
from map_generation import _generate_map

COORD_PREV_VAL_MAP = {}


def main():
    # Need to maintain state of the world,
    # as well as keep updating it.
    threshold = 0

    # we will share the same Game class instance across handler functions.

    game_instance = Game()

    print("Type the coordinates (separated by a space) where you would like to spawn")

    coords = input().split(" ")
    actual_coords = (int(coords[0]), int(coords[1]))

    _init_world(game_instance, actual_coords, game_instance.player)
    # game tolerates up to 20 wrong key presses in a row
    while threshold < 20:
        print("Make your next move!")

        user_input = input()

        curr_output = _game_state_manager(game_instance, user_input)

        if curr_output == 0:
            threshold += 1

    print(
        "Game has finished. Thank you for playing! This is your score: {}".format(
            game_instance.player_score
        )
    )


def _init_world(game_instance: Game, spawn_point: tuple[int], player: Robot):
    # set the world up

    game_instance.world = _generate_map(game_instance.world, COORD_PREV_VAL_MAP)

    game_instance.world[spawn_point[0]][spawn_point[1]] = player
    spawn_entity(player, spawn_point[0], spawn_point[1])
    display_world(game_instance)


def _game_state_manager(game_instance: Game, curr_action: str):
    if curr_action in {"W", "A", "S", "D"}:

        if isinstance(COORD_PREV_VAL_MAP[(game_instance.player.x,game_instance.player.y)],StaminaPotion):
            game_instance.world[game_instance.player.x][game_instance.player.y] = 0

        else:
            game_instance.world[game_instance.player.x][
            game_instance.player.y
            ] = COORD_PREV_VAL_MAP[(game_instance.player.x,game_instance.player.y)]


        move_entity(game_instance.player, curr_action)
        # post update stamina boost
        if isinstance(game_instance.world[game_instance.player.x][game_instance.player.y], StaminaPotion):
            curr_potion = game_instance.world[game_instance.player.x][game_instance.player.y]
            game_instance.player.stamina += curr_potion.stamina_grant
        
        else:
            game_instance.player.stamina -= 2

        game_instance.world[game_instance.player.x][
            game_instance.player.y
        ] = game_instance.player

        display_world(game_instance)
        return 1

    else:
        print("Please enter a valid action.")
        return 0


def display_world(game_instance: Game):
    for i in range(len(game_instance.world)):
        print(game_instance.world[i])


if __name__ == "__main__":
    main()
