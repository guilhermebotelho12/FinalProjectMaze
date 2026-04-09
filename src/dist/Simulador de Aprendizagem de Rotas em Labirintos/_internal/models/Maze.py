import random
from typing import Union
from collections import deque
from utils.log_exception import log_exception
class Maze:
    # Class constructor
    def __init__(self) -> None:
        # Class attributes
        self.grid:list[list['Cell']] = None
        self.rows:int = 0
        self.cols:int = 0
        self.start_cell:'Cell' = None
        self.end_cells:list = []
        self.current_cell:'Cell' = None
        self.stack:list = []
        self.queue:deque = deque()
        self.paths:list = []
        self.solutions:list = []

    # Grid attribute getter and setter methods
    def get_grid(self) -> list[list]:
        return self.grid
    def set_grid(self,grid:list[list]) -> None:
        self.grid = grid
    
    # Rows attribute getter and setter methods
    def get_rows(self) -> int:
        return self.rows
    def set_rows(self,rows:int) -> None:
        self.rows = rows
        
    # Cols attribute getter and setter methods
    def get_cols(self) -> int:
        return self.cols
    def set_cols(self,cols:int) -> None:
        self.cols = cols
    
    # start_cell attribute getter and setter methods
    def get_start_cell(self) -> 'Cell':
        return self.start_cell
    def set_start_cell(self,cell:'Cell') -> None:
        self.start_cell = cell
    
    # end_cell attribute getter, setter and other methods
    def get_end_cells(self) -> 'Cell':
        return self.end_cells
    def set_end_cells(self,list:list) -> None:
        self.end_cells = list
    
    def add_end_cells(self,cell:'Cell')-> None:
        self.end_cells.append(cell)
    
    # current_cell attribute getter and setter methods
    def get_current_cell(self)-> 'Cell':
        return self.current_cell
    def set_current_cell(self,cell:'Cell')->None:
        self.current_cell = cell
        
    # paths attribute getter, setter and other methods
    def get_paths(self)->list:
        return self.paths
    def set_paths(self,list:list)->None:
        self.paths = list
        
    def add_paths(self,list:list)->None:
        self.paths.append(list)
    
    # Method that will search on the paths list one path that is last element is the cell passed as parameter and then add to that path the element passed also on parameters
    def add_element_path(self,cell:'Cell',element:'Cell')->None:
        try:
            paths:list[list] = self.get_paths()
            for path in paths:
                if path[-1] == cell:
                    path.append(element)
        except TypeError as e: # self.get_paths() may return None which will raise a type exception
            log_exception(e)
        except Exception as e:
            log_exception(e)

    # Method that replicates a given path a certain number of times
    def add_copy_path(self,cell:'Cell',element:'Cell')->None:
        try:
            paths = self.get_paths()
            for path in paths:
                if path[-2] == cell:
                    temp_path:list = path[0:-1]
                    temp_path.append(element)
                    self.add_paths(temp_path)
                    break
        except TypeError as e:
            log_exception(e)
        except Exception as e:
            log_exception(e)
        
    def append_paths(self,index:int,cell:'Cell') -> None:
        self.paths[index].append(cell)
        
    # stack attribute getter, setter and other methods
    def get_stack(self)->list:
        return self.stack
    def set_stack(self,list:list)->None:
        self.stack = list
        
    def add_stack(self,cell:'Cell')->None:
        self.stack.append(cell)
        
    def pop_stack(self)->'Cell':
        return self.stack.pop()
    
    def remove_stack(self,element:'Cell')-> None:
        self.stack.remove(element)
    
    # queue attribute getter, setter and other methods
    def get_queue(self)->deque:
        return self.queue
    
    def set_queue(self,queue:deque)->None:
        self.queue = queue
        
    def add_queue(self,cell:'Cell')->None:
        self.queue.append(cell)
    
    def remove_queue(self)->'Cell':
        return self.get_queue().popleft()
    
    # solution attribute getter, setter and other methods
    def get_solutions(self) -> list:
        return self.solutions
    def set_solutions(self,solution:list) -> list:
        self.solutions = solution
        
    def add_solutions(self,list:list) -> None:
        self.solutions.append(list)
    
    # Method that will define the last cells
    def set_final_cells(self) -> None:
        try:
            # If the maze is greater than or equal to 15x15 then we can have zero, one or two final squares, if it is smaller we have zero or one final square
            number: int = random.randint(0, 2) if self.get_cols() * self.get_rows() >= 225 else random.randint(0, 1)
            # Assign a random final house in the 4th quadrant of the maze
            if number == 1: 
                self.add_end_cells(self.get_grid()[random.randint(self.get_rows()//2, self.get_rows()-1)][random.randint(self.get_cols()//2,self.get_cols()-1)])
            # If the maze is going to have more than one final square then we have to ensure that it does not land on exactly the same square
            # To do this, we define the first one and then check if the random numbers you gave us for the first one are not the same in the second one
            elif number == 2:
                start_end_1:int = random.randint(self.get_rows()//2, self.get_rows()-1)
                final_end_1:int = random.randint(self.get_cols()//2,self.get_cols()-1)
                self.add_end_cells(self.get_grid()[start_end_1][final_end_1]) # 1ª End_cell
                start_end_2:int = random.randint(self.get_rows()//2, self.get_rows()-1)
                final_end_2:int = random.randint(self.get_cols()//2,self.get_cols()-1)
                while start_end_1 == start_end_2 and final_end_1 == final_end_2: # Only enter if the cell is the same
                    start_end_2 = random.randint(self.get_rows()//2, self.get_rows()-1)
                    final_end_2 = random.randint(self.get_cols()//2,self.get_cols()-1)
                self.add_end_cells(self.get_grid()[start_end_2][final_end_2]) # 2ª end_cell
        except Exception as e: # We may have maze boundary exceptions
            log_exception(e)
    
    # Method that resets all variables used in the breadth search method
    def clear_breadth_variables(self) -> None:
        try:
            self.set_current_cell(None)
            self.set_queue(deque())
            self.set_paths([])
        except Exception as e:
            log_exception(e)
    
    # Method that resets all variables used in the depth and A* search method
    def clear_depth_A_Flood_variables(self) -> None:
        try:
            self.set_current_cell(None)
            self.set_stack([])
            self.set_paths([])
        except Exception as e:
            log_exception(e)
        
    # Method of the Breadth algorithm that aims to save the atual solution
    def save_solution(self) -> None:
        try:
            for path in self.get_paths():
                # If the path contains one of the final cells of the maze and that path has not already been saved in the list of solutions
                if path[-1] in self.get_end_cells() and path not in self.get_solutions(): 
                    # We save a copy of that path using the slicing technique
                    self.add_solutions(path[:])              
                    break    
        except Exception as e:
            log_exception(e)   

            
        