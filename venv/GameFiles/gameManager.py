import pygame

import camera
from characters import Characters
from player import Player
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
        # background
        self.background = pygame.Surface(self.screen.get_size())
        self.background.fill(self.black)
        self.background.convert()

        # -- IMAGES / SPRITES --

        # -- TEXT FONTS --
        self.font_type = pygame.font.get_default_font()

        # -- CLASS INSTANCES --
        # character class instance
        self.characters = Characters()
        # player class instance
        self.player = Player(300, 300, ((self.scr_w / 2) - 32), ((self.scr_h / 2) - 32), 50, 32, img1, 1)
        # enemy class instance
        self.enemy = Enemy(800, 800, 0, 0, 10, 160)
        # map class instance
        self.map = Map("smol_map.tmx")
        # camera class instance
        self.camera = Camera(self.scr_w, self.scr_h, self)

        # -- GAME LOOP --
        self.run = True
        while self.run:

            # - UPDATES
            # Time in seconds since the last update
            self.delta_time = self.g_clock.tick(100) / 1000
            self.enemy.update(self.delta_time)
            self.player.update(self.delta_time)
            self.enemy.hit_detection(player.x, player.y, player.sprite)
            self.player.draw()
            # - USER INPUT
            # event handling
            self.evt = pygame.event.poll()
            if self.evt.type == pygame.QUIT:
                self.run = False
            elif self.evt.type == pygame.KEYDOWN:
                if self.evt.key == pygame.K_ESCAPE:
                    self.run = False

            # - DRAW
            # screen
            self.screen.blit(self.background, (0, 0))
            self.map.render(self.background, (0,0), self.scr_w, self.scr_h)
            # game objects

            # text

            # camera
<<<<<<< Updated upstream
            self.camera.update(self.player, self.player.sprite, self.player.sprite)
=======
            # self.camera.update(self.player, player.spritesize, player.spritesize)
>>>>>>> Stashed changes

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
