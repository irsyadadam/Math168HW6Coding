from networkx import configuration_model
from tqdm import tqdm

import networkx as nx
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def create_config_model(p1:float, p2:float):
    """
    creates config model with given probabilities of having degree 1 and 3
    :param p1: is the probability of having degree 1
    :param p2: is the probability of having degree 3
    """
    degree = []
    for i in range(10000):
        degree.append(np.random.choice([1,3], p = [p1, p2]))
    g = configuration_model(degree)
    return g

if __name__ == "__main__":
    print("12.6a:")
    g = create_config_model(0.6, 0.4)
    print("Largest Connected Component of Config Model: ", g.subgraph(max(nx.connected_components(g), key=len)))
    print("\n")

    print("12.6b:")
    #create an array 0 - 1 with step 0.1
    p1 = np.arange(0, 1.1, 0.1)
    edgelist = []
    for i in tqdm(p1, desc="Creating Config Models: "):
        g = create_config_model(i, 1 - i)
        edgelist.append(g.subgraph(max(nx.connected_components(g), key=len)).number_of_edges())


    ax = sns.scatterplot(x = p1, y = edgelist, palette = "hls")
    ax.set(ylabel="Size of Connected Component", xlabel = "Probability of Node Degree 1")
    plt.savefig("Fig.png")
    print("Plot Saved")
