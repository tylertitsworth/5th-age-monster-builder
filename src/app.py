from utils.classes import Creature

if __name__ == '__main__':
    test = Creature(name="Half-Orc Commander",
                    abilities=[{"name": "Orcish Command", "description": "When a nearby ally of the half-orc commander scores a critical hit, that ally can roll a save against a save ends effect as a free action."}, {"name": "Lethal Swing", "description": "Once per battle, a half-orc can reroll a melee attack and use the result it prefers"}],
                    attacks=[{"name": "Jagged Longsword", "defense": "AC", "triggers": [{"condition": "even hit", "description": "One nearby lower-level mook makes an attack as a free action."}]}, {"name": "Thrown Javelin", "defense": "AC", "range": "Ranged", "triggers": [{"condition": "even hit", "description": "The half-orc commander gains 20 temporary hit points."}]}],
                    creature_type="Humanoid",
                    favored_defenses=["PD"],
                    initiative_type="Fast",
                    level=8,
                    role="Leader",
                    size="Medium",
                    strength="Normal",
                    template="Leader"
    )
    print(test)
