#Python Snake Game - Alexander Watermen
import numpy as np
import keyboard
import time
import sys
import random
import msvcrt as m
from tkinter import *
from tkinter import messagebox



class Snakegame():

    def __init__(self):

        self.screen = Tk()

        self.gamesize = 30
        self.snakeLocation = [self.gamesize/2, self.gamesize/2]
        self.snakeTailLength = 3
        self.snakeTailLocation = np.zeros((self.snakeTailLength,2), dtype = int)

        self.appleLocation = [random.randint(0,self.gamesize),random.randint(0,self.gamesize)]
        self.appleExst = True
        self.increaseRate = 3

        self.snakeVel = None

        self.gamerun = True

        self.setUp()
        self.RunGame()

        self.screen.destroy()


    def RunGame(self):


        while self.gamerun:
            self.draw()
            
            time.sleep(0.03)

            for i in range(self.snakeTailLength-1,-1,-1):
                self.snakeTailLocation[i] = self.snakeTailLocation[i-1] 

            self.snakeTailLocation[0] = self.snakeLocation 



            if ((keyboard.is_pressed('w') and self.snakeVel != 's')):
                self.snakeLocation = [self.snakeLocation[0]-1,self.snakeLocation[1]]
                self.snakeVel = 'w'
            elif ((keyboard.is_pressed('a')and self.snakeVel != 'd')):
                self.snakeLocation = [self.snakeLocation[0],self.snakeLocation[1]-1]
                self.snakeVel = 'a'
            elif ((keyboard.is_pressed('s')and self.snakeVel != 'w')):
                self.snakeLocation = [self.snakeLocation[0]+1,self.snakeLocation[1]]
                self.snakeVel = 's'
            elif ((keyboard.is_pressed('d')and self.snakeVel != 'a')):
                self.snakeLocation = [self.snakeLocation[0],self.snakeLocation[1]+1]
                self.snakeVel = 'd'
            else:
                if self.snakeVel == 'w':
                    self.snakeLocation = [self.snakeLocation[0]-1,self.snakeLocation[1]]
                elif self.snakeVel == 'a':
                    self.snakeLocation = [self.snakeLocation[0],self.snakeLocation[1]-1]
                elif self.snakeVel == 's':
                    self.snakeLocation = [self.snakeLocation[0]+1,self.snakeLocation[1]]
                elif self.snakeVel == 'd':
                    self.snakeLocation = [self.snakeLocation[0],self.snakeLocation[1]+1]




            if self.snakeLocation[0] > self.gamesize-1 or self.snakeLocation[1] > self.gamesize-1 or self.snakeLocation[1] < 0 or self.snakeLocation[0] < 0:
                self.gamerun = False

            for i in range(self.snakeTailLength):
                if np.array_equal(self.snakeLocation,self.snakeTailLocation[i]) and self.snakeVel != None:
                    self.gamerun = False

            if np.array_equal(self.appleLocation,self.snakeLocation):
                self.appleExst=False
                

            if self.appleExst == False:
                self.appleLocation = [random.randint(0,self.gamesize-1),random.randint(0,self.gamesize-1)]
                self.appleExst = True


                for i in range(self.increaseRate+1):
                    self.snakeTailLocation = np.append(self.snakeTailLocation,[self.snakeTailLocation[self.snakeTailLength-1]], axis = 0)
                    self.SnakeTail = np.append(self.SnakeTail,[0], axis = 0)
                
                self.snakeTailLength += self.increaseRate


    def setUp(self):
        self.gameWindWidth = 1000
        self.gameWindHeight = 800
        self.w = Canvas(self.screen, width = self.gameWindWidth, height = self.gameWindHeight)
        self.HeightScale = self.gameWindWidth/self.gamesize
        self.WidthScale = self.gameWindHeight/self.gamesize
        for i in range(self.gamesize):
            self.w.create_line(0,(self.WidthScale)*i,self.gameWindWidth,(self.WidthScale)*i)
            self.w.create_line((self.HeightScale)*i,0,(self.HeightScale)*i,self.gameWindHeight)
        self.SnakeHead = self.w.create_rectangle(self.snakeLocation[0]*self.WidthScale,self.snakeLocation[1]*self.HeightScale,(self.snakeLocation[0]*self.WidthScale)+self.WidthScale,(self.snakeLocation[1]*self.HeightScale)+self.HeightScale, fill = "green")
        self.SnakeTail = np.zeros(self.snakeTailLength, dtype = int)
        self.Apple = self.w.create_rectangle(self.appleLocation[1]*self.HeightScale,self.appleLocation[0]*self.WidthScale,(self.appleLocation[1]*self.HeightScale)+self.HeightScale,(self.appleLocation[0]*self.WidthScale)+self.WidthScale, fill = "red")

    def draw(self):
        try:
            self.w.pack_forget()
            self.w.pack()
            self.w.delete(self.SnakeHead)
            self.w.delete(self.Apple)
            for i in range(self.snakeTailLength):
                self.w.delete(self.SnakeTail[i])


            self.SnakeHead = self.w.create_rectangle(self.snakeLocation[1]*self.HeightScale,self.snakeLocation[0]*self.WidthScale,(self.snakeLocation[1]*self.HeightScale)+self.HeightScale,(self.snakeLocation[0]*self.WidthScale)+self.WidthScale, fill = "green")

            for i in range(self.snakeTailLength):
                self.SnakeTail[i] = self.w.create_rectangle(self.snakeTailLocation[i][1]*self.HeightScale, self.snakeTailLocation[i][0]*self.WidthScale, (self.snakeTailLocation[i][1]*self.HeightScale)+self.HeightScale, (self.snakeTailLocation[i][0]*self.WidthScale)+self.WidthScale, fill = "green")

            self.Apple = self.w.create_rectangle(self.appleLocation[1]*self.HeightScale,self.appleLocation[0]*self.WidthScale,(self.appleLocation[1]*self.HeightScale)+self.HeightScale,(self.appleLocation[0]*self.WidthScale)+self.WidthScale, fill = "red")

            self.screen.update_idletasks()
            self.screen.update()

        except:
            sys.exit()

        
        

def wait():
    m.getch()

    
if __name__ == "__main__":
    while(True):
        game = Snakegame()

        
        







