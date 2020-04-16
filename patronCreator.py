import random as rd
import numpy as np
import os

from matplotlib import colors
import matplotlib.pyplot as plt


class patronGen():
    def __init__(self):

        self.original_matrix = np.ones([5,5]) 
        self.cmap = colors.ListedColormap([
            (0.612,0.652,0.656),
            (0.88,0.08,0.24),
            (0,0.712,0.952),
            (0,0,0)
        ])
        self.bounds=[1,2,3,4,5]
        self.norm = colors.BoundaryNorm(self.bounds, self.cmap.N)

    def colores(self, repetitions, value):

        for i in range(repetitions):
            width = rd.randint(0,4) 
            height = rd.randint(0,4)

            while self.original_matrix[width,height] != 1:
                width = rd.randint(0,4)
                height = rd.randint(0,4)

            self.original_matrix[width,height] = value

    def create_figure(self):

        self.colores(1,4)
        self.colores(9,2)
        self.colores(8,3)

        fig, ax = plt.subplots(figsize=(10,10))
        
        ax.imshow(self.original_matrix.transpose(),cmap=self.cmap, norm=self.norm)
        ax.tick_params(axis=u'both', which=u'both',length=0)
        ax.axes.get_xaxis().set_visible(False)
        ax.axes.get_yaxis().set_visible(False)

        for i in range(4):
            ax.axvline(0.49 + i,c = "black",linewidth = 0.8)
            ax.axhline(0.49 + i,c = "black",linewidth = 0.8)

        plt.savefig('patron.png')
        plt.close(fig)

