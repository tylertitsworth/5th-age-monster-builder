import csv


def openData(filename, row, col, type):
    with open(f'data/{filename}', newline='', encoding='utf-8-sig') as datafile:
        reader = csv.reader(datafile)
        headings = next(reader)
        colVal = headings.index(col)
        for dataRow in reader:
            if dataRow[0] == str(row):
                if type == float:
                    if dataRow[colVal] == '':
                        return 0.0
                    return float(dataRow[colVal])
                elif type == int:
                    if dataRow[colVal] == '':
                        return 0
                    return int(dataRow[colVal])
                else:
                    return str(type(dataRow[colVal]))
        print(f'Error: {row} not found in {filename}')
        return 0


class Creature:
    def defPriority(favored_defenses, defense):
        if defense in favored_defenses:
            return "Better Defense"
        else:
            return "Lesser Defense"

    def statType(role, size, strength):
        if role == "Mook":
            return "mook_stats.csv"
        sizePower = 0
        match size:
            case 'Tiny':
                sizePower -= 2
            case 'Small':
                sizePower -= 1
            case 'Medium':
                pass
            case 'Large':
                sizePower += 1
            case 'Huge':
                sizePower += 2
        match strength:
            case 'Normal':
                pass
            case 'Double':
                sizePower += 1
            case 'Triple':
                sizePower += 2
        if sizePower == 0:
            return "normal_stats.csv"
        elif sizePower == 1:
            return "large_stats.csv"
        elif sizePower >= 2:
            return "huge_stats.csv"
        else:
            return "mook_stats.csv"

    def setAttacks(self, attacks):
        classAttacks = []
        for attack in attacks:
            classAttacks.append(Attack(attack, level=self.level, role=self.role,
                                size=self.size, strength=self.strength, template=self.template))
        return classAttacks

    def setAbilities(self, abilities):
        classAbilities = []
        for ability in abilities:
            classAbilities.append(Ability(ability))
        return classAbilities

    def enumerateList(self, list, str):
        for i, item in enumerate(list):
            if i:
                str += ', '
            str += f'{item}'
        return str

    def __init__(self,
                 abilities=[],
                 attacks=[],
                 condition_immunities=[],
                 favored_defenses=[],
                 immunities=[],
                 initiative_type=None,
                 level=None,
                 name=None,
                 role=None,
                 size=None,
                 strength=None,
                 template=None,
                 creature_type=None,
                 vulnerabilities=[]
                 ):
        self.ac = openData(filename=Creature.statType(role, size, strength), row=level, col="AC",
                           type=int) + openData(filename="template.csv", row=template, col="AC", type=int)
        self.hp = openData(filename=Creature.statType(role, size, strength), row=level, col="HP",
                           type=float) * openData(filename="template.csv", row=template, col="HP", type=float)
        self.initiative = level + \
            openData(filename="initiative.csv",
                     row=initiative_type, col="Modifier", type=int)
        self.md = openData(filename=Creature.statType(role, size, strength), row=level, col=Creature.defPriority(
            favored_defenses=favored_defenses, defense="MD"), type=int) + openData(filename="template.csv", row=template, col="MD", type=int)
        self.pd = openData(filename=Creature.statType(role, size, strength), row=level, col=Creature.defPriority(
            favored_defenses=favored_defenses, defense="PD"), type=int) + openData(filename="template.csv", row=template, col="PD", type=int)
        self.condition_immunities = condition_immunities
        self.creature_type = creature_type
        self.favored_defenses = favored_defenses
        self.immunities = immunities
        self.level = level
        self.name = name
        self.role = role
        self.size = size
        self.strength = strength
        self.template = template
        self.vulnerabilities = vulnerabilities

        self.attacks = self.setAttacks(attacks)
        self.abilities = self.setAbilities(abilities)

    def __str__(self):
        creatureStr = f'{self.name}'
        creatureStr += f'\n{self.size} {self.level} level {self.role} [{self.creature_type}]'
        creatureStr += f'\nInitiative: +{self.initiative}\n'

        if self.immunities != []:
            creatureStr += 'Immunities: '
            Creature.enumerateList(self, self.immunities, creatureStr)
            creatureStr += '\n'
        if self.condition_immunities != []:
            creatureStr += 'Condition Immunities: '
            Creature.enumerateList(
                self, self.condition_immunities, creatureStr)
            creatureStr += '\n'
        if self.vulnerabilities != []:
            creatureStr += 'Vulnerabilities: '
            Creature.enumerateList(self, self.vulnerabilities, creatureStr)
            creatureStr += '\n'
        for attack in self.attacks:
            creatureStr += f'{attack}\n'

        creatureStr += f'HP {int(self.hp)} - AC {self.ac}'
        creatureStr += f'\nMD {self.md} - PD {self.pd}'

        if self.abilities != []:
            for ability in self.abilities:
                creatureStr += f'\n{ability}'

        return creatureStr


class Ability:
    def __init__(self, ability):
        self.dc = ability.get('dc', None)
        self.description = ability.get('description', None)
        self.name = ability.get('name', None)

    def __str__(self):
        if self.dc == None:
            return f'{self.name}: {self.description}'
        return f'{self.name} {self.dc}+: {self.description}'


class Attack(Creature):
    def setTriggers(self, triggers):
        classTriggers = []
        for trigger in triggers:
            classTriggers.append(Trigger(trigger))
        return classTriggers

    def __init__(self,
                 attack,
                 level=None,
                 role=None,
                 size=None,
                 strength=None,
                 template=None,
                 ):
        self.attack_bonus = openData(filename=Creature.statType(role, size, strength), row=level,
                                     col="Attack Bonus", type=int) + openData(filename="template.csv", row=template, col="Attack", type=int)
        self.damage = openData(filename=Creature.statType(
                               role, size, strength), row=level, col="Strike Damage", type=int)
        self.damage_type = f' {attack.get("damage_type", None)}'
        self.defense = attack.get("defense", None)
        self.hit_effect = f', {attack.get("hit_effect", None)}'
        self.name = attack.get("name", None)
        self.range = attack.get("range", None)
        self.triggers = self.setTriggers(attack.get("triggers", []))

    def __str__(self):
        attackStr = f'{self.name} +{self.attack_bonus} vs. {self.defense}: {self.damage}'
        if self.damage_type == None:
            attackStr += f' {self.damage_type}'
        attackStr += ' damage'
        if self.hit_effect == None:
            attackStr += f'{self.hit_effect}'
        if self.range == "Ranged":
            attackStr = f'R: {attackStr}'
        elif self.range == "Close":
            attackStr = f'C: {attackStr}'
        if self.triggers != None:
            for trigger in self.triggers:
                attackStr += f'\n{trigger}'
        return attackStr


class Trigger:
    def __init__(self, trigger):
        self.condition = trigger.get("condition", None)
        self.description = trigger.get("description", None)
        self.recharge = trigger.get("recharge", None)

    def __str__(self):
        str = 'Natural '
        if self.condition != None:
            if isinstance(self.condition, int):
                str += f'{self.condition}+'
            else:
                str += f'{self.condition}'
        return f'{str}: {self.description}'
