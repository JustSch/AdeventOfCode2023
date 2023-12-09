from pathlib import Path

#puzzle_input_file_path = Path(__file__).with_name('example.txt')
puzzle_input_file_path = Path(__file__).with_name('input.txt')
puzzle_input_file = open(puzzle_input_file_path,'r')
puzzle_input = puzzle_input_file.read().splitlines() #can stay string 
puzzle_input_file.close()

extrapolated = 0
for line in puzzle_input:
    line = list(map(int, line.split(' ')))
    curr = [line]

    while set(curr[-1]) != set([0]):
        temp = []
        for i in range(0,len(curr[-1])-1):
            temp.append(curr[-1][i+1] - curr[-1][i])
        curr.append(temp)
    #print(curr)

    #find extrapolated

    for i in range(len(curr)-1,0,-1):
        curr[i-1].append(curr[i][-1] + curr[i-1][-1])
    extrapolated+=curr[0][-1]

print(extrapolated)



