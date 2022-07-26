import networkx as nx
from matplotlib import pyplot as plt
import math
import numpy as np

# create the depicted graph manually
G = nx.Graph()

# create 6 nodes
n = 5
iter = 0
while iter <= n:
    print(iter)
    name = 'Node_' + str(iter)
    print(name)
    G.add_node(name)
    iter += 1

# add the edges in the correct configuration
G.add_edge('Node_0', 'Node_1')
G.add_edge('Node_1', 'Node_2')
G.add_edge('Node_1', 'Node_3')
G.add_edge('Node_2', 'Node_3')

G.add_edge('Node_0', 'Node_4')
G.add_edge('Node_0', 'Node_5')
G.add_edge('Node_4', 'Node_5')

# print the graph 
nx.draw_networkx(G)
plt.show()


# the modularity matrix is given by
# Q = (1/4m)s^TBs
# where s is the n-dimensional vector with elements s_i and B is the nxn matrix with elements B_ij, called the modularity matrix
# B_ij = A_ij - (k_i*k_j/2m)
# s_i = 1 if node i belongs to group 1, 0 otherwise
# m is the total number of edges in the graph

A = nx.adjacency_matrix(G)
B = nx.modularity_matrix(G)

print(A)
print(B)

# now that we have the modularity matrix, we can get the eigenvalues and eigenvectors
eigenvalues = np.linalg.eigvals(B)
np.amax(eigenvalues)

eigenpairs = np.linalg.eig(B)

largest_eigenvalue = eigenpairs[0][0]
largest_eigenvalue_vec = eigenpairs[1][0]

print(largest_eigenvalue)
print(largest_eigenvalue_vec)