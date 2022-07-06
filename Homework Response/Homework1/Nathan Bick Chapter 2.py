# Configure plotting in Jupyter
from matplotlib import pyplot as plt
%matplotlib inline
plt.rcParams.update({
    'figure.figsize': (7.5, 7.5),
    'axes.spines.right': False,
    'axes.spines.left': False,
    'axes.spines.top': False,
    'axes.spines.bottom': False})
# Seed random number generator
import random
from numpy import random as nprand
seed = hash("Network Science in Python") % 2**32
nprand.seed(seed)
random.seed(seed)

# Import networkx
import networkx as nx

# The Graph Class: Working with undirected networks
G = nx.karate_club_graph()
karate_pos = nx.spring_layout(G, k=0.3)
nx.draw_networkx(G, karate_pos)
plt.show()

list(G.nodes)

# Checking for nodes
mr_hi = 0
mr_hi in G

G.has_node(mr_hi)

wild_goose = 1337
wild_goose in G

G.has_node(wild_goose)

# Finding node neighbors
list(G.neighbors(mr_hi))

member_id = 1
(mr_hi, member_id) in G.edges

G.has_edge(mr_hi, member_id)

john_a = 33
(mr_hi, john_a) in G.edges

G.has_edge(mr_hi, john_a)

# Adding attributes to nodes and edges

member_club = [
    0, 0, 0, 0, 0, 0, 0, 0, 1, 1,
    0, 0, 0, 0, 1, 1, 0, 0, 1, 0,
    1, 0, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1]

for node_id in G.nodes:
G.nodes[node_id]["club"] = member_club[node_id]

G.add_node(11, club=0)

G.nodes[mr_hi]

G.nodes[john_a]

node_color = [
    '#1f78b4' if G.nodes[v]["club"] == 0
    else '#33a02c' for v in G]

 nx.draw_networkx(G, karate_pos, label=True, node_color=node_color)
 plt.show()

 # Iterate through all edges
for v, w in G.edges:
    # Compare `club` property of edge endpoints
    # Set edge `internal` property to True if they match
    if G.nodes[v]["club"] == G.nodes[w]["club"]:
        G.edges[v, w]["internal"] = True
    else:
        G.edges[v, w]["internal"] = False

internal = [e for e in G.edges if G.edges[e]["internal"]]
external = [e for e in G.edges if not G.edges[e]["internal"]]

# Draw nodes and node labels
nx.draw_networkx_nodes(G, karate_pos, node_color=node_color)
nx.draw_networkx_labels(G, karate_pos)
# Draw internal edges as solid lines
nx.draw_networkx_edges(G, karate_pos, edgelist=internal)
# Draw external edges as dashed lines
nx.draw_networkx_edges(G, karate_pos, edgelist=external, style="dashed")
plt.show()

# Adding Edge Weights

def tie_strength(G, v, w):
    # Get neighbors of nodes v and w in G
    v_neighbors = set(G.neighbors(v))
    w_neighbors = set(G.neighbors(w))
    # Return size of the set intersection
    return 1 + len(v_neighbors & w_neighbors)

# Calculate weight for each edge
for v, w in G.edges: 
    G.edges[v, w]["weight"] = tie_strength(G, v, w)
# Store weights in a list
edge_weights = [G.edges[v, w]["weight"] for v, w in G.edges] 

weighted_pos = nx.spring_layout(G, pos=karate_pos, k=0.3, weight="weight")

# Draw network with edge color determined by weight
nx.draw_networkx(
    G, weighted_pos, width=8, node_color=node_color,
    edge_color=edge_weights, edge_vmin=0, edge_vmax=6, edge_cmap=plt.cm.Blues)
# Draw solid/dashed lines on top of internal/external edges
nx.draw_networkx_edges(G, weighted_pos, edgelist=internal, edge_color="gray")
nx.draw_networkx_edges(G, weighted_pos, edgelist=external, edge_color="gray", style="dashed")
plt.show()

# The DiGraph Class: When direction matters
# modified the path such that the code will run
G = nx.read_gexf("/Users/NathanBick/Documents/Graduate School/MATH517 - Social Network Analysis/Network-Science-with-Python-and-NetworkX-Quick-Start-Guide-master/data/knecht2008/klas12b-net-1.gexf", node_type=int)
student_pos = nx.spring_layout(G, k=1.5)
nx.draw_networkx(G, student_pos, arrowsize=20)
plt.show()

list(G.neighbors(0))

list(G.successors(0))

list(G.predecessors(0))

# Create undirected copies of G
G_either = G.to_undirected()
G_both = G.to_undirected(reciprocal=True)
# Set up a figure
plt.figure(figsize=(10,5))
# Draw G_either on left
plt.subplot(1, 2, 1)
nx.draw_networkx(G_either, student_pos)
# Draw G_both on right
plt.subplot(1, 2, 2)
nx.draw_networkx(G_both, student_pos)

plt.show()

# MultiGraph and MultiDiGraph: Parallel edges
# The seven bridges of Königsberg
G = nx.MultiGraph()
G.add_edges_from([
    ("North Bank", "Kneiphof", {"bridge": "Krämerbrücke"}),
    ("North Bank", "Kneiphof", {"bridge": "Schmiedebrücke"}),
    ("North Bank", "Lomse",    {"bridge": "Holzbrücke"}),
    ("Lomse",      "Kneiphof", {"bridge": "Dombrücke"}),
    ("South Bank", "Kneiphof", {"bridge": "Grüne Brücke"}),
    ("South Bank", "Kneiphof", {"bridge": "Köttelbrücke"}),
    ("South Bank", "Lomse",    {"bridge": "Hohe Brücke"})
])

list(G.edges)[0]
G.edges['North Bank', 'Kneiphof', 0]

# add the following
print(G.edges['North Bank', 'Kneiphof',0])
print(G.edges['North Bank', 'Kneiphof',1])

nx.draw_networkx(G, with_labels=True, connectionstyle='arc3, rad = 0.1')
plt.show()
