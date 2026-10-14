from alchemy.elements import create_earth, create_air
from ..elements import create_water, create_fire

def healing_potion() -> str:
    earth: str = create_earth()
    air: str = create_air()
    return f"Healing potion created using {earth} and {air}"


def strength_potion() -> str:
    fire: str = create_fire()
    water: str = create_water()
    return f"Strength potion brewed with {fire} and {water}"

