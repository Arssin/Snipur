# -------------- Package + Init -----------------
import random
import pygame , sys
pygame.init()

# -------------- Settings -----------------


screen = pygame.display.set_mode((1280,720))
blue = (0,0,255)
white = (2,200,200)

ms_delay = 3000
spawn_circle_event = pygame.USEREVENT+2
pygame.time.set_timer(spawn_circle_event, ms_delay)
pygame.display.set_caption('Snipur')
# Circles values
radiuscrosshair = 25
radiuscircles = 15
circlesX = 0
circlesY = 30
# Clock
#Max Tick Per second
max_tps = 60.0
#Points
points = 0
game_over = False

#COLORS
blue = (0,0,255)

hit = 0
count = 0

#Random generator 
obstacles = []
number = 5
ox = random.randint(0,1280)
oy = random.randint(0,720)
# for i in range(number):
#   ox = random.randint(0,1280)
#   oy = random.randint(0,720)
#   obstacles.append(pygame.Rect(ox,oy,25,60))


# -------------- GameLoop -----------------
clock = pygame.time.Clock()
game_over = False

while not game_over:

  # Handle events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit(0)


    if pygame.mouse.get_pressed()[0]:
      print('Mouse pressed')

    if event.type == pygame.USEREVENT+2:
      obstacles.append(pygame.Rect(ox,oy,25,60))
      print('bonjour')

  screen.fill('white')

  for obstacle in obstacles:
      pygame.draw.circle(screen, blue, (ox,oy), radiuscircles, 0 )




  #Border

  # Draw circle and mouse position
  mx,my = pygame.mouse.get_pos()
  pygame.draw.circle(screen, "red", (mx,my), radiuscrosshair, 5 )

  clock.tick(60)
  pygame.display.update()

pygame.quit()
