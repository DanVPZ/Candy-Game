import random

rows = 5
columns = 6
points = 0
grid = []
graphic_grid = ""
replace = [(0, 0)]

characters = ["A", "B", "C"]

def user_input():   # Gathers user input such as the characters to use
    getting_input = True
    while getting_input:
        character = str(input("Añade un tipo de caramelo (stop para finalizar):\n>>>")).upper()
        if not character == "STOP":
            characters.append(character)
        else:
            getting_input = False

    return characters


def new_grid(characters):   # Creates the logical grid (made of lists)
    for _ in range(rows):
        sublist = []
        for _ in range(columns):
            sublist.append(random.choice(characters))
        grid.append(sublist)

    while len(replace) != 0:
        check_collisions()
        replace_collided(replace, "random")


def draw_grid():    # Creates the graphical grid (string)
    global graphic_grid

    graphic_grid = ""
    for i in grid:
        graphic_grid += "\n"
        for j in i:
            graphic_grid += f"{j} "

    graphic_grid += "\n"


def replace_collided(replace_list, replace_with):  # Replaces every marked spot with a newly generated random character
    global replace, points

    duplicates = {}

    for pos_tuple in replace_list:
        if not pos_tuple in duplicates:
            x, y = pos_tuple[0], pos_tuple[1]
            if replace_with == "random":
                grid[x][y] = random.choice(characters)
            elif replace_with == "-":
                grid[x][y] = "-"
            duplicates[pos_tuple] = 1
            points += 10
        else:
            replace_list.remove(pos_tuple)
    
    draw_grid()


def check_collisions():
    global replace

    replace.clear()

    # Checks next position in the x axis (rows) for each column
    for x in range(rows - 2):
        for y in range(columns):
            condition = grid[x][y]
            if grid[x + 1][y] == condition and grid[x + 2][y] == condition:
                pos_tuple = (x, y)
                replace.append(pos_tuple)
                pos_tuple = (x + 1, y)
                replace.append(pos_tuple)
                pos_tuple = (x + 2, y)
                replace.append(pos_tuple)

    # Checks next position in the y axis (columns) for each row
    for x in range(rows):
        for y in range(columns - 2):
            condition = grid[x][y]
            if grid[x][y + 1] == condition and grid[x][y + 2] == condition:
                pos_tuple = (x, y)
                replace.append(pos_tuple)
                pos_tuple = (x, y + 1)
                replace.append(pos_tuple)
                pos_tuple = (x, y + 2)
                replace.append(pos_tuple)


def movement():
    global moving
    decision = input(f"Do you want to MOVE (M) or EXIT (E)? (You have {points} points)\n>>>")

    if decision != "E":
        tile = input("What candy do you want to move? e.g. 24 for row 2 and column 4\n>>>")
        direction = input("Where do you want to move it to? (L for Left, R for Right, U for Up, D for Down)")

        

    else:
        moving = False


# user_input()
new_grid(characters)
print(graphic_grid)
moving = True
points = 0

while moving:
    movement()
