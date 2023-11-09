import numpy as np 
import matplotlib.pyplot as plt
import gymnasium as gym
from gymnasium import spaces
import random
import pygame
import math
import time


i=1
j=0
v1=3
count=-1
blist=[0,1,2,3,4]
bul=[[0,0,1,1,v1],[0,0,1,1,v1],[0,0,1,1,v1],[0,0,1,1,v1],[0,0,1,1,v1]]
width = 960
height = 540
playerImg = pygame.image.load('drone.png')
bulletImg= pygame.image.load("1.png")

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

class idcard(gym.Env):
    def __init__(self):
        super(idcard, self).__init__()
        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.MultiDiscrete([961, 541, 961, 541, 961, 541, 961, 541, 961, 541, 961 , 541])


    def reset(self,seed=None):
        self.i=1
        self.j=1
        self.v1=30
        self.count=-1
        self.blist=[]
        self.bul=[]
        self.y=0
        self.d=0
        self.p=0      

        self.observation=np.array([np.random.randint(100, 900),np.random.randint(100, 540),0,0,0,0,0,0,0,0,0,0])
        self.observation[0] = random.randint(100,900)
        self.observation[1] = random.randint(100,540)

        a= self.observation[0]
        b= self.observation[1]


        self.observation[2] = random.randint(100,900)
        self.observation[3] = random.randint(100,540)

        bul[0][0]=self.observation[2]
        bul[0][1]=self.observation[3]

        self.observation[4] = random.randint(100,900)
        self.observation[5] = random.randint(100,540)

        bul[1][0]=self.observation[4]
        bul[1][1]=self.observation[5]

        self.observation[6] = random.randint(100,900)
        self.observation[7] = random.randint(100,540)
        
        bul[2][0]=self.observation[6]
        bul[2][1]=self.observation[7]


        self.observation[8] = random.randint(100,900)
        self.observation[9] = random.randint(100,540)

        bul[3][0]=self.observation[8]
        bul[3][1]=self.observation[9]

        self.observation[10] = random.randint(100,900)
        self.observation[11] = random.randint(100,540)

        bul[4][0]=self.observation[10]
        bul[4][1]=self.observation[11]
        
        
        pygame.init()
        pygame.display.set_caption("ESCAPE THE BULLET")
        icon = pygame.image.load("bullet.png")
        pygame.display.set_icon(icon)
        self.display = pygame.display.set_mode((width,height))
        self.clock = pygame.time.Clock()

        self.render()


        return self.observation,{}
        

    def step(self, action):

        a= self.observation[0]
        b= self.observation[1]
        y=self.y
        d=self.d
        p=self.p

        i = self.i
        j = self.j
        v1 = self.v1
        count = self.count
    
        if action==  0 and a-10 > 1:
            a=a-1*10

        if action==  0 and a-10 < 1:
            p=p-1000

        if action== 1 and a<width-40:
            a=a+1*10

        if action== 1 and a>width-40:
            p=p-1000    
        
        if action == 2 and b-10>1:
            b=b-1*10

        if action == 2 and b-10<1:
            p=p-1000

        if action== 3 and  b<height-40:
            b=b+1*10

        if action== 3 and  b>height-40:
            p=p-1000

        self.observation[0] = a
        self.observation[1] = b

        terminated=False
        scr=0
        for item in blist:
       
         bul_x=bul[item][0]
         bul_y=bul[item][1]
         i=bul[item][2]
         j=bul[item][3]
         v1=bul[item][4]

       
         
         if (bul_x>0 or bul_x<width-10) and (bul_y>0 or bul_y<height-10):
           i=i 
           j=j
         if (bul_x<=0 or bul_x>=width-10) : 
           i=-i
           j=j
           bul[item][2]=i
           bul[item][3]=j
           
         
         if (bul_y<=0 or bul_y>=height-10): 
           i=i
           j=-j
           bul[item][2]=i
           bul[item][3]=j
           
         
       
         
        
         bul_x=bul_x+v1*i
         bul_y=bul_y-v1*j

        

         bul[item][0]=bul_x
         bul[item][1]=bul_y
         
         self.observation[2*item+2] = random.randint(100,900)
         self.observation[2*item+3] = random.randint(100,540)

         scrl=math.sqrt(math.pow(a - bul_x, 2) + (math.pow(b - bul_y, 2)))
         scr=scr+scrl
         print(scr)
         if scrl < 60:
             scr=scr-10000
         collision = isCollision(a,b, bul_x, bul_y)
          
         if collision :
              d = d - 100000
              terminated=True
              print("game over")
              time.sleep(10)
         
        reward=(d/100)+(scr/5)+p

        
        d = d + 1
        self.d=d
            
        self.y=y

        truncated = False

        self.render()
        
        print(self.observation,action)
        print(reward)

        return self.observation, reward, terminated, truncated, {}
    
    def render(self):
        a= self.observation[0]
        b= self.observation[1]
        

        screen=self.display

        screen.fill((255, 255, 255))
        playerImg = pygame.image.load('drone.png')
        bulletImg= pygame.image.load("1.png")
        screen.blit(playerImg,(a,b))
        screen.blit(bulletImg,(bul[0][0],bul[0][1]))
        screen.blit(bulletImg,(bul[1][0],bul[1][1]))
        screen.blit(bulletImg,(bul[2][0],bul[2][1]))
        screen.blit(bulletImg,(bul[3][0],bul[3][1]))
        screen.blit(bulletImg,(bul[4][0],bul[4][1]))

        top_wall = pygame.Rect(0, 0, width, 10)

        bottom_wall = pygame.Rect(0, height - 10, width, 10)

        left_wall = pygame.Rect(0, 0, 10, height)

        right_wall = pygame.Rect(width - 10, 0, 10, height)
        
        wall_color = (0, 255, 255)  # White color
        
        pygame.draw.rect(screen, wall_color, top_wall)
        pygame.draw.rect(screen, wall_color, bottom_wall)
        pygame.draw.rect(screen, wall_color, left_wall)
        pygame.draw.rect(screen, wall_color, right_wall)
        
        pygame.display.update()
        self.clock.tick(60)

    def close(self):
        pygame.quit()    

    
           

        

       
