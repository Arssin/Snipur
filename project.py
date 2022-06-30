import pygame , sys

print('hello world')
print(pygame.__version__)

resolution = (1280,720)

screen = pygame.display.set_mode(resolution)

radius = 40

while True:
  # Handle events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit(0)

  screen.fill('white')
  mx,my = pygame.mouse.get_pos()
  # Draw
  circle1 = pygame.draw.circle(screen, "blue", (200,100), radius, 0 )
  circle2 = pygame.draw.circle(screen, "red", (mx,my), radius,5 )
  pygame.display.flip()