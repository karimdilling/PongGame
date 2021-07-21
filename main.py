import pygame

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

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    clock.tick(FPS)