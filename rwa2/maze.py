"""
This module contains all nessecary functions to initate the maze,
randomize goal placement, and print the maze after each user input
the global variables in this module don't depend on the other modules (no imports)
"""
import random

# Constants
# Here are all the emojis: "💥", "🏁", "⏫", "⏩", "⏪", "⏬", "🚧"
EMPTY = "  "
BOOM = "💥"
OBSTACLE = "🚧"
GOAL = "🏁"
ROBOT_UP = "⏫"
ROBOT_DOWN = "⏬"
ROBOT_LEFT = "⏪"
ROBOT_RIGHT = "⏩"
HORIZONTAL_WALL = "──"
VERTICAL_WALL = "│"
CORNER = "┼"

#moved MAZE_SIZE to robot.py
# Define the size of the maze
MAZE_SIZE = 4

# Define the maze as a 2D list
maze = [[EMPTY] * MAZE_SIZE for _ in range(MAZE_SIZE)]
# Rewrite the previous line using for loops

#decided to move robot position to robot.py

# Define the obstacles' positions
obstacle_positions = [[1, 1], [2, 2], [3, 3]]


#have to make sure robot will be randomized and not placed over obstacles or goal
#cell nums is a list of the number of cells in a row or a column of the maze
cell_nums= list(range(MAZE_SIZE))

#list of all positions in the maze
all_maze_pos=list()

# the variable x populates rows in all maze positions list
for x in cell_nums:
    # the variable i populates all columns in all maze positions list
    for i in cell_nums:
        all_maze_pos.append([cell_nums[x],cell_nums[i]])

# delete counters from previous loop
del x, i

# remove positions of obstacles from the all maze position list
for x in range(len(obstacle_positions)):
    all_maze_pos.remove(obstacle_positions[x])
  
# define and randomize goal position
goal_position = random.choice(all_maze_pos)
    
# remove position of goal from the all maze position list
all_maze_pos.remove(goal_position)

# Place obstacles, the robot, and the goal in the maze
for obstacle in obstacle_positions:
    maze[obstacle[0]][obstacle[1]] = OBSTACLE

# orientations_poss is a list of all possible orientations of robot
orientations_poss = ['up', 'down', 'left', 'right']

# randomizes robots position from all maze position list
robot_position = random.choice(all_maze_pos)

# randomizes robot orientation using orientation_pos
robot_orientation = random.choice(orientations_poss)

# place goal emoji
maze[goal_position[0]][goal_position[1]] = GOAL

#previous robot position (initially empty)
prev_rob_pos=robot_position

# Function to print the maze
def print_maze(robot_position, robot_orientation):
    # make previous robot position global to keep changes outside of function
    global prev_rob_pos
    # change emoji of robot based on robot orientation
    if robot_orientation == 'up':
        ROBOT=ROBOT_UP
    elif robot_orientation == 'down':
        ROBOT=ROBOT_DOWN
    elif robot_orientation == 'left':
        ROBOT=ROBOT_LEFT
    elif robot_orientation == 'right':
        ROBOT=ROBOT_RIGHT
    
    # terminate will terminate program when it's value is set true
    terminate=False
    
    # robot arrives at goal
    if robot_position == goal_position:
        maze[robot_position[0]][robot_position[1]] = ROBOT
        print('\n YOU WIN \\o/ \n')
        terminate = True
    #robot hits obstacle
    elif robot_position == obstacle_positions[0] \
    or robot_position == obstacle_positions[1] \
    or robot_position == obstacle_positions[2]:
        maze[robot_position[0]][robot_position[1]] = BOOM
        print('\n GAME OVER :\'( \n')
        terminate=True
    # robot does not hit obstace nor goal
    else:
        maze[robot_position[0]][robot_position[1]] = ROBOT
    
    # Print top boundary
    print("┌" + "─" * (MAZE_SIZE * 3 - 1) + "┐")    
    
    for i, row in enumerate(maze):
        # Print left boundary
        print(VERTICAL_WALL, end="")

        # Print cell contents
        for j, cell in enumerate(row):
            print(cell, end="")
            # Print vertical wall if not in the last column
            if j < MAZE_SIZE - 1:
                print(VERTICAL_WALL, end="")

        # Print right boundary
        print(VERTICAL_WALL)

        # Print horizontal wall between rows (except for the last row)
        if i < MAZE_SIZE - 1:
            print("├" + "─" * (MAZE_SIZE * 3 - 1) + "┤")

    # Print bottom boundary
    print("└" + "─" * (MAZE_SIZE * 3 - 1) + "┘")
    
    #delete robot emoji from previous position
    maze[prev_rob_pos[0]] [prev_rob_pos[1]] = EMPTY
    
    prev_rob_pos=robot_position
    #return terminate (tells main function to stop if nessecary)
    return terminate
# if __name__ == "__main__":
#     print_maze(robot_position, robot_orientation )