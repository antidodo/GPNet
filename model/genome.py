import networkx as nx
import random
from matplotlib import pyplot as plt


class Genome():
    def __init__(self,nodes,seed):
        self.nodes = nodes
        self.random = random
        self.random.seed(seed)
        self.graph = self.generate_dag_graph()
        self.print_graph(self.graph)
        self.permut_graph(10,0.5)
        self.print_graph(self.graph)

    def generate_dag_graph(self):
        """
        returns a random dag graph of size self.nodes that has only nodes that are reachable from the first node
        and can fifluence the last node. the liklihood of the inital graph of hafing a conetions is set by self.ege_prob
        :return: DAG_graph
        """
        # generate ranom graph
        G = nx.DiGraph()
        G.add_nodes_from(range(self.nodes))
        return self.fix_graph(G)

    def fix_graph(self,graph):
        """adds edges to the graph until all nodes are reachable"""
        graph_compleate_reachable = False
        while not graph_compleate_reachable:
            not_reachable_in ,not_reachable_out = self.not_reachable(graph)
            for n in not_reachable_in:
                graph.add_edge(self.random.randint(0,n-1),n)
            for n in not_reachable_out:
                graph.add_edge(n,self.random.randint(n+1, self.nodes-1))
            graph_compleate_reachable = len(not_reachable_in)==0 and len(not_reachable_out)==0
        return graph


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

    def permut_graph(self,permutaions,add_delete_prop):
        """chages self.graph as many times as given in permutaions with
        deletion  of edges p(1-add_delete_prop) or additions of edges p(add_delete_prop)
        at the ende the graph is fixed to ensure all nodes are reachable."""
        edges = list(self.graph.edges)
        nonedges = list(nx.non_edges(self.graph))
        nonedges = list(filter(lambda x: x[0]<x[1], nonedges))
        for _ in range(permutaions):
            if self.random.random() < add_delete_prop:
                chosen_edge = self.random.choice(nonedges)
                self.graph.add_edge(chosen_edge[0], chosen_edge[1])
                nonedges.remove(chosen_edge)
                edges.append(chosen_edge)
            else:
                chosen_edge = self.random.choice(edges)
                self.graph.remove_edge(chosen_edge[0], chosen_edge[1])
                edges.remove(chosen_edge)
                nonedges.append(chosen_edge)
        self.graph = self.fix_graph(self.graph)


    def merge_perent_graphs(self, first_PARENT_graph,second_parnt_graph):
        pass
genome  = Genome(20,42)