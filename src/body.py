import pygame
from pyengine import *


class Body(GameObject):
    
    
    def __init__(self, position : Vector, size : Vector, physics_layer: str) -> None:
        super().__init__(position, size, physics_layer)
        
        self.velocity : Vector = Vector(0, 0)
    
    
    def move(self):
        """Move the body with the given velocity. The method automatically ensures constant movement speed
        in spite of frame drops. Collisions are taken care of in accordance with the body's physics layer.

        Args:
            velocity (tuple[float]): The velocity of which the body should move.
        """
        
        # Get time since last frame
        dt = self.__game_controller.dt
        
        # Move in x-direction and check for collisions
        self.position.x += self.velocity.x * dt
        self.collision_rect.set_position(int(self.position.x), self.collision_rect.get_position().y)
        collisions: list[GameObject] = self.collision_rect.check_collision()
        
        # For each collision in x-direction, move rect horizontally out of the collision
        for collision_object in collisions:
            if self.velocity.x > 0 and self.collision_rect.right > collision_object.collision_rect.left:
                self.collision_rect.right = collision_object.collision_rect.left
            elif self.velocity.x < 0 and self.collision_rect.left < collision_object.collision_rect.right:
                self.collision_rect.left = collision_object.collision_rect.right
        self.x = self.collision_rect.get_position().x
        
        # Move in y-direction and check for collisions
        self.position.y += self.velocity.y * dt
        self.collision_rect.set_position(self.collision_rect.get_position().x, int(self.position.y))
        collisions: list[GameObject] = self.collision_rect.check_collision()
        
        # For each collision in y-direction, move rect vertically out of the collision
        for collision_object in collisions:
            if self.velocity.y > 0 and self.collision_rect.bottom > collision_object.collision_rect.top:
                self.rect.bottom = collision_object.collision_rect.top
            elif self.velocity.y < 0 and self.collision_rect.top < collision_object.collision_rect.bottom:
                self.rect.top = collision_object.collision_rect.bottom
        self.y = self.collision_rect.get_position().y
