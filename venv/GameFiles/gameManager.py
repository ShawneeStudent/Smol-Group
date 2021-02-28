import pygame

import camera
import characters

from map import Map
from camera import Camera


class GameManager:
    """Game Manager"""
    def __init__(self):

        # -- INITIALIZATION --
        pygame.init()

        # -- COLORS --
        self.black = (0, 0, 0)
        self.green = (0, 255, 0)

        # -- TIME --
        self.g_clock = pygame.time.Clock()
        self.delta_time = 0

        # -- DISPLAY --
        # screen
        self.scr_w = 1024
        self.scr_h = 768
        self.screen = pygame.display.set_mode((self.scr_w, self.scr_h))
        pygame.display.set_caption("Smol Game / Lab 5 / ETGG1802 / Prof: Jason / Team: Lane - Tanim - Evan | FPS: "
                                   + str(int(self.g_clock.get_fps())))
        img1 = pygame.image.load("Sprites\\BATS.png")
        img2 = pygame.image.load("Sprites\\Asteroid Brown.png")
        # background
        self.background = pygame.Surface(self.screen.get_size())
        self.background.fill(self.black)
        self.background.convert()

        # -- IMAGES / SPRITES --

        # -- TEXT FONTS --
        self.font_type = pygame.font.get_default_font()

        # -- CLASS INSTANCES --
        # camera class instance
        self.camera = Camera(self.scr_w, self.scr_h, self)
        # player class instance
        self.player = characters.Player(300, 300, ((self.scr_w / 2) - 32), ((self.scr_h / 2) - 32), 50, 32, img1, self.camera.x, self.camera.y, 1, 0)
        # enemy class instance
        self.enemy = characters.Enemy(800, 800, 0, 0, 10, 160, img2, self.camera.x, self.camera.y, 0, 0)
        # map class instance
        self.map = Map("smol_map.tmx")


        # -- GAME LOOP --
        self.run = True
        while self.run:

            # - UPDATES
            # Time in seconds since the last update
            self.delta_time = self.g_clock.tick(100) / 1000
            self.enemy.update(self.delta_time)
            self.player.update(self.delta_time)
            self.enemy.hit_detection(self.player.x, self.player.y, self.player.sprite)

            # - USER INPUT
            # event handling
            self.evt = pygame.event.poll()
            if self.evt.type == pygame.QUIT:
                self.run = False
            elif self.evt.type == pygame.KEYDOWN:
                if self.evt.key == pygame.K_ESCAPE:
                    self.run = False

            # - DRAW
            self.player.draw(self.map, self.map.getMapSize()[0], self.map.getMapSize()[1])
            self.enemy.draw(self.map, self.map.getMapSize()[0], self.map.getMapSize()[1])
            # screen
            self.screen.blit(self.background, (0, 0))
            self.map.render(self.background, (0,0), self.scr_w, self.scr_h)
            # game objects

            # text

            # camera

            self.camera.update(self.player, self.player.sprite, self.player.sprite)




            # - UPDATE DISPLAY
            pygame.display.flip()

        # -- EXIT GAME --
        pygame.quit()

    def draw_texts(self, text, size, x, y):
        """Draw and Display Texts"""
        font = pygame.font.Font(self.font_type, size)
        text_surf = font.render(text, True, self.green)
        text_rect = text_surf.get_rect()
        text_rect.center = (x, y)
        self.screen.blit(text_surf, text_rect)
