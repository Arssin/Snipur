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
lowerMargin = 100
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

max_tps = 60.0
game_over = False

# -------------- Classes  -----------------
class Circle:
    def __init__(self):
         self.x = random.randint(0,1280)
         self.y = random.randint(0,720)
         self.radius = 15
         self.color = random.choice([blue,red,purple,lightGreen,])

    def draw(self):
          pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def hit(self):
          global score
          pos = pygame.mouse.get_pos()

          # if hitCircle(self.x, self.y):
          #   score += 1
          #   self.reset()

    def reset(self): 
         self.x = random.randint(0,1280)
         self.y = random.randint(0,720)
         self.radius = 15
         self.color = random.choice([blue,red,purple,lightGreen,])
    
    
circles = []
noCircles = 10

for i in range(noCircles):
    obj = Circle()
    circles.append(obj)

# def hitCircle(x,y,a,b,pos):
#     if (x < pos[0] < x + a) and (y < pos[1] < y + b):
#         return True
#     else:
#         return False

def pointer():
  pos = pygame.mouse.get_pos()
  r = 25
  l = 20
  color = lightGreen
  # for i in range(noCircles):
  #   if hitCircle(circles[i].x, circles[i].y, circles[i].a, circles[i].b, pos):
  #     color = red
  pygame.draw.circle(screen, color,  (pos[0] - r/2, pos[1] - r/2), radiuscrosshair, 5 )

def upperScore():
    pygame.draw.rect(screen, purple, (0,0, 300, 60))

def scoreShow():
    scoreText = font.render("Circles shooted : " + str(score), True, white)
    screen.blit(scoreText, (30, 15))

def close():
    pygame.quit()
    sys.exit()

def game():
    global score
    loop = True

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    close()
                if event.key == pygame.K_r:
                    score = 0
                    game()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(noCircles):
                    circles[i].hit()

        screen.fill(white)
        
        for i in range(noCircles):
            circles[i].draw()

        pointer()
        
        
        upperScore()
        scoreShow()
        pygame.display.update()
        clock.tick(60)

game()