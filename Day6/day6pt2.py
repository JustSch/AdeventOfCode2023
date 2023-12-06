from pathlib import Path
import math

#puzzle_input_file_path = Path(__file__).with_name('example.txt')
puzzle_input_file_path = Path(__file__).with_name('input.txt')
puzzle_input_file = open(puzzle_input_file_path,'r')
puzzle_input = puzzle_input_file.read().splitlines() #can stay string 
puzzle_input_file.close()

times = puzzle_input[0].split(':')[1].split()
times = ''.join(times) 
times = int(times)

distances = puzzle_input[1].split(':')[1].split()
distances = ''.join(distances) 
distances = int(distances)

ways=[0]


#quadratic approach explained in https://topaz.github.io/paste/#XQAAAQDdBQAAAAAAAAARiAaI0h/d+z738iucoYyYKvSve+EpWWLMleDYxMARvyeWX3T70FcYmvQ3GzJ8bciZwAacyARnf//KFHOWnfBaAwtDWnow7DJ/0iJuXmAkYk7/V/IUBwYLgkyR1f3w8+OW8RbP8kI8W93tX1I71x5q2nk3oChPR+5QZLdY0pA2NYWN1VbVlTCMTjM5xvuGFPEGVHH4PAW91vUxkWSuBgEUmg6iXASAJPb9TDalmVBYq7EGCkY2BKx4aK676FLhViyC5v9hOjc+h3zk5XrB7XC4w768l1p2YQEdve4+iVzGHySf/vyTmMwRWKTS1fu/rYPQ+5pQjVjsmPsWzVblJ7DuFyFypoBbCARqRkd9ZuuNFDh0VJozGGv5K7YBPCG1UZxpeDoZOsGIuD85vohnfh35GSqTi24B+AhwExSLu2d/ro0wUyvxjOvDKib9mkc2YoVlCfYM8flJTFCJ5ca9FCiPZMipZZe/1Trbo9WDknumnpiMXq7UDzfOavjJEdFqTuRnwl2z6YdfU5OudM2IaIrEFcwR7bgKVVWjFSeXJ+ad8TpLpsgNv9dXPtdCuOIgBv7fiqy4SVkPj27yULPwcDHWyBA+SDj8Wp0owW1y7JAHzx8dmS4U41suQEktpzXFDHpczOns4tl2UucyGjIe/dbpS73zujAw6NtXjz24c2DMidHZ63FCksDNj8TnXmhgWNAgwpDzxq4LGpB9tzvRGBYvdDikOipjV1Qxo36v3etreKaREONtIYnwr/xuk6axjn0j3Ph6HVr9ISekcXrOEWThLXTjHyiGz4s+GoAi+gUZNGduUykwGRy70YYBDwJ1jdbuGnjso7y+O/F6EdkPJgP2J9TlQbWmp50U9KVv/PtOHQ==
#review of quaratics equations: https://study.com/skill/learn/how-to-write-the-equation-of-a-quadratic-function-given-its-graph-explanation.html

root1 = (-times + math.sqrt(times**2 - 4 * distances)) / -2
root2 = (-times - math.sqrt(times**2 - 4 * distances)) / -2


print(math.floor(root2) - math.ceil(root1) + 1)
