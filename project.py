# -------------- Package + Init -----------------

import random
import pygame , sys
pygame.init()

# -------------- Settings -----------------

resolution = (1280,720)
screen = pygame.display.set_mode(resolution)
ms_delay = 3000
spawn_circle_event = pygame.USEREVENT + 1
pygame.time.set_timer(spawn_circle_event, ms_delay)
# Circles values
radiuscrosshair = 25
radiuscircles = 15
# Clock
clock = pygame.time.Clock()
delta = 0.0
#Max Tick Per second
max_tps = 60.0
#Points
points = 0
game_over = False
all_targets = []

#COLORS
BLUE = (000,000,255)

circle1 = pygame.draw.circle(screen, "blue", (random.randint(0,1280),random.randint(0,720)), radiuscircles, 0 )

# -------------- Classes -----------------

class Circles:
  def __init__(self,x,y,radius=radiuscircles, color=BLUE, thick=0):
    self.x = x
    self.y = y
    self.radius = radius
    self.color = color
    self.thick = thick
    self.hitbox = (x,y,radius)
    self.count = 0

  def draw(self,screen):
    self.hitbox= ()
    if self.count >= 8:
      self.count = 0
    screen.blit(circle1,self.x,self.y)
    self.count += 1
    pygame.draw.circle(screen, "blue", self.hitbox, self.thick) 




# -------------- Functions -----------------


while not game_over:

  # for e in all_targets:
  #   e.draw(screen)

  # Handle events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit(0)

    if event.type == spawn_circle_event: 
      print('Hello')




    if pygame.mouse.get_pressed()[0]:
      print('Mouse pressed')

  for e in all_targets:
    e.draw(screen)

  #Border
  screen.fill('white')


  # Draw
  mx,my = pygame.mouse.get_pos()
  circle2 = pygame.draw.circle(screen, "red", (mx,my), radiuscrosshair, 5 )



  pygame.display.flip()
  clock.tick(60)