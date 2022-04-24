import pygame, sys
import numpy as np

pygame.init()

screen = pygame.display.set_mode()

WIDTH, HEIGHT = screen.get_size()

LINE_COLOR = (131,139,139)
PAPER_COLOR = (240,255,255)
CIRCLE_COLOR = (0, 0, 255)
CROSS_COLOR = (255, 0, 0)

LINE_WIDTH = 2

BOARD_ROWS = 1000
BOARD_COLS = 1000

CIRCLE_RADIUS = 6
CIRCLE_WIDTH = 1

CROSS_WIDTH = 2
SPACE = 5



screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TicTacToeAI')
screen.fill(PAPER_COLOR)

board = np.zeros((BOARD_ROWS, BOARD_COLS))

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * 20 + 10), int(row * 20 + 10)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, CROSS_COLOR, (col * 20 + SPACE, row * 20 + 20 - SPACE), (col * 20 + 20 - SPACE, row * 20 + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * 20 + SPACE, row * 20 + SPACE), (col * 20 + 20 - SPACE, row * 20 + 20 - SPACE), CROSS_WIDTH)
                

def draw_lines():
    divider_for_squares = 20
    WIDTH_SQUARES = int(WIDTH / divider_for_squares) # how many squares are on width side of paper
    HEIGHT_SQUARES = int(HEIGHT / divider_for_squares) # how many squares are on height side of paper

    for x in range(WIDTH_SQUARES):
        pygame.draw.line(screen, LINE_COLOR, (x * divider_for_squares, 0), (x * divider_for_squares, HEIGHT), LINE_WIDTH)
    
    for y in range(HEIGHT_SQUARES):
        pygame.draw.line(screen, LINE_COLOR, (0, y * divider_for_squares), (WIDTH, y * divider_for_squares), LINE_WIDTH)
    
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
            draw_vertical_winning_line(col, player)
            return True

    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row, player)
            return False
        
    if board[2][0] == player and board[1][1] == player and board[row][2] == player:
        draw_asc_diagonal(player)
        return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal(player)
        return True

    return False

def draw_vertical_winning_line(col, player):
    posX = col * 200 + 100

    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color =  CROSS_COLOR
    
    pygame.draw.line(screen, color, (posX, 15), (posX, HEIGHT - 15), 15)


def draw_horizontal_winning_line(row, player):
    posY = row * 200 + 100

    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (15, posY), (WIDTH - 15, posY), 15)


def draw_asc_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), 15)


def draw_desc_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
    
    pygame.draw.line(screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), 15)


def restart():
    screen.fill(PAPER_COLOR)
    draw_lines()
    player = 1
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0








draw_lines()

player = 1
game_over = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = int(mouseY // 20)
            clicked_col = int(mouseX // 20)

            if available_square(clicked_row, clicked_col):
                if player == 1:
                    mark_square(clicked_row, clicked_col, 1)
                    if check_win(player):
                        game_over = True
                    player = 2
                elif player == 2:
                    mark_square(clicked_row, clicked_col, 2)
                    if check_win(player):
                        game_over = True
                    player = 1
                draw_figures()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()

    pygame.display.update()
