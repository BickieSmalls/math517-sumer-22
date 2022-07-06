# Configure plotting in Jupyter
from matplotlib import pyplot as plt
#%matplotlib inline
plt.rcParams.update({
    'figure.figsize': (7.5, 7.5),
    'axes.spines.right': False,
    'axes.spines.left': False,
    'axes.spines.top': False,
    'axes.spines.bottom': False})
# Seed random number generator
from numpy import random as nprand
import random
seed = hash("Network Science in Python") % 2**32
nprand.seed(seed)
random.seed(seed)

import networkx as nx

# Create data directory path
from pathlib import Path
#data_dir = Path('.') / 'data'
data_dir=Path("/Users/NathanBick/Documents/Graduate School/MATH517 - Social Network Analysis/example")
# Read edge list
G = nx.read_edgelist(str(data_dir / 'example.edgelist'))
# Draw network
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos)
plt.gca().margins(0.15, 0.15)
plt.show()