from easydict import EasyDict as Dict
from functions import softmax
import numpy as np


class Network:
    def __str__(self):
        return "<object> RNN neural network for language model"

    def __init__(self, params):
        self.input_size = params.dimensions[0]
        self.hidden_size = params.dimensions[1]
        self.output_size = params.dimensions[2]
        self.w_first =   [] #TODO: init
        self.w_second =  [] #TODO: init
        self.w_reverse = []#TODO: init

    def forward(self, input_array_of_words):
        #TODO:
        return states, outputs


params = Dict({
    "dimensions": [3, 2, 3]
})

network = Network(params)
print(network.w_first.shape, network.w_second.shape, network.w_reverse.shape)

state, output = network.forward([2, 0, 1])
print(state)
print(output)
