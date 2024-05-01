import pygame
from pyengine import *

class CollisionRect(pygame.Rect):
    
    
    def __init__(self, parent : GameObject, position : Vector, size : Vector, offset : Vector = Vector(0, 0), physics_layer : str = "physics_layer_1") -> None:
        super.__init__(position.x, position.y, size.x, size.y)
        self.__game_controller = GameController()
        
        self.parent = parent
        self.physics_layer: str = physics_layer
        
        self._offset : Vector = offset
    
    
    def set_position(self, x, y) -> None:
        self.x = x + self._offset
        self.y = y + self._offset
    
    
    def get_position(self) -> Vector:
        return Vector(self.x - self._offset, self.y - self._offset)
        
        
    def check_collision(self) -> list[GameObject]:
        new_collisions: list[GameObject] = []
        
        possible_collisions = self.__game_controller.get_physics_layer_content(self.physics_layer)
        for possible_collision in possible_collisions:
            if self.colliderect(possible_collision.collision_rect):
                new_collisions.append(possible_collision)
                self.parent.collide(possible_collision)
        
        return new_collisions
