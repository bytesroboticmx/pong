import pygame
from pygame.locals import *

# Configuración de la pantalla
WIDTH = 640
HEIGHT = 480

# Configuración de los colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Inicialización de Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Posiciones y velocidades iniciales
player_pos = [50, HEIGHT // 2 - 50]
opponent_pos = [WIDTH - 50, HEIGHT // 2 - 50]
ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_vel = [5, 5]
paddle_vel = 5

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[K_UP]:
        player_pos[1] -= paddle_vel
    if keys[K_DOWN]:
        player_pos[1] += paddle_vel

    # Actualizar la posición de la pelota
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # Dibujar los objetos en la pantalla
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, Rect(player_pos[0], player_pos[1], 10, 100))
    pygame.draw.rect(screen, WHITE, Rect(opponent_pos[0], opponent_pos[1], 10, 100))
    pygame.draw.ellipse(screen, WHITE, Rect(ball_pos[0] - 10, ball_pos[1] - 10, 20, 20))

    # Actualizar la pantalla
    pygame.display.flip()
    clock.tick(60)

# Salir del juego
pygame.quit()
