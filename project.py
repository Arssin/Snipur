
import math
import pygame , sys

print('hello world')
print(pygame.__version__)

resolution = (1280,720)

screen = pygame.display.set_mode(resolution)

radius = 40
x = 200
y = 100

while True:
  # Handle events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit(0)

  screen.fill('white')
  mx,my = pygame.mouse.get_pos()
  # Draw
  circle1 = pygame.draw.circle(screen, "blue", (x,y), radius, 0 )
  circle2 = pygame.draw.circle(screen, "red", (mx,my), radius,5 )

  dx = mx - x
  dy = my - y

  angle = math.atan2(dx,dy)
  movex = math.sin(angle) 
  movey = math.cos(angle)

  x += movex
  y += movey

  pygame.display.flip()