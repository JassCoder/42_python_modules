from alchemy.elements import create_air
from ..potions import strength_potion
from elements import create_fire


def lead_to_gold() -> str:
    air: str = create_air()
    potion: str = strength_potion()
    fire: str = create_fire()
    return (
        f"Recipe transmuting Lead to Gold: "
        f"brew '{air}' and '{potion}' mixed with '{fire}'"
    )
