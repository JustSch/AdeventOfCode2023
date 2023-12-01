from pathlib import Path

#puzzle_input_file_path = Path(__file__).with_name('example.txt')
puzzle_input_file_path = Path(__file__).with_name('input.txt')
puzzle_input_file = open(puzzle_input_file_path,'r')
puzzle_input = puzzle_input_file.read().splitlines()
puzzle_input_file.close()

sum = 0
for pInput in puzzle_input:
  print('line: '+pInput)
  for i in range(0,len(pInput)):
    if pInput[i].isdigit():
      print('first number: {}'.format(int(pInput[i]) * 10))
      sum += (int(pInput[i]) * 10)
      break
    
  for i in range(len(pInput)-1,0,-1):
    if pInput[i].isdigit():
      print('second number: {}'.format(int(pInput[i])))
      sum += int(pInput[i])
      break
      
 

print(sum) 
