with open("input.txt", "r") as f:
    data = f.read().rstrip("\n").split("\n")

# PART 1
ranges = data[:data.index("")]
numbers = map(int, data[data.index("")+1:]) # convert to ints

valid_ranges = [] # Tried with set first to minimize doubles.
# Use list with range because this uses pythons optimalizations and doesn't precompute the range for all.
for valid_range in ranges:
    lower, upper = valid_range.split("-")
    valid_ranges.append(range(int(lower), int(upper)+1)) # python does not precompute ranges

fresh_counter = 0

for number in numbers:
    for valid_range in valid_ranges:
        if number in valid_range:
            fresh_counter += 1
            break
        
print(fresh_counter)

# PART 2
ranges = data[:data.index("")]
valid_ranges = []
for valid_range in ranges:
    lower, upper = valid_range.split("-")
    l_bound = int(lower)
    u_bound = int(upper)
    valid_ranges.append((l_bound, u_bound))


prev_valid = set(valid_ranges) # Remove duplicates

while True:
    new_valid = []
    
    for valid_range_1 in prev_valid:
        for valid_range_2 in prev_valid:
            if valid_range_1 != valid_range_2:
                if valid_range_2[0] <= valid_range_1[1] <= valid_range_2[1]:
                    new_range = (min(valid_range_1[0], valid_range_2[0]), valid_range_2[1])
                    # if the upper bound of one fits into another range, combine them, keeping the upper of the one it fits into and the lowest of the 2.
                    if new_range not in new_valid:
                        new_valid.append(new_range)
                    break
        else:
            new_valid.append((valid_range_1)) # If it is not in any bound at all, still keep it.
            
    if prev_valid == set(new_valid): #Check if the sets are the same
        break
    
    prev_valid = set(new_valid) # Once again, remove duplicates.

valid_id_ranges = 0
for valid_range in new_valid:
    valid_id_ranges += valid_range[1] - valid_range[0] + 1

print(valid_id_ranges)