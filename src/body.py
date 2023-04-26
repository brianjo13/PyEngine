import pygame
from objects.game_object import GameObject


class Body(GameObject):
    
    def __init__(self, width: float, height: float, x: float, y: float, physics_layer: str) -> None:
        super().__init__(width, height, x, y, physics_layer)
    
    def move(self, velocity: tuple[float]):
        """Move the body with the given velocity. The method automatically ensures constant movement speed
        in spite of frame drops. Collisions are taken care of in accordance with the body's physics layer.

        Args:
            velocity (tuple[float]): The velocity of which the body should move.
        """
        
        # Get time since last frame as well as the possible objects
        # to collide with from the game controller
        dt = self.game_controller.dt
        possible_collisions = self.game_controller.get_physics_layer_content(self.physics_layer)
        
        # Move in x-direction and check for collisions
        self.x += velocity[0] * dt
        self.rect.x = int(self.x)
        collisions: list[GameObject] = self.check_collision(possible_collisions)
        
        # For each collision in x-direction, move rect horizontally out of the collision
        for collision_object in collisions:
            if velocity[0] > 0 and self.rect.right > collision_object.rect.left:
                self.rect.right = collision_object.rect.left
            elif velocity[0] < 0 and self.rect.left < collision_object.rect.right:
                self.rect.left = collision_object.rect.right
        self.x = self.rect.x
        
        # Move in y-direction and check for collisions
        self.y += velocity[1] * dt
        self.rect.y = int(self.y)
        collisions: list[GameObject] = self.check_collision(possible_collisions)
        
        # For each collision in y-direction, move rect vertically out of the collision
        for collision_object in collisions:
            if velocity[1] > 0 and self.rect.bottom > collision_object.rect.top:
                self.rect.bottom = collision_object.rect.top
            elif velocity[1] < 0 and self.rect.top < collision_object.rect.bottom:
                self.rect.top = collision_object.rect.bottom
        self.y = self.rect.y
