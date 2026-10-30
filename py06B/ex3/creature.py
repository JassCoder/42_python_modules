from abc import ABC, abstractmethod


class Creature(ABC):
    """Abstract base class for all creatures."""
    
    def __init__(self, name: str, creature_type: str) -> None:
        self.name = name
        self.creature_type = creature_type
        
    @abstractmethod
    def attack(self) -> str:
        pass
    
    def describe(self) -> str:
        return f"{self.name} is a {self.creature_type} type Creature"

    class Flameling(creature):
        def __init__(self) -> None:
            super().__init__("Flameling", "Fire")
        
        def attack(self) -> str:
            return "Flameling uses Ember!"