from networkx.generators.random_graphs import gnm_random_graph
from networkx import connected_components

from math import log

from sympy import exp
from scipy.optimize import fsolve
import numpy as np

def calcGnm(n:int, c:int):
    """ 
    :param n: is the nodes
    :param c: is the mean degree 2m/n
    """
    m = c * n / 2
    g = gnm_random_graph(n, m)
    
    #get the max length of the connected components
    result = g.subgraph(max(connected_components(g), key=len))
    return result

def eq(r):
    x1 = r[0]
    x2 = r[1]
    return x1, 1 - exp(-1 * x2 * 2 * log(2))


def calcER(n, c):
    x = fsolve(eq, np.array([1.8,1.57]))
    return max(n / 10 * x[0], n / 10 * x[1])

if __name__ == "__main__":
    c = 2 * log(2)
    n = 1000000
    
    result = calcGnm(n, c)
    print("Connected component of G(n, m): ", result)

    result = calcER(n, c)
    print("Connected component of G(n, p): ", result, "nodes")
    

