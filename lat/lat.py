"""
This file operates as a collection class that will hold the info
for a set of nodes.
"""

from modules.fluid import fluid
from modules.node.Node import BaseNODE, ViewNODE, MagNODE
from modules.utils.consts import *

class lat:

    def __init__(self, name="lat no name"):
        self.name = name
        self.nodes = []
        self.length = 0
        self.ready = False

    def addNode(self, node):
        (self.nodes).append(node)

    def initialize(self):

        len = 0
        for node in self.nodes:
            len += node.length

        self.length = len
        self.ready = True

    def trackfluid(self, fluids, dict):

        if self.ready == False:
            self.initialize()

        for node in self.nodes:
            node.track(dict)
