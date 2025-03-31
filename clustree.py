import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def clustree(clusterings : list, ax):
    """ Compute and plot a tree to compare and link a list of clusters.
    
        Args:
            - clusterings: List of clusterings in the form of a list of arrays(n) of integers each standing for a cluster
        
        Outs:
            - G, pos: nx.Graph G and computed positions of nodes and edges"""
    graph_layers = []
    graph_edges_between_layers = []

    curr_clustering = clusterings[0]
    # Find the number of clusters
    curr_clusters = sorted(np.unique(curr_clustering))
    assert curr_clusters[0] == 0

    # Number of points
    n_points = len(curr_clustering)
    # Append the layer
    graph_layers.append([(i, np.sum([curr_clustering[j] == i for j in range(len(curr_clustering))])) for i in curr_clusters])

    for k in range(1,len(clusterings)):
        prev_clustering = curr_clustering
        curr_clustering = clusterings[k]
        # Find the number of clusters
        prev_clusters = curr_clusters
        curr_clusters = sorted(np.unique(curr_clustering))
        # Append the layer
        graph_layers.append([(i, np.sum([curr_clustering[j] == i for j in range(len(curr_clustering))])) for i in curr_clusters])

        edges = [[0 for c in curr_clusters] for pc in prev_clusters]
        for i, p in enumerate(curr_clustering):
            edges[prev_clustering[i]][p] += 1

        graph_edges_between_layers.append(edges)
    
    G = nx.Graph()
    pos = {}
    node_size = []
    node_color = []
    for l, layer in enumerate(graph_layers):
        for i, n in enumerate(layer):
            G.add_node((l,n[0]), size = n[1])
            pos[(l, n[0])] = [-1 + l*2/len(graph_layers), -1 + i*2/len(layer)]
            node_size.append(2000*n[1]/n_points)
            node_color.append(l)
    
    width = []
    label = {}
    for l, edges in enumerate(graph_edges_between_layers):
        for i in range(len(edges)):
            for j in range(len(edges[i])):
                if edges[i][j] > 0:
                    G.add_edge((l,i),(l+1,j), weight = edges[i][j])
                    width.append(edges[i][j]/n_points*50)
                    label[(l,i),(l+1,j)] = edges[i][j]
    nx.draw_networkx_edges(G, pos, width=width, ax = ax)
    nx.draw_networkx_nodes(G, pos, node_size=node_size, node_color = node_color, ax =ax)
    keys = [k for k,v in label.items()]
    label1 = {key : label[key] for key in keys[0:len(label):3]}
    label2 = {key : label[key] for key in keys[1:len(label):3]}
    label3 = {key : label[key] for key in keys[2:len(label):3]}
    nx.draw_networkx_edge_labels(G, pos, edge_labels = label1, label_pos = 0.2, ax =ax)
    nx.draw_networkx_edge_labels(G, pos, edge_labels = label2, label_pos = 0.5, ax =ax)
    nx.draw_networkx_edge_labels(G, pos, edge_labels = label3, label_pos = 0.8, ax =ax)
    plt.show()
    return G, pos