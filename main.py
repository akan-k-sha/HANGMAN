import pygame
import math
import random

#initializing 
pygame.init()

WIDTH=800
HEIGHT=500

#creating the screen
screen=pygame.display.set_mode((WIDTH,HEIGHT))

#Title and Icon
pygame.display.set_caption("_HANGMAN_GAME!")
icon=pygame.image.load("icon.png")
pygame.display.set_icon(icon)

#Font
letter_font=pygame.font.SysFont('ink free',30)
word_font=pygame.font.SysFont('ink free',40)
title_font=pygame.font.SysFont('Comic sans MS',40)

#button variables
RADIUS=20
GAP=15
SIDE=(WIDTH-(13*((RADIUS*2)+GAP)))//2
x_start=SIDE
y_start=400
letters=[]
A_ascii=65
for i in range(26):
    x= x_start+(GAP*2)+(GAP+2*RADIUS)*(i%13)
    y=y_start+(i//13)*(GAP+2*RADIUS)
    letters.append([x,y,chr(A_ascii+i),True])
#drawing
def draw():
    title_text=title_font.render("LETS PLAY HANGMAN!",1,(0,0,0))
    screen.blit(title_text,(WIDTH/2-title_text.get_width()/2,20))


    for letter in letters:
        x,y,l,vis=letter
        if vis:
            pygame.draw.circle(screen,(0,0,0),(x,y),RADIUS,3)
            text=letter_font.render(l,1,(0,0,0))
            screen.blit(text,(x-text.get_width()/2,y-text.get_height()/2))
    display_word=""
    for check in word:
        if check in guessed_list:
            display_word+=check+" "
        else:
            display_word+="_"+" "
    d_word=word_font.render(display_word,1,(0,0,0))
    screen.blit(d_word,(400,200))
    pygame.display.update()
def end_msg(message):
    
    pygame.time.delay(1000)
    screen.fill((255,255,255))
    win_text=word_font.render(message,1,(0,0,0))
    screen.blit(win_text,(WIDTH/2-win_text.get_width()/2, HEIGHT/2-win_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(2000)

#load hangman images
images=[]
for i in range(7):
    image=pygame.image.load("hangman"+str(i)+".png")
    images.append(image)

#game variables
hangman_staus=0
words=["DEVELOPER","MACHINE","SCIENCE","FACEBOOK","SUCCESS","HOME","HISTORY","CALENDAR","AUDIENCE","SISTER","SCHOOL","COLLEGE","JODHPUR","KOLKATA","DELICIOUS"]
word=random.choice(words)
guessed_list=[]


FPS=60
clock=pygame.time.Clock()

#gaming loop
running=True
while running:
    
    clock.tick(FPS)
    screen.fill((255,255,255))
    # draw()
    screen.blit(images[hangman_staus],(130,120))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            m_x,m_y=pygame.mouse.get_pos()
            for letter in letters:
                x,y,l,vis=letter
                dist=math.sqrt((x-m_x)**2 +(y-m_y)**2)
                if vis:
                    if dist<RADIUS:
                        letter[3]=False 
                        guessed_list.append(l)
                        if l not in word:
                            hangman_staus+=1   
    draw()            
    win=True
    for alpha in word:
        if alpha not in guessed_list:
            win=False
            break
    if win:
        end_msg("YOU WON!!!   The word was "+word)
        break
    if hangman_staus==6:
        end_msg("YOU LOST!!!   The word was "+word)
        break




    # pygame.display.update()
pygame.quit()
