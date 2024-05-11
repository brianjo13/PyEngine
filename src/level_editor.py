import pygame
import time
import json

from pyengine import *


class LevelEditor:
    
    
    def __init__(self) -> None:
        self.__frame_rate = 60
        self.__last_time = time.time()
        self.__dt = 0
        
        self.__screen : pygame.Surface
        self.__screen_size : Vector = Vector(960, 540)
        
        self.__display : pygame.Surface
        self.__display_size : Vector = Vector(480, 270)
        
        self.__canvas : pygame.Surface
        self.__canvas_scale : float = 4
        self.__canvas_scroll : Vector = Vector(0, 0)
        
        self.__clock : pygame.time.Clock
        self.__running : bool
        
        self.__input_schema : dict[str, str]
    
    
    def run(self):
        self.__initialize()

        while self.__running:
            # poll for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__running = False
            
            # fill the screen with a color to wipe away anything from last frame
            self.__display.fill("purple")
            self.__canvas.fill("blue")
            
            self.__update()
            self.__draw()

            # flip() the display to put your work on screen
            display_surf = pygame.transform.scale(self.__display, self.__screen_size.tuple())
            self.__screen.blit(display_surf, (0, 0))
            pygame.display.flip()

            self.__clock.tick(60)  # limits FPS to 60

        pygame.quit()
    
    
    def __initialize(self):
        pygame.init()
        
        # testing
        self.tile = Tile(0, Vector(150, 100), Vector(16, 16), pygame.image.load("data/sprites/tile.png"))
        
        self.__load_options()
        
        self.__screen = pygame.display.set_mode(self.__screen_size.tuple())
        self.__display = pygame.Surface(self.__display_size.tuple())
        self.__canvas = pygame.Surface(self.__screen_size.scale(1 / self.__canvas_scale).tuple())
        
        self.__clock = pygame.time.Clock()
        self.__running = True
    
    
    def __update(self):
        self.__update_dt()
        
        # testing
        key = pygame.key.get_pressed()
        if key[pygame.key.key_code(self.__input_schema["right"])]:
            self.__canvas_scroll.x += self.__dt
        if key[pygame.key.key_code(self.__input_schema["left"])]:
            self.__canvas_scroll.x -= self.__dt
        if key[pygame.key.key_code(self.__input_schema["up"])]:
            self.__canvas_scroll.y -= self.__dt
        if key[pygame.key.key_code(self.__input_schema["down"])]:
            self.__canvas_scroll.y += self.__dt
    
    
    def __update_dt(self):
        self.__dt = time.time() - self.__last_time
        self.__dt *= self.__frame_rate
        self.__last_time = time.time()
    
    
    def __draw(self):
        # testing
        self.tile.draw(self.__canvas, self.__canvas_scroll)
        
        canvas_surf = pygame.transform.scale(self.__canvas, self.__display_size.tuple())
        self.__display.blit(canvas_surf, (0, 0))
    
    
    def __load_options(self) -> None:
        with open("./config/options.json") as json_file:
            options : dict = json.load(json_file)
            self.__input_schema = options["input_schema"]


if __name__ == "__main__":
    editor = LevelEditor()
    editor.run()
