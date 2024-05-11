import pygame
import json
import time
from pyengine import *


class GameController(metaclass=Singleton):
    
    
    def __init__(self) -> None:
        self.last_time = time.time()
        self.dt = 0
        
        self.frame_rate = 60
        
        self.physics_layer_definitions: dict[str, int] = dict()
        self.physics_layer_contents: list[list[GameObject]] = []
        
        self.input_schema : dict[str, str] = dict()
        
        self.physics_debug : bool
        
        self.initialize()
        
        
    def update(self) -> None:
        self.update_dt()
    
    
    def update_dt(self):
        self.dt = time.time() - self.last_time
        self.dt *= self.frame_rate
        self.last_time = time.time()
        
        
    def initialize(self) -> None:
        self.__load_options()
        
        for i in range(len(self.physics_layer_definitions.keys())):
            self.physics_layer_contents.append([])
    
    
    def get_physics_layer_content(self, physics_layer) -> list:
        physics_layer_number = self.physics_layer_definitions[physics_layer]
        return self.physics_layer_contents[physics_layer_number]
    
    
    def add_physics_layer_content(self, physics_layer, new_content) -> None:
        physics_layer_number = self.physics_layer_definitions[physics_layer]
        self.physics_layer_contents[physics_layer_number].append(new_content)
    
    
    def __load_options(self) -> None:
        with open("./config/options.json") as json_file:
            options : dict = json.load(json_file)
            self.input_schema = options["input_schema"]
            self.physics_layer_definitions = options["physics_layers"]
            self.physics_debug = options["physics_debug"]
