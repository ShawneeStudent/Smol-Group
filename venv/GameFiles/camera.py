import pygame


class Camera:
    """Camera that follows player inside map_obj [Non-Vector Version]"""
    def __init__(self, width, height, gameManager):
        # gameManager class instance
        self.game_manager = gameManager
        # camera size
        self.cam_w = width
        self.cam_h = height
        # camera rect
        self.camera = pygame.Rect(0, 0, self.cam_w, self.cam_h)

    def draw_movement(self, map_obj):
        # camera movement: moved (newly drawn) rect shifted by (0, 0)
        return map_obj.rect.move(self.camera.topleft)

    def update(self, target):
        # coordinates, in (reverse directional) relation to the offset
        x = -target.rect.x + int(self.game_manager.scr_w / 2)
        y = -target.rect.y + int(self.game_manager.scr_h / 2)

        # -- CAM SCROLL BOUNDARY/BORDER --
        # camera scrolling limit => map_obj size
        # left
        x = min(0, x)
        # right
        x = max(-(self.cam_w - self.game_manager.scr_w), x)
        # top
        y = min(0, y)
        # bottom
        y = max(-(self.cam_h - self.game_manager.scr_h), y)

        # updated camera rect
        self.camera = pygame.Rect(x, y, self.cam_w, self.cam_h)
