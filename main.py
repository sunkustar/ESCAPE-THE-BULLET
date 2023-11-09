import pygame
import math

pygame.init()

height=1080
width=1920

screen = pygame.display.set_mode((width,height))

running=True

run=True
shoot=False

pygame.display.set_caption("ESCAPE THE BULLET")
icon = pygame.image.load("bullet.png")
pygame.display.set_icon(icon)

playerImg = pygame.image.load('drone.png')
bulletImg= pygame.image.load("1.png")

over_font = pygame.font.Font('freesansbold.ttf', 64)
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (0, 0, 0))
    screen.blit(over_text, (200, 250))
    pygame.time.delay(10000)


def player(x,y):
    screen.blit(playerImg,(x,y))

def bullet(x,y):
    screen.blit(bulletImg,(x,y))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

a=100
b=100 

aim=True

k=0

def shoot():
  i=1
  j=0
  if aim==False:
      v1=1
      bul_live=True
      global bul_x
      global bul_y
      bullet(bul_x,bul_y)
      while bul_live==True and (bul_x!=0 or bul_x!=width-10) and (bul_y!=0 or bul_y!=height-10):
       bul_x=a+v1*i
       bul_y=b+v1*j

i=1
j=1
v1=2

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =False

    screen.fill((255, 255, 255))

    top_wall = pygame.Rect(0, 0, width, 10)

    bottom_wall = pygame.Rect(0, height - 10, width, 10)

    left_wall = pygame.Rect(0, 0, 10, height)

    right_wall = pygame.Rect(width - 10, 0, 10, height)
    
    wall_color = (0, 255, 255)  # White color
    
    pygame.draw.rect(screen, wall_color, top_wall)
    pygame.draw.rect(screen, wall_color, bottom_wall)
    pygame.draw.rect(screen, wall_color, left_wall)
    pygame.draw.rect(screen, wall_color, right_wall)    
    

 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =False

    keys=pygame.key.get_pressed()   

    if keys[pygame.K_LEFT] and a>0:
        a=a-1
    if keys[pygame.K_RIGHT] and a<width-40:
        a=a+1
    if keys[pygame.K_UP] and b>0:
        b=b-1
    if keys[pygame.K_DOWN] and  b<height-40:
        b=b+1
    
    player(a,b)
    


    

    if keys[pygame.K_SPACE]:
        aim=False
        if aim==False :
            bul_x = a
            bul_y = b
            k=3
            
    
    if aim==False:
       if (bul_x>0 or bul_x<width-10) and (bul_y>0 or bul_y<height-10):
        i=i 
        j=j
       if (bul_x<=0 or bul_x>=width-10) : 
        k=1
        i=-i
        j=j
       if (bul_y<=0 or bul_y>=height-10): 
         k=1
         i=i
         j=-j
        
       print("trig")
       bul_x=bul_x+v1*i
       bul_y=bul_y-v1*j
       print(bul_x,bul_y)
       screen.blit(bulletImg,(bul_x,bul_y))

       collision = isCollision(a,b, bul_x, bul_y)

       if collision :
          if k==1:
           game_over_text()
           break

    pygame.display.update()  

    
