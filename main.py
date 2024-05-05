import pygame
import sys

sys.path.append('./src')
from pyengine import *


class Player(Body):
    
    def __init__(self, position: Vector, size: Vector, sprite : pygame.Surface) -> None:
        super().__init__(position, size, sprite)
        
        self.pace = 3
        self.animator = Animator(self.sprite, self.sprite_surface, Vector(8, 2), 10)
        self.sprite_surface.set_colorkey((255, 255, 255))
    
    def __poll_input(self):
        direction = Vector(0, 0)
        
        key = pygame.key.get_pressed()
        if key[pygame.K_d]:
            direction.x = 1
        if key[pygame.K_a]:
            direction.x = -1
        if key[pygame.K_w]:
            direction.y = -1
        if key[pygame.K_s]:
            direction.y = 1
        
        self.velocity = direction.normalize().scale(self.pace)   
        
    def update(self):
        self.velocity = Vector(0, 0)
        
        self.__poll_input()
        self._move()
        
        if self.velocity.x > 0:
            self.face_right = True
        elif self.velocity.x < 0:
            self.face_right = False
        
        if self.velocity.equals(Vector(0, 0)):
            self.surf = self.animator.update(0, self.face_right)
        else:
            self.surf = self.animator.update(1, self.face_right)


class Tile(GameObject):
    
    def __init__(self, position: Vector, size: Vector, sprite: pygame.Surface) -> None:
        super().__init__(position, size, sprite)
        self.sprite_surface.blit(sprite, position.tuple())
    

# pygame setup
pygame.init()
screen = pygame.display.set_mode((960, 540))
display = pygame.Surface((240, 135))
clock = pygame.time.Clock()
running = True

game_controller = GameController()
player = Player(Vector(100, 100), Vector(8, 16), pygame.image.load("data/sprites/player.png"))
tile = Tile(Vector(150, 100), Vector(16, 16), pygame.image.load("data/sprites/tile.png"))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    game_controller.update()
    player.update()    

    # fill the screen with a color to wipe away anything from last frame
    display.fill("purple")

    # RENDER YOUR GAME HERE
    tile.draw(display)
    player.draw(display)

    # flip() the display to put your work on screen
    surf = (pygame.transform.scale(display, (960, 540)))
    screen.blit(surf, (0, 0))
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
