import pygame, sys
import numpy as np
import random
import time


WIDTH = 600
HEIGHT = 600

LINE_COLOR = (131,139,139)
PAPER_COLOR = (240,255,255)
CIRCLE_COLOR = (0, 0, 255)
CROSS_COLOR = (255, 0, 0)
WINNING_LINE = (0, 0, 0)

LINE_WIDTH = 15

BOARD_ROWS = 3
BOARD_COLS = 3

CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15

CROSS_WIDTH = 25
SPACE = 55


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TicTacToeAI')
screen.fill(PAPER_COLOR)

board = np.zeros((BOARD_ROWS, BOARD_COLS))

def draw_cross():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                #pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * 200 + 100), int(row * 200 + 100)), CIRCLE_RADIUS, CIRCLE_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * 200 + SPACE, row * 200 + 200 - SPACE), (col * 200 + 200 - SPACE, row * 200 + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * 200 + SPACE, row * 200 + SPACE), (col * 200 + 200 - SPACE, row * 200 + 200 - SPACE), CROSS_WIDTH)
                
            #elif board[row][col] == 2:
                #pygame.draw.line(screen, CROSS_COLOR, (col * 200 + SPACE, row * 200 + 200 - SPACE), (col * 200 + 200 - SPACE, row * 200 + SPACE), CROSS_WIDTH)
                #pygame.draw.line(screen, CROSS_COLOR, (col * 200 + SPACE, row * 200 + SPACE), (col * 200 + 200 - SPACE, row * 200 + 200 - SPACE), CROSS_WIDTH)
                
def draw_circle():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 2:
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * 200 + 100), int(row * 200 + 100)), CIRCLE_RADIUS, CIRCLE_WIDTH)



def draw_lines():
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)


def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):
    return board[row][col] == 0

def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True

def check_win(player):
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col)
            return True

    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row)
            return False
        
    if board[2][0] == player and board[1][1] == player and board[row][2] == player:
        draw_asc_diagonal(player)
        return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal(player)
        return True

    return False

def draw_vertical_winning_line(col):
    posX = col * 200 + 100
    pygame.draw.line(screen, WINNING_LINE, (posX, 15), (posX, HEIGHT - 15), 15)


def draw_horizontal_winning_line(row):
    posY = row * 200 + 100

    pygame.draw.line(screen, WINNING_LINE, (15, posY), (WIDTH - 15, posY), 15)


def draw_asc_diagonal():
    pygame.draw.line(screen, WINNING_LINE, (15, HEIGHT - 15), (WIDTH - 15, 15), 15)


def draw_desc_diagonal():
    pygame.draw.line(screen, WINNING_LINE, (15, 15), (WIDTH - 15, HEIGHT - 15), 15)


def restart():
    screen.fill(PAPER_COLOR)
    draw_lines()
    player = 1
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0

def AI_move():
    return random.randint(0, 2), random.randint(0, 2)





draw_lines()

player = 1
game_over = False
moves_row = []
moves_col = []





while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = int(mouseY // 200)
            clicked_col = int(mouseX // 200)

            #pro pohyb hrace nejdrive hra zjistuje zda je pole volne
            if available_square(clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, 1)
                clicked_row_array = [clicked_row]
                clicked_col_array = [clicked_col]
                moves_row = moves_row + clicked_row_array
                moves_col = moves_col + clicked_col_array
                
                draw_cross()

                if check_win(1):
                    game_over = True

                #nyni hra zahajuje hru AI
                ai_row_move, ai_col_move = AI_move()
                while not available_square(ai_row_move, ai_col_move):
                    ai_row_move, ai_col_move = AI_move()

                mark_square(ai_row_move, ai_col_move, 2)

                
                draw_circle()

                if check_win(2):
                    game_over = True
                
                


                
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    restart()

        pygame.display.update()