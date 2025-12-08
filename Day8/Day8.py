import pandas as pd
import numpy as np
from scipy.spatial import distance_matrix

data = pd.read_csv("input.txt", header=None).to_numpy()

# PART 1
PAIRS = 1000

# https://stackoverflow.com/a/29482058
distances = distance_matrix(data, data)

square_size = distances.shape[0] # Amount of 0's because no distance.

# https://stackoverflow.com/a/16818143 (Argpart did not work.)
raveled_distance = np.ravel(distances)
min_distances = np.argsort(raveled_distance)[square_size:square_size + PAIRS * 2:2] # Start from the base number of zeroes, in steps of 2 to ignore doubles
positions = np.array([[pos // square_size, pos % square_size] for pos in min_distances])
positions = positions.tolist()

while True:
    pos_combinations = []

    for position in positions:
        for enum, known_combi in enumerate(pos_combinations):
            if any(option in known_combi for option in position):
                pos_combinations[enum].update(set(position))
                break
        else:
            pos_combinations.append(set(position))

    if pos_combinations == positions:
        break
    
    positions = pos_combinations

lengths = sorted(map(lambda x: len(x), pos_combinations), reverse=True)

print(np.prod(lengths[:3]))

# PART 2
len_arr = data.shape[0]
distances = distance_matrix(data, data)
square_size = distances.shape[0] # Amount of 0's because no distance.
raveled_distance = np.ravel(distances)
min_distances = np.argsort(raveled_distance)[square_size::2] # Start from the base number of zeroes, in steps of 2 to ignore doubles
positions = np.array([[pos // square_size, pos % square_size] for pos in min_distances])
positions = positions.tolist()

pos_combinations = set(positions[0])

for enum, position in enumerate(positions[1:]): 
    # Without the for loop, and pos_combinations.update(set(position)) it also gives the same answer, but this is just luck I think.
    # Because possibly the "last" one could be [X, Y] with neither having been seen before, this would not work, however, this was actually not the case here.
    # Still, I used the for loop to show how it SHOULD work (I think at least, I can never be 100% sure, as it could just do the same as the original code.)
    
    # Runs in about 25 seconds on my laptop.
    for position2 in positions[1:enum]: # Also add the ones that were not possible before but are possible now.
        if any(option in pos_combinations for option in position2):
            pos_combinations.update(set(position))
        
    if len(pos_combinations) == len_arr:
        break 

print(data[position[0]][0] * data[position[1]][0])