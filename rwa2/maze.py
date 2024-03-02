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

# Define the size of the maze
MAZE_SIZE = 4

# Define the maze as a 2D list
maze=list()
for _ in range(MAZE_SIZE):
    maze.append( [EMPTY] * MAZE_SIZE )

# Rewrite the previous line using for loops


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
  
# define and randomize goal position
goal_position = random.choice(all_maze_pos)
    
# remove position of goal from the all maze position list
all_maze_pos.remove(goal_position)

# orientations_poss is a list of all possible orientations of robot
orientations_poss = ['up', 'down', 'left', 'right']

# randomizes robots position from all maze position list
robot_position = random.choice(all_maze_pos)

#removes robots position from maze position list
all_maze_pos.remove(robot_position)

# randomizes robot orientation using orientation_pos
robot_orientation = random.choice(orientations_poss)

"""
based on the geometry of the maze the robot will not get trapped by obstacles 
so long as the obstacles are not heavily around the perimeter (outside) of the maze,
since there are only 3 obstacles the outer wall would have to be obstructing the robot
for the robot to be blocked in 4 directions

therefore if you can create a normal distrubution with the same center of the maze (2.5)
with a low standard deviation, then randomly select numbers from that distrubution, 
the numbers selected will almost always be toward the center of the maze.

It would be virtually impossible for all 3 obstacles to be along or near the perimeter,
therefore the robot would not be trapped
"""

#randomize obstacles based on normal distribution of numbers 
# where the mean is the center of maze
maze_distr=list()
num_of_obstacles=3
for x in range(num_of_obstacles):
    
    # random normal distrubution with a mean equal to half the maze size and SD = 0.5
    norm1=round(random.normalvariate(float(MAZE_SIZE-1)/2,0.5))
    norm2=round(random.normalvariate(float(MAZE_SIZE-1)/2,0.5))
    # add the distrubution to the list variable
    maze_distr.append([norm1,norm2])
    
    # maze_distr_match checks if there is a match between the distribution number
    #selected and the open spaces left in the maze
    maze_distr_match=False
    #loops until there is a match
    while maze_distr_match is False:
        # cycles through all empty spaces until match is found
        for i in range(len(all_maze_pos)):
            if maze_distr[x] == all_maze_pos[i]:
                maze_distr_match = True
                #remove the match from the list of empty spaces
                all_maze_pos.remove(maze_distr[x])
                break
        # no match found
        if maze_distr_match is False:
            # remove the distrubution number and re-generate it
            maze_distr.pop(x)
            # random normal distrubution with a mean equal to half the maze size and SD = 0.5
            norm1=round(random.normalvariate(float(MAZE_SIZE-1)/2,0.5))
            norm2=round(random.normalvariate(float(MAZE_SIZE-1)/2,0.5))
            # using normal distribution create a list of 6 numbers to be coords for obstacles
            maze_distr.append([norm1,norm2])
                 
# obstacles placed 
o1=maze_distr[0]
o2=maze_distr[1]
o3=maze_distr[2]
obstacle_positions = [o1, o2, o3]



# Place obstacles, the robot, and the goal in the maze
for obstacle in obstacle_positions:
    maze[obstacle[0]][obstacle[1]] = OBSTACLE

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