# %%
import networkx as nx
import numpy as np
import random
from matplotlib import pyplot as plt
random.seed()

# %%
# n = 1000000
# c = 2m/n = 2log2 
# m = nc/2 = nlog2 = 100*log2
G = nx.Graph()

# %% [markdown]
# We want to create a network of n nodes (one million). This is fixed. 
# Given this network, from the constraint on the mean degree produce, we know how many total edges we need. 
# So we just need to randomlt allocate these edges (could do while loop)
# 

# %%
# start with 100 nodes only
n = 100
iter = 0
while iter <= n:
    print(iter)
    name = 'Node_' + str(iter)
    print(name)
    G.add_node(name)
    iter += 1

# %%
# print the graph that has no edges
nx.draw_networkx(G)

# %%
tot_egdes = n * np.log(2)
print(tot_egdes)

# %%
# randomly add 69 edges
iter = 0
while iter < tot_egdes:
    print(iter)
    node1 = "Node_" + str(random.randint(0, n))
    node2 = "Node_" + str(random.randint(0, n))
    if not G.has_edge(node1,node2):
        G.add_edge(node1,node2)
        iter += 1

# %%
nx.draw_networkx(G)

# %%
degrees = [val for (node, val) in G.degree()]

sum_of_edges = sum(degrees)
avg_degree = sum_of_edges / tot_egdes

print(2*np.log(2))
print(avg_degree)

# %%
Gcc = sorted(nx.connected_components(G), key=len, reverse=True)
G0 = G.subgraph(Gcc[0])

# %%
print("full network node count is " + str(G.number_of_nodes()))
print("largest compent node count is " + str(G0.number_of_nodes()))
nx.draw_networkx(G0)
plt.show()


