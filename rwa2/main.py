"""
This is the main file which contains the entry point of your program.
"""
#import functions
from maze import print_maze # type: ignore
from robot import move_forward, move_backward, turn_right, turn_left #type: ignore 
#import initial robot orientation and position
from robot import  robot_orientation, robot_position # type: ignore

# inital robot position and orientation passed to main function
def main(robot_position, robot_orientation):
    print("Initial Maze:")
    #sending robot orientation and position to maze function
    print_maze(robot_position, robot_orientation)
    while True:
        #user input 
        action = input("Enter action (w: forward, s: backward, a: left, d: right, q: quit): ")
        print(robot_position)
        # interpret input from user
        if action =='w':
            print('going forward')
            # new position=move_forward(old position, unchanged orientation)
            robot_position=move_forward(robot_position, robot_orientation)
        elif action == 's':
            print('going backward')
            # new position=move_forward(old position, unchanged orientation)
            robot_position=move_backward(robot_position, robot_orientation)
        elif action == 'a':
            print('turning left')
            # new orientation=turn_left(old orientation)
            robot_orientation=turn_left(robot_orientation)
        elif action == 'd':
            print('turning right')
            # new orientation=turn_left(old orientation)
            robot_orientation=turn_right(robot_orientation)
        elif action == 'q':
            print('quitting program...')
            break
        else:
            print('please input listed keys')

        # Ctrl-c to stop the program
        print_maze(robot_position, robot_orientation)


# Run the main function
if __name__ == "__main__":
    main(robot_position, robot_orientation)
