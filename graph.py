# CS410 Reinforcement Learning
# Christopher Juncker
# graph.py
#
# Graphs
# starting with something basic, ex.
# https://matplotlib.org/stable/plot_types/basic/plot.html
# and making changes 'til it suits what I need to display
#
# on linux I wasn't able to show the graph until I installed
# pyqt5 (python3.x -m pip install pyqt5
#

import numpy as np
import matplotlib.pyplot as plt


class Graph:
    def __init__(self, x_lim=1000, y_lim=100, line_width=2.0, x_grid=100, y_grid=100):
        # configure any visual part of the graph that doesn't change
        plt.style.use('_mpl-gallery')

        # save axis dimensions, grid size, etc
        self.x_lim = x_lim
        self.y_lim = y_lim
        self.line_width = line_width
        self.x_grid = x_grid
        self.y_grid = y_grid

    def display(self, x, y):
        # plot the new data
        fig, ax = plt.subplots()

        fig.set_figwidth(8)
        fig.set_figheight(6)

        ax.plot(x, y, linewidth=self.line_width)


        # plt.set(xlim=(0, self.x_lim), xticks=np.arange(0, self.x_lim // self.x_grid)*self.x_grid,
        #       ylim=(0, self.y_lim), yticks=np.arange(0, self.y_lim // self.y_grid)*self.y_grid)

        plt.tight_layout()  # this fixes the window border cutting off the labels
        plt.show()

        # clear the old data
        plt.clf()  # clear figure - cla() can clear axes as well
