# Programmer: Zailyn Tamayo; Class: CIS 247; File: Lab15_2.py; Date: 05/31/2013 
 
#The instructor revised Mikael Kindborg's original code 
import pygame 
from pygame.locals import * 
 
class DrawCircles: 
    def __init__(self): 
        # Initialize PyGame 
        pygame.init() 
        self.screen = pygame.display.set_mode((400,400)) 
        self.screen.fill((0,0,0)) 
        # Instance variable for circle objects 
        self.circles = [] 
 
    def run(self): 
        # Run the event loop 
        self.loop() 
        # Close the Pygame window 
        pygame.quit() 
     
    def loop(self): 
        # Game Loop 
        exit = False 
        while not exit: 
            # Handle input events 
            exit = self.handleEvents() 
            # Draw screen 
            self.draw() 
            # Wait a little 
            pygame.time.delay(10) 
 
    def handleEvents(self): 
            # Handle events 
            exit = False 
            for event in pygame.event.get(): 
                if event.type == QUIT: 
                    exit = True 
                elif event.type == KEYDOWN: 
                    if event.key == K_ESCAPE: 
                        exit = True 
                elif event.type == MOUSEBUTTONDOWN: 
                    self.circles = self.circles + [Circle(pygame.mouse.get_pos())] 
            return exit 
         
    def draw(self): 
        # Draw all circles 
        for circle in self.circles: 
            circle.draw(self.screen) 
        # Update display 
        pygame.display.update() 
 
class Circle: 
    def __init__(self, pos): 
        self.pos = pos 
    def draw(self, screen): 
            pygame.draw.circle(screen, (255,255,255), self.pos, 10, 0) 
         
# Start the game 
DrawCircles().run() 