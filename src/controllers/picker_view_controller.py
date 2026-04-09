import pygame
import pygame_gui.ui_manager
from views.picker_view import PickerView

class PickerViewController:
    # Class Constructor
    def __init__(self) -> None:
        self.picker_view:PickerView = None
        
    # Method that aims to open the color_picker window by instantiating the PickerView object and calling the color_picker method
    def open_color_picker(self,screen:pygame.display,ui_manager:pygame_gui.ui_manager,current_color:pygame.color) -> pygame.color:
        self.picker_view:PickerView = PickerView(screen,ui_manager)
        return self.picker_view.color_picker(current_color)