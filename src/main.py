# To run this code it is necessary to install some libraries before running so use the command 
# "pip install -r requirements.txt"

import pygame
import pygame_widgets
import pygame_widgets.button
import pygame_widgets.widget
from views.view import View
from utils.log_exception import log_exception

# The main method of the entire program
def main() -> None:
    # Initializes all parts of Pygame modules that are necessary to start the application. This includes initializing the video subsystem, sound, fonts, etc.
    try:
        pygame.init()
    except Exception as e:
        log_exception(e)
        return
    
    try:
        # Call the main view of the program
        view = View()
        # Start the main loop that will keep the program running until the window is closed.
        running:bool = True
        while running:  
            events:pygame.event = pygame.event.get()  # Get all events
            for event in events:
                if event.type == pygame.QUIT: # User clicks the window close button            
                    view.stop_visual_part()
                    running = False
                    break                
            pygame_widgets.update(events) # Update Pygame widgets
            pygame.display.flip() # Update the screen once per iteration
    except Exception as e:
        log_exception(e)
    finally:
        try:
            pygame.quit() # Closes the program and all processes
        except Exception as e:
            log_exception(e)

if __name__ == "__main__":
    main()
    
    
    