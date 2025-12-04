with open("input.txt", "r") as f:
    data = f.read().rstrip("\n").split("\n")

# PART 1
SizeX = len(data[0])
SizeY = len(data)

rolls = 0

for pos_x in range(SizeX):
    for pos_y in range(SizeY):
        if data[pos_y][pos_x] == "@":
            surrounding = -1 # Ignore itself
            for dif_x in range(-1, 2): # Check the surrounding 8
                for dif_y in range(-1, 2):
                    dif_pos_x = pos_x + dif_x
                    dif_pos_y = pos_y + dif_y
                    if 0 <= dif_pos_x < SizeX and 0<= dif_pos_y < SizeY: # If legal position
                        if data[dif_pos_y][dif_pos_x] == "@":
                            surrounding += 1
            if surrounding < 4:
                rolls += 1 

print(rolls)

# PART 2
data = [list(line) for line in data] # Make lines lists because strings are immutable
SizeX = len(data[0])
SizeY = len(data)

total_rolls = 0

rolls = -1
while rolls != 0:
    rolls = 0
    removable_positions = []

    for pos_x in range(SizeX):
        for pos_y in range(SizeY):
            if data[pos_y][pos_x] == "@":
                surrounding = -1 # Ignore itself
                for dif_x in range(-1, 2): # Check the surrounding 8
                    for dif_y in range(-1, 2):
                        dif_pos_x = pos_x + dif_x
                        dif_pos_y = pos_y + dif_y
                        if 0 <= dif_pos_x < SizeX and 0<= dif_pos_y < SizeY: # If legal position
                            if data[dif_pos_y][dif_pos_x] == "@":
                                surrounding += 1
                if surrounding < 4:
                    rolls += 1 
                    removable_positions.append((pos_x, pos_y))

    for pos_x, pos_y in removable_positions: # Edit the data
        data[pos_y][pos_x] = "."

    total_rolls += rolls

print(total_rolls)
