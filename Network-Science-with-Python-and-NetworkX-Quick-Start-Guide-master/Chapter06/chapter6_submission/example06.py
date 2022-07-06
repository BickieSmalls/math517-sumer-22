# Configure plotting in Jupyter
from matplotlib import pyplot as plt
plt.rcParams.update({
    'figure.figsize': (7.5, 7.5)})
# Seed random number generator
from numpy import random as nprand
seed = hash("Network Science in Python") % 2**32
nprand.seed(seed)

import networkx as nx

from pathlib import Path
data_dir = Path('.') / 'data'

# Load karate club network
G_karate = nx.karate_club_graph()
mr_hi = 0
john_a = 33

# Load internet point of presence network
G_internet = nx.read_graphml(data_dir / 'UAITZ' / 'Geant2012.graphml')

# Load Germany electrical grid
with open(data_dir / 'mureddu2016' / '0.2' / 'branches.csv', 'rb') as f:
    # Skip header
    next(f)
    # Read edgelist format
    G_electric = nx.read_edgelist(
        f,
        delimiter="\t",
        create_using=nx.Graph,
        data=[('X', float), ('Pmax', float)])

plt.figure(figsize=(7.5, 2.75))
plt.subplot(1, 3, 1);
plt.title("Karate")
nx.draw_networkx(G_karate, node_size=0, with_labels=True)
plt.show()