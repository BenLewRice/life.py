life.py
=======

Python based life simulation through cellular automata.

This life simulation will be contained within two classes: the world and the cells

World:
  keep track of all living cells
  keep track of environmental state
  at each iteration:
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
