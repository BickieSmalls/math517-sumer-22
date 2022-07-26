import networkx as nx
import random

# write a program that generates a configuration model network with nodes of defree 1 and 3 only
# and then calculate the size of the largest componeent

#(a) Use your program to calculate the size of largest component for a network of
# n=10,000 nodes with p1==0.6 and p3==0.4, and pk==0 for all other values of k.

# create a random series of 1s and 3s with probability 0.6 and 0.4, respectively

sequence = [1] * 6000 + [3] * 4000
random.shuffle(sequence)
G = nx.configuration_model(sequence)

Gcc = sorted(nx.connected_components(G), key=len, reverse=True)
G0 = G.subgraph(Gcc[0])

G0.number_of_nodes()
G0.number_of_edges()

# (b) modify the program to calculate the size of largest component for values of p1 from 0.0 to 1.0 
# in steps of 0.1. THen make the graph of the results as a function of p1. 
# Hence estimate the value of p1 at the phase transition where the giant component disappears.

def configuration_model_attempt(i):
    sequence = [1] * int(1000 * i) + [3] * int(10000 - 1000 * i)
    random.shuffle(sequence)
    G = nx.configuration_model(sequence)
    Gcc = sorted(nx.connected_components(G), key=len, reverse=True)
    G0 = G.subgraph(Gcc[0])
    return [G0.number_of_nodes(), G0.number_of_edges()]

for i in (0,1,2,3,4,5,6,7,8,9,10):
    print(configuration_model_attempt(i))

"""
for i in (0,1,2,3,4,5,6,7,8,9,10):
    sequence = [1] * int(1000 * i) + [3] * int(10000 - 1000 * i)
    random.shuffle(sequence)
    G = nx.configuration_model(sequence)
    Gcc = sorted(nx.connected_components(G), key=len, reverse=True)
    G0 = G.subgraph(Gcc[0])
    print(i/100, G0.number_of_nodes(), G0.number_of_edges())
"""
