import pygame , sys

print('hello world')
print(pygame.__version__)

resolution = (1280,720)

screen = pygame.display.set_mode(resolution)
print(screen)

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit(0)