import unittest

from war.models.soldier import Soldier
from inspect import signature


class TestSoldier(unittest.TestCase):

    def setUp(self):
        self.strength = 150
        self.health = 300
        self.soldier = Soldier(self.health, self.strength)

    def testConstructorSignature(self):
        self.assertEqual(len(signature(Soldier).parameters), 2)

    def testHealth(self):
        self.assertEqual(self.soldier.health, self.health)

    def testStrength(self):
        self.assertEqual(self.soldier.strength, self.strength)

    def testAttackShouldBeFunction(self):
        self.assertEqual(callable(self.soldier.attack), True)

    def testAttackHasNoParams(self):
        self.assertEqual(len(signature(self.soldier.attack).parameters), 0)

    def testAttackRetunsStrength(self):
        self.assertEqual(self.soldier.attack(), self.strength)

    def testReceivesDamage(self):
        self.assertEqual(callable(self.soldier.receive_damage), True)

    def testReceivesDamageHasParams(self):
        self.assertEqual(
            len(signature(self.soldier.receive_damage).parameters), 1)

    def testReceiveDamageReturnNone(self):
        self.assertEqual(self.soldier.receive_damage(50), None)

    def testCanReceiveDamage(self):
        self.soldier.receive_damage(50)
        self.assertEqual(self.soldier.health, self.health - 50)


if __name__ == '__main__':
    unittest.main()
