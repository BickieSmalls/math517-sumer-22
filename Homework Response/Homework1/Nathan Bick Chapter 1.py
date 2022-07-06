"""
First I include the script as is, and later with modifications.
"""

# Configure plotting in Jupyter
from matplotlib import pyplot as plt
#%matplotlib inline
plt.rcParams.update({
    'figure.figsize': (7.5, 7.5),
    'axes.spines.right': False,
    'axes.spines.left': False,
    'axes.spines.top': False,
    'axes.spines.bottom': False})

import networkx as nx

G = nx.Graph()

G.add_node('A')
G.add_nodes_from(['B', 'C'])

G.add_edge('A', 'B')
G.add_edges_from([('B', 'C'), ('A', 'C')])

plt.figure(figsize=(7.5, 7.5))
nx.draw_networkx(G)

plt.show()

# Seed random number generator
import random
from numpy import random as nprand
seed = hash("Network Science in Python") % 2**32
nprand.seed(seed)
random.seed(seed)


G.add_edges_from([('B', 'D'), ('C', 'E')])
nx.draw_networkx(G)

plt.show()

"""
Below are the examples with modifications
"""


G = nx.Graph()

G.add_node('A')
G.add_nodes_from(['B', 'C'])

G.add_edge('A', 'B')
G.add_edges_from([('B', 'C'), ('A', 'C')])

# Add some nodes here
G.add_nodes_from(['X','Y']) # no edges yet
G.add_edges_from([('X','B'),('Y','A')]) # add some edges to connect graph

plt.figure(figsize=(7.5, 7.5))
nx.draw_networkx (G)

plt.show()

# Add several nodes and edges at the same time
G.add_edges_from([('B', 'D'), ('C', 'E')])

# lets add another example as above
G.add_edges_from([('D', 'F'), ('E', 'G')])

nx.draw_networkx(G)
plt.show()