import pygame
import json
import time

from objects.game_object import GameObject
from meta_classes.singleton import Singleton


class GameController(metaclass=Singleton):
    
    def __init__(self) -> None:
        self.last_time: time.time()
        self.dt = 0
        
        self.frame_rate = 60
        
        self.physics_layer_definitions: dict[str, int] = dict()
        self.physics_layer_contents: list[list[GameObject]] = []
        
        self.initialize()
        
    def update(self) -> None:
        self.update_dt()
    
    def update_dt(self):
        self.dt = time.time() - self.last_time
        self.dt *= self.frame_rate
        self.last_time = time.time()
        
    def initialize(self) -> None:
        self.load_physics_layer_definitions
    
    def load_physics_layer_definitions(self) -> None:
        with open("../config/physics_layers.json") as json_file:
            self.physics_layer_definitions = json.load(json_file)
    
    def get_physics_layer_content(self, physics_layer) -> list[GameObject]:
        physics_layer_number = self.physics_layer_definitions[physics_layer]
        return self.physics_layer_contents[physics_layer_number]
