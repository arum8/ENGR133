"""
===============================================================================
ENGR 13300 Fall 2021

Program Description
    This code creates a game that allows the user to press the arrow keys to 
    move the character around and consume dumplings. The game ends when the player 
    consumes all of the dumplings. The game also ends if the player doesn't finish 
    dumplings within a certain amount of time.
    
    This function calculates the distance between the character and the dumplings

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
import math as m

#make a UDF for the distance between the character and the dumplings
def consume(char_x,char_y,dump_x,dump_y):
    x1 = char_x + 32
    x2 = dump_x + 16
    y1 = char_y + 32
    y2 = dump_y + 16
    dist = m.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    if dist < 27: # take in account of the size of the dumpling and character
        return True
    