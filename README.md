life.py
=======

Python based life simulation through cellular automata.

This life simulation will be contained within two classes: the world and the cells

World:
  keep track of all living cells
  keep track of environmental state
  at each iteration:
    print matrix
    presents each cell with the observations
    cells return intentions
    world resolves conflicts and determines new observations
  Features:
    Each object in the environment has an update method.
    Some objects could have large sets of information,
      such as a particular chemicals concentration at any point.
  Methods:
    get_neighbors(cell_ID, radius)
      For a particular cell, returns a list of the cell's observed objects.
  Matrix for the world -- use hashtable instead
  40x40 matrix
  e.g
    ________
    ____E___
    __C___C_
    E_______
    
    where E is energy and C is a cell


pass to cell:
  ___
  __E
  ___
 where underscore is empty and E is energy

Cell

  int energyValue;
  setSurroundings(Matrix surroundings)
    genetic algorithm (eventually) that will process the surroundings and return an intent
    e.g. 
    if(seeEnergy())
      go in direction of energy
    else
      go forward
    return direction 
    123
    456
    789
      
  private - checkReproduce()
    check energy levels against reproduction requirements
    reproduce() -- uses energy -- returns genetic code to the world object
    
    
    
