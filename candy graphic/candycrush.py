import pygame as pg
import random, os

# Screen Settings
pg.init()
clock = pg.time.Clock()
screen_width, screen_height = 800, 800
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Candy Game")

# Main Variables
directory = os.getcwd()
rows, columns = 6, 5
cell_size = screen_width / columns
score = 0
candy_list = []

images = [
    pg.image.load(f"{directory}\\img\\bg.jpg"),
    pg.image.load(f"{directory}\\img\\candy1.png"),
    pg.image.load(f"{directory}\\img\\candy2.png"),
    pg.image.load(f"{directory}\\img\\candy3.png"),
    pg.image.load(f"{directory}\\img\\candy4.png"),
    pg.image.load(f"{directory}\\img\\candy5.png"),
    pg.image.load(f"{directory}\\img\\candy6.png")
]

def draw_grid():
    for row in range(rows):
        for col in range(columns):
            pg.draw.rect(screen, "black", (col * cell_size, row * cell_size, cell_size, cell_size), 1)

def logical_grid():
    for _ in range(rows):
        candy_sublist = []
        for _ in range(columns):
            sprite = random.randint(1,6)
            candy_sublist.append(sprite)
        candy_list.append(candy_sublist)

def draw_candies():
    img_pos_y = 0
    for row in candy_list:
        img_pos_x = 0
        for col in row:
            screen.blit(pg.transform.scale(images[col], (cell_size, cell_size)), (img_pos_x * cell_size, img_pos_y * cell_size))
            img_pos_x += 1
        img_pos_y += 1
# NO SE DEBEN BLITEAR EN COL Y ROW PQ COL Y ROW SON LAS POSICIONES DE LOS SPRITES EN LA LISTA


logical_grid()

while True:

    screen.fill("white")
    screen.blit(pg.transform.scale(images[0], (1422, 800)), (0, 0))
    draw_grid()
    draw_candies()

    pg.display.flip()
    