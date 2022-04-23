import pygame, sys
import numpy as np

pygame.init()

WIDTH = 600
HEIGHT = 600
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0,255, 0)
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
LOL = 3

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TicTacToeAI')
screen.fill(RED)

board = np.zeros((BOARD_ROWS, BOARD_COLS))
print(board)

def draw_lines():
    pygame.draw.line(screen, GREEN, (0, 200), (600, 200), LINE_WIDTH)
    pygame.draw.line(screen, GREEN, (0, 400), (600, 400), LINE_WIDTH)

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




mark_square(0, 0, 1)
mark_square(1, 1, 2)
print(available_square(1, 1))
print(board)
draw_lines()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()