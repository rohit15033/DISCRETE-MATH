import networkx as nx
import matplotlib.pyplot as plt

def duplicatedInsideInput(n):
	# CHECK THE OCCURANCE EVERY CHARACTER
	for i in n:
		if n.count(i) > 1: return True
	return False

G = nx.Graph()

edges = []
edgesInput = int(input("How many edges do you want? >>> "))

# GET INPUT FROM USER
while len(edges) < edgesInput:
    print ("\nFor edge ", len(edges) + 1)
    n = input("Enter 1st Vertex and 2nd Vertex (Ex. 'a,b') >>> ").split(",")
    
    duplicated = False
    if duplicatedInsideInput(n):
        # CHECK IF THE INPUTTED ARRAY (n) HAS SAME ELEMENT, EX. (a,a), (b,b)
        duplicated = True
    else:
        d = 0
        for e in edges:
            for i in n:
                if i in e:
                    d += 1
            if d >= len(n):
                duplicated = True
                break
            d = 0
    
    if duplicated:
        print("\nInput Duplicated! Please Try Again")
    else:
        edges.append(n)

    """
    RULES:

    CANNOT
    1. (a,b), (b,a)
    2. (a,b), (a,b)

    CAN
    1. (a,b), (b,c)
    2. (a, b), (c,d)

    """

# DEFINE DEGREES IN EACH VERTICES
degrees = {}
for edge in edges: # iterates for every edge in the list
    for v in edge: # iterates for every vertice in the list edge
        if v in degrees.keys(): # makes a list containing the keys of vertice v P.S Key means the objects inside the list
            degrees[v] = degrees[v] + 1;
        else:
            degrees[v] = 1;

highestDegrees = 0
highestVertex = 0

for key in degrees:
    print (key, "has", degrees[key], "vertices")
    if degrees[key] > highestDegrees:
        highestDegrees = degrees[key]
        highestVertex = [key]
    elif highestDegrees == degrees[key]:
        highestVertex.append(key)
print("The Vertices {} has the highest degrees of {}".format(highestVertex, highestDegrees))

# ADDING THE EDGE TO GRAPH AND PLOTTING GRAPH
G.add_edges_from(edges)
nx.draw_circular(G, with_labels=True)
plt.savefig("graph.png")