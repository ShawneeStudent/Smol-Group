import pygame


class Characters:
    def __init__(self, x, y, world_x, world_y, speed, spritesize, cur_frame=0, cur_direct=0):
        self.x = x
        self.y = y
        self.wx = world_x
        self.wy = world_y
        self.speed = speed
        self.sprite = spritesize
        self.frame = cur_frame
        self.direct = cur_direct

    def draw(self, surf, img):
        surf.blit(img, (self.x, self.y), (self.frame * self.sprite, self.direct * self.sprite, self.sprite, self.sprite))








class Player(Characters):

    def __init__(self, x, y, world_x, world_y, speed, spritesize, cur_frame, cur_direct):


        super().__init__(self, x, y, world_x, world_y, speed, spritesize, cur_frame, cur_direct)

    def draw(self, surf, img):
        super().draw(self, surf, img, spritesize, cur_frame, cur_direct)

    def update(self, dt):
        event = pygame.event.poll()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.y -= self.speed * dt
                self.direct = 2
            if event.key == pygame.K_a:
                self.x -= self.speed * dt
                self.direct = 3
            if event.key == pygame.K_s:
                self.y += self.speed * dt
                self.direct = 0
            if event.key == pygame.K_d:
                self.x += speed * dt
                self.direct = 1

        self.frame += 1
        if self.frame > 3:
            self.frame = 1

class Enemy(Characters):

    def __init__(self, x, y, world_x, world_y, speed, spritesize, cur_frame, cur_direct):


        super().__init__(self, x, y, world_x, world_y, speed, spritesize, cur_frame, cur_direct)
        self.timer_left = 3
        self.timer_right = 3
    def draw(self, surf, img):
        super().draw(self, surf, img, spritesize, cur_frame, cur_direct)

    def update(self, dt):
        if self.timer_left > 0:

            self.x -= 5 * dt

            self.timer_left -= 1 * dt

            self.timer_right = 3
        else:
            self.x += 5 * dt

            self.timer_right -= 1 * dt


        if self.timer_right <= 0:
            self.timer_left = 3

done = False
win = pygame.display.set_mode((800, 600))

x = 50
y = 50

x2 = 700
y2 = 500

clock = pygame.time.Clock()

p = pygame.image.load("Sprites\\BATS.png")
e = pygame.image.load("Sprites\\Asteroid Brown.png")
while not done:
    win.fill((0, 0, 0))
    dt = clock.tick() / 100
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        done = True
    player = Player(x, y, 0, 0, 50, 128, 1, 0)
    player.update(dt)
    player.draw(win, p)
    pygame.display.flip()
pygame.quit()