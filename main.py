import pygame
from pygame.constants import K_DOWN, K_UP
import random
import os

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

# Define window
WIN_WIDTH = 1280
WIN_HEIGHT = 960
WINDOW = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Pong Game")
WINDOW_RECT = pygame.Rect(0, 0 , WIN_WIDTH, WIN_HEIGHT) # used for the clamp method

# Setup game clock
clock = pygame.time.Clock()
FPS = 60

# Define rectangles for both players and the ball (gets later drawn to circular shape)
player1 = pygame.Rect(0, WIN_HEIGHT / 2 - 70, 20, 140)
player2 = pygame.Rect(WIN_WIDTH - 20, WIN_HEIGHT / 2 - 70, 20, 140)
ball = pygame.Rect(WIN_WIDTH / 2 - 20, WIN_HEIGHT / 2 - 20, 40, 40)

# Define speeds
ball_speed_x = 5
ball_speed_y = 5
player1_speed = 8
player2_speed = 5

# Score of the players
points_player1 = 0
points_player2 = 0
font_color = (255, 255, 255)
font = pygame.font.Font(None, 36)
loc_score_player1 = (player1.right + 10, 10)
loc_score_player2 = (WIN_WIDTH - 150, 10)

# Implement sounds
current_dir = os.path.dirname(os.path.abspath(__file__))
hit_sound = pygame.mixer.Sound(current_dir + "/sounds/hit_sound.wav")
scored_sound = pygame.mixer.Sound(current_dir + "/sounds/scored_sound.wav")

def draw_shapes():
    pygame.draw.rect(WINDOW, "white", player1)
    pygame.draw.rect(WINDOW, "white", player2)
    pygame.draw.ellipse(WINDOW, "white", ball)

def setup_keylistener():
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[K_UP]:
        player1.y -= player1_speed
    if keys_pressed[K_DOWN]:
        player1.y += player1_speed

def handle_quitting():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

def handle_ball_movement():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    if ball.top <= 0 or ball.bottom >= WIN_HEIGHT:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= WIN_WIDTH:
        update_score()
        reset_ball()
        pygame.mixer.Sound.play(scored_sound)
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x *= -1
        pygame.mixer.Sound.play(hit_sound)

def control_player2_ai():
    if player2.top< ball.y:
        player2.top += player2_speed
    if player2.bottom > ball.y:
        player2.bottom -= player2_speed

def reset_ball():
    global ball_speed_x, ball_speed_y
    ball.center = (WIN_WIDTH / 2 - 20, WIN_HEIGHT / 2 - 20)
    ball_speed_x *= random.choice((-1, 1))
    ball_speed_y *= random.choice((-1, 1))

def update_score():
    global points_player1, points_player2
    if ball.left <= 0:
        points_player2 += 1
        print(points_player2)
    if ball.right >= WIN_WIDTH:
        points_player1 += 1
        print(points_player1)

def setup_score_labels():
    WINDOW.blit(font.render(f"Player 1: {points_player1}", True, font_color), loc_score_player1)
    WINDOW.blit(font.render(f"Player 2: {points_player2}", True, font_color), loc_score_player2)

# Game loop
while True:
    handle_quitting()
    player1.clamp_ip(WINDOW_RECT) # handles player bars to not being able to move out of the window
    player2.clamp_ip(WINDOW_RECT)
    setup_keylistener()
    handle_ball_movement()
    control_player2_ai()
    WINDOW.fill("black")
    draw_shapes()
    setup_score_labels()
    pygame.display.update()
    clock.tick(FPS)