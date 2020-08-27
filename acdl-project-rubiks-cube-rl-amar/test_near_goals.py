from cube import Cube
import utils

def makeNearGoal():
    cube = Cube()
    cube.set_up([['W','W','W'],['W','W','W'],['W','W','W']])
    cube.set_down([['B','B','B'],['B','B','B'],['B','B','B']])
    cube.set_left([['O','O','O'],['G','G','G'],['G','G','G']])
    cube.set_right([['G','G','G'],['O','O','O'],['O','O','O']])
    cube.set_front([['R','R','R'],['Y','Y','Y'],['Y','Y','Y']])
    cube.set_back([['Y','Y','Y'],['R','R','R'],['R','R','R']])

    solved_cube = cube.copy();
    print("Initial state of the cube : ", solved_cube)

    for action in cube.actions:
        solved_cube = utils.perform_action(cube, action)
        print(action)
        if solved_cube.is_goal_state_reached():
            print("executing the " + action + " action resulted in the below goal state " + str(solved_cube))
            print(solved_cube.is_goal_state_reached())

    print("\nFinal state of the Cube : ", solved_cube)

#print(cube_perform_action(cube, 'top'))

makeNearGoal()