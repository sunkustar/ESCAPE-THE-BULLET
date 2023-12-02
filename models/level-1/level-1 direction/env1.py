import numpy as np 
import matplotlib.pyplot as plt
import gymnasium as gym
from gymnasium import spaces
import random
import pygame
import math
import time



v1=2
count=-1
blist=[]
bul=[]
width = 1920
height = 1080
playerImg = pygame.image.load('drone.png')
bulletImg= pygame.image.load("1.png")



class idcard(gym.Env):
    def __init__(self):
        super(idcard, self).__init__()
        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.MultiDiscrete([1920, 1080, 1920 ,1080])


    def reset(self,seed=None):
        self.i=(np.random.randint(0,100)/100)
        self.j=1-((self.i)**2)
        self.v1=30
        self.count=-1
        self.blist=[]
        self.bul=[]
        self.y=0
        self.d=0
        self.p=0      

        self.observation=np.array([np.random.randint(100, 1800),np.random.randint(100, 900),0,0])
        self.observation[0] = random.randint(100,1800)
        self.observation[1] = random.randint(100,900)

        a= self.observation[0]
        b= self.observation[1]

        self.bul_x=a+6
        self.bul_y=b+6
        
        self.observation[2] = self.bul_x
        self.observation[3] = self.bul_y
        
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

        bul_x=self.bul_x
        bul_y=self.bul_y
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

        
        bul_x=bul_x+v1*i
        bul_y=bul_y-v1*j
       
        
        if (bul_x<=0 or bul_x>=width-10) : 
         i=-i
         j=j
         y = 1
        if (bul_y<=0 or bul_y>=height-10): 
         i=i
         j=-j
         y = 1


        self.i=i
        self.j=j 



        def isCollision(a, b, bul_x, bul_y):
           distance = math.sqrt(math.pow(a - bul_x, 2) + (math.pow(b - bul_y, 2)))
           if distance < 27:
              return True
           else:
              return False
           

        collision = isCollision(a, b, bul_x, bul_y)

        self.bul_x=bul_x
        self.bul_y=bul_y

        terminated=False

        
        d = d + 1

        if collision :
              d = d - 100
              terminated=True
              print("game over")
              time.sleep(10)

        reward=d/100+math.sqrt(math.pow(a - bul_x, 2) + (math.pow(b - bul_y, 2)))/100+p

        

        self.d=d
            
        self.y=y

        truncated = False
           
        if collision and y == 1:
            print("exit")
        
        
        

        self.render()
        
        print(self.observation,action)
        print(reward)

        return self.observation, reward, terminated, truncated, {}
    
    def render(self):
        a= self.observation[0]
        b= self.observation[1]

        bul_x=self.bul_x
        bul_y=self.bul_y
        

        screen=self.display

        screen.fill((255, 255, 255))
        playerImg = pygame.image.load('drone.png')
        bulletImg= pygame.image.load("1.png")
        screen.blit(playerImg,(a,b))
        screen.blit(bulletImg,(bul_x,bul_y))
        

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

    
           

        

       
