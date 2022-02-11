# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 10:32:50 2015

@author: yuan
"""

import networkx as nx
import matplotlib.pyplot as plt

#draw the simpliest network

#initiate a graph
G=nx.Graph()

#add nodes or edges
G.add_node('A')
G.add_node('B')
G.add_node('C')
G.add_node('D')
G.add_edge('A','B')
G.add_edge('A','C')
G.add_edge('D','C')

#visulization
nx.draw(G, with_labels=True)
plt.show()