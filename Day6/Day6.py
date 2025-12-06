import numpy as np
import pandas as pd

# PART 1
table = pd.read_csv("input.txt", header=None, sep='\\s+')
array = table.to_numpy().T
num_array = array[:,:-1].astype(int)
operations_array = array[:,-1]

total_sum = 0

for operation, numbers in zip(operations_array.T, num_array):
    if operation == "*":
        total_sum += np.prod(numbers)
    elif operation == "+":
        total_sum += np.sum(numbers)

print(total_sum)

# PART 2:
with open("input.txt", "r") as f:
    data = f.read().rstrip("\n").split("\n")
    
array = np.array([list(l) for l in data])
empty_columns = [-1] + [enum for enum, column in enumerate(array.T) if "".join(column).isspace()] + [array.shape[1]] # Finds all empty colums, and adds the option to account for a first and last array too.
subarrays = [array[:,column+1:empty_columns[enum+1]].T for enum, column in enumerate(empty_columns[:-1])] # Makes a list of all separate arrays of the sub-arrays by empty columns, and then transposes them to be in order from "top to bottom" going to left to right.

total_sum = 0

for subarray in subarrays:
    numbers = [int("".join(line)) for line in subarray[:,:-1]] # transforms the array of strings into a list of numbers
    operation = subarray[0,-1]
    if operation == "*":
        total_sum += np.prod(numbers)
    elif operation == "+":
        total_sum += np.sum(numbers)
        
print(total_sum)
