"""
===============================================================================
ENGR 13300 Fall 2021

Program Description

    This code creates a game that allows the user to press the arrow keys to 
    move the character around and consume dumplings. The game ends when the player 
    consumes all of the dumplings. 
    
    I chose this topic because I enjoy eating dumplings, and this seemed like 
    a good way to express this interest. This code achieves a stress free game
    to play when taking a mental break. 
    
    The inputs are just pressing down the arrow keys and the out put is moving
    the character, eating the dumplings and the "finished" text when the game
    is over. 
    
Assignment Information
    Assignment:     INDIVIDUAL PROJECT
    Author:         Alia Rumreich, arumreic@purdue.edu
                   
    Team ID:        LC2 - 21 

Contributor:
    
    My contributor(s) helped me:
    [x] understand the assignment expectations without
        telling me how they will approach it.
    [x] understand different ways to think about a solution
        without helping me plan my solution.
    [x] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor here as well.
    
ACADEMIC INTEGRITY STATEMENT
I have not used source code obtained from any other unauthorized
source, either modified or unmodified. Neither have I provided
access to my code to another. The project I am submitting
is my own original work.
===============================================================================
"""

import pygame as pg
from sys import exit
import random
from Ind_UDF_arumreic import consume

#make a UDF for the character
def character(character_img, char_x, char_y,screen):
    screen.blit(character_img, (char_x, char_y))  #blit means draw
   
    
#make a UDF for the dumplings going to be consumed
def dumpling(dump,screen, dump_x,dump_y):
    #loop through all of the x and y values and draw the dumplings on the screen
    for i in range(25):
        screen.blit(dump, (dump_x[i], dump_y[i]))  #blit means draw

    
def main():
    #initialize the pygame
    pg.init()
    #set dimensions of the game screen window (x,y)
    screen = pg.display.set_mode((800,600))
    
    
    #Title and Icon
    pg.display.set_caption("dumpling")
    dump = pg.image.load('dumpling.png')
    pg.display.set_icon(dump)
    
    #bamboo background
    bamboo = pg.image.load('bamboo.png')
    
    #font : game over text
    font = pg.font.Font('freesansbold.ttf', 40)
    done = font.render('finished ^-^', True, (255, 255, 255))
    
    # # user name text
    # input_name = input('insert your name\nEater: ')
    # name = font.render(input_name, True, (255,255,255))
    
    
    # #character initialization
    character_xchange = 0
    character_ychange = 0
    char_x = 700
    char_y = 500
    character_img = pg.image.load('redpanda.png')        
    
    #dumpling initialization
    i = 0
    ate = 0  
    
    #create empty lists
    dump_x = []
    dump_y = []
     
    #loop to add multiple dumplings in random places
    for i in range(25):
        dump_x.append(random.randint(50,700))
        dump_y.append(random.randint(50,500))    
    
    
    #loop the game until user closes the game window
    playing = True
   

    while playing:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
                
        #RGB background
        screen.fill((0,0,0))  #must call all other images after the screen so it is drawn on top of it
        
        #background 
        screen.blit(bamboo, (0, 0))
        
        # #user input : name (error check if invalid username)      
        # if input_name.isnumeric() == True:
        #     print('error: invalid username')
        #     break
        # else:
        #     screen.blit(name, (350,20))
            
            
        #if an arrow key is pressed, check the direction L,R,U,D
        if event.type == pg.KEYDOWN: 
            if event.key == pg.K_LEFT:
                character_xchange = -0.1 #set the speed of left motion
            if event.key == pg.K_RIGHT:
                character_xchange = 0.1 #set speed of right motion
            if event.key == pg.K_UP:
                character_ychange = -0.1 #set the speed of up motion
            if event.key == pg.K_DOWN:
                character_ychange = 0.1 #set speed of down motion
        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                character_xchange = 0  # stop the character when release the key
            if event.key == pg.K_UP or event.key == pg.K_DOWN:
                character_ychange = 0  # stop the character when release the key
                
        #increment the inital x and y value
        char_x += character_xchange 
        char_y += character_ychange
        
        #error: check if the character goes out of bounds and resets so it is in bounds
        if char_x <= 0:
            char_x = 0
        elif char_x >= 736: #takes into account the size of character being 64 pixels
            char_x = 736
        if char_y <= 0:
            char_y = 0
        elif char_y >= 536:
            char_y = 536
             
        #consumption
        for i in range(25):
            eat = consume(char_x,char_y,dump_x[i],dump_y[i])
            if eat:
                dump_x[i] = 1000
                dump_y[i] = 1000
                ate += 1
        if ate > 24:
            screen.blit(done, (250,250))
            
        #call the functions
        character(character_img,char_x,char_y,screen)  
        dumpling(dump,screen, dump_x,dump_y)
        
        #update the display when adding to or changing the game window
        pg.display.update()  
        
if __name__ == '__main__':
    main()