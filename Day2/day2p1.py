from pathlib import Path

#puzzle_input_file_path = Path(__file__).with_name('example.txt')
puzzle_input_file_path = Path(__file__).with_name('input.txt')
puzzle_input_file = open(puzzle_input_file_path,'r')
puzzle_input = puzzle_input_file.read().splitlines()
puzzle_input_file.close()

cube_dict = {
            'red':  12,
            'green': 13,
            'blue': 14,
}
#parsing each line/game:
#  find the the right of colon
#     then split further with semicolon to get turns

i = 0
sum=0
game_failed = False
for game in puzzle_input:
    game_id = game.split(':')[0]
    print(game_id)
    turns = game.split(':')[1]
    turn_num=0
    for turn in turns.split(';'):
        print(' Turn: {}'.format(turn_num))
        for colors in turn.split(','): 
            print(colors) ##there is space in front use [1] and [2] after split
            #if impossible aka greater then limit in dict: break (both turn and game)
            # else: add id to sum

            if int(colors.split(' ')[1]) > cube_dict[colors.split(' ')[2]]:
                game_failed = True
                break        
        turn_num+=1
        if game_failed:
            break
    if game_failed:
        game_failed = False
        continue
    print('Game {} is possible'.format(game_id.split(' ')[1]))
    sum+=int(game_id.split(' ')[1])

print('game id sum: {}'.format(sum))

        
#amounts are in format number: (space) color
  #use split with space or regex?

