from models.Cell import Cell
from utils.log_exception import log_exception
class CellController:
    # Constructor of the CellController class
    def __init__(self) -> None:
        pass

    # Method that allows the creation of a new cell
    def create_cell(self,x:int,y:int) -> Cell:
        try:
            return Cell(x, y)
        except Exception as e:
            log_exception(e)
            return None  
    
    # Method that returns the value of the x attribute of the cell passed as a parameter
    def get_x(self,cell:Cell) -> int:
        return cell.get_x()
    
    # Method that returns the value of the y attribute of the cell passed as a parameter
    def get_y(self,cell:Cell) -> int:
        return cell.get_y()
    
    # Method that returns the value of the size attribute of the cell passed as a parameter
    def get_size(self,cell:Cell) -> int:
        return cell.get_size()
    
    # Method that returns a value of the walls attribute of the cell passed as a parameter
    def get_wall(self,cell:Cell,direction:str) -> str:
        return cell.get_wall(direction)
    
    # Method that makes use of the method named "remove_walls" of the Cell class, which aims to remove certain stops by checking the current cell and the next
    def remove_walls(self,cell:Cell, next:'Cell') -> None:
        cell.remove_walls(next)
        
    # Methods that make use of the get and set methods of the visited attribute of the passed cell
    def get_visited(self,cell:Cell) -> bool:
        return cell.get_visited()   
    def set_visited(self,cell:Cell,visited:bool) -> None:
        cell.set_visited(visited)
        
    # Methods that make use of the get and set methods of the cost attribute of the passed cell
    def get_cost(self,cell:Cell) -> int:
        return cell.get_cost()
    def set_cost(self,cell:Cell,value:int) -> None:
        cell.set_cost(value)
        
    # Method that find the neighbors if they exist around the cell
    def find_neighbors(self,check_cell_method:callable,cell:'Cell') -> list['Cell']:
        try:
            # Check the top neighbor
            top:'Cell' = check_cell_method(cell.get_x(), cell.get_y()-1)
            # Check the right neighbor
            right:'Cell' = check_cell_method(cell.get_x() + 1, cell.get_y())
            # Check the bottom neighbor
            bottom:'Cell' = check_cell_method(cell.get_x(), cell.get_y() + 1)
            # Check the left neighbor
            left:'Cell' = check_cell_method(cell.get_x() - 1, cell.get_y())
            return (top,right,bottom,left)
        except Exception as e: # We mainly use this block because of the check_cell_method, as all the methods depend on it.
            log_exception(e)
        
    # Method that sees which neighbors are available and chooses one to follow
    def check_neighbors_generate_maze(self,check_cell_method:callable,cell:'Cell') -> list['Cell']:
        try:
            neighbors:list['Cell'] = []
            # Neighbors
            top,right,bottom,left = self.find_neighbors(check_cell_method,cell)

            # If there is a cell on top/right/bottom/left of the current cell, and that cell(top/right/bottom/left) it's not visited 
            # gets added to the list.
            if top and not top.get_visited():
                neighbors.append(top)
            if right and not right.get_visited():
                neighbors.append(right)
            if bottom and not bottom.get_visited(): 
                neighbors.append(bottom)
            if left and not left.get_visited(): 
                neighbors.append(left)
            return neighbors
        except Exception as e:
            log_exception(e)
    
    # Method that sees which neighbors are available and chooses one to follow
    def check_neighbors_algorithms(self,check_cell_method:callable,cell:'Cell') -> list['Cell']:
        try:
            neighbors:list['Cell'] = []
            top,right,bottom,left = self.find_neighbors(check_cell_method,cell) # Neighbors
            # If there is a cell on top/right/bottom/left of the current cell, and that cell(top/right/bottom/left) it's not visited 
            # gets added to the list.
            if top and not top.get_visited() and not top.get_wall("bottom"):
                neighbors.append(top)
            if right and not right.get_visited() and not right.get_wall("left"):
                neighbors.append(right)
            if bottom and not bottom.get_visited() and not bottom.get_wall("top"): 
                neighbors.append(bottom)
            if left and not left.get_visited() and not left.get_wall("right"): 
                neighbors.append(left)
            return neighbors
        except Exception as e:
            log_exception(e)
            
            
    