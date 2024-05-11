import pygame
from pyengine import *


class Tile(GameObject):
    
    def __init__(self, tile_id : int, position: Vector, size: Vector, sprite: pygame.Surface) -> None:
        super().__init__(position, size, sprite)
        
        self.tile_id : int = id
        self.sprite_surface.blit(sprite, position.tuple())
