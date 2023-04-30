# 5th-age-monster-builder

## Project Structure

```
.
├── README.md
├── data
│   ├── huge_stats.csv
│   ├── initiative.csv
│   ├── large_stats.csv
│   ├── mook_stats.csv
│   ├── normal_stats.csv
│   └── template.csv
├── docker
├── requirements.txt
├── src
│   ├── app.py
│   └── utils
│       ├── classes.py
│       └── data.py
└── tests
```

## Steps

### 1. OOP

Create a creature class in `utils/classes.py` and import it into `src/app.py` to test it. Add optional parameters to the class to allow for more customization down the road.

```python
from utils.classes import Creature

if __name__ == '__main__':
    test = Creature(name="Hello World")
    print(test.name)
```

```bash
$ python src/app.py
Hello World
```

### 2. Database

Create stat and options data in the `data` folder and options lists in `utils/data.py`. Import the data into `src/app.py` to test it. Convert the csv files into dictionaries for use in the `Creature` class and populating options lists later down the road.

```python
import csv
from utils.classes import Creature

if __name__ == '__main__':
    test = Creature(name="Orc")
    
    with open('data/normal_stats.csv', newline='', encoding='utf-8-sig') as statsfile:
        reader = csv.DictReader(statsfile)
        for row in reader:
            print(f'A Level {row["Monster Level"]} {test.name} has {row["AC"]} AC')
```

```bash
$ python src/app.py 
A Level 0 Orc has 16 AC
A Level 1 Orc has 17 AC
A Level 2 Orc has 18 AC
A Level 3 Orc has 19 AC
A Level 4 Orc has 20 AC
A Level 5 Orc has 21 AC
A Level 6 Orc has 22 AC
A Level 7 Orc has 23 AC
A Level 8 Orc has 24 AC
A Level 9 Orc has 25 AC
A Level 10 Orc has 26 AC
A Level 11 Orc has 27 AC
A Level 12 Orc has 28 AC
A Level 13 Orc has 29 AC
A Level 14 Orc has 30 AC
```

### 3. Conversion App

#### a. Create a global function to open data files

This method looks for a given row in column 0 and returns the value in another given column. It can also be used to return the type of the value in the given column.

```python
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
```

#### b. Create Class Variables for A Printing Method

We originally created inputs for users to enter data, but now we need to use those inputs to create outputs for the `Creature`, `Attack`, `Ability`, and `Trigger` objects.

```python
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
```

#### c. Create Subclass Constructors

When creating an `Attack` object, it needs to inherit some of the `Creature` object's attributes.

```python
self.attacks = self.setAttacks(attacks)
```

```python
def setAttacks(self, attacks):
    classAttacks = []
    for attack in attacks:
        classAttacks.append(Attack(attack, level=self.level, role=self.role,
                            size=self.size, strength=self.strength, template=self.template))
    return classAttacks
```

#### d. Create a Printing Method

```python
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
```

#### e. Test the Printing Method

```python
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
```

```bash
$ python src/app.py 
Half-Orc Commander
Medium 8 level Leader [Humanoid]
Initiative: +13
Jagged Longsword +13 vs. AC: 38 damage
Natural even hit: One nearby lower-level mook makes an attack as a free action.
R: Thrown Javelin +13 vs. AC: 38 damage
Natural even hit: The half-orc commander gains 20 temporary hit points.
HP 201 - AC 24
MD 21 - PD 22
Orcish Command: When a nearby ally of the half-orc commander scores a critical hit, that ally can roll a save against a save ends effect as a free action.
Lethal Swing: Once per battle, a half-orc can reroll a melee attack and use the result it prefers
```

### 4. Unit Testing

For each class, create a test class that inherits from `unittest.TestCase`. Then, create a test suite function for each method in the class. In each test suite create test cases or assertions for each potential input/output of that method.

```python
# Unit Test for Creature Class
class Test_TestCreature(unittest.TestCase):
    # Test Suite for defPriority Method
    def test_defPriority(self):
        # Test Case for input (["MD"], "MD"); output "Better Defense"
        self.assertEqual(Creature.defPriority(["MD"], "MD"), "Better Defense")
        ...
    # Test Suite for openData Method
    def test_openData(self):
        ...
```

Ensure the tests are running properly.

```bash
$ python -m unittest tests/test.py -v
test_setTriggers (tests.test.Test_TestAttack) ... ok
test_defPriority (tests.test.Test_TestCreature) ... ok
test_enumerateList (tests.test.Test_TestCreature) ... ok
test_openData (tests.test.Test_TestCreature) ... ok
test_setAbilities (tests.test.Test_TestCreature) ... ok
test_setAttacks (tests.test.Test_TestCreature) ... ok
test_statType (tests.test.Test_TestCreature) ... ok

----------------------------------------------------------------------
Ran 7 tests in 0.196s

OK
```

While making each test, you might discover bugs in your code. For example, I discovered that the `Creature.openData` method was not working properly because the `initiative.csv` file was not formatted correctly. I fixed the formatting and then the test passed.

Afterwards, you can make some CI for your testing to ensure that they run on a new pull request. This will ensure that your code is always working properly. For my purposes, a simple GitHub Action is sufficient.

```yaml
name: Run Unit Tests

on:
    push:

jobs:
    unit-tests:
        runs-on: ubuntu-latest
        steps:
            - uses: actions/checkout@v3
            - name: Install Python 3
              uses: actions/setup-python@v2
              with:
                  python-version: 3.10.11
            - name: Install dependencies
              run: pip install -U pip -r requirements.txt
            - name: run tests with unittest
              run: python -m unittest tests/test.py -v

```

### 5. GUI

<!--- https://www.pythonguis.com/ --->
