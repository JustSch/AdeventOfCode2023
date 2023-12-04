from pathlib import Path

#puzzle_input_file_path = Path(__file__).with_name('example.txt')
puzzle_input_file_path = Path(__file__).with_name('input.txt')
puzzle_input_file = open(puzzle_input_file_path,'r')
puzzle_input = puzzle_input_file.read().splitlines() #can stay string 
puzzle_input_file.close()

card_num = 0

card_copies = []

for line in puzzle_input:
    card_copies.append(1)

for line in puzzle_input:
    
    card_content = line.split(':')[1]
    card_winners = card_content.split('|')[0].split()
    card_numbers = card_content.split('|')[1].split()
    winning_card_numbers = set(card_winners) & set(card_numbers)
    winners = len(winning_card_numbers)

    for j in range(card_copies[card_num]):
        for i in range(1, winners +1):
            card_copies[card_num + i]+=1

    card_num +=1


    #need to keep track of which cards have copies in order to duplicate winners

    #if there is enough cards left split number of copies between next cards in card_copies list
print(card_copies)
print(sum(card_copies))
