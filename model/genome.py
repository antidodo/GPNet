import networkx as nx
import random
from matplotlib import pyplot as plt


class Genome():
    def __init__(self,nodes):
        self.nodes = nodes
        self.random = random
        self.graph = self.generate_dag_graph()
        #self.permut_graph()

    def generate_dag_graph(self):
        """
        returns a random dag graph of size self.nodes that has only nodes that are reachable from the first node
        and can fifluence the last node. the liklihood of the inital graph of hafing a conetions is set by self.ege_prob
        :return: DAG_graph
        """
        # generate ranom graph
        G = nx.DiGraph()
        G.add_nodes_from(range(self.nodes))
        graph_compleate_reachable = False
        while not graph_compleate_reachable:
            not_reachable_in ,not_reachable_out = self.not_reachable(G)
            for n in not_reachable_in:
                G.add_edge(self.random.randint(0,n-1),n)
            for n in not_reachable_out:
                G.add_edge(n,self.random.randint(n+1, self.nodes-1))
            graph_compleate_reachable = len(not_reachable_in)==0 and len(not_reachable_out)==0
        self.print_graph(G)
        # all the edges that are reachable from the first node and that can influence the last node
        return G


    def not_reachable(self,graph):
        """
        test if all nodes can be reached from the input node and influence the output node.
        :param graph:
        :return:  list_not_ reachable_in , list_not_ reachable_out
        """
        reachable_in = nx.descendants(graph, 0)
        reachable_out = nx.ancestors(graph, self.nodes - 1)
        # add the last node back in
        reachable_out.add(self.nodes - 1)
        reachable = reachable_in and reachable_out
        set_of_nodes = set(range(1, self.nodes))

        not_reachable_in = set_of_nodes - reachable_in
        not_reachable_out = set_of_nodes - reachable_out
        return not_reachable_in ,not_reachable_out

    def print_graph(self,graph):
        """
        print the graph
        :param graph:
        :return:
        """
        plt.tight_layout()
        nx.draw_networkx(graph, arrows=True)
        plt.show()

    def permut_graph(self):
        
        set(self.graph.nodes)


genome  = Genome(100)