from pathlib import Path

#puzzle_input_file_path = Path(__file__).with_name('example.txt')
puzzle_input_file_path = Path(__file__).with_name('input.txt')
puzzle_input_file = open(puzzle_input_file_path,'r')
puzzle_input = puzzle_input_file.read().splitlines()
puzzle_input_file.close()


num_dict = {"one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9}
sum = 0
matchFound = False
for line in puzzle_input:
#for line in ['4stonekdgdhxrtqv9sixonevhhmhqzp']:
  print('line: '+line)
  for i in range(0,len(line)):
    if line[i].isdigit():
      print('first number: {}'.format(int(line[i]) * 10))
      sum += (int(line[i]) * 10)
      break
    #if isalpha here
      #check using while if current letter through 5 letters ahead matches a key (keep in mind len limit)
      #(3 - 5 letters may work for this)
      #make sure to break correctly so it proceeds to looking at right side when match found
    for j in range(3,6):
      if (i + j) < len(line):
        if line[i:i+j] in num_dict:
            num_as_int = num_dict[line[i:i+j]]
            print('first number: {}'.format(num_as_int * 10))
            sum += (int(num_as_int) * 10)
            matchFound = True
            break
    if matchFound:
      matchFound = False
      break
    
    
  for i in range(len(line)-1,-1,-1):
    if line[i].isdigit():
      print('second number: {}'.format(int(line[i])))
      sum += int(line[i])
      break

    for j in range(2,5):
      if (i - j) > -1:
        #print(line[i-j:i+1])
        if line[i-j:i+1] in num_dict:
            num_as_int = num_dict[line[i-j:i+1]]
            print('second number: {}'.format(num_as_int))
            sum += (int(num_as_int))
            matchFound = True
            break
    if matchFound:
      matchFound = False
      break
      

print(sum) 

#check left then check right:
#go through line until letter or number is found
#if is number proceed to add it to sum
#if is letter check if matches first letter of a word in num_dict
#  if match found then match the rest of the letters
#    if all letters match add to sum
#if match not found keep proceeding until match is found