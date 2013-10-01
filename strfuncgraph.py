# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 15:08:05 2013

@author: Abhishek
"""
import networkx as nx
import matplotlib.pyplot as plt
import pylab

def createstr():
#    fd = open('input_text.txt','r')
#    chars = ''
#    for line in fd:
#       for c in line:
#           chars += c
    chars='hello how are you? Im fine. Hope you are fine too. Im going to college now'
    #alpha_array = [x for x in input_sentence.replace(" ","")]      
           
    chars= ''.join(e for e in chars if (e.isalpha())) 
    chars = chars.lower()
    
    alphalist = set(chars)
    #alphalist = [chr(x) for x in range(ord('a'),ord('z'))]
    return alphalist,chars  
    
def createstrGraph(alphalist,chars):
    
    G = nx.DiGraph()
    G.add_nodes_from(alphalist)
    xp = ' '
    
    for x in chars:
    #    if (x == ' ' or xp == ' '):
    #        xp = x        
    #        continue
    #    
        if G.has_edge(x,xp):
            G[x][xp]['weight'] += 1
        else:
            G.add_edge(x,xp,weight=1)      
        xp=x
    return G
    
def drawstrGraph(G):  
    pos=nx.spring_layout(G)
    # version 2
    pylab.figure(2)
    nx.draw(G,pos)
    # specifiy edge labels explicitly
    edge_labels=dict([((u,v,),d['weight'])
                 for u,v,d in G.edges(data=True)])
    nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
    # show graphs
    pylab.show()
    return