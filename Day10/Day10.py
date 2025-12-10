import numpy as np
from itertools import combinations
from cvxpy import Variable, Problem, Minimize
import cvxpy as cp

with open("input.txt", "r") as f:
    data = f.read().rstrip("\n").split("\n")

# PART 1
lines = [line.split(" ") for line in data]
indicators = [line[0] for line in lines]
switches = [line[1:-1] for line in lines]

indicator_sets = []
for indicator in indicators:
    indicator = indicator[1:-1]
    indicator_set = set()
    for enum, char in enumerate(indicator):
        if char == "#":
            indicator_set.add(enum)
    indicator_sets.append(indicator_set)

switch_sets = []
for switch_list in switches:
    switch_subset = []
    for switch in switch_list:
        switch = set([int(i) for i in switch[1:-1].split(",")])
        switch_subset.append(switch)
    switch_sets.append(switch_subset)

total_switches = 0

for enum, indicator in enumerate(indicator_sets):
    switches = switch_sets[enum]
    if indicator == set():
        continue
    found = False
    # https://docs.python.org/3/library/itertools.html#itertools.combinations
    for len_combi in range(1, len(switches) + 1):
        combis = combinations(switches, len_combi)
        for combi in combis:
            outcome = set()
            for switch in combi: # Find the symmetric difference of the whole combination
                outcome ^= switch 
            if outcome == indicator:
                total_switches += len_combi
                found = True
                break
        if found:
            break
        
print(total_switches)
        
# PART 2
lines = [line.split(" ") for line in data]
switches = [line[1:-1] for line in lines]
joltages = [line[-1] for line in lines]

switch_sets = []
for switch_list in switches:
    switch_subset = []
    for switch in switch_list:
        switch = set([int(i) for i in switch[1:-1].split(",")])
        switch_subset.append(switch)
    switch_sets.append(switch_subset)

joltages_lists = []
for joltage_list in joltages:
    joltages_lists.append(np.array([int(i) for i in joltage_list[1:-1].split(",")]))

button_presses = 0

for enum, joltage_list in enumerate(joltages_lists):
    switches = switch_sets[enum]
    
    x_size = len(switches)
    y_size = max([max(a) for a in switches]) + 1
    f_matrix = np.full((y_size, x_size), 0)
    for x in range(x_size):
        for y in switches[x]:
            f_matrix[y, x] = 1
    
    # https://stackoverflow.com/a/43166112   
    # https://stackoverflow.com/questions/43194615/force-a-variable-to-be-an-integer-cvxpy
    # https://stackoverflow.com/questions/43194615/force-a-variable-to-be-an-integer-cvxpy#comment97040340_45196153

    sol = Variable(f_matrix.shape[1], integer=True)
    constr = [f_matrix @ sol == joltage_list, sol >= 0]
    obj = Minimize(sum(sol))
    prob = Problem(obj, constr)
    prob.solve()
    
    button_presses += round(obj.value) # Remove possible slight deviations in floating point math

print(button_presses)