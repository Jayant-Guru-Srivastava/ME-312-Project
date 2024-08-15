import random
import textwrap
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



def create_fixed_grid(grid_world, matrix):
    for row in matrix:
        for col in row:
            if matrix[row][col] == '1':
                grid_world.obstacles.add((row, col))
            if matrix[row][col] == 'S':
                pass


def create_obstacles_from_hex(grid_world):
    hex_code = '0xc00409454010010842905a4880282852d21055081414900154d0028100300120a040890000a982c1c70914a00840485002041d000008980212510b831600001020810f401010508784d4140310135900a993c255c81201001022d5862080064460a811b2e08082102c0060a100000037478a0e0290a002a126811b002034a4005fa04800b30094010807986850461421e60080104ddc0900618a03c8348a0190649129100fa114001a142040a010095104744272239400441006018f1545a4100404114180ec028'
    binary_code = bin(int(hex_code, 16))[2:]
    binary_code = binary_code.zfill(grid_world.m * grid_world.n)
    print(len(binary_code))
    rows = textwrap.wrap(binary_code, grid_world.n)
    print(rows)
    for row_index in range(len(rows)):
        for c_index in range(len(rows[row_index])):
            number = rows[row_index][c_index]
            # print(number)
            if number == '1':
                grid_world.obstacles.add((row_index, c_index))
    # exit()
    # for s in binary_code:


# density: float between 0 and 1, defines the percentage of obstacles in the grid
def create_random_obstacles(grid_world, density):
    total_blocks = grid_world.m * grid_world.n
    number_of_walls = int(density * total_blocks)
    for i in range(number_of_walls):
        x = random.randint(0, grid_world.m - 1)
        y = random.randint(0, grid_world.n - 1)
        if not ((x == grid_world.start_x and y == grid_world.start_y) or (
                x == grid_world.end_x and y == grid_world.end_y)):
            grid_world.obstacles.add((x, y))


# distance_between_walls: defines distance between 2 fixed walls
def create_fixed_obstacles(grid_world, distance_between_walls):
    for i in range(1, grid_world.m - 1):
        for j in range(grid_world.n - 1):
            if j % distance_between_walls == 0:
                if not ((i == grid_world.start_x and j == grid_world.start_y) or (
                        i == grid_world.end_x and j == grid_world.end_y)):
                    grid_world.obstacles.add((i, j))
                if j % (2 * distance_between_walls) != 0:
                    if not ((0 == grid_world.start_x and j == grid_world.start_y) or (
                            0 == grid_world.end_x and j == grid_world.end_y)):
                        grid_world.obstacles.add((0, j))
            if j % (2 * distance_between_walls) == 0:
                if not ((grid_world.m - 1 == grid_world.start_x and j == grid_world.start_y) or (
                        grid_world.m - 1 == grid_world.end_x and j == grid_world.end_y)):
                    grid_world.obstacles.add((grid_world.m - 1, j))


def is_same(x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        return True
    return False
