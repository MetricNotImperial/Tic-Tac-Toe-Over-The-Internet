import socket


import pygame
import os
import time
import random




WIDTH = 850
HEIGHT = 850
WIN = pygame.display.set_mode((WIDTH, HEIGHT))




pygame.display.set_caption("Tic Tac Toe")


pygame.font.init()


WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,43,43)


FPS = 60
FONT = pygame.font.SysFont("Times New Roman", 200)








CROSS_IMAGE = pygame.image.load(os.path.join("assets","cross.png"))
CIRCLE_IMAGE = pygame.image.load(os.path.join("assets","circle.png"))
SERVER = "10.0.0.160"










HEADER = 64
PORT = 5050
FORMAT = "utf-8"
DISCONNECTED_MESSAGE = "!DISCONNECT"
ADDR = (SERVER, PORT)




client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)




def send(msg):
    message = msg.encode(FORMAT)
    send_length = str(len(message)).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)




def draw_window(BOARD):
    WIN.fill(WHITE)


    pygame.draw.rect(WIN, BLACK, pygame.Rect(250, 0, 50, 850))
    pygame.draw.rect(WIN, BLACK, pygame.Rect(550, 0, 50, 850))
    pygame.draw.rect(WIN, BLACK, pygame.Rect(0, 250, 850, 50))
    pygame.draw.rect(WIN, BLACK, pygame.Rect(0, 550, 850, 50))


    #25,325,625
   
    for i in range(3):
        for j in range(3):
            if BOARD[i][j] == "x":
                x = 25 + j*300
                y = 25 + i*300
                WIN.blit(CROSS_IMAGE,(x,y))


            elif BOARD[i][j] == "o":
                x = 25 + j*300
                y = 25 + i*300
                WIN.blit(CIRCLE_IMAGE,(x,y))
   
    pygame.display.update()






def main(PLAYER):
    run = True
    clock = pygame.time.Clock()
    TURN = "x"
    BOARD = [[".",".","."],[".",".","."],[".",".","."]]
   


    while run:
        draw_window(BOARD)
        clock.tick(FPS)
   
        TURN = (client.recv(2048).decode(FORMAT))[0:10]
        print(TURN)
        x = False
       
        while TURN[0] == PLAYER:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x = (pygame.mouse.get_pos())[0]//283
                    y = (pygame.mouse.get_pos())[1]//283


                    send((str(x)+str(y)))


                   
                    x = True
            if x ==  True:
                break


       
        BOARD[0] = list(TURN[1:4])
        BOARD[1] = list(TURN[4:7])
        BOARD[2] = list(TURN[7:])
        print(BOARD)


       
       
    pygame.quit()
   
PLAYER = client.recv(2048).decode(FORMAT)


main(PLAYER)






