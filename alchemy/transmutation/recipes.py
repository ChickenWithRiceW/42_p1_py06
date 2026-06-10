import alchemy.elements
# from alchemy.elements import create_fire
from alchemy.potions import strength_potion


def lead_to_gold() -> str:
    text = "Recipe transmuting Lead to Gold: brew " \
            f"{alchemy.elements.create_air()} and " \
            f"{strength_potion()} mixed with " \
            f"{alchemy.elements.create_fire()}"
    return text
