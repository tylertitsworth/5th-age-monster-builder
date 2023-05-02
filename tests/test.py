from src.utils.classes import Ability, Attack, Creature, Trigger
import unittest


class Test_TestCreature(unittest.TestCase):
    def test_defPriority(self):
        self.assertEqual(Creature.defPriority(["MD"], "MD"), "Better Defense")
        self.assertEqual(Creature.defPriority(["PD"], "PD"), "Better Defense")
        self.assertEqual(Creature.defPriority(["PD"], "MD"), "Lesser Defense")
        self.assertEqual(Creature.defPriority(["MD"], "PD"), "Lesser Defense")
        self.assertEqual(Creature.defPriority(["MD", "PD"], "MD"), "Better Defense")
        self.assertEqual(Creature.defPriority(["MD", "PD"], "PD"), "Better Defense")

    def test_enumerateList(self):
        self.assertEqual(
            Creature.enumerateList(self, ["Acid", "Fire"], "Immunities: "),
            "Immunities: Acid, Fire",
        )

    def test_openData(self):
        filenames = [
            "normal_stats.csv",
            "large_stats.csv",
            "huge_stats.csv",
            "mook_stats.csv",
            "template.csv",
            "initiative.csv",
        ]
        rows = ["11", "8", "2", "7", "Brittle", "Super-slow and utterly clumsy"]
        cols = [
            "Fear threshold (HP)",
            "Strike Damage",
            "Lesser Defense",
            "HP",
            "HP",
            "Modifier",
        ]
        fileAnswers = [96, 76, 12, 27, 0.7, -1]
        types = [int, int, int, int, float, int]

        for idx, answer in enumerate(fileAnswers):
            self.assertEqual(
                Creature.openData(filenames[idx], rows[idx], cols[idx], types[idx]),
                answer,
            )

    def test_setAbilities(self):
        abilities = [
            {
                "name": "Orcish Command",
                "description": "When a nearby ally of the half-orc commander scores a critical hit, that ally can roll a save against a save ends effect as a free action.",
                "dc": "16",
            },
            {
                "name": "Lethal Swing",
                "description": "Once per battle, a half-orc can reroll a melee attack and use the result it prefers",
            },
        ]
        abilitiesAnswer = [
            Ability(
                {
                    "name": "Orcish Command",
                    "description": "When a nearby ally of the half-orc commander scores a critical hit, that ally can roll a save against a save ends effect as a free action.",
                    "dc": "16",
                }
            ),
            Ability(
                {
                    "name": "Lethal Swing",
                    "description": "Once per battle, a half-orc can reroll a melee attack and use the result it prefers",
                }
            ),
        ]
        self.assertEqual(
            type(Creature.setAbilities(self, abilities)), type(abilitiesAnswer)
        )

        for idx, ability in enumerate(abilities):
            self.assertEqual(
                Creature.setAbilities(self, abilities)[idx].dc, abilitiesAnswer[idx].dc
            )
            self.assertEqual(
                Creature.setAbilities(self, abilities)[idx].description,
                abilitiesAnswer[idx].description,
            )
            self.assertEqual(
                Creature.setAbilities(self, abilities)[idx].name,
                abilitiesAnswer[idx].name,
            )

    def test_setAttacks(self):
        self.level = 8
        self.role = "Leader"
        self.size = "Medium"
        self.strength = "Normal"
        self.template = "Leader"
        attacks = [
            {
                "name": "Jagged Longsword",
                "defense": "AC",
                "triggers": [
                    {
                        "condition": "even hit",
                        "description": "One nearby lower-level mook makes an attack as a free action.",
                        "recharge": "16",
                    }
                ],
            },
            {
                "name": "Thrown Javelin",
                "defense": "AC",
                "range": "Ranged",
                "triggers": [
                    {
                        "condition": "even hit",
                        "description": "The half-orc commander gains 20 temporary hit points.",
                    }
                ],
            },
        ]
        attacksAnswer = [
            Attack(
                {
                    "name": "Jagged Longsword",
                    "defense": "AC",
                    "triggers": [
                        {
                            "condition": "even hit",
                            "description": "One nearby lower-level mook makes an attack as a free action.",
                            "recharge": "16",
                        }
                    ],
                },
                level=self.level,
                role=self.role,
                size=self.size,
                strength=self.strength,
                template=self.template,
            ),
            Attack(
                {
                    "name": "Thrown Javelin",
                    "defense": "AC",
                    "range": "Ranged",
                    "triggers": [
                        {
                            "condition": "even hit",
                            "description": "The half-orc commander gains 20 temporary hit points.",
                        }
                    ],
                },
                level=self.level,
                role=self.role,
                size=self.size,
                strength=self.strength,
                template=self.template,
            ),
        ]
        self.assertEqual(type(Creature.setAttacks(self, attacks)), type(attacksAnswer))

        for idx, attack in enumerate(attacks):
            self.assertEqual(
                Creature.setAttacks(self, attacks)[idx].attack_bonus,
                attacksAnswer[idx].attack_bonus,
            )
            self.assertEqual(
                Creature.setAttacks(self, attacks)[idx].damage,
                attacksAnswer[idx].damage,
            )
            self.assertEqual(
                Creature.setAttacks(self, attacks)[idx].damage_type,
                attacksAnswer[idx].damage_type,
            )
            self.assertEqual(
                Creature.setAttacks(self, attacks)[idx].defense,
                attacksAnswer[idx].defense,
            )
            self.assertEqual(
                Creature.setAttacks(self, attacks)[idx].hit_effect,
                attacksAnswer[idx].hit_effect,
            )
            self.assertEqual(
                Creature.setAttacks(self, attacks)[idx].name, attacksAnswer[idx].name
            )
            self.assertEqual(
                Creature.setAttacks(self, attacks)[idx].range, attacksAnswer[idx].range
            )

    def test_statType(self):
        self.assertEqual(
            Creature.statType("Mook", "Medium", "Normal"), "mook_stats.csv"
        )
        self.assertEqual(
            Creature.statType("Troop", "Small", "Normal"), "mook_stats.csv"
        )
        self.assertEqual(
            Creature.statType("Troop", "Medium", "Normal"), "normal_stats.csv"
        )
        self.assertEqual(
            Creature.statType("Troop", "Tiny", "Triple"), "normal_stats.csv"
        )
        self.assertEqual(
            Creature.statType("Troop", "Medium", "Double"), "large_stats.csv"
        )
        self.assertEqual(
            Creature.statType("Troop", "Large", "Normal"), "large_stats.csv"
        )
        self.assertEqual(Creature.statType("Troop", "Huge", "Normal"), "huge_stats.csv")
        self.assertEqual(
            Creature.statType("Troop", "Normal", "Triple"), "huge_stats.csv"
        )
        self.assertEqual(
            Creature.statType("Troop", "Large", "Double"), "huge_stats.csv"
        )


