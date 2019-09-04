
"""
This Example aims to simulate nothing. Its sole purpose is to prove
working concept and the files and code structure work
"""

print("Start.")


#IMPORTS
from modules.fluid.fluid import fluid
from modules.lat.lat import lat
from modules.node.Node import BaseNODE, ViewNODE, MagNODE
from modules.utils.consts import *

nodecount = 10
LatLength = 10 #meters
# nParts = 100

lattice = lat(name="Test Lat")


Nlist = [None] * nodecount
N_len = LatLength / nodecount

for i in range(nodecount):
    Nlist[i] = MagNODE(len=N_len)

for node in Nlist:
    """
    Here we are making a list of nodes then populating a lattice
    """
    node.setParams(E=[0.0,0.0,0.0], B=[0.0,0.0,0.0])
    lattice.addNode(node)



F = fluid(name="electon SOUP")

F.setType(type="e")

#ONLY ONE PARTICLE
X = [ 0.0, 0.0, 0.0 ]
V = [ 0.0, 0.0, 0.0 ]
t = 0.0

F.addParticle(X,V,t)

lattice.trackfluid(F,dict)

print("Stop.")













#eof
