"""War class."""

import random

from war.models.viking import Viking
from war.models.saxon import Saxon


class War():
    """War class.

    Attributes
    ----------
    viking_army : list[Viking]
        A list of Vikings in the Viking army.
    saxon_army : list[Saxon]
        A list of Saxons in the Saxon army.
    status : str
        The current status of the war.
    
    Methods
    ----------
    add_viking(viking: Viking) -> None:
        Adds a Viking to the Viking army.
    add_saxon(saxon: Saxon) -> None:
        Adds a Saxon to the Saxon army.
    viking_attack():
        A Viking attacks a random Saxon. The Saxon receives damage equal to the Viking's strength.
        If the Saxon dies, it is removed from the army.
    saxon_attack():
        A Saxon attacks a random Viking. The Viking receives damage equal to the Saxon's strength.
        If the Viking dies, it is removed from the army.
    show_status():
        Returns a string with the current status of the war.
    """

    def __init__(self):
        self.viking_army: list[Viking] = []
        self.saxon_army: list[Saxon] = []
        self.status: str = "Vikings and Saxons are still in the thick of battle."

    def add_viking(self, viking: Viking) -> None:
        """Method to add a Viking to the Viking army.
        
        Parameters
        ----------
        viking : Viking
            A Viking soldier.
        """

        self.viking_army.append(viking)
    
    def add_saxon(self, saxon: Saxon) -> None:
        """Method to add a Saxon to the Saxon army.
        
        Parameters
        ----------
        viking : Saxon
            A Saxon soldier.
        """
        
        self.saxon_army.append(saxon)
    
    def viking_attack(self) -> str:
        """Viking attack method. A random Viking deals damage to a random Saxon."""
        viking_idx: int = random.randint(0, len(self.viking_army) - 1)
        saxon_idx: int = random.randint(0, len(self.saxon_army) - 1)
        
        viking: Viking = self.viking_army[viking_idx]
        saxon: Saxon = self.saxon_army[saxon_idx]

        print(viking.battle_cry())
        battle_result: str = saxon.receive_damage(viking.attack())

        if saxon.health <= 0:
            self.saxon_army.pop(saxon_idx)

        return battle_result
    
    def saxon_attack(self) -> str:
        """Saxon attack method. A random Saxon deals damage to a random Viking."""
        saxon_idx: int = random.randint(0, len(self.saxon_army) - 1)
        viking_idx: int = random.randint(0, len(self.viking_army) - 1)
        
        saxon: Saxon = self.saxon_army[saxon_idx]
        viking: Viking = self.viking_army[viking_idx]

        battle_result: str = viking.receive_damage(saxon.attack())

        if viking.health <= 0:
            self.viking_army.pop(viking_idx)

        return battle_result

    def show_status(self) -> str:
        n_saxons: int = len(self.saxon_army)
        n_vikings: int = len(self.viking_army)
        
        if n_saxons == 0:
            self.status = "Vikings have won the war of the century!"
        elif n_vikings == 0:
            self.status = "Saxons have fought for their lives and survive another day..."
        
        return self.status
