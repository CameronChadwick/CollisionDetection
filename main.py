import pygame
import random

# create color constants
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
COLORS = [BLACK, GREEN, RED, BLUE]

# width by height
FPS = 60
DISPLAY_WIDTH = 700
DISPLAY_HEIGHT = 500


class Box():
    def __init__(self, display, x, y, width, height, color):
        self.display = display
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.x_speed = 0
        self.y_speed = random.randint(3, 5)
        self.color = color

    def draw_box(self):
        pygame.draw.rect(self.display, self.color, (self.x, self.y, self.width, self.height))

    def update(self):
        self.x += self.x_speed

        if self.x <= 0:
            self.x = 0
        elif self.x + self.width >= DISPLAY_WIDTH:
            self.x = DISPLAY_WIDTH - self.width

    def drop_box(self):
        # increase drop speed when a certain height is achieved
        # if self.y > .33333*DISPLAY_HEIGHT:
        #     self.y_speed += 1

        # respawn above the screen, with a new x, y location and speed
        if self.y > DISPLAY_HEIGHT:
            self.x = random.randrange(0, DISPLAY_WIDTH, 5)
            self.y = random.randrange(-100, 0, 5)
            self.y_speed = random.randint(3, 5)

        # move the box downward
        self.y += self.y_speed

    def is_collided(self, other):
        counter = 0
        if (self.x <= other.x <= self.x+self.width or \
            self.x <= other.x+other.width < self.x+self.width) and \
                (self.y < other.y < self.y + self.width or \
                self.y < other.y+other.width < self.y+self.width):

                counter += 1
                self.color = random.choice(COLORS)
        if counter == 3:
                return True




pygame.init()

screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Game Title")

clock = pygame.time.Clock()

# create player
player_width = 50
x_loc = (DISPLAY_WIDTH - player_width)/2
y_loc = DISPLAY_HEIGHT - 2*player_width
player = Box(screen, x_loc, y_loc, player_width, player_width, BLUE)

# create enemies
enemy_width = 20
enemy_list = []
for i in range(10):
    x_coord = random.randrange(0, DISPLAY_WIDTH, 5)
    random_y = random.randrange(-100, 0, 5)
    enemy = Box(screen, x_coord, random_y, enemy_width, enemy_width, RED)
    enemy_list.append(enemy)

pygame.mouse.set_visible(False)
running = True

while running:

    pos = pygame.mouse.get_pos()
    player.x = pos[0]-.5*player.width
    player.y = pos[1]-.5*player.width

    # pressed_lft = pygame.mouse.get_pressed()[0]
    # print(pressed_lft)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_RIGHT:
        #         player.x_speed = 5
        #     if event.key == pygame.K_LEFT:
        #         player.x_speed = -5
        # if event.type == pygame.KEYUP:
        #     player.x_speed = 0

    screen.fill(WHITE)

    for enemy in enemy_list:
        enemy.draw_box()
        enemy.drop_box()
        if player.is_collided(enemy):
            running = False

    player.draw_box()
    player.update()

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
