from __future__ import annotations

class Vector:
    
    
    def __init__(self, x : float, y : float) -> None:
        self.x : float = x
        self.y : float = y
    
    
    def length(self) -> float:
        return (self.x**2 + self.y**2)**(1/2)
