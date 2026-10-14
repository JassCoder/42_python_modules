from alchemy.elements import create_air
from ..potions import strength_potion
from elements import create_fire, create_water


def lead_to_gold() -> str:
    air: str = create_air()
    potion: str = strength_potion()
    fire: str = create_fire()
    water: str = create_water()
    final: str = (
        f"Recipe transmuting Lead to Gold: brew {air} and {potion}"
        f"brewed with {fire} and {water} mixed with {fire}"
        )
    return final
