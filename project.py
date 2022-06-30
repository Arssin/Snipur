
import math
import pygame , sys

print('hello world')
print(pygame.__version__)

resolution = (1280,720)

screen = pygame.display.set_mode(resolution)

radius = 40
x = 10
y = 20

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

 # To which point is going
  dx = mx - x
  dy = my - y

  angle = math.atan2(dx,dy)
  movex = math.sin(angle) 
  movey = math.cos(angle)

  x += movex * 0.2
  y += movey * 0.2

  pygame.display.flip()