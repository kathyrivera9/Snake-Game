import pygame
import time
import random
pygame.init()

#setting window displays
win_height = 400
win_width = 600
window = pygame.display.set_mode((win_width,win_height))
pygame.display.set_caption("Snake Game by Katherinne R.")
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
clock = pygame.time.Clock()   
high_score = 0

#colors
white = (255,255,255)
black = (0,0,0)
pastelYellow = (250,250,210)
pink = (255,192,203)
pastelBlue = (198,226,255)
darkBlue = (74,112,139)
yellow = (255, 255, 102)
purple = (171,130,255)
blue = (0,0,255)
red = (255, 0 , 0)

#snake settings
snake_block = 10
snake_speed = 10

#displays score
def Your_score(score):
    value = score_font.render("Your Score:" + str(score), True, darkBlue)
    window.blit(value, [0,0])

#this function leads to increasing the size of the snake
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, pink, [x[0], x[1], snake_block, snake_block])    #sets the shape and color of the snake

#function to display messages on the window
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    window.blit(mesg, [win_width/6, win_height/3])

def gameLoop():
    game_over = False 
    game_close = False
    
    #coordinates
    x1 = win_width/2
    y1 = win_height/2
    
    x1_change = 0
    y1_change = 0
    
    snake_List = []
    Length_of_snake = 1
    
    #setting up food settings
    foodx = round(random.randrange(0, win_width - snake_block)/ 10) * 10
    foody = round(random.randrange(0, win_height - snake_block)/ 10) * 10
    
    while not game_over:
        while game_close == True:
            window.fill(pastelBlue)
            message("You Lost! Press Q-Quit or C-Play Again", darkBlue)
            Your_score(Length_of_snake - 1 )
            pygame.display.update()

            for event in pygame.event.get():             #this uses q and c to quit or play again
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:                 #this tells the window to close when clicking on the exit button  
                game_over = True
            if event.type == pygame.KEYDOWN:              #this sets actions to the keyboard keys
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block

        if x1 >= win_width or x1 < 0 or y1 >= win_height or y1 < 0:   
            game_close = True                              #this exits game if snake goes out of bounds

        x1 += x1_change
        y1 += y1_change
        window.fill(pastelYellow)                          #this changes the window screen color to white from default black
        
        pygame.draw.rect(window, purple, [foodx, foody, snake_block, snake_block])      #sets the food on the screen
        
        #snake
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
            
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
                
        our_snake(snake_block, snake_List) 
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, win_width - snake_block)/ 10) * 10
            foody = round(random.randrange(0, win_height - snake_block)/ 10) * 10
            #snake_speed += 1
            Length_of_snake += 1
            
        clock.tick(snake_speed)

    pygame.quit()

gameLoop()
