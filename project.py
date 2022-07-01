import pygame , sys


pygame.init()
resolution = (1280,720)
screen = pygame.display.set_mode(resolution)

# viewfinder image
# crosshair = pygame.image.load('crosshair.png')

# Circles values
radiuscrosshair = 25
radiuscircles = 15
x = 100
y = 200

# Clock
clock = pygame.time.Clock()
delta = 0.0

#Max Tick Per second
max_tps = 60.0

#Points
points = 0

while True:
  # Handle events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit(0)


  #Border
  screen.fill('white')


  # Draw
  mx,my = pygame.mouse.get_pos()
  circle1 = pygame.draw.circle(screen, "blue", (x,y), radiuscircles, 0 )
  circle2 = pygame.draw.circle(screen, "red", (mx,my), radiuscrosshair, 5 )


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
  clock.tick(60)