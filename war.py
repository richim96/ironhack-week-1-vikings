import random

from vikingsClasses import Viking, Saxon, War


def create_viking_army(
        war: War,
        names: list[str] = ["Lothark", "Thornull", "Grisja", "Nomor", "Kaiuln"],
        n_vikings: int = 5,
    ) -> None:
    """Creates the Viking army.
    
    Parameters
    ----------
    war : War
        Singleton instance of the great war.
    names : list[str]
        The names of the Vikings.
    n_vikings : int
        Number of Viking soldiers.
    """
    
    for i in range(1, n_vikings):
        war.add_viking(Viking(
            name=names[random.randint(0, len(names) - 1)],
            health=240,
            strength=random.randint(25, 100))
        )


def create_saxon_army(war: War, n_saxons: int = 12) -> None:
    """Creates the Saxon army.
    
    Parameters
    ----------
    war : War
        Singleton instance of the great war.
    n_saxons : int
        Number of Saxon soldiers.
    """

    for i in range(1, n_saxons):
        great_war.add_saxon(Saxon(health=100, strength=random.randint(5, 80)))


if __name__ == "__main__":   
    great_war: War = War() # Singleton

    create_viking_army(great_war)
    create_saxon_army(great_war)

    battle: int = 0
    while great_war.show_status() == "Vikings and Saxons are still in the thick of battle.":
        battle += 1
        
        if len(great_war.viking_army) > 0:
            print(great_war.viking_attack())
        if len(great_war.saxon_army) > 0:
            print(great_war.saxon_attack())

        print(
            f"Battle {battle} || ",
            f"Viking army: {len(great_war.viking_army)} warriors survived {[viking.name for viking in great_war.viking_army]}",
            f"- Saxon army: {len(great_war.saxon_army)} warriors survived"
        )
        print(great_war.show_status())
