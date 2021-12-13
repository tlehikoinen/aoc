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

    if d[0].lower() == d[0]:
        smallCaves.add(d[0])
    if d[1].lower() == d[1]:
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

    # Checks if current node is lower case and if it has been visited earlier
    if path[-1].lower() == path[-1] and path.count(path[-1]) > 1 and path[-1] not in ["start"]:
        # Returns if has been visited twice before
        if path.count(path[-1]) > 2:
            return
        # Returns if any other (lower case) item has been visited twice before
        for item in smallCaves:
            if item not in ["start", "end", path[-1]]:
                if path.count(item) >= 2:
                    return

    newnodes = [node for node in nodes[path[-1]]]
    for node in newnodes:
        if node in ["start", path[-1]]:
            continue
        visitCaves(path+[node])
    
# Part2
visitCaves()
print(caveVisits)
