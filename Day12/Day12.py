import numpy as np
import itertools
import pulp

with open("input.txt", "r") as f:
    data = f.read().rstrip("\n").split("\n\n")
    
# PART 1
original_shapes = []
shapes = []
for shape in data[:-1]:
    shape = np.array([list(l) for l in shape.split("\n")[1:]]) == "#"
    original_shapes.append(shape)
    rot_flip_shape = [shape, np.rot90(shape), np.rot90(np.rot90(shape)), np.rot90(np.rot90(np.rot90(shape))),
                      np.flip(shape), np.rot90(np.flip(shape)), np.rot90(np.rot90(np.flip(shape))), np.rot90(np.rot90(np.rot90(np.flip(shape))))
                     ]
    for edited_shape in rot_flip_shape:
        shape_list = []
        for enum, sub_shape in enumerate(edited_shape.ravel()):
            if sub_shape == True:
                shape_list.append((enum // shape.shape[0], enum % shape.shape[0]))
        shapes.append(shape_list)

problems = []
for problem in data[-1].split("\n"):
    size, presents = problem.split(": ")
    size = tuple(map(int, size.split("x")))
    presents = tuple(map(int, presents.split(" ")))
    problems.append((size, presents))

total_possible = 0
problems_solved = []
for enum, problem in enumerate(problems):
    rows_allow = problem[0][1]
    columns_allow = problem[0][0]
    total_allowed = rows_allow * columns_allow
    if sum(problem[1]) <= total_allowed // 9: # Definitely Solvable
        total_possible += 1
        problems_solved.append(enum)
        continue
    
    if sum([np.sum(rot_flip_shape[enum])*i for enum, i in enumerate(problem[1])]) > total_allowed: # Definitly Unsolvable
        problems_solved.append(enum)
    
for enum in sorted(problems_solved, reverse=True): # Pop from high to low to not disturb ranges
    problems.pop(enum)


# AINT NO WAY I MADE THIS ENTIRE FUNCTION JUST TO NOT USE IT D:
# https://stackoverflow.com/a/47929350
def covered(tile, base):
    return {(base[0] + t[0], base[1] + t[1]): True for t in tile}

amount_problems = len(problems)
for enum, problem in enumerate(problems):
    print(f"{enum} / {amount_problems}", end="\r")
    rows = problem[0][1]
    cols = problem[0][0]

    squares = {x: True for x in itertools.product(range(rows), range(cols))}
    vars = list(itertools.product(range(rows), range(cols), range(len(shapes))))
    vars = [x for x in vars if all([y in squares for y in covered(shapes[x[2]], (x[0], x[1])).keys()])]

    x = pulp.LpVariable.dicts('shapes', vars, lowBound=0, upBound=1, cat=pulp.LpInteger)
    # print(vars)
    mod = pulp.LpProblem('polyominoes', pulp.LpMaximize)
    # Objective value is number of squares in tile
    mod += sum([len(shapes[p[2]]) * x[p] for p in vars])
    for s in squares:
        mod += sum([x[p] for p in vars if s in covered(shapes[p[2]], (p[0], p[1]))]) <= 1
    
    for tnum in range(0, len(shapes), 8):
        mod += sum([x[p] for p in vars if p[2] // 8 == tnum // 8]) == problem[1][tnum // 8]
    
    # https://stackoverflow.com/a/64216831
    mod.solve(pulp.PULP_CBC_CMD(msg=False))
    
    total_possible += (mod.status+1)//2

print(total_possible)

# PART 2:
# There was no part 2
# I wish anyone reading this a MERRY CHRISTMAS and a HAPPY NEW YEARS!