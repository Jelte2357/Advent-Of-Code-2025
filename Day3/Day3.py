with open("input.txt", "r") as f:
    data = f.read().rstrip("\n").split("\n")

# PART 1
joltage = 0

for line in data:
    splitline = list(line)
    f_num = max(splitline[:-1])
    f_num_index = splitline.index(f_num)
    s_num = max(splitline[f_num_index+1:])
    # print(f_num+s_num)
    joltage += int(f_num+s_num)

print(joltage)

# PART 2

joltage = 0

for line in data:
    splitline = list(line)

    num_1 = max(splitline[:-11])
    num_1_i = splitline[:-11].index(num_1)
    
    previndexes = num_1_i
    for i in range(2,13):
        if i != 12:
            selectable = splitline[previndexes + i - 1 : -12+i]
        else:
            selectable = splitline[previndexes + i - 1 :      ] # indexing to :0 wont return anything so edge case.

        num_i = max(selectable)
        previndexes += selectable.index(num_i)
        num_1 += num_i
    
    joltage += int(num_1)

print(joltage)