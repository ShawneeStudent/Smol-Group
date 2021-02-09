import pygame

# Pygame startup
win_width = 1024
win_height = 768
pygame.display.init()
pygame.font.init()
screen = pygame.display.set_mode((win_width, win_height))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Courier New", 16)
done = False

while not done:
    # Update
    dt = clock.tick() / 1000.0
    evt = pygame.event.poll()
    if evt.type == pygame.QUIT:
        done = True
    elif evt.type == pygame.KEYDOWN:
        if evt.key == pygame.K_ESCAPE:
            done = True

    # Drawing
    screen.fill((64, 64, 64))
    pygame.draw.rect(screen, (0, 0, 0), [0, 0, win_width, win_height])

    pygame.display.flip()

pygame.font.quit()
pygame.display.quit()