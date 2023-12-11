from pathlib import Path

puzzle_input_file_path = Path(__file__).with_name('example.txt')
#puzzle_input_file_path = Path(__file__).with_name('input.txt')
puzzle_input_file = open(puzzle_input_file_path,'r')
puzzle_input = puzzle_input_file.read().splitlines() #can stay string 
puzzle_input_file.close()

lines_to_double_x = []
lines_to_double_y = []
def check_horizontal(puzzle_input):
    i = 0
    while i < len(puzzle_input):
        if set(puzzle_input[i].split()[0]) == set('.'):
            lines_to_double_x.append(i)
        i+=1


#print(puzzle_input)

def check_vertical(puzzle_input):
    i = 0
    while i < len(puzzle_input[0]):
        j = 0
        all_dots = True
        while j < len(puzzle_input):
            if '.' != puzzle_input[j][i]:
                all_dots = False
                break
            j+=1
        if all_dots:
            all_dots = False
            lines_to_double_y.append(i)
            
        i+=1

check_horizontal(puzzle_input)

add_to_line = 0
for x in lines_to_double_x:
    temp = puzzle_input[x+add_to_line]
    puzzle_input.insert(x+add_to_line,temp)
    add_to_line+=1


check_vertical(puzzle_input)
add_to_line = 0
for y in lines_to_double_y:
    i = 0
    while i < len(puzzle_input):
        temp = list(puzzle_input[i].split()[0])
        temp.insert(y+add_to_line,'.')
        temp = ''.join(temp)
        puzzle_input[i] = temp
        
        i+=1
    add_to_line+=1


#now that its expanded find shortest path

#djikstra's but on each vertex?