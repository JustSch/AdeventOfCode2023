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

seed_pairs = []
for i in range(0,len(seeds),2):
    seed_pairs.append([int(seeds[i]),int(seeds[i+1]) + int(seeds[i])])

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



# figure out overlapping ranges?


#approach based on https://github.com/Tyranties/AOC-2023/blob/main/day_05/day_05_part_2.py


def find_ranges(seed_ranges,list_ranges):
    
    new_ranges = []
    while 0 < len(seed_ranges):
        seeds_start, seeds_end = seed_ranges.pop()
        overlapped = False
        for list_range in list_ranges:
            overlap_start = max(seeds_start,list_range[1])
            overlap_end = min(seeds_end,list_range[1] + list_range[2])

            if overlap_start < overlap_end:
                new_ranges.append([overlap_start - list_range[1] + list_range[0], overlap_end - list_range[1] + list_range[0]])
                if overlap_start > seeds_start:
                  seed_ranges.append([list_range[1], overlap_start])

                if overlap_end < seeds_end:
                    seed_ranges.append([overlap_end,seeds_end])
                overlapped = True
                break

        if not overlapped:
            overlapped = False
            new_ranges.append([seeds_start,seeds_end])
    return new_ranges


# print(seed_pairs)
seed_pairs = find_ranges(seed_pairs,seed_to_soil)
seed_pairs = find_ranges(seed_pairs,soil_to_fertilizer)
seed_pairs = find_ranges(seed_pairs,fertilizer_to_water)
seed_pairs = find_ranges(seed_pairs,water_to_light)
seed_pairs = find_ranges(seed_pairs,light_to_temperature)
seed_pairs = find_ranges(seed_pairs,temp_to_humidity)
seed_pairs = find_ranges(seed_pairs,humidity_to_location)

print(min(seed_pairs)[0])