class Test_TestAttack(unittest.TestCase):
    def test_setTriggers(self):
        triggers = [
            {
                "condition": "even hit",
                "description": "One nearby lower-level mook makes an attack as a free action.",
                "recharge": "16",
            },
            {
                "condition": "even hit",
                "description": "The half-orc commander gains 20 temporary hit points.",
            },
        ]
        triggersAnswer = [
            Trigger(
                {
                    "condition": "even hit",
                    "description": "One nearby lower-level mook makes an attack as a free action.",
                    "recharge": "16",
                }
            ),
            Trigger(
                {
                    "condition": "even hit",
                    "description": "The half-orc commander gains 20 temporary hit points.",
                }
            ),
        ]
        self.assertEqual(type(Attack.setTriggers(self, triggers)), type(triggersAnswer))

        for idx, trigger in enumerate(triggers):
            self.assertEqual(
                Attack.setTriggers(self, triggers)[idx].condition,
                triggersAnswer[idx].condition,
            )
            self.assertEqual(
                Attack.setTriggers(self, triggers)[idx].description,
                triggersAnswer[idx].description,
            )
            self.assertEqual(
                Attack.setTriggers(self, triggers)[idx].recharge,
                triggersAnswer[idx].recharge,
            )


if __name__ == "__main__":
    unittest.main()
