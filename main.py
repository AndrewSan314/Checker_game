import pygame

from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE
from checkers.game import Game

FPS = 120
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checker')


def get_row_col_from_pos(pos):
    x, y = pos
    col = x // SQUARE_SIZE
    row = y // SQUARE_SIZE
    return row, col


def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    if game.board.winner():
        print(game.board.winner())
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_pos(pos)
                game.select(row, col)
        game.update()
    pygame.quit()


main()
