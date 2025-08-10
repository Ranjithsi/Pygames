import pygame

# Initialize pygame and font
pygame.init()
pygame.font.init()

# Create window
screen = pygame.display.set_mode((500, 600))
pygame.display.set_caption("SUDOKU SOLVER USING BACKTRACKING")

# Load icon (make sure 'icon.png' is in the same folder)
try:
    img = pygame.image.load('icon.png')
    pygame.display.set_icon(img)
except:
    print("icon.png not found! Skipping icon.")

# Grid setup
x = 0
y = 0
dif = 500 / 9
val = 0

# Default grid
grid = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

# Fonts
font1 = pygame.font.SysFont("comicsans", 40)
font2 = pygame.font.SysFont("comicsans", 20)

def get_cord(pos):
    global x, y
    x = pos[0] // dif
    y = pos[1] // dif

def draw_box():
    for i in range(2):
        pygame.draw.line(screen, (255, 0, 0), (x * dif - 3, (y + i) * dif), (x * dif + dif + 3, (y + i) * dif), 7)
        pygame.draw.line(screen, (255, 0, 0), ((x + i) * dif, y * dif), ((x + i) * dif, y * dif + dif), 7)

def draw():
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                pygame.draw.rect(screen, (0, 153, 153), (j * dif, i * dif, dif + 1, dif + 1))
                text1 = font1.render(str(grid[i][j]), 1, (0, 0, 0))
                screen.blit(text1, (j * dif + 15, i * dif + 15))

    for i in range(10):
        thick = 7 if i % 3 == 0 else 1
        pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (500, i * dif), thick)
        pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), thick)

def draw_val(val):
    text1 = font1.render(str(val), 1, (0, 0, 0))
    screen.blit(text1, (x * dif + 15, y * dif + 15))

def raise_error1():
    text1 = font1.render("WRONG !!!", 1, (255, 0, 0))
    screen.blit(text1, (20, 570))

def raise_error2():
    text1 = font1.render("Invalid Key!", 1, (255, 0, 0))
    screen.blit(text1, (20, 570))

def valid(m, i, j, val):
    for it in range(9):
        if m[i][it] == val or m[it][j] == val:
            return False
    it = i // 3
    jt = j // 3
    for i in range(it * 3, it * 3 + 3):
        for j in range(jt * 3, jt * 3 + 3):
            if m[i][j] == val:
                return False
    return True

def solve(grid, i, j):
    while grid[i][j] != 0:
        if i < 8:
            i += 1
        elif i == 8 and j < 8:
            i = 0
            j += 1
        elif i == 8 and j == 8:
            return True
    pygame.event.pump()
    for it in range(1, 10):
        if valid(grid, i, j, it):
            grid[i][j] = it
            global x, y
            x, y = j, i
            screen.fill((255, 255, 255))
            draw()
            draw_box()
            pygame.display.update()
            pygame.time.delay(20)
            if solve(grid, i, j):
                return True
            grid[i][j] = 0
            screen.fill((255, 255, 255))
            draw()
            draw_box()
            pygame.display.update()
            pygame.time.delay(50)
    return False

def instruction():
    text1 = font2.render("D: Default | R: Reset | Enter: Solve", 1, (0, 0, 0))
    screen.blit(text1, (20, 520))
    text2 = font2.render("Arrow Keys: Move | 1-9: Input Number", 1, (0, 0, 0))
    screen.blit(text2, (20, 540))

def result():
    text1 = font1.render("SOLVED! PRESS R or D", 1, (0, 0, 0))
    screen.blit(text1, (20, 570))

run = True
flag1 = 0
flag2 = 0
rs = 0
error = 0

while run:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            flag1 = 1
            pos = pygame.mouse.get_pos()
            get_cord(pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: x = max(x - 1, 0)
            if event.key == pygame.K_RIGHT: x = min(x + 1, 8)
            if event.key == pygame.K_UP: y = max(y - 1, 0)
            if event.key == pygame.K_DOWN: y = min(y + 1, 8)
            if event.key in [pygame.K_1, pygame.K_KP1]: val = 1
            if event.key in [pygame.K_2, pygame.K_KP2]: val = 2
            if event.key in [pygame.K_3, pygame.K_KP3]: val = 3
            if event.key in [pygame.K_4, pygame.K_KP4]: val = 4
            if event.key in [pygame.K_5, pygame.K_KP5]: val = 5
            if event.key in [pygame.K_6, pygame.K_KP6]: val = 6
            if event.key in [pygame.K_7, pygame.K_KP7]: val = 7
            if event.key in [pygame.K_8, pygame.K_KP8]: val = 8
            if event.key in [pygame.K_9, pygame.K_KP9]: val = 9
            if event.key == pygame.K_RETURN: flag2 = 1
            if event.key == pygame.K_r:
                grid = [[0]*9 for _ in range(9)]
                rs = error = flag2 = 0
            if event.key == pygame.K_d:
                grid = [
                    [7, 8, 0, 4, 0, 0, 1, 2, 0],
                    [6, 0, 0, 0, 7, 5, 0, 0, 9],
                    [0, 0, 0, 6, 0, 1, 0, 7, 8],
                    [0, 0, 7, 0, 4, 0, 2, 6, 0],
                    [0, 0, 1, 0, 5, 0, 9, 3, 0],
                    [9, 0, 4, 0, 6, 0, 0, 0, 5],
                    [0, 7, 0, 3, 0, 0, 0, 1, 2],
                    [1, 2, 0, 0, 0, 7, 4, 0, 0],
                    [0, 4, 9, 2, 0, 6, 0, 0, 7]
                ]
                rs = error = flag2 = 0

    if flag2 == 1:
        if not solve(grid, 0, 0):
            error = 1
        else:
            rs = 1
        flag2 = 0

    if val != 0:
        if valid(grid, int(y), int(x), val):
            grid[int(y)][int(x)] = val
            flag1 = 0
        else:
            raise_error2()
        val = 0

    if error: raise_error1()
    if rs: result()

    draw()
    if flag1: draw_box()
    instruction()
    pygame.display.update()

pygame.quit()