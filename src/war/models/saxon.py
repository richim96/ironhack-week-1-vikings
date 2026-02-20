"""Saxon class."""

from war.models.soldier import Soldier


class Saxon(Soldier):
    """Saxon class, extends Soldier.
    
    Methods
    ----------
    receive_damage(damage: int) -> str:
        Subtracts the damage from the Saxon's health.
        If the Viking is stil alive, return "A Saxon has received DAMAGE points of damage".
        If the Viking dies, return "A Saxon has died in combat".
    """

    def __init__(self, health: int, strength: int):
        super().__init__(health, strength)

    def receive_damage(self, damage: int) -> str:
        """Receive damage method.
        
        Parameters
        ----------
        damage : int
            The damage received by the Saxon.
        """

        self.health -= damage

        if self.health <= 0:
            return "A Saxon has died in combat"
        
        return f"A Saxon has received {damage} points of damage"
