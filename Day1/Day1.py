with open("input.txt", "r") as file:
    data = file.read().rstrip("\n").split("\n")
   
data = [int(d.replace("L", "-").replace("R", "")) for d in data]

# PART 1
pos = 50
counter = 0

for d in data:
    pos += d
    
    while pos < 0:
        pos += 100
    while pos > 99:
        pos -= 100
    
    if pos == 0:
        counter += 1
        
print(counter)

# PART 2
pos = 50
counter = 0

# I am aware this code is HORRIBLY inefficient, but cmon, it ran less than a second, who cares
for d in data:
    for _ in range(abs(d)):
        if d > 0:
            pos += 1
        else:
            pos -= 1
            
        if pos == 100:
            pos = 0
        if pos == -1:
            pos = 99
            
        if pos == 0:
            counter += 1
print(counter)