# What is this code doing?  What is the purpose of this file?
# This file is used to create the grid world and the obstacles in the grid world.  The grid world is a 2D array of
# cells.  The obstacles are represented as a set of (x, y) coordinates.  The grid world is used to create the UI for the
# grid world.  The obstacles are used to create the obstacles in the grid world.  The obstacles can be created in
# different ways.  The obstacles can be created randomly, fixed, or from a hex code.  The hex code is a string of 1s and
# 0s that represents the obstacles in the grid world.  The obstacles are created in the grid world by adding the
# coordinates of the obstacles to the obstacles set.  The grid world is created by creating a 2D array of cells and
# setting the start and end points of the grid world.  The grid world is then used to create the UI for the grid world.
# The UI is created by creating a window and drawing the grid world on the window.  The grid world is drawn by drawing
# the cells of the grid world and the obstacles in the grid world.  The obstacles are drawn as black squares on the grid
# world.  The cells are drawn as white squares on the grid world.  The start and end points are drawn as green and red
# squares on the grid world.  The grid world is then displayed on the window.  The grid world is used to create the
# environment for the agent.  The environment is created by creating the grid world and the obstacles in the grid world.
# The environment is then used to create the agent.  The agent is created by creating the q table for the agent.  The q
# table is a 2D array of cells.  The q table is used to store the q values for the agent.  The q values are used to
# determine the action of the agent.  The action of the agent is determined by taking the action with the highest q
# value.  The q table is then used to create the agent.

class Graph:

    def __init__(self, root):
        self.root = root
        self.adjacency_map = {}