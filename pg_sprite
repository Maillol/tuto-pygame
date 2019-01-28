import pygame


pygame.init()

screen = pygame.display.set_mode((800,480))

background = pygame.Surface((screen.get_size()))
background.fill((255,255,255)) # fill white

clock = pygame.time.Clock()
mainloop = True
FPS = 30


from dataclasses import dataclass 


@dataclass
class Velocity:
    _x: int 
    _y: int
    min_x: int
    min_y: int
    max_x: int
    max_y: int

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, x):
        self._x = x
        if self._x > self.max_x:
            self._x = self.max_x
        elif self._x < self.min_x:
            self._x = self.min_x
 
    @y.setter
    def y(self, y):
        self._y = y
        if self._y > self.max_y:
            self._y = self.max_y
        elif self._y < self.min_y:
            self._y = self.min_y
 


class Block(pygame.sprite.Sprite):

    def __init__(self, color, x, y, width, height):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity = Velocity(0, 0, -20, -20, 20, 20)

    def update(self):
        if self.velocity.x > 0: 
            self.velocity.x += 1
        else:
            self.velocity.x -= 1

        if self.velocity.y > 0: 
            self.velocity.y += 1
        else:
            self.velocity.y -= 1

        self.rect.move_ip(self.velocity.x, self.velocity.y)
        if self.rect.x >= 800:
            self.velocity.x = -1
        elif self.rect.x < 0:
            self.velocity.x = 1
        if self.rect.y >= 480:
            self.velocity.y = -1
        elif self.rect.y < 0:
            self.velocity.y = 1


blocks = pygame.sprite.Group()
colors = [
    (30, 60, 30),
    (60, 60, 30),
    (90, 60, 60),
    (30, 30, 60),
    (60, 30, 90),
    (90, 30, 90),
    (30, 90, 30),
    (60, 90, 30),
    (90, 90, 60),
    (30, 30, 60),
    (60, 30, 90),
    (90, 30, 90),
    (30, 30, 60),
    (60, 30, 90),
    (90, 30, 90)
] * 2

for i in range(0, 400, 100):
    for j in range(0, 400, 100):
        blocks.add(
            Block(colors.pop(), i, j, 20, 20)
        )


while mainloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False  # pygame window closed by user
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop = False # user pressed ESC

    screen.blit(background, (0, 0))
    
    blocks.update()    
    blocks.draw(screen)
    pygame.display.set_caption(f"[FPS]: {clock.get_fps():.2f}")


    clock.tick(FPS)
    pygame.display.flip()        # flip the screen
