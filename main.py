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
    
def issunk(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

a=100
b=100 


k=1



i=1
j=1
v1=2
count=-1
blist=[]
bul=[]
k=1

s1x=100
s1y=100
vs=1
s1i=0
s1j=1
s2x=width-100
s2y=height-100
s2i=0
s2j=-1
vs=1
live=0
time=1000
while running:
    
    k=k+1
    

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

    if (s1y<=0 or s1y>=height-10): 
         s1i=s1i
         s1j=-s1j

    s1x=s1x+vs*s1i
    s1y=s1y-vs*s1j     

    circle_color = (255, 0, 0)  # Red color (RGB)
    circle_center = (s1x, s1y)  # Center of the screen
    circle_radius = 27
    pygame.draw.circle(screen, circle_color, circle_center, circle_radius)
    

    if (s2y<=0 or s2y>=height-10): 
         s2i=s2i
         s2j=-s2j

    s2x=s2x+vs*s2i
    s2y=s2y-vs*s2j     

    circle_color = (255, 0, 0)  # Red color (RGB)
    circle_center = (s2x, s2y)  # Center of the screen
    circle_radius = 27
    pygame.draw.circle(screen, circle_color, circle_center, circle_radius)

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
    if keys[pygame.K_SPACE] or k==time:
        print(k)
        print(live)
        angle=int(input("enter angle"))
        o = math.radians(angle)
        i=math.cos(o)
        j=math.sin(o)
        count=count+1
        k=k+1
        blist.append(count)
        bul.append([])  
        print(bul)
        bul[count].append(a)  # x start 
        bul[count].append(b)  # y start
        bul[count].append(i)  # x dir
        bul[count].append(j)  # y dir
        bul[count].append(v1) # velocity
        bul[count].append(1)  # life
        bul[count].append(0)  # ref no
        print(bul) 
        print(blist)
        k=1
        time=live*1000

    live=1
    print(time)    
    for item in blist:
       
       bul_x=bul[item][0]
       bul_y=bul[item][1]
       i=bul[item][2]
       j=bul[item][3]
       v1=bul[item][4]

       
       if bul[item][5]==1:
        live=live+1
        if (bul_x>0 or bul_x<width-10) and (bul_y>0 or bul_y<height-10):
         i=i 
         j=j
        if (bul_x<=0 or bul_x>=width-10) : 
         i=-i
         j=j
         bul[item][2]=i
         bul[item][3]=j
         bul[item][6]=bul[item][6]+1
         
        if (bul_y<=0 or bul_y>=height-10): 
         i=i
         j=-j
         bul[item][2]=i
         bul[item][3]=j
         bul[item][6]=bul[item][6]+1
         
       
         
        
        bul_x=bul_x+v1*i
        bul_y=bul_y-v1*j

        

        bul[item][0]=bul_x
        bul[item][1]=bul_y

        screen.blit(bulletImg,(bul_x,bul_y))

        collision = isCollision(a,b, bul_x, bul_y)

        sink1=issunk(bul_x,bul_y,s1x,s1y)
        sink2=issunk(bul_x,bul_y,s2x,s2y)
        
        if collision and bul[item][6] > 1:
            game_over_text()
            running=False
            
        
        if sink1 and bul[item][6] > 1:
            bul[item][5]=2

        if sink2 and bul[item][6] > 1:
            bul[item][5]=2
    print(live)
    pygame.display.update()  

    
