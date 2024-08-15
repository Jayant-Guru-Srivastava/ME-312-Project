import Functions
from GridWorld import GridWorld
from sarsa_agent import SARSAgent
from matplotlib import pylab
from pylab import *
import ast
import collections
# What is this code doing?
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



if __name__ == "__main__":
    grid_world = GridWorld(26,26)
    # Functions.create_grid_from_hex(grid_world)
    Functions.create_random_obstacles(grid_world, 0)
    grid_world.scan_grid_and_generate_graph()
    grid_world.print_graph()
    grid_world.create_grid_ui(grid_world.m, grid_world.n, (grid_world.start_x, grid_world.start_y),
                              (grid_world.end_x, grid_world.end_y), grid_world.obstacles)

    SA = SARSAgent(list(range(4)))
    scores, episodes = [], []

    try:
        with open("q_table_episode_13100.txt", "r") as f:
            q_table_string = f.read()
            q_table_string = q_table_string[q_table_string.index('{'):q_table_string.rindex('}') + 1]
            SA.q_table = collections.defaultdict(lambda: [0, 0, 0, 0], ast.literal_eval(q_table_string))
    except FileNotFoundError:
        print("No existing Q-table found. Starting with a new Q-table.")

    number_of_episodes = 100000
    for episode in range(number_of_episodes):
        score =0
        state = grid_world.reset()
        grid_world.is_visited = [[0] * grid_world.m for temp in range(grid_world.n)]
        while True:
            grid_world.render()

            action = SA.get_action(str(state))
            next_state, reward, done = grid_world.step(action)
            next_action = SA.get_action(str(next_state))

            SA.learn(str(state), action, reward, str(next_state),next_action)
            print("<state:{0} , action:{1} , reward:{2} , next_state:{3}>".format(
                str(state), str(action), str(reward), str(next_state)))
            # grid_world.is_visited[state[0]][state[1]] += 1
            state = next_state
            action = next_action
            score += reward
            

            if done:
                scores.append(score)
                episodes.append(episode)
                pylab.plot(episodes, scores, 'b')
                pylab.savefig("./SARSA_learning10.png")
                if episode % 100 == 0:  # Save q_table every 100 episodes
                    with open(f"q_table_episode_{episode+13200}.txt", "w") as f:
                        f.write(str(SA.q_table))
                break
    print(SA.q_table)
