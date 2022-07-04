# -------------- Package + Init -----------------
import random
import pygame , sys
pygame.init()

# -------------- Settings -----------------


width = 1280
height = 720
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Snipur')
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()

margin = 100
bar = 100
score = 0

font = pygame.font.SysFont("Arial", 25)


#COLORS
blue = (0,0,255)
red = (255,0,0)
white = (230, 230, 230)
lightGreen = (25, 111, 61)
purple = (155, 89, 182)





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


hit = 0
count = 0


# -------------- Classes  -----------------
class Circle:
    def __init__(self):
         self.a = random.randint(30, 40)
         self.b = self.a + random.randint(0, 10)
         self.x = random.randrange(margin, width - self.a - margin)
         self.pos = [random.randint(0, 1280), random.randint(0, 720)]
         self.color = blue
         self.radius = 15
         self.color = random.choice([blue,red,purple,lightGreen,])

    def draw(self):
         pygame.draw.circle(screen, self.color, (self.pos[0], self.pos[1]), self.radius)

    


def pointer():
  mx,my = pygame.mouse.get_pos()
  pygame.draw.circle(screen, red, (mx,my), radiuscrosshair, 5 )


#Random generator 
targets = []
noTargets = 10
number = 5
ox = random.randint(0,1280)
oy = random.randint(0,720)




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


  #Border
  screen.fill('white')

  # Draw circle and mouse position

  
    


  pointer()




  

  pygame.display.update()
  clock.tick(60)

pygame.quit()
