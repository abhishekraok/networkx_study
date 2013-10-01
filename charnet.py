# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 13:50:00 2013

@author: Abhishek
"""

#word net
import strfuncgraph as sfg
import graph_analyze_mod_dir as gam

#Create string for graph
alphalist,chars = sfg.createstr() 

# Create graph out of string with weighted edges
G = sfg.createstrGraph(alphalist,chars) 

#Show graph
sfg.drawstrGraph(G)  

#analyze graph
gam.analyze_graphc(G)