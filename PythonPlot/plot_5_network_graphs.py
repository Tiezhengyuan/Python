# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 10:32:50 2015

@author: yuan
"""
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(nodes_df, edges_df, graph_layout='shell',
               Nsize=1600, Nratio=500, Ncolor='blue', Nalpha=0.3,Nshape='o',
               Ecolor='blue', Ealpha=0.3, Etickness=1, edge_text_pos=0.3,
               text_font='sans-serif'):
    #format nodes
    Nlist=map(lambda x: x[0], nodes_df)
    if len(nodes_df[0])>=2:
        Nsize=map(lambda x: x[1]*Nratio, nodes_df)
    if len(nodes_df[0])>=3:
        Ncolor=map(lambda x: x[2], nodes_df)


    #format edges
    Elist=map(lambda x: (x[0], x[1]), edges_df)
    if len(edges_df[0])>=3:    
        Elabel=map(lambda x: x[2], edges_df)
        Elabel=dict(zip(Elist, Elabel))
    if len(edges_df[0])>=4:
        Ecolor=map(lambda x: x[3], edges_df)
    if len(edges_df[0])>=5:
        Ewidth=map(lambda x: x[4], edges_df)

    
    ###############
    # create a network graph
    G=nx.Graph()
        
    # add edges
    G.add_edges_from(Elist)

    # layouts for the network
    if graph_layout == 'spring':
        graph_pos=nx.spring_layout(G)
    elif graph_layout == 'spectral':
        graph_pos=nx.spectral_layout(G)
    elif graph_layout == 'random':
        graph_pos=nx.random_layout(G)
    else:
        graph_pos=nx.shell_layout(G)

    #
    nx.draw_networkx(G, graph_pos,font_family=text_font, nodelist=Nlist, 
                     node_size=Nsize, node_color=Ncolor,node_shape=Nshape,
                     edgelist=Elabel.keys(), edge_color=Ecolor, width=Ewidth,
                     )
 #   print Elabel
    nx.draw_networkx_edge_labels(G, graph_pos, edge_labels=Elabel)

    # show graph
    plt.show()

#main program
#layout: shell, random, spectral, spring
#format of nodes:[node, node_size, node_color]
#format of edges: [nodeA, nodeB, edge_label, edge_color, edge_width]
#node_shape:cicle:'o', rectangle:'s', triangle:'^', reversed triangle:'v', octangle:'8',hexangle:'h', hxangle:'p'
if __name__=="__main__":
    nodes_df = [['J',2,9], ['C',2,9], ['B',2,8],  ['D',2,7], ['E',2,6], ['F',2,5],
                     ['G',3,4], ['A',10,1],['H',4,3], ['I',2,2] ]
    edges_df = [['A', 'B', 4, 1,1], ['B', 'F', 30, 2,1], ['B', 'H', 5,3,1], 
                ['E', 'F', 10,4,1], ['E', 'I', 3,5,2],['B', 'G', 6,6,2], 
                ['D', 'H',67,7,2], ['F', 'J',5,8,2],['C', 'E',4,9,3], 
                ['A', 'E',10,9,3],['C', 'F',3,5,3], ['D', 'G',6,3,3], 
                ['I', 'J',3,2,3]] 
    #draw_graph(graph, labels)
    draw_graph(nodes_df, edges_df)
