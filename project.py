import pygame , sys


print(pygame.__version__)
pygame.init()
resolution = (1280,720)

screen = pygame.display.set_mode(resolution)

# Circles values
radius = 30
x = 100
y = 200

# Clock
clock = pygame.time.Clock()
delta = 0.0



while True:
  # Handle events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit(0)

  #Border
  screen.fill('white')

  # Ticking (frames per second)
  delta += clock.tick()/1000.0
  while delta > 1/2.0: 
    print("Hey")
    delta -= 1/2.0


  # Draw
  mx,my = pygame.mouse.get_pos()
  circle1 = pygame.draw.circle(screen, "blue", (x,y), radius, 0 )
  circle2 = pygame.draw.circle(screen, "red", (mx,my), radius,5 )

 # To which point is going
  # dx = mx - x
  # dy = my - y


  # angle = math.atan2(dx,dy)
  # movex = math.sin(angle) 
  # movey = math.cos(angle)

# Speed of following circles
  # x += movex * 0.2
  # y += movey * 0.2


  pygame.display.flip()