
class DAGNode():
    def __init__(self ,neurons, combination_function ,dropout,random):
        """
        defines a node with the count of nourons, the function that combines the inputs and the dropout during training

        :param neurons:
        :param combination_function:
        :param dropout:
        """
        self.random = random
        self.neurons = neurons
        self.combination_function = combination_function
        self.dropout = dropout

    def init_random(self ,neurons_range ,combination_function_set ,dropout_range):
        """
        sets a random initialization from the given range
        :param neurons_range: (min,max)
        :param combination_function_set: (func_1,..,func_n)
        :param dropout_range: (min,max)
        """
        pass
    def init_from_parent(self,first_parent,second_parent):
        """
        combines the parameters from the parent nodes
        :param first_parent:
        :param second_parent:
        :return:
        """
        pass

