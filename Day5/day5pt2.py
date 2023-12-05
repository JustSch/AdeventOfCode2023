from pathlib import Path
import sys

#puzzle_input_file_path = Path(__file__).with_name('example.txt')
puzzle_input_file_path = Path(__file__).with_name('input.txt')
puzzle_input_file = open(puzzle_input_file_path,'r')
puzzle_input = puzzle_input_file.read().splitlines()
puzzle_input_file.close()

#create maps:
# find highest source by summing source and range size
# create list "map" of that size
# initialize to same as i then use source, destination and range to map


def create_map(starting,map_list):
    #find ending aka next empty string after starting
    #find length to initialize map
    #initialize map
    #do mapping
    
    ending = starting +1
 

    while ending < len(puzzle_input) and puzzle_input[ending] != '':
        ending+=1

    for i in range(starting+1,ending):
        current = puzzle_input[i].split()

        range_of = int(current[2])
        destination = int(current[0])
        source = int(current[1])
        

        map_list.append([destination,source,range_of])

    
    return map_list


seeds = puzzle_input[0].split(':')[1].split()

seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temp_to_humidity = []
humidity_to_location = []

create_map(puzzle_input.index('seed-to-soil map:'),seed_to_soil)
create_map(puzzle_input.index('soil-to-fertilizer map:'),soil_to_fertilizer)
create_map(puzzle_input.index('fertilizer-to-water map:'),fertilizer_to_water)
create_map(puzzle_input.index('water-to-light map:'),water_to_light)
create_map(puzzle_input.index('light-to-temperature map:'),light_to_temperature)
create_map(puzzle_input.index('temperature-to-humidity map:'),temp_to_humidity)
create_map(puzzle_input.index('humidity-to-location map:'),humidity_to_location)

def find_mapping(map_list,i):
    for cur in map_list:
        if i >= cur[1] and i < (cur[1] + cur[2]):
            #print(cur[0] + (i - cur[1]))
            return cur[0] + (i - cur[1])   
    #print(i)     
    return i

min_location = sys.maxsize
#print(seeds)
i = 0
while i < len(seeds):
    seeds_start = int(seeds[i])
    seeds_end = int(seeds[i]) + int(seeds[i+1])

    if find_mapping(seed_to_soil,seeds_start) != seeds_start and find_mapping(seed_to_soil,seeds_end) != seeds_end:

        for seed in range(int(seeds[i]),int(seeds[i])+int(seeds[i+1])):    
            #check if mapped first?    
        
            soil = find_mapping(seed_to_soil, seed)
            fertilizer = find_mapping(soil_to_fertilizer, soil)
            water = find_mapping(fertilizer_to_water, fertilizer)
            light = find_mapping(water_to_light, water)
            temp = find_mapping(light_to_temperature, light)
            humidity = find_mapping(temp_to_humidity, temp)
            location = find_mapping(humidity_to_location, humidity)
            min_location = min(min_location,location)
            #print('                  ')
       
    i+=2


print(min_location)