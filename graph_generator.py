"""
Created on Feb 17, 2018

@author: vm
"""


import numpy as np
from scipy.optimize import linprog

""" DATA"""
edges = [('A', 'B', 8),
         ('A', 'F', 10),
         ('B', 'C', 4),
         ('B', 'E', 10),
         ('C', 'D', 3),
         ('D', 'E', 25),
         ('D', 'F', 18),
         ('E', 'D', 9),
         ('E', 'G', 7),
         ('F', 'A', 5),
         ('F', 'B', 7),
         ('F', 'C', 3),
         ('F', 'E', 2),
         ('G', 'D', 2),
         ('G', 'H', 3),
         ('H', 'A', 4),
         ('H', 'B', 9)]
s, t = 'G', 'C'

""" Prepossessing """
nodes = sorted(set([i[0] for i in edges]))  # assumption: each node has an outedge
n_nodes = len(nodes)
n_edges = len(edges)

edge_matrix = np.zeros((len(nodes), len(nodes)), dtype=int)
for edge in edges:
    i, j, v = edge
    i_ind = nodes.index(i)  # slow
    j_ind = nodes.index(j)  # """
    edge_matrix[i_ind, j_ind] = v

nnz_edges = np.nonzero(edge_matrix)
edge_dict = {}
counter = 0
for e in range(n_edges):
    a, b = nnz_edges[0][e], nnz_edges[1][e]
    edge_dict[(a,b)] = counter
    counter += 1

s_ind = nodes.index(s)
t_ind = nodes.index(t)

""" LP """
bounds = [(0, 1) for i in range(n_edges)]
c = [i[2] for i in edges]

A_rows = []
b_rows = []
for source in range(n_nodes):
    out_inds = np.flatnonzero(edge_matrix[source, :])
    in_inds = np.flatnonzero(edge_matrix[:, source])

    rhs = 0
    if source == s_ind:
        rhs = 1
    elif source == t_ind:
        rhs = -1

    n_out = len(out_inds)
    n_in = len(in_inds)

    out_edges = [edge_dict[a, b] for a, b in np.vstack((np.full(n_out, source), out_inds)).T]
    in_edges = [edge_dict[a, b] for a, b in np.vstack((in_inds, np.full(n_in, source))).T]

    A_row = np.zeros(n_edges)
    A_row[out_edges] = 1
    A_row[in_edges] = -1

    A_rows.append(A_row)
    b_rows.append(rhs)

A = np.vstack(A_rows)
b = np.array(b_rows)
res = linprog(c, A_eq=A, b_eq=b, bounds=bounds)
print(res)
