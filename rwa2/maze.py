"""
This module contains the maze and the robot's initial position, as well as functions to print the maze and move the robot.
"""
# from robot import MAZE_SIZE, robot_orientation, robot_position #type: ignore

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
# Define the robot's initial position
# robot_position = [2, 3]  # [row, column]
# robot_orientation = robot_orientation

# Define the obstacles' positions
obstacle_positions = [[1, 1], [2, 2], [3, 3]]

# Define the goal position
goal_position = [3, 2]

# Place obstacles, the robot, and the goal in the maze
for obstacle in obstacle_positions:
    maze[obstacle[0]][obstacle[1]] = OBSTACLE

# maze[robot_position[0]][robot_position[1]] = ROBOT
maze[goal_position[0]][goal_position[1]] = GOAL

# Function to print the maze
def print_maze(robot_position, robot_orientation):
    # change emoji of robot based on robot orientation
    if robot_orientation == 'up':
        ROBOT=ROBOT_UP
    elif robot_orientation == 'down':
        ROBOT=ROBOT_DOWN
    elif robot_orientation == 'left':
        ROBOT=ROBOT_LEFT
    elif robot_orientation == 'right':
        ROBOT=ROBOT_RIGHT
    # Print top boundary
    print("┌" + "─" * (MAZE_SIZE * 3 - 1) + "┐")
    
    maze[robot_position[0]][robot_position[1]] = ROBOT
    
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
    maze[robot_position[0]][robot_position[1]] = EMPTY
 
# if __name__ == "__main__":
#     print_maze(robot_position, robot_orientation )