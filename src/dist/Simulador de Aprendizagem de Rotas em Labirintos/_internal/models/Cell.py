from typing import Union
from utils.log_exception import log_exception
class Cell:
    # Class constructor
    def __init__(self,x,y) -> None:
        # Class attributes
        self.x:int = x 
        self.y:int = y 
        self.size:int = 20 
        self.walls:dict = {"top": True, "right": True, "bottom": True, "left": True} 
        self.visited:bool = False 
        self.cost:int = 0

    # x attribute getter and setter methods
    def get_x(self) -> int:
        return self.x
    def set_x(self,x:int) -> None:
        self.x = x

    # y attribute getter and setter methods
    def get_y(self) -> int:
        return self.y
    def set_y(self,y:int) -> None:
        self.y = y
    
    # size attribute getter and setter methods
    def get_size(self) -> int:
        return self.size
    def set_size(self,size:int) -> None:
        self.size = size
    
    # walls attribute getter and setter methods
    def get_wall(self,direction:str) -> str:
        return self.walls[direction]
    def set_wall(self,direction:str,value:bool) -> None:
        self.walls[direction] = value
    
    # visited attribute getter and setter methods
    def get_visited(self) -> bool:
        return self.visited
    def set_visited(self,visited:bool) -> None:
        self.visited = visited
        
    # cost attribute getter and setter methods
    def get_cost(self) -> int:
        return self.cost
    def set_cost(self,value:int) -> None:
        self.cost = value
    
    # Method that remove the walls from the cells
    def remove_walls(self, next:'Cell') -> None:
        try:
            # Calculate the difference in x coordinates between the current cell and the next cell
            dx:int = self.x - next.x
            # If the difference is 1 (indicating next cell is to the left of current cell)
            if dx == 1:
                self.set_wall('left',False) # In the current cell removes the left wall 
                next.set_wall('right',False) # In the next cell removes the right wall 
            # If the difference is -1 (indicating next cell is to the right of current cell)
            elif dx == -1:
                self.set_wall('right',False) # In the current cell removes the right wall 
                next.set_wall('left',False) # In the next cell removes the left wall 
            # Calculate the difference in y coordinates between the current cell and the next cell
            dy:int = self.y - next.y
            # If the difference is 1 (indicating next cell is above the current cell)
            if dy == 1:
                self.set_wall('top',False) # In the current cell removes the top wall 
                next.set_wall('bottom',False) # In the next cell removes the bottom wall 
            # If the difference is -1 (indicating next cell is below the current cell)
            elif dy == -1:
                self.set_wall('bottom',False) # In the current cell removes the bottom wall 
                next.set_wall('top',False) # In the next cell removes the top wall 
        except Exception as e:
            log_exception(e)
            
   