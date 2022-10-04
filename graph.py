# CS410 Reinforcement Learning
# Christopher Juncker
#
# Graphs
# starting with something basic, ex.
# https://matplotlib.org/stable/plot_types/basic/plot.html
# and making changes 'til it suits what I need to display
#

import numpy as np
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, x_lim=1000, y_lim=100, line_width=2.0, x_grid=100, y_grid=10):
        # configure any visual part of the graph that doesn't change
        plt.style.use('_mpl-gallery')

        # save axis dimensions, grid size, etc
        self.x_lim = x_lim
        self.y_lim = y_lim
        self.line_width = line_width
        self.x_grid = x_grid
        self.y_grid = y_grid


    def display(self, x, y):
        # clear the old data
        plt.clf()  # clear figure - cla() can clear axes as well
        # make data

        # plot the new data
        fig, ax = plt.subplots()

        ax.plot(x, y, linewidth=self.line_width)

        ax.set(xlim=(0, self.x_lim), xticks=np.arange(0, x_lim // self.x_grid)*self.x_grid,
               ylim=(0, self.y_lim), yticks=np.arange(0, y_lim // self.y_grid)*self.y_grid)

        plt.show()