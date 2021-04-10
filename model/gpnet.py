import torch.nn as nn
import torch


class GPNet(nn.Module):
    def __init__(self,genome):
        super(GPNet, self).__init__()
        self.model = self.generate_from_genome(genome)


    def forward(self):
        pass


    def generate_from_genome(self):
        pass


