from enum import Enum

class Difficulty(int, Enum):
    EASY = 5
    MEDIUM = 10
    HARD = 15

class Tileset(str, Enum):
    EMPTY = 'x'
    HERO = 'H'
    
    
# TODO resolve error when going out of bounds
def main():

    hero_position_x = 0
    hero_position_y = 0
    game_map = [[Tileset.EMPTY.value for _ in range(Difficulty.EASY)] for _ in range(Difficulty.EASY)]
    game_map[hero_position_y][hero_position_x] = Tileset.HERO.value
    while True:
        for row in game_map:
            print(row)
        user_input = input('Choose a direction\n')
        hero_last_pos_x = hero_position_x
        hero_last_pos_y = hero_position_y
        match user_input:
            case 'w':
                hero_position_y = hero_position_y - 1
            case 'a':
                hero_position_x = hero_position_x - 1
            case 's':
                hero_position_y = hero_position_y + 1
            case 'd':
                hero_position_x = hero_position_x + 1
            
        game_map[hero_last_pos_y][hero_last_pos_x] = Tileset.EMPTY.value
        game_map[hero_position_y][hero_position_x] = Tileset.HERO.value

    

if __name__ == '__main__':
    main()