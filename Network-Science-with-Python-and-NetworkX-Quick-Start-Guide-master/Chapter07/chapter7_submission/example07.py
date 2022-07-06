# Configure plotting in Jupyter
from matplotlib import pyplot as plt
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

import networkx as nx

import networkx.algorithms.community as nxcom

from pathlib import Path
data_dir = Path('.') / 'data'

# Generate the network
G_internet = nx.read_graphml(data_dir / 'UAITZ' / 'Geant2012.graphml')
# Find the communities
communities = sorted(nxcom.greedy_modularity_communities(G_internet), key=len, reverse=True)
# Count the communities
len(communities)

def set_node_community(G, communities):
    '''Add community to node attributes'''
    for c, v_c in enumerate(communities):
        for v in v_c:
            # Add 1 to save 0 for external edges
            G.nodes[v]['community'] = c + 1
            
def set_edge_community(G):
    '''Find internal edges and add their community to their attributes'''
    for v, w, in G.edges:
        if G.nodes[v]['community'] == G.nodes[w]['community']:
            # Internal edge, mark with community
            G.edges[v, w]['community'] = G.nodes[v]['community']
        else:
            # External edge, mark as 0
            G.edges[v, w]['community'] = 0

def get_color(i, r_off=1, g_off=1, b_off=1):
    r0, g0, b0 = 0, 0, 0
    n = 16
    low, high = 0.1, 0.9
    span = high - low
    r = low + span * (((i + r_off) * 3) % n) / (n - 1)
    g = low + span * (((i + g_off) * 5) % n) / (n - 1)
    b = low + span * (((i + b_off) * 7) % n) / (n - 1)
    return (r, g, b)


# Set node and edge communities
set_node_community(G_internet, communities)
set_edge_community(G_internet)

# Set community color for nodes
node_color = [get_color(G_internet.nodes[v]['community']) for v in G_internet.nodes]

# Set community color for internal edges
external = [(v, w) for v, w in G_internet.edges if G_internet.edges[v, w]['community'] == 0]
internal = [(v, w) for v, w in G_internet.edges if G_internet.edges[v, w]['community'] > 0]
internal_color = [get_color(G_internet.edges[e]['community']) for e in internal]


karate_pos = nx.spring_layout(G_internet)
# Draw external edges
nx.draw_networkx(
    G_internet,
    pos=karate_pos,
    node_size=0,
    edgelist=internal,
    edge_color="#333333")
plt.show()
"""
# Draw nodes and internal edges
nx.draw_networkx(
    G_internet,
    pos=karate_pos,
    node_color=node_color,
    edgelist=internal,
    edge_color=internal_color)

plt.show()
"""
