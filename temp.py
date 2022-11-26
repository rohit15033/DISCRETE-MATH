import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

NoOfEdges = int(input("How many edges do you want?: "))
ListOfEdges = []

while len(ListOfEdges) < NoOfEdges:
    n = input("Enter 1st Vertex and 2nd Vertex to form an edge(Input example: a, b): ")
    
    duplicated = 0
    for i in ListOfEdges:
        for k in n:
            if k in i:
                duplicated += 1
    
    if duplicated >= 2 or n in ListOfEdges:
        print ("Duplicated edge input try again")
    else:
        edge = n.split(", ")
        ListOfEdges.append(edge)
    
    # DONE ROHIT :) 
    # I found error :'(
    # wait, i gonna work my self through this code OKE. I cannot focus in anydesk or call
    # if i cannnot, just record the good part. OK NIGGA
    # OK
    # Where this is saved?

#Degree in each Vertice
Degree = {}

for edge in ListOfEdges: #Iterates for every edge in the list
    for v in edge: #iterates for every vertice in the list edge
        if v in Degree.keys(): #Makes a list containing the keys of vertice v P.S Key means the objects inside the list
            Degree[v] = Degree[v] + 1;
        else:
            Degree[v] = 1;

print("\n")

HighestDegree = 0
HighestVertex = 0

for key in Degree:
    print (key, "has", Degree[key], "vertices")
    if Degree[key] > HighestDegree:
        HighestDegree = Degree[key]
        HighestVertex = [key]
    elif HighestDegree == Degree[key]:
        HighestVertex.append(key)


print ("\nThe Vertice", HighestVertex, "has the highest degree of", HighestDegree)

G.add_edges_from(ListOfEdges)
nx.draw_circular(G, with_labels=True)
plt.savefig("Filename.png")