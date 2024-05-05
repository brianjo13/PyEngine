from __future__ import annotations
import math


class Vector:
    
    
    def __init__(self, x : float, y : float) -> None:
        self.x : float = x
        self.y : float = y
    
    
    def length(self) -> float:
        return (self.x**2 + self.y**2)**(1/2)

    
    def tuple(self) -> tuple:
        return (self.x, self.y)

    
    def equals(self, other) -> bool:
        return self.x == other.x and self.y == other.y
    
    
    def scale(self, scalar):
        self.x *= scalar
        self.y *= scalar
        return self

    
    def normalize(self):
        if self.x == 0 and self.y == 0:
            return self
        if self.x == 0:
            self.y /= abs(self.y)
            return self
        elif self.y == 0:
            self.x /= abs(self.x)
            return self
        
        angle = math.atan(self.y / self.x)
        
        if self.x > 0:
            self.x = math.cos(angle)
            self.y = math.sin(angle)
        elif self.x < 0 and self.y > 0:
            self.x = -math.cos(angle)
            self.y = math.cos(angle)
        elif self.x < 0 and self.y < 0:
            self.x = -math.cos(angle)
            self.y = -math.cos(angle)
        
        return self
