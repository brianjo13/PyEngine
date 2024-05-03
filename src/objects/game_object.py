from __future__ import annotations
import pygame
from pyengine import *


class GameObject(object):
    
    
    def __init__(self, position : Vector, size : Vector, sprite, physics_layer: str = "physics_layer_1", collision_rect : CollisionRect = None) -> None:
        self.__game_controller = GameController()
        
        self.position : Vector = position
        self.size : Vector = size
        
        self.sprite_surface : pygame.Surface = pygame.Surface((size.x, size.y))
        self.sprite : pygame.Surface = sprite
        self.face_right : bool = True

        self.collision_rect: CollisionRect = collision_rect if collision_rect else CollisionRect(self, size, offset=Vector(0, 0), physics_layer=physics_layer)
        self.last_collisions: list[GameObject] = []
    
    
    def collide(self, collision_object: GameObject) -> None:
        if collision_object not in self.last_collisions:
            self.last_collisions.append(collision_object)
        if self not in collision_object.last_collisions:
            collision_object.last_collisions.append(self)
    
    
    def draw(self, target) -> None:
        target.blit()
