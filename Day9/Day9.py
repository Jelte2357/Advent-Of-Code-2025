import pandas as pd
import numpy as np
from shapely.geometry import Polygon

# A HUGE SHOUTOUT TO: 
# (I wrote the area calculation as abs((x1-x2+1)*(y1-y2+1)) )
# https://www.reddit.com/r/adventofcode/comments/1piebzl/2025_day_9_part_2_your_code_may_be_wrong_where/

data = pd.read_csv("input.txt", header=None).to_numpy()

# PART 1
highest_found = 0

for point1 in data:
    for point2 in data:
        x1, y1 = point1
        x2, y2 = point2
        size = (abs((x1-x2))+1)*(abs((y1-y2))+1)
        # +1 is to account for inclusive indexes
        
        if size > highest_found:
            highest_found = size
            
print(highest_found)

# PART 2

highest_found = 0
# https://stackoverflow.com/questions/52149075/how-can-i-check-if-a-polygon-contains-a-point?rq=3
poly = Polygon(data)

for point1 in data:
    for point2 in data:
        x1, y1 = point1
        x2, y2 = point2
        
        min_x, max_x = min(x1, x2), max(x1, x2)
        min_y, max_y = min(y1, y2), max(y1, y2)
        p1, p2, p3, p4 = (min_x, min_y), (min_x, max_y), (max_x, max_y), (max_x, min_y)
        
        poly2 = Polygon([p1, p2, p3, p4])
        
        if poly.covers(poly2):
            size = (abs((x1-x2))+1)*(abs((y1-y2))+1)
        # +1 is to account for inclusive indexes
        
            if size > highest_found:
                highest_found = size
                
print(highest_found)