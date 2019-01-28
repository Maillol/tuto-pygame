import pygame


pygame.init()

screen = pygame.display.set_mode((800,480))

background = pygame.Surface(screen.get_size())
background.fill((255,255,255)) # fill white

clock = pygame.time.Clock()
mainloop = True
FPS = 30


while mainloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False  # pygame window closed by user
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop = False # user pressed ESC

    screen.blit(background, (0, 0))
    pygame.display.set_caption(f"[FPS]: {clock.get_fps():.2f}")

    clock.tick(FPS)
    pygame.display.flip()        # flip the screen
