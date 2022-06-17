from turtle import position
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
                pygame.draw.line(screen, CROSS_COLOR, (col * 200 + SPACE, row * 200 + 200 - SPACE), (col * 200 + 200 - SPACE, row * 200 + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * 200 + SPACE, row * 200 + SPACE), (col * 200 + 200 - SPACE, row * 200 + 200 - SPACE), CROSS_WIDTH)

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
    if row == 3 or col == 3:
        return False#mozna nepotrebuju
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
            return True
        
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal()
        return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal()
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

def kkk(winning_fields, max_index):
    winning_fields.sort()
    x = 8
    for i in winning_fields:
        x = x - 1
        if winning_fields[x] < max_index:
            return max_index
    

def AI_move(winning_fields, number):
    if winning_fields == [0, 0, 0, 0, 0, 0, 0, 0, 0]:
        print('kde')
        return random.randint(0, 2), random.randint(0, 2)
    else:
        for position, elem in enumerate(winning_fields):
            if elem == number:
                if position == 0 and available_square(0, 0):
                    return 0, 0
                if position == 1 and available_square(0, 1):
                    return 0, 1 
                if position == 2 and available_square(0, 2):
                    return 0, 2
                if position == 3 and available_square(1, 0):
                    return 1, 0
                if position == 4 and available_square(1, 1):
                    return 1, 1
                if position == 5 and available_square(1, 2):
                    return 1, 2
                if position == 6 and available_square(2, 0):
                    return 2, 0
                if position == 7 and available_square(2, 1):
                    return 2, 1
                if position == 8 and available_square(2, 2):
                    return 2, 2
                else:
                    return 3, 3
    print('kurva')

        

        
        

def winning_fields_writer(ai_row_moves, ai_col_moves, winning_fields):
    i = -1
    for row in ai_row_moves:
        i += 1
        col = ai_col_moves[i]
        if row == 0:
            if col == 0:
                winning_fields[0] += 1
            if col == 1:
                winning_fields[1] += 1
            if col == 2:
                winning_fields[2] += 1
        if row == 1:
            if col == 0:
                winning_fields[3] += 1
            if col == 1:
                winning_fields[4] += 1
            if col == 2:
                winning_fields[5] += 1
        if row == 2:
            if col == 0:
                winning_fields[6] += 1
            if col == 1:
                winning_fields[7] += 1
            if col == 2:
                winning_fields[8] += 1
    return winning_fields

def list_sorter(list):
    list.sort()
    return list


draw_lines()

player = 1
game_over = False
moves_row = []
moves_col = []
number_of_played_games = 0
ai_row_moves = []
ai_col_moves = []
winning_fields = [0, 0, 0, 0, 0, 0, 0, 0, 0]

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        #hra zahajuje hru hrace
        if event.type == pygame.MOUSEBUTTONDOWN:
            number_of_played_games += 1

            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = int(mouseY // 200)
            clicked_col = int(mouseX // 200)


            if available_square(clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, 1)

                clicked_row_array = [clicked_row]
                clicked_col_array = [clicked_col]
                moves_row = moves_row + clicked_row_array
                moves_col = moves_col + clicked_col_array
                
                draw_cross()

                if check_win(1):
                    ai_row_moves = []
                    ai_col_moves = []
                    pygame.display.update()
                    time.sleep(0.2)
                    number_of_played_games = 0
                    restart()
                else:
                    if number_of_played_games == 5:
                        number_of_played_games = 0
                        ai_row_moves = []
                        ai_col_moves = []
                        restart()

                    pygame.display.update()
                    
                    #nyni hra zahajuje hru AI
                    time.sleep(0.2)
                    good_move = False
                    sorted_list = winning_fields.copy()
                    sorted_list.sort()
                    w = 0

                    while not good_move and w > -9:
                        #print(w)
                        
                        w = w - 1
                        ai_row_move, ai_col_move = AI_move(winning_fields, sorted_list[w])
                        if ai_row_move != 3:
                            if available_square(ai_row_move, ai_col_move):
                                print('bbbbb')
                                if 0 <= ai_row_move <=2:
                                    w = 0
                                    good_move = True
                        
                    if w == 9:
                        ai_row_move, ai_col_move = random.randint(0, 2), random.randint(0, 2)
                        while not available_square(ai_row_move, ai_col_move):
                            ai_row_move, ai_col_move = random.randint(0, 2), random.randint(0, 2)
                    
                    if ai_row_move == 3:
                        ai_row_move, ai_col_move = random.randint(0, 2), random.randint(0, 2)
                        while not available_square(ai_row_move, ai_col_move):
                            ai_row_move, ai_col_move = random.randint(0, 2), random.randint(0, 2)

                    mark_square(ai_row_move, ai_col_move, 2)

                    ai_row_moves.append(ai_row_move)
                    ai_col_moves.append(ai_col_move)

                    draw_circle()


                    if check_win(2):
                        winning_fields = winning_fields_writer(ai_row_moves, ai_col_moves, winning_fields)
                        ai_row_moves = []
                        ai_col_moves = []
                        pygame.display.update()
                        time.sleep(0.2)
                        number_of_played_games = 0
                        restart()

                    pygame.display.update()

                    if number_of_played_games == 5:
                        number_of_played_games = 0
                        ai_row_moves = []
                        ai_col_moves = []
                        restart()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    restart()

        pygame.display.update()

