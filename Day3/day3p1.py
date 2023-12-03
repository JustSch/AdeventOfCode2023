# -when reading file make sure is list of lists rather than list of strings
# -find number on line
#   -keep track of intervals of number
# Use Len to get right side

# -build box around the word that is one unit larger.
#   —check if box contains symbols (not a dot or a digit)
#   -box need to keep track of boundary limits

# -if box contains symbol add digit to sum and break through loop if needed


from pathlib import Path

#puzzle_input_file_path = Path(__file__).with_name('example.txt')
puzzle_input_file_path = Path(__file__).with_name('input.txt')
puzzle_input_file = open(puzzle_input_file_path,'r')
puzzle_input = puzzle_input_file.read().splitlines() #can stay string 
puzzle_input_file.close()

#print(puzzle_input[0][1])

#BEWARE OF NEGATIVE INDEXING!!!!!!



def find_nums(line):
    # find number and interval and return as list of lists
    nums = []
    num = 0
    i = 0
    while i < len(line):
        if line[i].isdigit():
            j = i
            while (j < len(line) and line[j].isdigit()):
                j+=1
            num = int(line[i:j])
            nums.append([num,i,j])
            i = j                  
        else:
            i+=1
    return nums


def create_and_check_box(nums,i,puzzle_input):
    boxes = []
    for j in range(nums[1], nums[2]): #check each part of number
        box= []
        for k in range(-1,2):
            for l in range(-1,2):
                if k == 0 and l == 0:
                    continue
                if ((i + k)  < 0 or (i+k) >=len(puzzle_input))\
                    or( (j + l) >= len(puzzle_input[i]) or 0 > (j + l)):
                    continue
                else:
                    # print('j {} i+k {} j+l {}'.format(j,i+k,j+l))
                    if not puzzle_input[i+k][j + l].isdigit() and puzzle_input[i+k][j + l] !='.':
                        box.append(puzzle_input[i+k][j + l])
        if  len(box) != 0:
            boxes.append(box)
    return len(boxes) != 0 

i = 0
sum = 0
while i < len(puzzle_input):
    line = puzzle_input[i]
    #print(find_nums(line))
    #find nums
    nums = find_nums(line)
    for num in nums:
        #create_box(num,i,puzzle_input)
        if create_and_check_box(num,i,puzzle_input):
            sum += num[0]

    #create box
    
    #look for symbols in box and add to sum if it contains a symbol

    i+=1
print(sum)