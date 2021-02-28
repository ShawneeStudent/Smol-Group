import pygame


class Characters:
    def __init__(self, x, y, screen_x, screen_y, speed, spritesize, img, camera_x, camera_y, cur_frame=0, cur_direct=0):
        self.sx = screen_x
        self.sy = screen_y
        self.speed = speed
        self.sprite = spritesize
        self.frame = cur_frame
        self.direct = cur_direct
        self.x = x
        self.y = y
        self.img = img
        self.camx = camera_x
        self.camy = camera_y
    def draw(self, surf, world_width, world_height):


        position = self.convert_world_position_to_screen(self.x, self.y)

        surf.blit(self.img, (position), (int(self.frame * self.sprite), int(self.direct * self.sprite),
                                                    self.sprite, self.sprite))

        if self.x <= 0:
            self.x = 1
        if self.y <= 0:
            self.y = 0
        if self.x >= world_width:
            self.x = world_width
        if self.y >= world_height:
            self.y = world_height

    def convert_screen_position_to_world(self, x, y, to_int = True):
        world_x = x + self.camx
        world_y = y + self.camy
        if to_int:
            world_x = int(world_x)
            world_y = int(world_y)
        return (world_x, world_y)

    def convert_world_position_to_screen(self, x, y, to_int = True):
        screen_x = x - self.camx
        screen_y = y - self.camy
        if to_int:
            screen_x = int(screen_x)
            screen_y = int(screen_y)
        return (screen_x, screen_y)






class Player(Characters):

    def __init__(self, x, y, world_x, world_y, speed, spritesize, img, camera_x, camera_y, cur_frame, cur_direct):


        super().__init__(x, y, world_x, world_y, speed, spritesize, img, camera_x, camera_y, cur_frame, cur_direct)
        self.timer = 1

    def draw(self, surf, world_w, world_h):
        super().draw(surf, world_w, world_h)

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

    def __init__(self, x, y, world_x, world_y, speed, spritesize, img, camera_x, camera_y, cur_frame, cur_direct):


        super().__init__(x, y, world_x, world_y, speed, spritesize, img, camera_x, camera_y, cur_frame, cur_direct)
        self.timer_left = 15
        self.timer_right = 15
        self.velocity = [0, 0]
        self.is_in_range = False

    def draw(self, surf, world_w, world_h):
        super().draw(surf, world_w, world_h)

    def update(self, dt):
        if not self.is_in_range:
            if self.timer_left > 0:

                self.x -= 10 * dt

                self.timer_left -= 1 * dt

                self.timer_right = 15
            else:
                self.x += 10 * dt

                self.timer_right -= 1 * dt



        if self.timer_right <= 0:
            self.timer_left = 15

    def hit_detection(self, x, y, other_sprite):
        x2 = x - other_sprite / 2
        y2 = y - other_sprite / 2
        d = self.distance(int(self.x + (self.sprite / 2)), int(self.y + (self.sprite / 2)), x2, y2)
        if d <= 400 and d > 300:

            self.is_in_range = True
            offset = self.get_direction_towards(x, y)
            self.x += (offset[0] * dt) * self.speed
            self.y += (offset[1] * dt) * self.speed
        elif d < 300:


            if x2 > int(self.x + (self.sprite / 2)):
                self.x += self.speed * dt
            if x2 < int(self.x + (self.sprite / 2)):
                self.x -= self.speed * dt
            if y2 > int(self.y + (self.sprite / 2)):

                self.y += self.speed * dt
            if y2 < int(self.y + (self.sprite / 2)):
                self.y -= self.speed * dt

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
