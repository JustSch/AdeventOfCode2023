from pathlib import Path

#puzzle_input_file_path = Path(__file__).with_name('example.txt')
puzzle_input_file_path = Path(__file__).with_name('input.txt')
puzzle_input_file = open(puzzle_input_file_path,'r')
puzzle_input = puzzle_input_file.read().splitlines() #can stay string 
puzzle_input_file.close()



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

stars = {}
def create_and_check_box(nums,i,puzzle_input,stars):
  
    for j in range(nums[1], nums[2]): #check each part of number
        for k in range(-1,2):
            for l in range(-1,2):
                if k == 0 and l == 0:
                    continue
                if ((i + k)  < 0 or (i+k) >=len(puzzle_input))\
                    or( (j + l) >= len(puzzle_input[i]) or 0 > (j + l)):
                    continue
                else:
                    if puzzle_input[i+k][j + l] =='*':
                        if str([(i+k),(j+l)]) not in stars:
                            stars[str([(i+k),(j+l)])] = []
                        
                        if nums[0] not in stars[str([(i+k),(j+l)])]:
                            stars[str([(i+k),(j+l)])].append(nums[0])
                        
  
   

i = 0
sum = 0
while i < len(puzzle_input):
    line = puzzle_input[i]
    #print(find_nums(line))
    #find nums
    nums = find_nums(line)
    for num in nums:
        #create_box(num,i,puzzle_input)
        create_and_check_box(num,i,puzzle_input,stars)
    i+=1
        
for k,v in stars.items():
    print(v)
    if len(v) == 2:
        sum += (v[0]*v[1])
        

print(sum)

#find numbers with adjacent stars
# if two numbers have same adjacent star multiply and add to sum

