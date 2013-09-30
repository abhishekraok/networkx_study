# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 15:29:59 2013

@author: Abhishek
"""
# Basic Analysis for graphs
import networkx as nx
import matplotlib.pyplot as plt

def analyze_graphc(m): # Analyzes graph
    
    #Basic
    e = m.number_of_edges()
    n = m.number_of_nodes()
    print 'The number of nodes is ' + str(n) +' and the number of edges is ' + str(e)
    plt.figure(e)
    
    #Degree Distr
    dm = nx.degree(m)
    dmv = dm.values()
    plt.subplot(211)
    plt.title('Degree Distribution')
    plt.ylabel('Number of nodes')
    plt.xlabel('Degree of nodes')
    plt.hist(dmv,bins=max(dmv))
    
    #Distance
#    ad = nx.average_shortest_path_length(nx.connected_component_subgraphs(m)[0])
    ad = nx.average_shortest_path_length(m)
    print 'The average shortest path length is ' + str(ad)
    
    #Connected Components
    #ccm = nx.connected_components(m)
    #print 'The connected components are ' + str(ccm)
    
    #Centrality
    bwc = nx.betweenness_centrality(m)
    bwcrv = [round(float(x),2) for x in bwc.values()]
    print 'The betweenness centrality is ' + str(bwcrv)
    plt.subplot(212)
    plt.title('Betweenness centrality distr')
    plt.hist(bwcrv)
    
    #Clustering
    cl = nx.clustering(m.to_undirected())
    print 'The clustering clustering coefficient is ' + str(cl)
    
    # Show  the graph
#    plt.subplot(212)
#    plt.title('Network Visualization')
#    nx.draw(m)

    #Cleanup
    print 'End of analyzing network'
    print ' '
    m.clear()
    return