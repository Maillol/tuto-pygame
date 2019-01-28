import pygame

from itertools import cycle



SCREEN_WIDTH = 800
SCREEN_HEIGHT = 480
BOARD_WIDTH = SCREEN_WIDTH
BOARD_HEIGHT = SCREEN_HEIGHT
BOARD_SIZE = (BOARD_WIDTH, BOARD_HEIGHT)




class Case(pygame.sprite.Sprite):
    """

    x0123456
    0   a
    1   
    2d     b
    3   
    4g  c  e
    5 
    6   f

    """

    size = 120
    key_color = (0, 255, 0)

    def __init__(self, color, x, y, z):
        pygame.sprite.Sprite.__init__(self)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill(self.key_color)
        self.image.set_colorkey(self.key_color)

        offset_2 = int(self.size / 2) 
        offset_3 = int(self.size / 3)

        a = (offset_2, 0)
        b = (self.size, offset_3)
        c = (offset_2, offset_3 * 2)
        d = (0, offset_3)
        e = (self.size, offset_3 * 2)
        f = (offset_2, self.size)
        g = (0, offset_3 * 2)

        pygame.draw.polygon(
            self.image, 
            [min(e + 15, 255) for e in color],
            (a, b, c, d)
        )

        pygame.draw.polygon(
            self.image, 
            color,
            (c, f, g, d)
        )

        pygame.draw.polygon(
            self.image, 
            [max(e - 15, 0) for e in color],
            (b, e, f, c)
        )

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()

        self.rect.x = x * offset_2 + (y * offset_2)
        self.rect.y = (BOARD_HEIGHT / 2) + (y * offset_3)  - x * offset_3 - z * offset_3

    def update(self):
        pass


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background = pygame.Surface(BOARD_SIZE)
background.fill((255,255,255)) # fill white


MAINLOOP = True
FPS = 30


GROUP = pygame.sprite.Group()


colors = cycle(
    ((0, 200, 20), (0, 20, 200))
)


for x in range(3, 0, -1):
    for y in range(1, 4):
        GROUP.add(Case(next(colors), x, y, 0))


GROUP.add(Case((43, 12, 65), 3, 2, 1))
GROUP.add(Case((43, 12, 65), 3, 3, 1))
GROUP.add(Case((43, 12, 65), 2, 2, 1))
GROUP.add(Case((43, 12, 65), 3, 2, 2))


clock = pygame.time.Clock()

while MAINLOOP:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            MAINLOOP = False  # pygame window closed by user
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                MAINLOOP = False # user pressed ESC


    screen.blit(background, (0, 0))

    GROUP.draw(screen)

    pygame.display.set_caption(f"[FPS]: {clock.get_fps():.2f}")

    clock.tick(FPS)
    pygame.display.flip()        # flip the screen
