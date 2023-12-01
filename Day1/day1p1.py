from pathlib import Path

#puzzle_input_file_path = Path(__file__).with_name('example.txt')
puzzle_input_file_path = Path(__file__).with_name('input.txt')
puzzle_input_file = open(puzzle_input_file_path,'r')
puzzle_input = puzzle_input_file.read().splitlines()
puzzle_input_file.close()

sum = 0
for line in puzzle_input:
  print('line: '+line)
  for i in range(0,len(line)):
    if line[i].isdigit():
      print('first number: {}'.format(int(line[i]) * 10))
      sum += (int(line[i]) * 10)
      break
    
  for i in range(len(line)-1,-1,-1):
    if line[i].isdigit():
      print('second number: {}'.format(int(line[i])))
      sum += int(line[i])
      break
 

print(sum) 
