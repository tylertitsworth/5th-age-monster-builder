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

#### 1. Setup

Create a windows virtual environment and install the required packages so you can access the GUI designer GUI.

_Minimum Requirements:_ `python3.10`

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
python -m pip install -U pip 
python -m pip install -r requirements.txt
.\venv\Lib\site-packages\qt6_applications\Qt\bin\designer.exe
```

#### 2. Design the GUI

Design your application using the GUI designer and save it as `builder.ui`. Then, convert the `.ui` file into a `.py` file.

```powershell
pyuic6 .\builder.ui -o .\src\builderUI.py
```

The output file will be very long, and since it's a generated file you should not change it. All of the operating functions will be in `app.py`.

Start with something simple, and replace your main function with:

```python
from builderUI import Ui_role
from PyQt6 import QtWidgets, QtCore, QtGui

class MainWindow(QtWidgets.QMainWindow, Ui_role):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = MainWindow()

    window.show()
    app.exec()
```

#### 3. Add Functionality to GUI Elements

For each button you add, ensure that you have a function to handle the button press.

```python
self.addAbilityButton.clicked.connect(self.addAbility)
self.addAttackButton.clicked.connect(self.addAttack)
self.generateButton.clicked.connect(self.generateCreature)
self.resetButton.clicked.connect(self.displayOutput.clear)
```

Add functionality to generate more UI elements by adding a bunch of hidden elements and functionality to show them on a button press. This is a bit of a hack, but it works and I'm omitting the attack and trigger functions for brevity.

```python
class MainWindow(QtWidgets.QMainWindow, Ui_role):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.ability_buttons = []
        self.ability_dcs = []
        self.ability_descriptions = []
        self.ability_labels = []
        self.ability_names = []

        self.abilityRows = ["Hide", "Hide", "Hide", "Hide"]

        for n, i in enumerate(self.abilityRows):
            self.ability_names.append(QtWidgets.QLineEdit(parent=self.abilityGridLayoutWidget))
            self.ability_names[n].setObjectName(f"ability_name_{n}")
            self.ability_names[n].setText(QtCore.QCoreApplication.translate("role", "Ability Name"))
            self.ability_names[n].hide()
            self.abilityGridLayout.addWidget(self.ability_names[n], n, 0, 1, 1)

            self.ability_dcs.append(QtWidgets.QLineEdit(parent=self.abilityGridLayoutWidget))
            self.ability_dcs[n].setObjectName(f"ability_dc_{n}")
            self.ability_dcs[n].setText(QtCore.QCoreApplication.translate("role", "DC"))
            self.ability_dcs[n].hide()
            self.abilityGridLayout.addWidget(self.ability_dcs[n], n, 1, 1, 1)

            self.ability_labels.append(QtWidgets.QLabel(parent=self.abilityGridLayoutWidget))
            self.ability_labels[n].setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
            self.ability_labels[n].setAlignment(
                QtCore.Qt.AlignmentFlag.AlignRight
                | QtCore.Qt.AlignmentFlag.AlignTrailing
                | QtCore.Qt.AlignmentFlag.AlignVCenter
            )
            self.ability_labels[n].setObjectName(f"ability_label_{n}")
            self.ability_labels[n].setText(QtCore.QCoreApplication.translate("role", ":"))
            self.ability_labels[n].hide()
            self.abilityGridLayout.addWidget(self.ability_labels[n], n, 2, 1, 1)

            self.ability_descriptions.append(QtWidgets.QLineEdit(parent=self.abilityGridLayoutWidget))
            self.ability_descriptions[n].setObjectName(f"ability_description_{n}")
            self.ability_descriptions[n].setText(QtCore.QCoreApplication.translate("role", "Description"))
            self.ability_descriptions[n].hide()
            self.abilityGridLayout.addWidget(self.ability_descriptions[n], n, 3, 1, 1)

            self.ability_buttons.append(QtWidgets.QPushButton(parent=self.abilityGridLayoutWidget))
            self.ability_buttons[n].setObjectName(f"ability_button_{n}")
            self.ability_buttons[n].setText(QtCore.QCoreApplication.translate("role", "-"))
            self.abilityGridLayout.addWidget(self.ability_buttons[n], n, 4, 1, 1)
            self.ability_buttons[n].row = n
            self.ability_buttons[n].hide()
            self.ability_buttons[n].clicked.connect(self.removeAbility)

    def addAbility(self):
        for idx, row in enumerate(self.abilityRows):
            if row == "Hide":
                self.abilityRows[idx] = "Show"
                self.ability_names[idx].show()
                self.ability_dcs[idx].show()
                self.ability_labels[idx].show()
                self.ability_descriptions[idx].show()
                self.ability_buttons[idx].show()
                break

    def removeAbility(self):
        self.abilityRows[self.sender().row] = "Hide"
        self.ability_names[self.sender().row].hide()
        self.ability_dcs[self.sender().row].hide()
        self.ability_labels[self.sender().row].hide()
        self.ability_descriptions[self.sender().row].hide()
        self.ability_buttons[self.sender().row].hide()
```

Add Functionality to generate a creature. Again omitting the attack and trigger functions for brevity.

```python
def generateCreature(self):
    abilities = []
    for idx, row in enumerate(self.abilityRows):
        if row == "Show":
            if self.ability_dcs[idx]:
                abilities.append(
                    {
                        "name": self.ability_names[idx].text(),
                        "description": self.ability_descriptions[idx].text(),
                        "dc": self.ability_dcs[idx].text(),
                    }
                )
            else:
                abilities.append(
                    {
                        "name": self.ability_names[idx].text(),
                        "description": self.ability_descriptions[idx].text(),
                    }
                )
    self.displayOutput.clear()

    if self.favored_defense.selectedItems() == []:
        self.displayOutput.insertPlainText("Please select a Favored Defense")
        return

    self.displayOutput.insertPlainText(
        str(
            Creature(
                name=self.name.text(),
                abilities=abilities,
                attacks=attacks,
                creature_type=self.type.currentText(),
                favored_defenses=[i.text() for i in self.favored_defense.selectedItems()],
                immunities=[i.text() for i in self.immunities.selectedItems()],
                initiative_type=self.initiative_modifier.currentText(),
                level=int(self.level.currentText()),
                role=self.role.currentText(),
                size=self.creatureSize.currentText(),
                strength=self.strength.currentText(),
                template=self.template.currentText(),
                vulnerabilities=[i.text() for i in self.vulnerabilities.selectedItems()],
            )
        )
    )
```

#### 4. Run the GUI

```powershell
python .\src\app.py
```

![image](https://user-images.githubusercontent.com/43555799/235815513-5ac987a7-956e-4f61-8bbe-eca6e3e0c79e.png)

#### 5. Build a Creature!

![image](https://user-images.githubusercontent.com/43555799/235817616-d544ebec-0ef2-43df-83df-ddbf71880a6c.png)

>Unit Tests for the `MainWindow` class functions were unable to be produced because the GUI can't run in the test environment so the functions can't be tested.

### 6. Packaging

<!--- https://www.pythonguis.com/tutorials/packaging-pyqt6-applications-windows-pyinstaller/ --->
