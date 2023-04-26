from __future__ import annotations

import pygame

from game_controller import GameController


class GameObject(object):
    
    def __init__(self, width: float, height: float, x: float, y: float, physics_layer: str) -> None:
        self.game_controller = GameController()
        
        self.width: float = width
        self.height: float = height
        self.x: float = x
        self.y: float = y
        
        self.rect: pygame.Rect = pygame.Rect(x, y, width, height)
        
        self.physics_layer: str = physics_layer
        
        self.last_collisions: list[GameObject] = []
        
    def check_collision(self, possible_collisions: list[GameObject]) -> list[GameObject]:
        new_collisions: list[GameObject] = []
        
        for possible_collision in possible_collisions:
            if self.rect.colliderect(possible_collision.rect):
                new_collisions.append(possible_collision)
                self.collide(possible_collision)
        
        return new_collisions
    
    def collide(self, collision_object: GameObject) -> None:
        self.last_collisions.append(collision_object)
        collision_object.last_collisions.append(self)
