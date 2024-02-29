"""
This module contains the functions that control the robot's movement.
"""
# import size of maze from maze so that code knows boandaries of maze
from maze import MAZE_SIZE # type: ignore
# initial pos and orient of robot
robot_position = [2, 3]  # [row, column]
robot_orientation = 'up'


def move_forward(robot_position, robot_orientation):

    #make sure robot is in bounds of maze
    if robot_position[0] <=0 and robot_orientation == 'up':  
        print('no more room this way')        
    elif robot_position[1] <= 0 and robot_orientation == 'left':
        print('no more room this way')
    elif robot_position[0] >=MAZE_SIZE-1 and robot_orientation == 'down':        
        print('no more room this way')
    elif robot_position[1] >= MAZE_SIZE-1 and robot_orientation == 'right':
        print('no more room this way')
        
    # orientation specific movement
    elif robot_orientation == 'up':
        #updates row by moving robot toward 0th row
        robot_position[0]=robot_position[0]-1
        print(robot_position) 
    elif robot_orientation == 'down':
        #updates row by moving toward highest row
        robot_position[0]=robot_position[0]+1  
    elif robot_orientation == 'left':
        #updates column by moving toward 0th column
        robot_position[1]=robot_position[1]-1    
    elif robot_orientation =='right':
        #updates column by moving toward highest column
        robot_position[1]=robot_position[1]+1
        
    return robot_position

def move_backward(robot_position, robot_orientation):
    #make sure robot is in bounds of maze
    if robot_position[0] <=0 and robot_orientation == 'down':  
        print('no more room this way')        
    elif robot_position[1] <= 0 and robot_orientation == 'right':
        print('no more room this way')
    elif robot_position[0] >=MAZE_SIZE-1 and robot_orientation == 'up':        
        print('no more room this way')
    elif robot_position[1] >= MAZE_SIZE-1 and robot_orientation == 'left':
        print('no more room this way')
        
    # orientation specific movement
    elif robot_orientation == 'down':
        #updates row by moving robot toward 0th row
        robot_position[0]=robot_position[0]-1
        print(robot_position)
    elif robot_orientation == 'up':
        #updates row by moving toward highest row
        robot_position[0]=robot_position[0]+1
    elif robot_orientation == 'right':
        #updates column by moving toward 0th column
        robot_position[1]=robot_position[1]-1   
    elif robot_orientation =='left':
        #updates column by moving toward highest column
        robot_position[1]=robot_position[1]+1
        
    return robot_position    


def turn_left(robot_orientation):
    # turns robot left of where it was oriented previously
    if robot_orientation == 'up':
        robot_orientation = 'left'
    elif robot_orientation == 'down':
        robot_orientation = 'right'
    elif robot_orientation == 'left':
        robot_orientation = 'down'
    elif robot_orientation == 'right':
        robot_orientation = 'up'
    return robot_orientation

def turn_right(robot_orientation):
    # turns robot right of where it was oriented previously
    if robot_orientation == 'up':
        robot_orientation = 'right'
    elif robot_orientation == 'down':
        robot_orientation = 'left'
    elif robot_orientation == 'left':
        robot_orientation = 'up'
    elif robot_orientation == 'right':
        robot_orientation = 'down'
    return robot_orientation

