from time import perf_counter
with open("input.txt") as f:
    lines = f.read().rstrip("\n").split("\n")
    
# PART 1:
data_dict = {line.split(": ")[0]: line.split(": ")[1].split() for line in lines}
found_dict = {}
queue = []

queue.append("you")
out_count = 0

while queue: # I believe this could be optimized due to the fact this runs multiple times, but its quick enough.
    item = queue.pop(0)
    if item == "out":
        out_count+=1
        continue
    found_dict[item] = found_dict.get(item, 0) + 1
    for value in data_dict[item]:
        queue.append(value)

print(out_count)

# PART 2:
data_dict = {line.split(": ")[0]: line.split(": ")[1].split() for line in lines}
# You know there can not be infinite loops
# Thus FFT and DAC must be in a given order
# The order MUST be svr -> fft -> dac -> out (found by trying the reverse (dac -> fft) and getting 0 routes)
order = [("svr", "fft"), ("fft", "dac"), ("dac", "out")]
final = "out"
current_multiplyer = 1

for part in order: # Code shortened from 3 separate for loops which did the same thing.
    queue = [part[0]]
    goto = part[1]
    queue_mult = {part[0]: current_multiplyer}
    current_multiplyer = 0
    while queue:
        item = queue.pop(0)
        item_mult = queue_mult[item]
        queue_mult[item] = 0
        if item == goto:
            current_multiplyer += item_mult
            continue
        
        if item == final:
            continue
        new_items = data_dict[item]
        for new_item in new_items:
            if new_item not in queue:
                queue.append(new_item)
            queue_mult[new_item] = queue_mult.get(new_item, 0) + item_mult

print(current_multiplyer)