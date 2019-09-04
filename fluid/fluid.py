"""
This file will be the basis for fluid options and specifications
"""

# IMPORTS
from modules.utils.consts import *

class fluid:

    def __init__(self,name="no name"):
        self.name = name
        self.mass = 0.0
        self.charge = 0.0
        self.parts = []

    def setType(self, type="none"):
        """
        This function set the species of the fluid
        i.e. ions or electrons
        """
        self.type = type

        if type=="e":
            self.mass = m_e
            self.charge = -1.0*q
        elif type=="ion":
            self.mass = 1
            self.charge = q

    def GetType(self):
        return self.type

    def addParticle(self,X,V,t):
        p = [ X[0:], V[0:], t, 0]
        (self.parts).append(p)

    def getParticle(index):
        return self.parts[index]

    #COORDINATES
    def x(self, index):
        return self.parts[index][0]
    def y(self, index):
        return self.parts[index][1]
    def z(self, index):
        return self.parts[index][2]
    def vx(self, index):
        return self.parts[index][3]
    def vy(self, index):
        return self.parts[index][4]
    def vz(self, index):
        return self.parts[index][5]
    def t(self, index):
        return self.parts[index][6]

    def compress(self):
        """
        Removes the flagged particles that are "LOST"
        """
        for i,p in enumerate(self.parts):
            if p[7] == 1:
                (self.parts).pop(i)




class RandomDist:

    def __init__(self, xlim, ylim):
        self.xlim = xlim
        self.ylim = ylim

    def getCoords():

        x = (2*random.random() - 1) * xlim
        y = (2*random.random() - 1) * ylim
        X = [x, y, 0.0]

        vx=0.0
        vy=0.0
        vz=0.0

        V = [vx, vy, vz]

        return [X[0:],V[0:],0.0]




        #eof
