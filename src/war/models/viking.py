"""Viking class."""

from war.models.soldier import Soldier


class Viking(Soldier):
    """Viking class, extends Soldier.
    
    Attributes
    ----------
    name : str
        The name of the Viking.

    Methods
    ----------
    battle_cry() -> str:
        Returns "Odin Owns You All!".
    receive_damage(damage: int) -> str:
        Subtracts the damage from the Vikings's health.
        If the Viking is stil alive, return "NAME has received DAMAGE points of damage".
        If the Viking dies, return "NAME has died in act of combat".
    """

    def __init__(self, name: str, health: int, strength: int):
        super().__init__(health, strength)

        self.name: str = name

    def battle_cry(self) -> str:
        """Battle cry method."""

        return "Odin Owns You All!"

    def receive_damage(self, damage: int) -> str:
        """Receive damage method.
        
        Parameters
        ----------
        damage : int
            The damage received by the Viking.

        Returns
        ----------
        str : The message from the Viking, whether he received damage or if he died.
        """

        self.health -= damage

        if self.health <= 0:
            return f"{self.name} has died in act of combat"
        
        return f"{self.name} has received {damage} points of damage"
