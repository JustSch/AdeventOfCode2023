from pathlib import Path

#puzzle_input_file_path = Path(__file__).with_name('example.txt')
puzzle_input_file_path = Path(__file__).with_name('input.txt')
puzzle_input_file = open(puzzle_input_file_path,'r')
puzzle_input = puzzle_input_file.read().splitlines() #can stay string 
puzzle_input_file.close()

sum = 0

for line in puzzle_input:
    card_content = line.split(':')[1]
    card_winners = card_content.split('|')[0].split()
    card_numbers = card_content.split('|')[1].split()
    winning_card_numbers = set(card_winners) & set(card_numbers)
    if (len(winning_card_numbers) > 0):
        sum += (2 ** (len(winning_card_numbers)-1))

print(sum)