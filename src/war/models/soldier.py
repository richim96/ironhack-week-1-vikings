"""Soldier class."""

from typing import Optional


class Soldier:
    """Soldier class.
    
    Attributes
    ----------
    health : int
        The health of the soldier.
    strength : int
        The strength of the soldier.
    
    Methods
    ----------
    attack() -> int:
        Returns the strength of the soldier.
    receive_damage(damage: int) -> None:
        Subtracts the damage from the soldier's health.
    """

    def __init__(self, health: int, strength: int):
        self.health: int = health
        self.strength: int = strength
    
    def attack(self) -> int:
        """Attack method.
        
        Returns
        ----------
        int : The power of the attack
        """

        return self.strength

    def receive_damage(self, damage: int) -> Optional[str]:
        """Receive damage method.
        
        Parameters
        ----------
        damage : int
            The damage received by the Viking.
        """

        self.health -= damage
