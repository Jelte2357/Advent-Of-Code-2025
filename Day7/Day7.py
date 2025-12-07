import numpy as np

with open("input.txt") as f:
    data = f.read().rstrip("\n").split("\n")
    
# PART 1
data_array = np.array([list(line) for line in data])

start = np.array(np.where(data_array == "S")).T.tolist()
splitters = np.array(np.where(data_array == "^")).T.tolist()

beam_positions = start
total_splits = 0

while beam_positions:
    beam_pos = beam_positions.pop(0)
    new_beam = [beam_pos[0] + 1, beam_pos[1]]
    if new_beam[0] == data_array.shape[0] or new_beam[0] == data_array.shape[1]:
        continue
    if new_beam in splitters:
        new_beam_1 = [beam_pos[0] + 1, beam_pos[1] - 1]
        new_beam_2 = [beam_pos[0] + 1, beam_pos[1] + 1]
        if new_beam_1[0] != data_array.shape[0] and new_beam_1[1] != -1:
            if new_beam_1 not in beam_positions:
                beam_positions.append(new_beam_1)
                # data_array[new_beam_1[0], new_beam_1[1]] = "|"
        if new_beam_2[0] != data_array.shape[0] and new_beam_1[1] != data_array.shape[1]:
            if new_beam_2 not in beam_positions:
                beam_positions.append(new_beam_2)
                # data_array[new_beam_2[0], new_beam_2[1]] = "|"
        total_splits += 1
        # print("\n".join(["".join(line) for line in data_array]))
        # print(total_splits)
    else:
        # data_array[new_beam[0], new_beam[1]] = "|"
        if new_beam not in beam_positions:
            beam_positions.append(new_beam)

# print(data_array)
print(total_splits)

# PART 2

# Uses basically the same concept but adds in multipliers that are added, basically, how often a line ends up at that place
# If we keep track of this, we only need to calculate the movement of a line once, instead of doing it a lot of times.
# If you comment the dataframe operations out, you will get a view of how the numbers go down the tree.
data_array = np.array([list(line) for line in data])

start = np.array(np.where(data_array == "S")).T.tolist()
splitters = np.array(np.where(data_array == "^")).T.tolist()

beam_positions = start
beam_positions_mult = [1]
total_splits = 0

while beam_positions:
    beam_pos = beam_positions.pop(0)
    
    new_beam = [beam_pos[0] + 1, beam_pos[1]]
    if new_beam[0] == data_array.shape[0]-1 or new_beam[1] == data_array.shape[1]:
        break
    
    beam_pos_mult = beam_positions_mult.pop(0)
    
    if new_beam in splitters:
        new_beam_1 = [beam_pos[0] + 1, beam_pos[1] - 1]
        new_beam_2 = [beam_pos[0] + 1, beam_pos[1] + 1]
        if new_beam_1[0] != data_array.shape[0] and new_beam_1[1] != -1:
            if new_beam_1 not in beam_positions:
                beam_positions.append(new_beam_1)
                beam_positions_mult.append(beam_pos_mult)
                
                # data_array[new_beam_1[0], new_beam_1[1]] = str(beam_pos_mult) #XXX
            else:
                beam_positions_mult[beam_positions.index(new_beam_1)] += beam_pos_mult
                # data_array[new_beam_1[0], new_beam_1[1]] = str(beam_positions_mult[beam_positions.index(new_beam_1)]) # XXX
        if new_beam_2[0] != data_array.shape[0] and new_beam_2[1] != data_array.shape[1]:
            if new_beam_2 not in beam_positions:
                beam_positions.append(new_beam_2)
                beam_positions_mult.append(beam_pos_mult)
                
                # data_array[new_beam_2[0], new_beam_2[1]] = str(beam_pos_mult) # XXX
            else:
                beam_positions_mult[beam_positions.index(new_beam_2)] += beam_pos_mult
                # data_array[new_beam_2[0], new_beam_2[1]] = str(beam_positions_mult[beam_positions.index(new_beam_2)]) # XXX
        total_splits += beam_pos_mult
        # print("\n".join(["".join(line) for line in data_array])) # XXX
        # print(total_splits) # XXX
    else:
        if new_beam not in beam_positions:
            beam_positions.append(new_beam)
            beam_positions_mult.append(beam_pos_mult)
            # data_array[new_beam[0], new_beam[1]] = str(beam_pos_mult) # XXX
        else:
            beam_positions_mult[beam_positions.index(new_beam)] += beam_pos_mult
            # data_array[new_beam[0], new_beam[1]] = str(beam_positions_mult[beam_positions.index(new_beam)]) # XXX
    #     print("\n".join(["".join(line) for line in data_array])) # XXX
    #     print(total_splits) # XXX
    # print(beam_positions_mult)
            
print(np.sum(beam_positions_mult))