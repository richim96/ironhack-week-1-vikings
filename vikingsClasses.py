import random


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

    def receive_damage(self, damage: int) -> None:
        """Receive damage method.
        
        Parameters
        ----------
        damage : int
            The damage received by the Viking.
        """

        self.health -= damage
    

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
