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
blist=[0,1,2]
width = 800
height = 600
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
        self.action_space = spaces.MultiDiscrete([36,36])
        self.observation_space = spaces.MultiDiscrete([810]*10)


    def reset(self,seed=None):
        self.i=1
        self.j=1
        self.v1=5
        self.count=-1
        self.blist=[]
        self.bul=[[200,400,1,1,0,0],[600,400,-1,1,0,0],[400,400,1,1,0,0]]

        self.y=0
        self.d=0
        self.sink=[0,0,100,0,0,0]
        self.sinkc=0
        self.reward=0
        
  
        self.observation=np.array([np.random.randint(100, 700),np.random.randint(100, 700),200,400,600,400,400,200,0,0])
        self.observation[8] = self.observation[0]
        self.observation[9] = self.observation[1]

        a= self.observation[0]
        b= self.observation[1]
    
        
        
        pygame.init()
        pygame.display.set_caption("ESCAPE THE BULLET")
        icon = pygame.image.load("bullet.png")
        pygame.display.set_icon(icon)
        self.display = pygame.display.set_mode((width,height))
        self.clock = pygame.time.Clock()
        
        self.render()

        

        return self.observation,{}
        

    def step(self, action):
        reward=self.reward
        bul=self.bul
        terminated=False
        a= self.observation[0]
        b= self.observation[1]
        
       

        
        v1 = self.v1
        count = self.count

        def degrees_to_radians(degrees):
         return degrees * (math.pi / 180)

        angle_radians = degrees_to_radians(action[0]*10)
    
        a=a+(v1)*math.cos(angle_radians)
        b=b+(v1)*math.sin(angle_radians)

        if a>800 or a < 0 or b>600 or b<=0:
           print("out of boundary")
           reward=reward-100000
           terminated=True
           
           
           

        self.observation[0] = a
        self.observation[1] = b

        if self.sink[3]==0:

         angle_radians2 = degrees_to_radians(action[1]*10)
         self.sink[3]=1
         self.sink[0]=a
         self.sink[1]=b
         self.sink[4]=math.cos(angle_radians2)
         self.sink[5]=math.cos(angle_radians2)
         
         
        if self.sink[2]>0 and self.sink[3]==1:
         j=self.sink[5]
         i=self.sink[4]
         
         

         if (self.sink[0]>10 or self.sink[0]<width-10) and (self.sink[1]>0 or self.sink[1]<height-10):
              i=i 
              j=j
              if (self.sink[0]<=10 or self.sink[0]>=width-10) : 
                i=-i
                j=j
                self.sink[4]=i
                self.sink[5]=j
              if (self.sink[1]<=10 or self.sink[1]>=height-10): 
                i=i
                j=-j
                self.sink[4]=i
                self.sink[5]=j
         self.sink[0]=self.sink[0]+((5)*self.sink[4])
         self.sink[1]=self.sink[1]+((5)*self.sink[5])
         self.sink[2]=self.sink[2]-0.05        
         self.observation[8] = int(self.sink[0])
         self.observation[9] = int(self.sink[1])
         
        

        if self.sink[2]<=0:
           self.sink[3]==1
           self.sink[0]=a
           self.sink[1]=b
           self.sink[2]=100
           self.sinkc+=1
           reward=reward-150
           print("lol")

        if self.sinkc==2:
           terminated=True   
           print("out of bullets")
           
        

        for item in blist:
       
            bul_x=bul[item][0]
            bul_y=bul[item][1]
            i=bul[item][2]
            j=bul[item][3]
            v1=3

            if bul[item][5]==0:
         
             if (bul_x>0 or bul_x<width-10) and (bul_y>0 or bul_y<height-10):
              i=i 
              j=j
             if (bul_x<=10 or bul_x>=width-10) : 
                i=-i
                j=j
                bul[item][2]=i
                bul[item][3]=j
           
         
             if (bul_y<=10 or bul_y>=height-10): 
                i=i
                j=-j
                bul[item][2]=i
                bul[item][3]=j
           
         
       
         
        
             bul_x=bul_x+v1*i
             bul_y=bul_y-v1*j

        

             bul[item][0]=bul_x
             bul[item][1]=bul_y
         
             self.observation[2*item+2] = bul_x
             self.observation[2*item+3] = bul_y

             scrl=math.sqrt(math.pow(a - bul_x, 2) + (math.pow(b - bul_y, 2)))
             if scrl < 100 and bul[item][4]==0:
              reward=reward-100
              bul[item][4]==1

             if scrl > 100 and bul[item][4]==1:
              reward=reward+50 
              bul[item][4]==0 
             if scrl < 27 :
              reward=reward-500
              print("game over")
              terminated=True
              
              
              
              
            scr2=math.sqrt(math.pow(self.sink[0] - bul_x, 2) + (math.pow(self.sink[1] - bul_y, 2)))
            if scr2<27:
               reward=reward+200
               print("collision")
               self.d=self.d+1
               bul[item][5]=1


        if self.d==3:
           reward=reward+300
           terminated=True
           
           
         
        self.reward=reward

    
        self.bul=bul
        truncated = False

        self.render()
        
        
        print(self.observation)
        print(reward)

        return self.observation, reward, terminated, truncated, {}
    
    def render(self):
        a= self.observation[0]
        b= self.observation[1]
        
        bul=self.bul
        screen=self.display

        screen.fill((255, 255, 255))
        playerImg = pygame.image.load('drone.png')
        bulletImg= pygame.image.load("1.png")
        bulletImg2= pygame.image.load("2.png")

        screen.blit(playerImg,(a,b))
        screen.blit(bulletImg,(bul[0][0],bul[0][1]))
        screen.blit(bulletImg,(bul[1][0],bul[1][1]))
        screen.blit(bulletImg,(bul[2][0],bul[2][1]))
        screen.blit(bulletImg2,(self.sink[0],self.sink[1]))
         

        top_wall = pygame.Rect(0, 0, width, 10)

        bottom_wall = pygame.Rect(0, height - 10, width, 10)

        left_wall = pygame.Rect(0, 0, 10, height)

        right_wall = pygame.Rect(width - 10, 0, 10, height)
        
        wall_color = (0, 0, 0)  
        
        pygame.draw.rect(screen, wall_color, top_wall)
        pygame.draw.rect(screen, wall_color, bottom_wall)
        pygame.draw.rect(screen, wall_color, left_wall)
        pygame.draw.rect(screen, wall_color, right_wall)
        
        pygame.display.update()
        self.clock.tick(60)

    def close(self):
        pygame.quit()    

    
           

        

       
