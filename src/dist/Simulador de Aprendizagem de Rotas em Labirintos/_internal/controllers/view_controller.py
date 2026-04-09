import os
import random
import threading
import time
import pygame
import pygame_gui.ui_manager
from typing import Union
from controllers.cell_controller import CellController
from controllers.maze_controller import MazeController
from controllers.picker_view_controller import PickerViewController
from utils.log_exception import log_exception

class ViewController:
    # ViewController class constructor
    def __init__(self) -> None:
        self.maze_controller:MazeController = MazeController() # Maze controller     
        self.cell_controller:CellController = CellController() # Cell controller  
        self.stop_handle_algorithms:threading.Event = threading.Event()
        self.handle_algorithms_thread:threading.Thread = None
    
    # Method that returns the starting cell
    def get_start_cell(self) -> 'Cell':
        return self.maze_controller.get_start_cell()
        
    # Method that returns the ending cells
    def get_end_cells(self) -> list['Cell']:
        return self.maze_controller.get_end_cells()
    
    # Method that, in connection with the Cell class controller, returns the value of the "x" attribute of the same
    def get_x_cell(self,cell:'Cell') -> int:
        return self.cell_controller.get_x(cell)
    
    # Method that, in connection with the Cell class controller, returns the value of the "y" attribute of the same
    def get_y_cell(self,cell:'Cell') -> int:
        return self.cell_controller.get_y(cell)
    
    # Method that, in connection with the Cell class controller, returns the value of the "size" attribute of the same
    def get_size_cell(self,cell:'Cell') -> int:
        return self.cell_controller.get_size(cell)
    
    # Method that, in connection with the Cell class controller, returns one value of the "walls" attribute of the same
    def get_wall(self,cell:'Cell',direction:str) -> str:
        return self.cell_controller.get_wall(cell,direction)
    
    # Check input rows and columns
    def check_inputs(self,rows:str,columns:str,width:int,height:int):
        try:
            # Min columns and min rows = 7
            if int(columns) < 7 or int(rows) < 7:
                return ("Min columns:7","Min rows:7")
            else:
                #valid max columns = width - right elements - left and right margins  || valid max height = height - top margin - bottom margin - taskbar_height
                return () if int(columns)<=(width - 370 - 40) // 20 and int(rows)<=(height - 20 - 40 - 80) // 20 else (f"Max Columns:{(width - 370 - 40) // 20}",f"Max rows:{(height - 20 - 40 - 80) // 20}")
        except ValueError:
            return ("Write only integers","Write only integers")
        except Exception as e:
            log_exception(e)
            
    # Method that aims to call the function in the color_picker window controller that opens it
    def open_color_picker(self,screen:pygame.display,ui_manager:pygame_gui.ui_manager,current_color:pygame.color) -> pygame.color:
        self.picker_color_controller:PickerViewController = PickerViewController()
        return self.picker_color_controller.open_color_picker(screen,ui_manager,current_color)
    
    # Method that contacts the maze controller to tell it to generate the maze
    def generate_maze(self,rows:int,cols:int) -> list[list['Cell']]: 
        self.maze_controller.set_grid(rows,cols) # Method that creates the grid
        self.grid_maze:list[list['Cell']] = self.maze_controller.generate_maze() # Method that creates the maze in the grid created above
        return self.grid_maze
    
    # Method that allows you to save the current maze in png format
    def save_maze(self,screen:pygame.display) -> None:
        try:
            pygame.display.flip()
            # We create a surface that represents the area to capture
            size:tuple = self.maze_controller.get_px_size_maze() # Get the size of the maze with margins
            capture_surface:pygame.Surface = pygame.Surface(size)
            # Capture the screen area, excluding the button part
            capture_surface.blit(screen, (0, 0), pygame.Rect(0, 0, size[0], size[1]))
            # Get the path of the user's "Images" folder
            folder_images:str = os.path.join(os.path.expanduser('~'), 'Pictures')
            # Save the image of the captured area
            pygame.image.save(capture_surface,os.path.join(folder_images, self.maze_controller.get_save_name_maze()))
            # Wait for the image to be saved
            pygame.time.delay(500)
        except Exception as e:
            log_exception(e)
    
    # Method to obtain a different color from the background and walls of the maze
    def get_different_color(self,color1: pygame.Color, color2: pygame.Color, color3: pygame.Color, color4: pygame.Color) -> pygame.Color:
        try:
            while True:
                new_color:pygame.color = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                # Check if the new color is sufficiently different from color1
                if all(abs(new_color[i] - color1[i]) > 50 for i in range(3)):
                    # Check if the new color is sufficiently different from color2
                    if all(abs(new_color[i] - color2[i]) > 50 for i in range(3)):
                        # Check if the new color is sufficiently different from color3
                        if all(abs(new_color[i] - color3[i]) > 50 for i in range(3)):
                            # Check if the new color is sufficiently different from color4
                            if all(abs(new_color[i] - color4[i]) > 50 for i in range(3)):
                                return new_color
        except Exception as e:
            log_exception(e)
    
    # Method whose objective is to use a specific algorithm to solve the maze
    def solve_maze(self,view:'view') -> None:
        try:
            cols:int = self.maze_controller.get_cols()
            rows:int = self.maze_controller.get_rows()
            
            # Choose which algorithm use depending the size of the maze created
            if cols <=10 and rows <= 10:
                self.start_handle_algorithms(view,self.first_fase_breadth,self.second_fase_breadth,self.delete_breadth,"Breadth Algorithm")
            elif cols <= 15 and rows <= 15:
                self.start_handle_algorithms(view,self.first_fase_depth,self.second_fase_depth,self.delete_depth_A,"Depth Algorithm")
            else:
                self.start_handle_algorithms(view,self.first_fase_A,self.second_fase_A,self.delete_depth_A,"A* Algorithm")
                
        except AttributeError as e:
            log_exception(e)
            return
        except Exception as e:
            log_exception(e)
            return    
    
    # Method that initializes or resets the thread responsible for running the algorithms
    def start_handle_algorithms(self,view:'view', first_phase_method:callable, second_phase_method:callable,delete_method:callable, algorithm_name:str) -> None:
        try:
            # Check if the secondary thread is not already running
            if self.handle_algorithms_thread and self.handle_algorithms_thread.is_alive(): # If the thread is running
                self.stop_handle_algorithms.set() # This variable is like a "flag" that will tell the method in the thread to stop
                self.handle_algorithms_thread.join() # Command to wait until the previous thread finishes
        except Exception as e:
            self.stop_visual_part()
            view.clear_screen()
            log_exception(e)
        else:
            # In the code below, we clear the "flag" variable and start or reset the thread that will handle the algorithm and then start it
            self.stop_handle_algorithms.clear()
            self.handle_algorithms_thread = threading.Thread(target=self.handle_algorithms,args=(view, first_phase_method, second_phase_method,delete_method, algorithm_name))
            self.handle_algorithms_thread.start()

    # Method that we use to iterate in Breadth and Depth algorithms
    def handle_algorithms(self,view:'view', first_phase_method:callable, second_phase_method:callable,delete_method:callable, algorithm_name:str) -> None:
        try:
            # Clear and draw the main screen
            view.clear_screen()
            view.draw_maze()

            counter:int = 0 # Count the iterations until reaching the final solution or solutions
            
            # Controller method that returns a color different from the 4 that we passed as a parameter, and this will be the color in which we will draw the solution/s
            solution_color:pygame.color = self.get_different_color(view.current_color_bg,view.current_color_wls,pygame.Color("green"),pygame.Color("red"))
            
            start:float = time.time()
            first_phase_method()
            running:bool = True
                    
            # Cycle that we will iterate until the "second_fase" method returns a list of possible solutions in this maze with this algorithm
            while running:
                # Stops the algorithm cycle and resets the used variables
                if self.stop_handle_algorithms.is_set():
                    delete_method()
                    break
                
                # Execute the second phase of the algorithm passed
                return_value:Union['Cell',list,None] = second_phase_method()
                
                if isinstance(return_value, list):   # The returned value is the list of solutions
                    generate_algorithm_time:int = abs(round(time.time() - start - (counter*0.100), 4)) # end - start - times that we use the delay time
                    #generate_algorithm_time:int = abs(round(time.time() - start, 4)) # end - start - times that we use the delay time
                    view.clear_screen()
                    view.draw_maze()
                    view.draw_labels(f"{algorithm_name} time: {generate_algorithm_time}", pygame.font.SysFont("Arial",15),view.color_black,20,self.maze_controller.get_px_size_maze()[1]-40) # Draw timer
                    view.draw_labels(f"Cells explored: {counter + len(return_value) + 1}", pygame.font.SysFont("Arial",15),view.color_black,20,self.maze_controller.get_px_size_maze()[1]-20)
                    # Draw the returned solutions
                    for solution in return_value: 
                        for cell in solution[1:-1]:
                            view.draw_solution(cell, view.current_color_bg, view.current_color_wls, solution_color)
                    running = False
                    
                    # Draw again the Start and End cells because the solutions we return may have to go through a final cell to reach the second
                    view.draw_cell(self.maze_controller.get_start_cell(),"green",view.current_color_wls)  
                    for cell in self.get_end_cells():
                        view.draw_cell(cell,"red",view.current_color_wls)
                    pygame.display.update()
                elif return_value is None:   # The returned value is one of the end cells or a death end, so the method returned None
                    continue       
                else:   # The returned value is a cell
                    # Draw the returned cell, which is the cell that was explored, and give the program a delay of 100 milliseconds so that it is clear to the user how the algorithm is exploring
                    view.draw_solution(return_value, view.current_color_bg, view.current_color_wls, solution_color)
                    counter+=1
                    pygame.time.delay(100)
        except Exception as e:
            self.stop_visual_part()
            view.clear_screen()
            log_exception(e)
        
    # Methods for the Breadth algorithm
    def first_fase_breadth(self) -> None:
        self.maze_controller.first_fase_breadth()
    
    def second_fase_breadth(self) -> Union['Cell',list,None]:
        return self.maze_controller.second_fase_breadth()
    
    def delete_breadth(self) -> None:
        self.maze_controller.delete_breadth()
    
    # Methods for the Depth algorithm
    def first_fase_depth(self) -> None:
        self.maze_controller.first_fase_depth()
    
    def second_fase_depth(self) -> Union['Cell',list,None]:
        return self.maze_controller.second_fase_depth()

    def delete_depth_A(self) -> None:
        self.maze_controller.delete_depth_A()
    
    # Methods for the A* algorithm
    def first_fase_A(self) -> None:
        self.maze_controller.first_fase_A()
    
    def second_fase_A(self) -> Union['Cell',list,None]:
        return self.maze_controller.second_fase_A()
    
    # Methods for the Flood Fill algorithm
    def first_fase_flood(self) -> None:
        self.maze_controller.first_fase_flood()
    
    def second_fase_flood(self) -> Union['Cell',list,None]:
        return self.maze_controller.second_fase_flood()
    
    def delete_flood(self) -> None:
        self.maze_controller.delete_flood()
    
    # Method that stops the visual part of the program before closing the program
    def stop_visual_part(self) -> None:
        try:
            if self.handle_algorithms_thread and self.handle_algorithms_thread.is_alive():
                self.stop_handle_algorithms.set()
                self.handle_algorithms_thread.join()
        except Exception as e:
            log_exception(e)
    