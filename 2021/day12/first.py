with open('input.txt','r') as f:
    data = [item.split('-') for item in f.read().strip().split('\n')]

nodes = {}
smallCaves = set()
for d in data:
    if d[0] in nodes:
        nodes[d[0]].append(d[1])
    else:
        nodes[d[0]] = [d[1]]
    if d[1] in nodes:
        nodes[d[1]].append(d[0])
    else:
        nodes[d[1]] = [d[0]]

    if d[0].lower():
        smallCaves.add(d[0])
    if d[1].lower():
        smallCaves.add(d[1])

caveVisits = 0
visitedCaves = {} 
for key in nodes.keys():
    visitedCaves[key] = 0

def printGraph(graph):
    for key, values in graph.items():
        print("\n"+key)
        print(values)

def visitCaves(path=["start"]):
    global caveVisits
    if path[-1] == "end": 
        caveVisits+=1
        return

    # returns if the current node is lower case and has been visited earlier
    if path[-1].lower() == path[-1] and path[-1] in path[:-1]:
        return 

    newnodes = [node for node in nodes[path[-1]]]
    for node in newnodes:
        if node in ["start", path[-1]]:
            continue
        visitCaves(path+[node])
    





# Part1
visitCaves()
print(caveVisits)
