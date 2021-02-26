import pygame


class Camera:
    """Camera that follows player inside map_obj [Non-Vector Version]"""
    def __init__(self, width, height, gameManager):
        # -- CLASS INSTANCES --
        # gameManager class instance
        self.game_manager = gameManager

        # -- CAMERA SETUP --
        # size
        self.cam_w = width
        self.cam_h = height
        # (x, y) coordinates
        self.x = 0
        self.y = 0
        # rect
        self.camera = pygame.Rect(0, 0, self.cam_w, self.cam_h)

    def draw_movement(self, map_obj):
        # camera movement: moved (newly drawn) rect shifted by (0, 0)
        return map_obj.rect.move(self.camera.topleft)

    def update(self, target):
        # coordinates, in (reverse directional) relation to the offset
        self.x = -target.rect.x + int(self.game_manager.scr_w / 2)
        self.y = -target.rect.y + int(self.game_manager.scr_h / 2)

        # -- CAM SCROLL BOUNDARY/BORDER --
        # camera scrolling limit => map_obj size
        # left
        self.x = min(0, self.x)
        # right
        self.x = max(-(self.cam_w - self.game_manager.scr_w), self.x)
        # top
        self.y = min(0, self.y)
        # bottom
        self.y = max(-(self.cam_h - self.game_manager.scr_h), self.y)

        # updated camera rect
        self.camera = pygame.Rect(self.x, self.y, self.cam_w, self.cam_h)

    def position(self):
        """ Camera Position in a tuple """
        pass

