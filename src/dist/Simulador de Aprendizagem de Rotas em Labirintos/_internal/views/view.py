import os
import platform
import time
import pygame
import pygame_gui
import pygame_gui.ui_manager
from pygame_widgets.button import Button
from pygame_widgets.textbox import TextBox
from controllers.view_controller import ViewController
from utils.log_exception import log_exception

class View:
    # Class constructor
    def __init__(self) -> None:
        try:
            self.view_controller:ViewController = ViewController()
            
            # Variables for timers
            self.generate_maze_time:float = 0.0
            self.generate_algorithm_time:float = 0.0
            
            # Get the size of the main monitor
            screen_info:pygame.display = pygame.display.Info()
            self.screen_width:int = screen_info.current_w # Screen width
            self.screen_height:int = screen_info.current_h # Screen height
                
            # Set the screen to fullscreen with the obtained resolution
            self.screen:pygame.display = pygame.display.set_mode((self.screen_width, self.screen_height-55))
            self.ui_manager:pygame_gui.ui_manager = pygame_gui.UIManager((self.screen_width, self.screen_height-55))
            self.screen.fill((255, 255, 255))
            pygame.display.set_caption("Maze Simulator")
            # Define the icon for the window
            pygame.display.set_icon(pygame.image.load(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "images", "icon.png")))

            # Draw the elements in the view
            os_name = platform.system()
            if os_name == "Darwin":
                self.text_font:pygame.font= pygame.font.SysFont("Arial",17) # Source of texts
            elif os_name == "Windows":
                self.text_font:pygame.font= pygame.font.SysFont("Arial",20) # Source of texts
            self.title_font:pygame.font = pygame.font.SysFont("Arial Black",30) # Source of titles
            self.color_black:tuple=(0, 0, 0) # Color use in texts
            
            # Draw title in view (title, font, color, x, y)
            self.draw_labels("Create Maze", self.title_font,self.color_black,self.screen_width-286.5,17)
            # Draw text in view
            self.draw_labels("Number of columns :", self.text_font,self.color_black,self.screen_width-370,75)
            # Draw textbox to insert the desired number of columns (screen, x, y, text width, text height, font size, border color, text color)        
            self.txtNumbCols:TextBox = TextBox(self.screen, self.screen_width-212, 70, 200, 35, fontSize=20, borderColour=(255, 0, 0), textColour=(0, 0, 0))
            # Draw text in view
            self.draw_labels("Number of rows :", self.text_font,self.color_black,self.screen_width-343,120)
            # Draw textbox to insert the desired number of lines
            self.txtNumbRowss:TextBox = TextBox(self.screen, self.screen_width-212, 115, 200, 35, fontSize=20, borderColour=(255, 0, 0), textColour=(0, 0, 0))
            
            # Draw text in view
            self.draw_labels("Walls color :", self.text_font,self.color_black,self.screen_width-306,170)
            # Below we have initialized the initial colors of both the background and the walls of the maze, and we also have an explanation of the button parameters
            # The rectangles serve to show the user which color is chosen in the picker and which will be used to create the maze
            self.current_color_wls:pygame.color = pygame.Color(255,140,0)
            # (screen where the button will be drawn, button x position, button y position, button width, button height, button radius, button text, text font size,
            # margin around text, button color when inactive, button color when mouse hovers over, button color when clicked, function to be called when button is clicked, button background image) 
            pickColor_img:pygame.image = pygame.image.load(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "images", "pickColor.png")).convert()
            self.pick_color_btn_wls = Button(self.screen, self.screen_width-192, 165, 100, 35, radius=0, onClick=self.pick_color_btn_wls_click, image=pygame.transform.scale(pickColor_img,(100,35)))
            self.rect_wls:pygame.rect = pygame.draw.rect(self.screen, self.current_color_wls, (self.screen_width-57, 165, 35, 35))
            # Draw text in view
            self.draw_labels("Background color :", self.text_font,self.color_black,self.screen_width-353,220)
            self.current_color_bg:pygame.color = pygame.Color(0,0,0)
            self.pick_color_btn_bg = Button(self.screen, self.screen_width-192, 215, 100, 35, radius=0, onClick=self.pick_color_btn_bg_click, image=pygame.transform.scale(pickColor_img,(100,35)))
            self.rect_bg:pygame.rect = pygame.draw.rect(self.screen, self.current_color_bg, (self.screen_width-57, 215, 35, 35))
            
            # Design of the 4 main simulator buttons (Create, Solve, Clear, Save)
            # The background of each button will be an image created by us
            create_Btn_img:pygame.image = pygame.image.load(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "images", "botaocreate.png")).convert()
            self.createBtn = Button(self.screen, self.screen_width-370, 285, 175, 60, radius=0, onClick=self.create_btn_click, image=pygame.transform.scale(create_Btn_img,(175,60)))
            
            solve_Btn_img:pygame.image = pygame.image.load(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "images", "botaosolve.png")).convert()   
            self.solveBtn = Button(self.screen, self.screen_width-185, 285, 175, 60, radius=0, onClick=self.solve_btn_click, image=pygame.transform.scale(solve_Btn_img,(175,60)))
            
            clear_Btn_img:pygame.image = pygame.image.load(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "images", "botaoclear.png")).convert()   
            self.clearBtn = Button(self.screen, self.screen_width-370, 365, 175, 60, radius=0, onClick=self.clear_btn_click, image=pygame.transform.scale(clear_Btn_img,(175,60)))
            
            save_Btn_img:pygame.image = pygame.image.load(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "images", "botaosave.png")).convert()   
            self.saveBtn = Button(self.screen, self.screen_width-185, 365, 175, 60, radius=0, onClick=self.save_btn_click, image=pygame.transform.scale(save_Btn_img,(175,60)))
            
            # Draw text in view
            self.draw_labels("Options", self.title_font,self.color_black,self.screen_width-248,455)
            # Design of the 4 secondary buttons whose objectives are to let the user choose which algorithm they want to solve the maze with
            # Each button is named after the function that can be used for resolution (Flood Fill, Breadth, Depth, A*) 
            fsBtn:pygame.image = pygame.image.load(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "images", "floodfillsearch.png")).convert()  
            self.fsearchBtn:Button = Button(self.screen, self.screen_width-370, 508, 175, 60, radius=50, onClick=self.fsearchBtn_click, image=pygame.transform.scale(fsBtn,(175,60)))

            brBtn:pygame.image = pygame.image.load(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "images", "breadthSearch.png")).convert()  
            self.breadthBtn:Button = Button(self.screen, self.screen_width-185, 508, 175, 60, radius=50, onClick=self.breadthBtn_click, image=pygame.transform.scale(brBtn,(175,60)))

            daBtn:pygame.image = pygame.image.load(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "images", "depthSearch.png")).convert()  
            self.depthBtn:Button = Button(self.screen, self.screen_width-370, 588, 175, 60, radius=50, onClick=self.depthBtn_click, image=pygame.transform.scale(daBtn,(175,60)))

            asBtn:pygame.image = pygame.image.load(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "images", "ASearch.png")).convert()  
            self.asearchBtn:Button = Button(self.screen, self.screen_width-185, 588, 175, 60, radius=50, onClick=self.asearchBtn_click, image=pygame.transform.scale(asBtn,(175,60)))
            
            # Enable and Disable certain buttons
            self.pick_color_btn_wls.enable()
            self.pick_color_btn_bg.enable()
            self.createBtn.enable()
            self.solveBtn.disable()
            self.clearBtn.disable()
            self.saveBtn.disable()
            self.fsearchBtn.disable()
            self.breadthBtn.disable()
            self.depthBtn.disable()
            self.asearchBtn.disable()
            
            pygame.display.update()#updates the display
        except pygame.error as e: # can occur, for example, if the drawing coordinates are wrong 
            log_exception(e)
        except Exception as e:
            log_exception(e)
    
    # Method whose function is to draw a certain cell on the screen according to certain restrictions or characteristics
    def draw_cell(self,cell:'Cell', bg_color:pygame.color, wl_color:pygame.color) -> None: 
        try:
            x:int = self.view_controller.get_x_cell(cell) * self.view_controller.get_size_cell(cell) # Stores the x coordinate of the cell on the screen
            y:int = self.view_controller.get_y_cell(cell) * self.view_controller.get_size_cell(cell) # Stores the y coordinate of the cell on the screen
            
            # Drawing the cell on the screen
            pygame.draw.rect(self.screen, pygame.Color(bg_color),(x,y,self.view_controller.get_size_cell(cell), self.view_controller.get_size_cell(cell)))

            # The following code checks which walls the cell is supposed to have by checking the walls attribute 
            # of the respective cell and, if so, draw it on the screen using pygame.draw.line
            if self.view_controller.get_wall(cell,'top'):
                pygame.draw.line(self.screen, pygame.Color(wl_color), (x, y), (x + self.view_controller.get_size_cell(cell), y)) #line(surface, color, start_pos, end_pos)
            if self.view_controller.get_wall(cell,'right'):
                pygame.draw.line(self.screen, pygame.Color(wl_color), (x + self.view_controller.get_size_cell(cell), y), (x + self.view_controller.get_size_cell(cell), y + self.view_controller.get_size_cell(cell)))
            if self.view_controller.get_wall(cell,'bottom'):
                pygame.draw.line(self.screen, pygame.Color(wl_color), (x + self.view_controller.get_size_cell(cell), y + self.view_controller.get_size_cell(cell)), (x , y + self.view_controller.get_size_cell(cell)))
            if self.view_controller.get_wall(cell,'left'):
                pygame.draw.line(self.screen, pygame.Color(wl_color), (x, y + self.view_controller.get_size_cell(cell)), (x, y))
        except pygame.error as e: # can occur, for example, if the drawing coordinates are wrong 
            log_exception(e)
        except TypeError as e: # May occur if the types of parameters passed are of the wrong type
            log_exception(e)
        except Exception as e:
            log_exception(e)
            
    # Method whose function is to draw the solution on the screen
    def draw_solution(self, cell: 'Cell', bg_color: pygame.color, wl_color: pygame.color,solution:pygame.color) -> None:
        try:
            x: int = self.view_controller.get_x_cell(cell) * self.view_controller.get_size_cell(cell) + self.view_controller.get_size_cell(cell) // 2  # Stores the x coordinate of the center of the cell on the screen
            y: int = self.view_controller.get_y_cell(cell) * self.view_controller.get_size_cell(cell) + self.view_controller.get_size_cell(cell) // 2  # Stores the y coordinate of the center of the cell on the screen
            
            # Draw the cell background
            pygame.draw.rect(self.screen, pygame.Color(bg_color), (self.view_controller.get_x_cell(cell) * self.view_controller.get_size_cell(cell), cell.get_y() * self.view_controller.get_size_cell(cell), self.view_controller.get_size_cell(cell), self.view_controller.get_size_cell(cell)))

            # Draw a circle in the middle of the cell
            pygame.draw.circle(self.screen, solution, (x, y), self.view_controller.get_size_cell(cell) // 4)  # circle(surface, color, center, radius)

            # Draw walls if present
            if self.view_controller.get_wall(cell,'top'):
                pygame.draw.line(self.screen, pygame.Color(wl_color), (self.view_controller.get_x_cell(cell) * self.view_controller.get_size_cell(cell), self.view_controller.get_y_cell(cell) * self.view_controller.get_size_cell(cell)), ((self.view_controller.get_x_cell(cell) + 1) * self.view_controller.get_size_cell(cell), self.view_controller.get_y_cell(cell) * self.view_controller.get_size_cell(cell)))
            if self.view_controller.get_wall(cell,'right'):
                pygame.draw.line(self.screen, pygame.Color(wl_color), ((self.view_controller.get_x_cell(cell) + 1) * self.view_controller.get_size_cell(cell), self.view_controller.get_y_cell(cell) * self.view_controller.get_size_cell(cell)), ((self.view_controller.get_x_cell(cell) + 1) * self.view_controller.get_size_cell(cell), (self.view_controller.get_y_cell(cell) + 1) * self.view_controller.get_size_cell(cell)))
            if self.view_controller.get_wall(cell,'bottom'):
                pygame.draw.line(self.screen, pygame.Color(wl_color), ((self.view_controller.get_x_cell(cell) + 1) * self.view_controller.get_size_cell(cell), (self.view_controller.get_y_cell(cell) + 1) * self.view_controller.get_size_cell(cell)), (self.view_controller.get_x_cell(cell) * self.view_controller.get_size_cell(cell), (self.view_controller.get_y_cell(cell) + 1) * self.view_controller.get_size_cell(cell)))
            if self.view_controller.get_wall(cell,'left'):
                pygame.draw.line(self.screen, pygame.Color(wl_color), (self.view_controller.get_x_cell(cell) * self.view_controller.get_size_cell(cell), (self.view_controller.get_y_cell(cell) + 1) * self.view_controller.get_size_cell(cell)), (self.view_controller.get_x_cell(cell) * self.view_controller.get_size_cell(cell), self.view_controller.get_y_cell(cell) * self.view_controller.get_size_cell(cell)))
        except pygame.error as e: # can occur, for example, if the drawing coordinates are wrong 
            log_exception(e)
        except Exception as e:
            log_exception(e)
            
    # The method that aims to draw the entire maze on the screen also uses the "draw_cell" method
    def draw_maze(self) -> None:
        try:
            self.clear_screen()        
            self.draw_labels(f"Maze Generating time: {self.generate_maze_time}", pygame.font.SysFont("Arial",15),self.color_black,20,0)
            for row in self.grid_maze:
                for cell in row:
                    self.draw_cell(cell,self.current_color_bg,self.current_color_wls)
            self.draw_cell(self.view_controller.get_start_cell(),"green",self.current_color_wls)
            for cell in self.view_controller.get_end_cells():
                self.draw_cell(cell,"red",self.current_color_wls)

            pygame.display.update() 
        except pygame.error as e: # can occur, for example, if the drawing coordinates are wrong 
            log_exception(e)
        except Exception as e:
            log_exception(e)
        
    # The method that generate the maze
    def generate_maze(self)->None:
        try:
            start:float = time.time()
            self.grid_maze = self.view_controller.generate_maze(int(self.txtNumbRowss.getText()),int(self.txtNumbCols.getText()))
            self.generate_maze_time = abs(round(time.time() - start, 4))
            self.draw_maze()
        except pygame.error as e: # can occur, for example, if the drawing coordinates are wrong 
            log_exception(e)
        except Exception as e:
            log_exception(e)
            
    # Method that draws all labels on the screen according to certain characteristics and in the locations determined and passed as a parameter
    def draw_labels(self,text:str,font:pygame.font.Font, color, x:int, y:int) -> None:
        try:
            text_surface: pygame.surface = font.render(text, True, color)
            self.screen.blit(text_surface,(x,y))
        except pygame.error as e:
            log_exception(e)
        except TypeError as e:
            log_exception(e)
        except Exception as e:
            log_exception(e)
        
    # Method to clean the screen
    def clear_screen(self) -> None:
        try:
            self.screen.fill((255,255,255),pygame.Rect(0, 0, self.screen_width-370, self.screen_height))
        except TypeError as e:
            log_exception(e)
        except ValueError as e:
            log_exception(e)
        
    # Method called when clicking on the walls picker_color button    
    def pick_color_btn_wls_click(self) -> None:
        try:
            # Open a second window for the user to choose the color they want
            self.current_color_wls:pygame.color = self.view_controller.open_color_picker(self.screen,self.ui_manager,self.current_color_wls)
            self.rect_wls:pygame.rect = pygame.draw.rect(self.screen, self.current_color_wls, (self.screen_width-57, 165, 35, 35))
            self.clear_screen()
        except pygame.error as e:
            log_exception(e)
        except Exception as e:
            log_exception(e)
    
    # Method called when clicking on the background picker_color button
    def pick_color_btn_bg_click(self) -> None:
        try:
            # Open a second window for the user to choose the color they want
            self.current_color_bg:pygame.color = self.view_controller.open_color_picker(self.screen,self.ui_manager,self.current_color_bg)
            self.rect_bg:pygame.rect = pygame.draw.rect(self.screen, self.current_color_bg, (self.screen_width-57, 215, 35, 35))
            self.clear_screen()
        except pygame.error as e:
            log_exception(e)
        except Exception as e:
            log_exception(e)

    # Method called when clicking on the main create button
    def create_btn_click(self) -> None:   
        try:
            # check inputs
            check:tuple = self.view_controller.check_inputs(self.txtNumbRowss.getText(),self.txtNumbCols.getText(),self.screen_width,self.screen_height)
            if len(check)==0:
                # Disable certain buttons and call the method that draws the maze
                self.pick_color_btn_wls.disable()
                self.pick_color_btn_bg.disable()
                self.createBtn.disable()
                self.solveBtn.enable()
                self.clearBtn.enable()
                self.saveBtn.disable()
                self.fsearchBtn.enable()
                self.breadthBtn.enable()
                self.depthBtn.enable()
                self.asearchBtn.enable()
                
                self.generate_maze()
            else:
                self.txtNumbCols.setText(check[0])
                self.txtNumbRowss.setText(check[1])
        except ValueError as e:
            log_exception(e)
        except Exception as e:
            log_exception(e)
    
    # Method called when clicking on the main solve button
    def solve_btn_click(self) -> None:
        try:
            # Disable and enable certain buttons
            self.ena_dis_buttons()
            self.view_controller.solve_maze(self)
        except Exception as e:
            log_exception(e)
    
    # Method called when the main clear button is clicked
    def clear_btn_click(self) -> None:
        try:
            # Disable certain buttons and call the method that clears the maze
            self.pick_color_btn_wls.enable()
            self.pick_color_btn_bg.enable()
            self.createBtn.enable()
            self.solveBtn.disable()
            self.clearBtn.disable()
            self.saveBtn.disable()
            self.fsearchBtn.disable()
            self.breadthBtn.disable()
            self.depthBtn.disable()
            self.asearchBtn.disable()
            
            # Clear the screen
            self.clear_screen()
            self.view_controller.stop_visual_part()
        except Exception as e:
            log_exception(e)
    
    # Call method when clicking on the main Save button
    def save_btn_click(self) -> None:
        try:
            # Disable and enable certain buttons
            self.ena_dis_buttons()
            self.view_controller.save_maze(self.screen)
        except Exception as e:
            log_exception(e)
    
    # Method called when clicking on the secondary button for the L* Search algorithm
    def fsearchBtn_click(self) -> None:
        try:
            # Disable and enable certain buttons
            self.ena_dis_buttons()
            self.view_controller.start_handle_algorithms(self,self.view_controller.first_fase_flood,self.view_controller.second_fase_flood,self.view_controller.delete_flood,"Flood Fill Algorithm")
        except Exception as e:
            log_exception(e)

    # Method called when clicking on the secondary button for the Breadth Search algorithm
    def breadthBtn_click(self) -> None:
        try:
            # Disable and enable certain buttons
            self.ena_dis_buttons()
            self.view_controller.start_handle_algorithms(self,self.view_controller.first_fase_breadth,self.view_controller.second_fase_breadth,self.view_controller.delete_breadth,"Breadth Algorithm")
        except Exception as e:
            log_exception(e)
        
    # Method called when clicking on the secondary button for the Depth First Search algorithm
    def depthBtn_click(self) -> None:
        try:
            # Disable and enable certain buttons
            self.ena_dis_buttons()
            self.view_controller.start_handle_algorithms(self,self.view_controller.first_fase_depth,self.view_controller.second_fase_depth,self.view_controller.delete_depth_A,"Depth Algorithm")
        except Exception as e:
            log_exception(e)  
    
    # Method called when clicking on the secondary button for the A* Search algorithm
    def asearchBtn_click(self) -> None:
        try:
            # Disable and enable certain buttons
            self.ena_dis_buttons()
            self.view_controller.start_handle_algorithms(self,self.view_controller.first_fase_A,self.view_controller.second_fase_A,self.view_controller.delete_depth_A,"A* Algorithm")
        except Exception as e:
            log_exception(e)
    
    
    # Method that enables or disables buttons when the user chooses the solve button,Save button or any of the algorithm buttons
    def ena_dis_buttons(self):
        # Disable certain buttons
            self.pick_color_btn_wls.disable()
            self.pick_color_btn_bg.disable()
            self.createBtn.disable()
            self.solveBtn.enable()
            self.clearBtn.enable()
            self.saveBtn.enable()
            self.fsearchBtn.enable()
            self.breadthBtn.enable()
            self.depthBtn.enable()
            self.asearchBtn.enable()
            
    def stop_visual_part(self)-> None:
        self.view_controller.stop_visual_part()

    

    






