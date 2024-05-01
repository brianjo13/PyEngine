import pygame
from ..pyengine import *


class Animator:
    
    
    def __init__(self, sprite_sheet : pygame.Surface, surface : pygame.Surface, image_count : Vector, switch_time : float) -> None:
        self.__game_controller : GameController = GameController()
        
        self.sprite_sheet : pygame.Surface = sprite_sheet
        self.surface : pygame.Surface = surface
        self.image_count : Vector = image_count
        self.switch_time : float = switch_time
        self.total_time : float = 0
        self.current_image : Vector = Vector(0, 0)
        
    
    def update(self, row : int, face_right : bool, image : int = -1):
        dt = self.__game_controller.dt
        
        self.current_image.y = row
        self.total_time += dt
        
        if image >= 0:
            self.current_image.x = image
        else:
            if self.total_time >= self.switch_time:
                self.total_time -= self.switch_time
                self.current_image.x += 1
                
                if self.current_image.x >= self.image_count.x:
                    self.current_image.x = 0
        
        if face_right:
            sprite_sheet_copy = pygame.transform.flip(self.sprite_sheet, False, False)
            self.surface.blit(
                sprite_sheet_copy,
                (- self.current_image.x * self.surface.get_width(),
                 - self.current_image.y * self.surface.get_height())
            )
        
        else:
            sprite_sheet_copy = pygame.transform.flip(self.sprite_sheet, True, False)
            self.surface.blit(
                sprite_sheet_copy,
                ((self.current_image.x - self.image_count.x + 1) * self.surface.get_width(),
                 - self.current_image.y * self.surface.get_height())
            )
        
        return self.surface
