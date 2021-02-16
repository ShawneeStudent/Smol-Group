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
        surf.blit(img, (int(self.x), int(self.y)), (int(self.frame * self.sprite), int(self.direct * self.sprite),
                                                    self.sprite, self.sprite))








class Player(Characters):

    def __init__(self, x, y, world_x, world_y, speed, spritesize, cur_frame, cur_direct):


        super().__init__(x, y, world_x, world_y, speed, spritesize, cur_frame, cur_direct)
        self.timer = 1
    def draw(self, surf, img):
        super().draw(surf, img)

    def update(self, dt):
        frame_delay = 1
        all_keys = pygame.key.get_pressed()
        if all_keys[pygame.K_w]:
            self.y -= self.speed * dt
            self.direct = 2
        if all_keys[pygame.K_a]:
            self.x -= self.speed * dt

            self.direct = 3
        if all_keys[pygame.K_s]:
            self.y += self.speed * dt
            self.direct = 0
        if all_keys[pygame.K_d]:
            self.x += self.speed * dt
            self.direct = 1
        self.timer -= dt
        if self.timer <= 0:


            self.frame += 1

            self.timer = frame_delay
        if self.frame > 3:
            self.frame = 1

class Enemy(Characters):

    def __init__(self, x, y, world_x, world_y, speed, spritesize, cur_frame, cur_direct):


        super().__init__(x, y, world_x, world_y, speed, spritesize, cur_frame, cur_direct)
        self.timer_left = 15
        self.timer_right = 15
        self.velocity = [0, 0]
        self.is_in_range = False
    def draw(self, surf, img):
        super().draw(surf, img)

    def update(self, dt):
        if not self.is_in_range:
            if self.timer_left > 0:

                self.x -= 10 * dt

                self.timer_left -= 1 * dt

                self.timer_right = 15
            else:
                self.x += 10 * dt

                self.timer_right -= 1 * dt
        if self.y - (self.sprite / 2) < 1:
            self.y = 1 + (self.sprite / 2)


        if self.timer_right <= 0:
            self.timer_left = 15

    def hit_detection(self, x, y):
        d = enemy.distance(self.x, self.y, x, y)
        if d <= 400:

            self.is_in_range = True
            offset = enemy.get_direction_towards(x, y)
            self.x += (offset[0] * dt) * self.speed
            self.y += (offset[1] * dt) * self.speed


        else:
            self.is_in_range = False

    def get_direction_towards(self, tgt_x, tgt_y):

        horiz_offset = tgt_x - self.x
        vert_offset = tgt_y - self.x


        magnitude = (horiz_offset ** 2 + vert_offset ** 2) ** 0.5
        if magnitude > 0:
            horiz_offset /= magnitude
            vert_offset /= magnitude

        return (horiz_offset, vert_offset)


    def distance(self, x, y, x2, y2):
        a = x - x2
        b = y - y2
        c = (a ** 2 + b ** 2) ** 0.5
        return c