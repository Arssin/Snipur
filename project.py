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
pygame.time.set_timer(pygame.USEREVENT+1, 1000)

score = 0
timeLeft = 30



font = pygame.font.SysFont("Consolas", 23)



#COLORS
blue = (0,0,255)
red = (255,0,0)
white = (230, 230, 230)
lightGreen = (25, 111, 61)
purple = (155, 89, 182)


# Circles values
radiuscrosshair = 15
radiuscircles = 25

max_tps = 60.0

# -------------- Classes  -----------------
class Circle:
    def __init__(self):
         self.x = random.randint(30,1250)
         self.y = random.randint(100,690)
         self.radius = radiuscircles
         self.color = random.choice([blue,red,purple,lightGreen,])

    def draw(self):
          pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, 5)

    def hit(self):
          global score
          pos = pygame.mouse.get_pos()

          if hitCircle(self.x, self.y,pos):
            score += 1
            self.reset()

    def reset(self): 
         self.x = random.randint(30,1250)
         self.y = random.randint(100,690)
         self.radius = radiuscircles
         self.color = random.choice([blue,red,purple,lightGreen,])
    
    
circles = []
noCircles = 1

for i in range(noCircles):
    obj = Circle()
    circles.append(obj)

def hitCircle(x,y,pos):
    if (x - radiuscircles/2 <= pos[0] <= x + radiuscircles/2) and (y - radiuscircles/2 <= pos[1] <= y + radiuscircles/2): 
        return True
    else:
        return False

def pointer():
  pos = pygame.mouse.get_pos()
  color = blue
  for i in range(noCircles):
    if hitCircle(circles[i].x  , circles[i].y, pos ):
      color = red
  pygame.draw.circle(screen, color,  (pos[0] , pos[1]), radiuscrosshair, 0 )

def upperBar():
    pygame.draw.rect(screen, purple, (0,0, 300, 60))
    pygame.draw.rect(screen, purple, (980,0, 300, 60))

def scoreShow():
    scoreText = font.render("Points : " + str(score), True, white)
    screen.blit(scoreText, (30, 15))
    timerText = font.render("Time left: " + str(timeLeft), True, (white))
    screen.blit(timerText, (1050, 15))
  
def scoredPoints():
    pygame.draw.rect(screen, red, (0,0, 1280, 720))
    scoredPoints = font.render("You got : " + str(score) + "points!", True, white)
    screen.blit(scoredPoints, (0, 0))

def close():
    pygame.quit()
    sys.exit()

def game():
    global score
    global timeLeft
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
            
            if event.type == pygame.USEREVENT+1:
              timeLeft -= 1
              if timeLeft <= 0:
                pygame.time.set_timer(pygame.USEREVENT+1, 0)
                

        screen.fill(white)

        
        for i in range(noCircles):
            circles[i].draw()

        pointer()
        
        
        upperBar()
        scoreShow()
        pygame.display.update()
        clock.tick(60)

game()