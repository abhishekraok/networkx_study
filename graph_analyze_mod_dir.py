# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 15:29:59 2013

@author: Abhishek
"""
# Basic Analysis for graphs
import networkx as nx
import matplotlib.pyplot as plt
<<<<<<< HEAD
import numpy as np
=======
>>>>>>> 1ac0ffa4b0db2ed5db811b8b8ae53877ed921674

def analyze_graphc(m): # Analyzes graph
    
    #Basic
    e = m.number_of_edges()
    n = m.number_of_nodes()
<<<<<<< HEAD
    print 'Start of analyzing network'
=======
>>>>>>> 1ac0ffa4b0db2ed5db811b8b8ae53877ed921674
    print 'The number of nodes is ' + str(n) +' and the number of edges is ' + str(e)
    plt.figure(e)
    
    #Degree Distr
    dm = nx.degree(m)
    dmv = dm.values()
<<<<<<< HEAD
    plt.subplot(221)
=======
    plt.subplot(211)
>>>>>>> 1ac0ffa4b0db2ed5db811b8b8ae53877ed921674
    plt.title('Degree Distribution')
    plt.ylabel('Number of nodes')
    plt.xlabel('Degree of nodes')
    plt.hist(dmv,bins=max(dmv))
<<<<<<< HEAD
    dmva = np.average(dmv)
    print 'The average degree is ' + str(dmva)

    #Distance
    ad = nx.average_shortest_path_length(m)
    dd = nx.shortest_path_length(m)
    ddv = dd.values()
    ddvv = [x.values() for x in ddv]
    ddvvv = []   # This will have all the distances 
    for x in ddvv:
        for y in x:
            ddvvv.append(y)
    plt.subplot(222)
    plt.title('Distance Distribution')
    plt.ylabel('Number of possible edge paths (u,v)')
    plt.xlabel('Distance')
    plt.hist(ddvvv)        
    print 'The average shortest path length is ' + str(ad)

    #Centrality
    bwc = nx.betweenness_centrality(m)
    bwcrv = [round(float(x),5) for x in bwc.values()]
    print 'The betweenness centrality is ' + str(bwc)
    plt.subplot(223)
    plt.title('Betweenness centrality distribution')
    plt.ylabel('Number of nodes')
    plt.xlabel('Betwenness centrality')
    plt.hist(bwcrv)
    
    #Clustering
    cl = nx.clustering(m.to_undirected())  #This function cannot be used with
                                            #directed graphs
    clv = [round(x,5) for x in cl.values()] #Rounding off for better display
    print 'The clustering clustering coefficient is ' + str(cl)
    plt.subplot(224)
    plt.title('Clustering Coefficient Distribution')
    plt.ylabel('Number of nodes')
    plt.xlabel('Clustering Coeff')
    plt.hist(clv)
    
    
=======
    
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

>>>>>>> 1ac0ffa4b0db2ed5db811b8b8ae53877ed921674
    #Cleanup
    print 'End of analyzing network'
    print ' '
    m.clear()
    return