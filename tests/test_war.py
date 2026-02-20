import unittest

from war.models import Viking, Saxon, War
from inspect import signature


class TestWar(unittest.TestCase):

    def setUp(self):
        self.war = War()

    def testWarShouldReciveNoParams(self):
        self.assertEqual(len(signature(War).parameters), 0)

    def testVikingArmy(self):
        self.assertEqual(self.war.viking_army, [])

    def testSaxonArmy(self):
        self.assertEqual(self.war.saxon_army, [])


class TestWar2(unittest.TestCase):
    def setUp(self):
        def generateViking():
            name = 'Harald'
            health = 300
            strength = 150
            return Viking(name, health, strength)

        def generateSaxon():
            health = 60
            strength = 25
            return Saxon(health, strength)

        self.viking = generateViking()
        self.saxon = generateSaxon()
        self.war = War()
        self.war.add_saxon(self.saxon)
        self.war.add_viking(self.viking)

    def testAddViking(self):
        self.assertEqual(callable(self.war.add_viking), True)

    def testAddVikingShouldReceiveOneParam(self):
        self.assertEqual(len(signature(self.war.add_viking).parameters), 1)

    def testAddVikingInList(self):
        self.assertEqual(self.war.viking_army, [self.viking])

    def testAddVikingReturnNull(self):
        self.assertEqual(self.war.add_viking(self.viking), None)

    def testAddSaxonShouldBeFunction(self):
        self.assertEqual(callable(self.war.add_saxon), True)

    def testAddSaxonReceiveOneParam(self):
        self.assertEqual(len(signature(self.war.add_saxon).parameters), 1)

    def testSaxonArmyReturnEmptyList(self):
        self.assertEqual(self.war.saxon_army, [self.saxon])

    def testAddSaxonReturnNone(self):
        self.assertEqual(self.war.add_saxon(self.saxon), None)

    def testVikingAttackIsFunction(self):
        self.assertEqual(callable(self.war.viking_attack), True)

    def testVikingAttackReceiveNoParam(self):
        self.assertEqual(len(signature(self.war.viking_attack).parameters), 0)

    def testSaxonHealth(self):
        old_health = self.saxon.health
        self.war.viking_attack()
        self.assertEqual(self.saxon.health, old_health - self.viking.strength)

    def testVikingAttack(self):
        self.war.viking_attack()
        self.assertEqual(len(self.war.saxon_army), 0)

    def testAddSaxon(self):
        print(self.war.__dict__)
        self.assertEqual(self.war.viking_attack(), 'A Saxon has died in combat')

    def testSaxonAttackIsFunction(self):
        self.assertEqual(callable(self.war.saxon_attack), True)

    def testSaxonAttackReceiveNoParam(self):
        self.assertEqual(len(signature(self.war.saxon_attack).parameters), 0)

    def testVikingHealth(self):
        old_health = self.viking.health
        self.war.saxon_attack()
        self.assertEqual(self.viking.health, old_health - self.saxon.strength)

    def testVikingArmyList(self):
        for _ in range(12):
            if(len(self.war.viking_army) == 0):
                break
            self.war.saxon_attack()
        self.assertEqual(len(self.war.viking_army), 0)

    def testReturnOfSaxonAttack(self):
        self.assertEqual(self.war.saxon_attack(), self.viking.name +
                         ' has received ' + str(self.saxon.strength) + ' points of damage')

    def testShowStatusShouldIsFunction(self):
        self.assertEqual(callable(self.war.show_status), True)

    def testShowStatusReceiveNoParams(self):
        self.assertEqual(len(signature(self.war.show_status).parameters), 0)

    def testShouldReturnStringVikingsWon(self):
        self.war.viking_attack()
        self.assertEqual(self.war.show_status(),
                         'Vikings have won the war of the century!')

    def testShouldReturnStringSaxonsWon(self):
        for _ in range(12):
            self.war.saxon_attack()
        self.assertEqual(self.war.show_status(
        ), 'Saxons have fought for their lives and survive another day...')

    def testShouldReturnStringStillFighting(self):
        self.assertEqual(
            self.war.show_status(), 'Vikings and Saxons are still in the thick of battle.')


if __name__ == '__main__':
    unittest.main()
