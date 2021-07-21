import pygame
from pygame.constants import K_DOWN, K_UP
import random

pygame.init()

# Define window
WIN_WIDTH = 1280
WIN_HEIGHT = 960
WINDOW = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Pong Game")

# Setup game clock
clock = pygame.time.Clock()
FPS = 60

# Define rectangles for both players and the ball (gets later drawn to circular shape)
player1 = pygame.Rect(0, WIN_HEIGHT / 2 - 70, 20, 140)
player2 = pygame.Rect(WIN_WIDTH - 20, WIN_HEIGHT / 2 - 70, 20, 140)
ball = pygame.Rect(WIN_WIDTH / 2 - 20, WIN_HEIGHT / 2 - 20, 40, 40)

# Define speed of the ball
ball_speed_x = 5
ball_speed_y = 5

def draw_shapes():
    pygame.draw.rect(WINDOW, "white", player1)
    pygame.draw.rect(WINDOW, "white", player2)
    pygame.draw.ellipse(WINDOW, "white", ball)

def setup_keylistener():
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[K_UP]:
        player1.y -= 8
    if keys_pressed[K_DOWN]:
        player1.y += 8

def handle_quitting():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

# Game loop
while True:
    handle_quitting()
    setup_keylistener()
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    if ball.top <= 0 or ball.bottom >= WIN_HEIGHT:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= WIN_WIDTH:
        ball_speed_x *= -1
    WINDOW.fill("black")
    draw_shapes()
    pygame.display.update()
    clock.tick(FPS)