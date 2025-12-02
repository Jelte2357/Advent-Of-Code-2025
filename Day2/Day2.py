with open("input.txt", "r") as f:
    data = f.read().rstrip("\n").split(",")

# PART 1
id_sum = 0

for i in data:
    lower_bound, upper_bound = i.split("-")
    lower_bound, upper_bound = int(lower_bound), int(upper_bound) + 1
    for number in range(lower_bound, upper_bound):
        numstr = str(number)
        len_numstr = len(numstr)
        if len_numstr % 2 == 0:
            lower_numstr = numstr[:len_numstr//2]
            upper_numstr = numstr[len_numstr//2:]
            if lower_numstr == upper_numstr:
                id_sum += number

print(id_sum)
      
# PART 2  
id_sum = 0

for i in data:
    lower_bound, upper_bound = i.split("-")
    lower_bound, upper_bound = int(lower_bound), int(upper_bound) + 1
    for number in range(lower_bound, upper_bound):
        numstr = str(number)
        len_numstr = len(numstr)
        for possible_div in range(1, len_numstr//2+1):
            if len_numstr % possible_div == 0:
                all_parts = []
                for part in range(len_numstr//possible_div):
                    all_parts.append(numstr[part*possible_div:(1+part)*(possible_div)])
                if len(set(all_parts)) == 1:
                    id_sum += number
                    break # If number is already added (2222) via [2,2,2,2], dont add it again via [22,22]

print(id_sum)

    
    