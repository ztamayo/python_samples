# Programmer: Zailyn Tamayo; Class: CIS 247; File: Lab15_4.py; Date: 05/31/2013

# Orginally created by Lorenzo E. Danielsson 
import pygame,sys,os            
import random 
from pygame.locals import * 
from sys import exit 
  
class Worm: 
    def __init__(self, surface): 
        self.surface = surface 
        self.x = surface.get_width() / 2 
        self.y = surface.get_height() / 2 
        self.length = 1 
        self.grow_to = 50 
        self.vx = 0 
        self.vy = -1 
        self.body = [] 
        self.crashed = False 
        self.color = 255, 255, 0 
 
    def eat(self): 
        self.grow_to += 25 
 
    def event(self, event): 
        """ Handle keyboard events. """ 
        if event.key == pygame.K_UP: 
            if self.vy == 1: return 
            self.vx = 0 
            self.vy = -1 
        elif event.key == pygame.K_DOWN: 
            if self.vy == -1: return 
            self.vx = 0 
            self.vy = 1 
        elif event.key == pygame.K_LEFT: 
            if self.vx == 1: return 
            self.vx = -1 
            self.vy = 0 
        elif event.key == pygame.K_RIGHT: 
            if self.vx == -1: return 
            self.vx = 1 
            self.vy = 0 
  
    def move(self): 
        """ Move the worm. """ 
        self.x += self.vx 
        self.y += self.vy 
 
        if (self.x, self.y) in self.body: 
            self.crashed = True 
 
        self.body.insert(0, (self.x, self.y)) 
 
        if (self.grow_to > self.length): 

            self.length += 1 
 
        if len(self.body) > self.length: 
            self.body.pop() 
 
    def draw(self): 
        #for x, y in self.body: 
        #    self.surface.set_at((x, y), self.color) 
 
        x, y = self.body[0] 
        self.surface.set_at((int(x), int(y)), self.color) 
        x, y = self.body[-1] 
        self.surface.set_at((int(x), int(y)), (0, 0, 0)) 
 
 
class Food: 
    def __init__(self, surface): 
        self.surface = surface 
        self.x = random.randint(0, surface.get_width()) 
        self.y = random.randint(0, surface.get_height()) 
        self.color = 255, 255, 255 
 
    def draw(self): 
        pygame.draw.rect(self.surface, self.color, (self.x, self.y, 10, 10), 0) 
 
    def erase(self): 
        pygame.draw.rect(self.surface, (0, 0, 0), (self.x, self.y, 10, 10), 0) 
  
    def check(self, x, y): 
        if x < self.x or x > self.x + 10: 
            return False 
        elif y < self.y or y > self.y + 10: 
            return False 
        else: 
            return True 
 
w = 500 
h = 500 
  
screen = pygame.display.set_mode((w, h)) 
clock = pygame.time.Clock() 
 
pygame.mixer.init() 
chimes = pygame.mixer.Sound("chimes.wav") 
 
score = 0 
worm = Worm(screen) 
food = Food(screen) 
running = True 
  
while running: 
    worm.move() 
    worm.draw() 
    food.draw() 
 
    if worm.crashed: 
        running = False 
    elif worm.x <= 0 or worm.x >= w-1: 
        running = False 
    elif worm.y <= 0 or worm.y >= h-1: 
        running = False 
    elif food.check(worm.x, worm.y): 
        chimes.play() 

        score += 1 
        worm.eat() 
        print("Score: %d" % score) 
        food.erase() 
        food = Food(screen) 
      
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 
        elif event.type == pygame.KEYDOWN: 
            worm.event(event) 
 
    pygame.display.flip() 
    clock.tick(50) # speed 
 
while True: 
  for event in pygame.event.get(): 
    if event.type == QUIT: 
      exit() 
  
  pygame.display.update() 