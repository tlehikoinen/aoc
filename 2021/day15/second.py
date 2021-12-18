from queue import PriorityQueue
import time

start_time = time.time()

# Task, read input into 2d array
with open('input.txt','r') as f:
    data = [[int(i) for i in item] for item in f.read().strip().split('\n')]

# Tracks vertices currently known short path, infinite at start
costs = [[1e9 for y in range(5*len(data[0]))] for x in range(5*len(data))]
# First element has distance of 0
costs[0][0] = 0

# Non visited vertices, shortest distance pops first
pq_non_visited = PriorityQueue()
pq_non_visited.put((costs[0][0],0,0))

# Visited vertices, tracks vertices with shortest path assigned to them, does not allow duplicates
visited = {}

while not pq_non_visited.empty():
    d,x,y = pq_non_visited.get()

    # If position is in visited the shortest distance is already known
    if (x,y) in visited.keys():
        continue

    # Visit neighbours 
    for i in [[1,0],[0,1],[0,-1],[-1,0]]:
        nx = x+i[0]
        ny = y+i[1]
        # Neighbours (x,y) must be in allowed range 
        if nx not in range(0, 5*len(data)) or ny not in range(0,5*len(data[0])):
            continue

        # Calculate the corrected distance value
        rx = nx // len(data)
        ry = ny // len(data[0])
        distance = data[nx-(rx*len(data))][ny-(ry*len(data[0]))] 
        corrected_distance = distance+rx+ry if distance+rx+ry < 10 else distance -9 + rx + ry

        # Update costs if it is less than currently known 
        if costs[x][y] + corrected_distance < costs[nx][ny]:
            costs[nx][ny] = costs[x][y] + corrected_distance

        # Put the neighbour into non_visited to be visited later
        pq_non_visited.put((rx+ry + costs[x][y],nx,ny))

    # Smallest distance from the neighbours for (x,y) is now known, adding it to visited
    visited[x,y] = costs[x][y]
        

# Part 2 answer
print(f'Part 2 answer = {costs[len(data)*5-1][len(data[0])*5-1]}')
print(f'Time was {time.time()-start_time}')






