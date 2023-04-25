from tests.data import creature_types, damage_types, defenses, levels, ranges, sizes, strengths
from src.utils.classes import Creature
import unittest


class Test_TestCreature(unittest.TestCase):
    maxDiff = None
    def test_creature_size(self):
        answers = {"Tiny": """Half-Orc Commander
Tiny 8 level Leader [Humanoid]
Initiative: +13
Jagged Longsword +13 vs. AC: 23 damage
Natural even hit: One nearby lower-level mook makes an attack as a free action.
R: Thrown Javelin +13 vs. AC: 23 damage
Natural even hit: The half-orc commander gains 20 temporary hit points.
HP 50 - AC 24
MD 21 - PD 22
Orcish Command: When a nearby ally of the half-orc commander scores a critical hit, that ally can roll a save against a save ends effect as a free action.
Lethal Swing: Once per battle, a half-orc can reroll a melee attack and use the result it prefers""",
"Small": """Half-Orc Commander
Small 8 level Leader [Humanoid]
Initiative: +13
Jagged Longsword +13 vs. AC: 23 damage
Natural even hit: One nearby lower-level mook makes an attack as a free action.
R: Thrown Javelin +13 vs. AC: 23 damage
Natural even hit: The half-orc commander gains 20 temporary hit points.
HP 50 - AC 24
MD 21 - PD 22
Orcish Command: When a nearby ally of the half-orc commander scores a critical hit, that ally can roll a save against a save ends effect as a free action.
Lethal Swing: Once per battle, a half-orc can reroll a melee attack and use the result it prefers""",
"Medium": """Half-Orc Commander
Medium 8 level Leader [Humanoid]
Initiative: +13
Jagged Longsword +13 vs. AC: 38 damage
Natural even hit: One nearby lower-level mook makes an attack as a free action.
R: Thrown Javelin +13 vs. AC: 38 damage
Natural even hit: The half-orc commander gains 20 temporary hit points.
HP 201 - AC 24
MD 21 - PD 22
Orcish Command: When a nearby ally of the half-orc commander scores a critical hit, that ally can roll a save against a save ends effect as a free action.
Lethal Swing: Once per battle, a half-orc can reroll a melee attack and use the result it prefers""", 
"Large": """Half-Orc Commander
Large 8 level Leader [Humanoid]
Initiative: +13
Jagged Longsword +13 vs. AC: 76 damage
Natural even hit: One nearby lower-level mook makes an attack as a free action.
R: Thrown Javelin +13 vs. AC: 76 damage
Natural even hit: The half-orc commander gains 20 temporary hit points.
HP 403 - AC 24
MD 21 - PD 22
Orcish Command: When a nearby ally of the half-orc commander scores a critical hit, that ally can roll a save against a save ends effect as a free action.
Lethal Swing: Once per battle, a half-orc can reroll a melee attack and use the result it prefers""", 
"Huge": """Half-Orc Commander
Huge 8 level Leader [Humanoid]
Initiative: +13
Jagged Longsword +13 vs. AC: 114 damage
Natural even hit: One nearby lower-level mook makes an attack as a free action.
R: Thrown Javelin +13 vs. AC: 114 damage
Natural even hit: The half-orc commander gains 20 temporary hit points.
HP 604 - AC 24
MD 21 - PD 22
Orcish Command: When a nearby ally of the half-orc commander scores a critical hit, that ally can roll a save against a save ends effect as a free action.
Lethal Swing: Once per battle, a half-orc can reroll a melee attack and use the result it prefers"""}
        
        for size in sizes:
            self.assertEqual(Creature(name="Half-Orc Commander",
                                    abilities=[{"name": "Orcish Command", "description": "When a nearby ally of the half-orc commander scores a critical hit, that ally can roll a save against a save ends effect as a free action."}, {
                                        "name": "Lethal Swing", "description": "Once per battle, a half-orc can reroll a melee attack and use the result it prefers"}],
                                    attacks=[{"name": "Jagged Longsword", "defense": "AC", "triggers": [{"condition": "even hit", "description": "One nearby lower-level mook makes an attack as a free action."}]}, {
                                        "name": "Thrown Javelin", "defense": "AC", "range": "Ranged", "triggers": [{"condition": "even hit", "description": "The half-orc commander gains 20 temporary hit points."}]}],
                                    creature_type="Humanoid",
                                    favored_defenses=["PD"],
                                    initiative_type="Fast",
                                    level=8,
                                    role="Leader",
                                    size=size,
                                    strength="Normal",
                                    template="Leader"
                                    ).__str__(), answers[size])

if __name__ == '__main__':
    unittest.main()
