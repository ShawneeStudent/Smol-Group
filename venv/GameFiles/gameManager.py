import pygame
from characters import Characters
from map import Map


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

        # enemy class instance

        # map class instance
        self.map = Map("sample_map.tmx")
        # camera class instance

        # -- GAME LOOP --
        self.run = True
        while self.run:

            # - UPDATES
            # Time in seconds since the last update
            self.delta_time = self.g_clock.tick(100) / 1000

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
            # game objects

            # text

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
