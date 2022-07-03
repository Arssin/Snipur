# -------------- Package + Init -----------------
import random
import pygame , sys
pygame.init()

# -------------- Settings -----------------


screen = pygame.display.set_mode((1280,720))
blue = (0,0,255)
white = (2,200,200)

ms_delay = 3000

pygame.time.set_timer(pygame.USEREVENT+2, ms_delay)
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


# -------------- Classes  -----------------
class Circle:
    def __init__(self):
         #You can initialise the position to a random value
         self.pos = [random.randint(0, 1280), random.randint(0, 720)]
         self.color = blue
         self.radius = 15

    def draw(self):
         pygame.draw.circle(screen, self.color, (self.pos[0], self.pos[1]), self.radius)



#Random generator 
obstacles = []
number = 5
ox = random.randint(0,1280)
oy = random.randint(0,720)

for i in range(number):
  obstacles.append(Circle())
# for count in range(number):
#   count += 1
#   print(count)



# for obstacle in obstacles:
#   if count <= 0:
#     count += 1
    # obstacles.append(pygame.draw.circle(screen, blue, (ox,oy), radiuscircles, 0 ))
  # pygame.draw.circle(screen, blue, (ox,oy), radiuscircles, 0 )
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


  # for obstacle in obstacles:
  #     pygame.draw.circle(screen, blue, (ox,oy), radiuscircles, 0 )




  #Border
  screen.fill('white')

  # Draw circle and mouse position
  mx,my = pygame.mouse.get_pos()
  pygame.draw.circle(screen, "red", (mx,my), radiuscrosshair, 5 )

  for circle in obstacles:
    circle.draw()

  clock.tick(60)

  pygame.display.update()

pygame.quit()
