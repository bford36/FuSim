"""
This file will serve as a collection of various nodes
"""

from modules.utils.consts import *
from modules.fluid import fluid

class BaseNODE:

    def __init__(self, name="base node #00"):
        self.type = "BaseNode"
        self.name = name

    def _GetType(self):
        return self.type

    def track(self, dict):
        """
        Overwrite this function in each of the nodes made
        """
        pass

class ViewNODE(BaseNODE):

    def __init__(self, name="view node #00", filename=None):
        self.type = "ViewNODE"

    def track(self, dict):
        fluid1 = dict["f1"]
        fluid2 = dict["f2"]

        if filename == None:
            filename = "last_ViewNode.txt"

        filedump(fluid1, fluid2, filename)

class MagNODE(BaseNODE):

    def __init__(self, name="mag node #00", len=0.0):
        self.type = "MagNODE"
        self.length = len

    def setParams(E=[0.0,0.0,0.0], B=[0.0,0.0,0.0]):
        self.E = E
        self.B = B

    def track(self, dict):
        # print("tracking")
        #F = q*E + v*B
        f = dict["fluid"]

        for p in f.parts:

            angle = atan( p.v[1] / p.v[0] )

            kickx = f.charge*self.E[0] + vx*self.B[0]*cos(angle)
            kicky = f.charge*self.E[1] + vy*self.B[1]*cos(angle)

            # [ x y z vx vy vz ]
            p[3] += kickx
            p[4] += kicky
