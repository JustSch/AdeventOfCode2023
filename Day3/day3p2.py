from pathlib import Path

puzzle_input_file_path = Path(__file__).with_name('example.txt')
#puzzle_input_file_path = Path(__file__).with_name('input.txt')
puzzle_input_file = open(puzzle_input_file_path,'r')
puzzle_input = puzzle_input_file.read().splitlines() #can stay string 
puzzle_input_file.close()



def find_adjacent_nums(i,j,puzzle_input):
    
    nums= []
    for k in range(-1,2):
        for l in range(-1,2):
            if k == 0 and l == 0:
                continue
            if ((i + k)  < 0 or (i+k) >=len(puzzle_input))\
                or( j >= len(puzzle_input[i]) or 0 >  j):
                continue
            else:
                if  puzzle_input[i+k][j + l].isdigit():
                    #find the rest of the number 
                    #nums.append(find_all_ of digit)
                    nums.append(puzzle_input[i+k][j+l])
    
    print(nums)



i = 0
while i < len(puzzle_input):
    if '*' in puzzle_input[i]:
        find_adjacent_nums(i,puzzle_input[i].find('*'),puzzle_input)
    i+=1
        
    

#find stars (use .find to get interavl)
#find if adjacent to two groups of numbers
  # find entire range of number that includes index of adjacent number

#cases after finding star
# no adjacent
# left and top left and bottom left: keep going left to find beginning interval
# right and top right and bottom right: keep going right find ending interval
# top center and bottom center: look left and right for beginning and ending interval


