import networkx as nx 
import pandas as pd
V = {'sports complex', 'siwaka', 'phase1B', 'phase1A'}
E = [('sports complex', 'siwaka', 450), ('siwaka', 'phase1B', 230), ('siwaka', 'phase1A', 10)]
G = nx.DiGraph()
G.add_nodes_from(V)
G.add_weighted_edges_from(E)
# G.nodes
# G.edges
