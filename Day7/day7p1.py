from pathlib import Path
from queue import PriorityQueue

puzzle_input_file_path = Path(__file__).with_name('example.txt')
#puzzle_input_file_path = Path(__file__).with_name('input.txt')
puzzle_input_file = open(puzzle_input_file_path,'r')
puzzle_input = puzzle_input_file.read().splitlines() #can stay string 
puzzle_input_file.close()

cards=['2','3','4','5','6','7','8','9','T','J','Q','K','A']  # highest rank at end

#sort cards then check if next is the same card
#keep track of max of the same card (3same + 2same is fullhouse) #can use count function
def check_hand_rank(hand): # opposite 5 is highest here
    if hand[0] == hand[1] == hand[2] == hand[3] == hand[4]:
        return 7
    freq = {}
    for card in hand:
        if card not in freq:
            freq[card] = 1
        else:
            freq[card]+=1
    max_freq = 0

    for card in freq.values():
        if max_freq < card:
            max_freq = card
    if max_freq == 4:
        return 6
       
    if max_freq == 3:
        #sort then check count of first and look at first two or last two cards
        #check for full house
        hand_clone = hand.copy()
        hand_clone.sort()
        if hand_clone[0] == hand_clone[1] or hand_clone[-1] == hand_clone[-2]:
            return 5
        else:
            return 4


    if max_freq == 2:
        #check for two differnet pairs
        #check if two with count two?

        pass
    return  max_freq #keep pairs in mind !!!!!!!!

# print(check_hand_rank(['3','1','A','J','2'])) 

#rank first with pq using hand rank
#pop same rank from pq and rank again with card rank

pq = PriorityQueue()
for line in puzzle_input:
    hand = list(line.split(' ')[0])
    money = int(line.split(' ')[1])
    hand_rank = check_hand_rank(hand)
    pq.put((hand_rank,[hand,money]))

true_rank=0
while not pq.empty():
    ranked_card = []
    first = pq.get()
    ranked_card.append(first[1])
    while not pq.empty():
        cur = pq.get()
        if cur[0] == first[0]:
            ranked_card.append(cur[1])
        else:
            pq.put(cur)
            break
    #sort ranked cards by card ranking
    #brute force with loop?

    print(ranked_card)