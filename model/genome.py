import networkx as nx
from random import Random
from matplotlib import pyplot as plt
import math
import numpy as np
from tqdm import tqdm




class Genome():
    def __init__(self,nodes,random):
        self.nodes = nodes
        self.random = random
        self.graph = self.generate_dag_graph()
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
        at the ende the graph is fixed to ensure all nodes are reachable.
        p --> add : 1- p --> delete
        """
        edges = list(self.graph.edges)
        nonedges = list(nx.non_edges(self.graph))
        nonedges = self.filter_edges(nonedges)

        for _ in tqdm(range(permutaions)):
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


    def filter_edges(self,edges):
        """
        filters a list of edges to only return edgeswith x[0]<x[1]
        :param edges:
        :return:
        """
        return list(filter(lambda x: x[0]<x[1],edges))


    def merge_perent_graphs(self, first_parent,second_parent):
        assert (first_parent.nodes == second_parent.nodes == self.nodes)
        G = nx.DiGraph()
        G.add_nodes_from(range(first_parent.nodes))
        first_edges = set(first_parent.graph.edges)
        second_edges = set(second_parent.graph.edges)
        commen_edges = set(set(first_edges).intersection(second_edges))
        unique_edges = list((first_edges - commen_edges).union( second_edges -commen_edges))
        selected_unique_edges =unique_edges[:math.floor(len(unique_edges) / 2)]
        G.add_edges_from(commen_edges)
        G.add_edges_from(selected_unique_edges)
        G = self.fix_graph(G)
        self.graph = G

        addet_egdges = math.floor(self.graph.number_of_edges()-(second_parent.graph.number_of_edges()+ first_parent.graph.number_of_edges())/2)
        if addet_egdges > 0:
            self.permut_graph(addet_egdges,0)
        else:
            self.permut_graph(-addet_egdges,1)


random = Random()
genome1  = Genome(2000,random)
genome2 =  Genome(2000,random)
genome_child = Genome(2000,random)
genome_child.merge_perent_graphs(genome1,genome2)


