from pathlib import Path

#puzzle_input_file_path = Path(__file__).with_name('example.txt')
puzzle_input_file_path = Path(__file__).with_name('input.txt')
puzzle_input_file = open(puzzle_input_file_path,'r')
puzzle_input = puzzle_input_file.read().splitlines()
puzzle_input_file.close()

sum = 0
for game in puzzle_input:
    game_id = game.split(':')[0]
    print(game_id)
    turns = game.split(':')[1]
    turn_num=0
    color_dict= {
            'red': 0,
            'blue': 0,
            'green': 0
    }

    for turn in turns.split(';'):
        print(' Turn: {}'.format(turn_num))
        
        for colors in turn.split(','):
            print(colors)
            #keep track of largest of all turns
            color_dict[colors.split(' ')[2]] = max(int(colors.split(' ')[1]),color_dict[colors.split(' ')[2]])
        
        turn_num+=1

    product = 1
    print('Fewest cubes needed: red: {}, blue: {}, green: {}'.format(color_dict['red'],color_dict['blue'], color_dict['green']))
    for val in color_dict.values():
        product *= val
    sum+=product

print('sum of powers: {}'.format(sum))


