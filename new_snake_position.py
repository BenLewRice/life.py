##
##### V1: Returns the position number of the energy closest to 9 ###
##
##def new_snake_position(neighbors_matrix):
##    position_matrix = [[1,2,3],[4,5,6],[7,8,9]]
##    new_position = 5                            #default movement
##    for i in range(0,3):                        #parse through rows
##        for j in range(0,3):                    #parse through columns
##            if neighbors_matrix[i][j] == 'E':   #check for energy
##                new_position = int(position_matrix[i][j])
##    return(new_position)
##
##

### V2: Creates a list of all energy positions and returns one randomly ###

from random import choice, randrange

def new_snake_position(neighbors_matrix):
    position_matrix = [[1,2,3],[4,5,6],[7,8,9]]
    new_position = randrange(1,10)              #random direction if no E present
    energy_positions = []
    for i in range(0,3):                        #parse through rows
        for j in range(0,3):                    #parse through columns
            if neighbors_matrix[i][j] == 'E':   #check for energy
                energy_positions.append(int(position_matrix[i][j]))
    if len(energy_positions)>=1:
        new_position = choice(energy_positions)
    return(new_position)
