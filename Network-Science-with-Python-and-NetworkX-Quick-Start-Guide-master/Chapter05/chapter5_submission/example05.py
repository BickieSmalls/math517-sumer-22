# Configure plotting in Jupyter
from matplotlib import pyplot as plt
plt.rcParams.update({
    'figure.figsize': (7.5, 7.5),
    'axes.spines.right': False,
    'axes.spines.left': False,
    'axes.spines.top': False,
    'axes.spines.bottom': False})
# Seed random number generator
from numpy import random as nprand
seed = hash("Network Science in Python") % 2**32
nprand.seed(seed)

import networkx as nx

# Create empty affiliation network and list of people
B = nx.Graph()
people = set()
# Load data file into network
from pathlib import Path
data_dir = Path('.') / 'data'
with open(data_dir / 'crossley2012' / '50_ALL_2M.csv') as f:
    # Parse header
    events = next(f).strip().split(",")[1:]
    # Parse rows
    for row in f:
        parts = row.strip().split(",")
        person = parts[0]
        people.add(person)
        for j, value in enumerate(parts[1:]):
            if value != "0":
                B.add_edge(person, events[j], weight=int(value))
# Project into person-person co-affilation network
from networkx import bipartite
G = bipartite.projected_graph(B, people)

pagerank = nx.pagerank(G)
pagerank_sorted = sorted(pagerank.items(), key=lambda x:x[1], reverse=True)[0:10]

print(pagerank)
print(agerank_sorted)