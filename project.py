import pygame , sys


pygame.init()
resolution = (1280,720)
screen = pygame.display.set_mode(resolution)



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

  if pygame.mouse.get_pressed()[0]:
    print('Mouse pressed')

  pygame.display.flip()
  clock.tick(60)