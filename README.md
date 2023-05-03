# 5th-age-monster-builder

## Project Structure

```
.
├── build.ps1
├── data
│   ├── huge_stats.csv
│   ├── initiative.csv
│   ├── large_stats.csv
│   ├── mook_stats.csv
│   ├── normal_stats.csv
│   └── template.csv
├── README.md
├── requirements.txt
├── src
│   ├── app.py
│   ├── builderUI.py
│   └── utils
│       └── classes.py
└── tests
    └── test.py
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

Write a script to package the application into a single zip folder with an executable. I had to copy the data folder to go with the application since it is referenced during the application's runtime.

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -U pip
python -m pip install -r requirements.txt
pyinstaller .\src\app.py --onefile --clean --noconsole
cp -r data dist\data
Compress-Archive -LiteralPath dist -DestinationPath 5th-age-monster-builder.zip
```

```powershell
❯ .\build.ps1
Requirement already satisfied: pip in d:\dev\5th-age-monster-builder\venv\lib\site-packages (22.3.1)
Collecting pip
  Using cached pip-23.1.2-py3-none-any.whl (2.1 MB)
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 22.3.1
    Uninstalling pip-22.3.1:
      Successfully uninstalled pip-22.3.1
Successfully installed pip-23.1.2
Collecting PyInstaller (from -r requirements.txt (line 1))
  Using cached pyinstaller-5.10.1-py3-none-win_amd64.whl (1.3 MB)
Collecting pyinstaller-hooks-contrib (from -r requirements.txt (line 2))
  Using cached pyinstaller_hooks_contrib-2023.2-py2.py3-none-any.whl (261 kB)
Collecting PyQt6 (from -r requirements.txt (line 3))
  Using cached PyQt6-6.5.0-1-cp37-abi3-win_amd64.whl (6.5 MB)
Collecting PyQt6-tools (from -r requirements.txt (line 4))
  Using cached pyqt6_tools-6.4.2.3.3-py3-none-any.whl (29 kB)
Requirement already satisfied: setuptools>=42.0.0 in d:\dev\5th-age-monster-builder\venv\lib\site-packages (from PyInstaller->-r requirements.txt (line 1)) (65.5.0)
Collecting altgraph (from PyInstaller->-r requirements.txt (line 1))
  Using cached altgraph-0.17.3-py2.py3-none-any.whl (21 kB)
Collecting pefile>=2022.5.30 (from PyInstaller->-r requirements.txt (line 1))
  Using cached pefile-2023.2.7-py3-none-any.whl (71 kB)
Collecting pywin32-ctypes>=0.2.0 (from PyInstaller->-r requirements.txt (line 1))
  Using cached pywin32_ctypes-0.2.0-py2.py3-none-any.whl (28 kB)
Collecting PyQt6-sip<14,>=13.4 (from PyQt6->-r requirements.txt (line 3))
  Using cached PyQt6_sip-13.5.1-cp311-cp311-win_amd64.whl (72 kB)
Collecting PyQt6-Qt6>=6.5.0 (from PyQt6->-r requirements.txt (line 3))
  Using cached PyQt6_Qt6-6.5.0-py3-none-win_amd64.whl (58.7 MB)
Collecting click (from PyQt6-tools->-r requirements.txt (line 4))
  Using cached click-8.1.3-py3-none-any.whl (96 kB)
Collecting PyQt6 (from -r requirements.txt (line 3))
  Using cached PyQt6-6.4.2-cp37-abi3-win_amd64.whl (6.4 MB)
Collecting pyqt6-plugins<6.4.2.3,>=6.4.2.2.2 (from PyQt6-tools->-r requirements.txt (line 4))
  Using cached pyqt6_plugins-6.4.2.2.3-cp311-cp311-win_amd64.whl (72 kB)
Collecting python-dotenv (from PyQt6-tools->-r requirements.txt (line 4))
  Using cached python_dotenv-1.0.0-py3-none-any.whl (19 kB)
Collecting PyQt6-Qt6>=6.4.0 (from PyQt6->-r requirements.txt (line 3))
  Using cached PyQt6_Qt6-6.4.3-py3-none-win_amd64.whl (57.5 MB)
Collecting qt6-tools<6.4.3.2,>=6.4.3.1.2 (from pyqt6-plugins<6.4.2.3,>=6.4.2.2.2->PyQt6-tools->-r requirements.txt (line 4))
  Using cached qt6_tools-6.4.3.1.3-py3-none-any.whl (13 kB)
Collecting colorama (from click->PyQt6-tools->-r requirements.txt (line 4))
  Using cached colorama-0.4.6-py2.py3-none-any.whl (25 kB)
Collecting qt6-applications<6.4.3.3,>=6.4.3.2.2 (from qt6-tools<6.4.3.2,>=6.4.3.1.2->pyqt6-plugins<6.4.2.3,>=6.4.2.2.2->PyQt6-tools->-r requirements.txt (line 4))
  Using cached qt6_applications-6.4.3.2.3-py3-none-win_amd64.whl (71.3 MB)
Installing collected packages: pywin32-ctypes, PyQt6-Qt6, altgraph, qt6-applications, python-dotenv, PyQt6-sip, pyinstaller-hooks-contrib, pefile, colorama, PyQt6, PyInstaller, click, qt6-tools, pyqt6-plugins, PyQt6-tools
Successfully installed PyInstaller-5.10.1 PyQt6-6.4.2 PyQt6-Qt6-6.4.3 PyQt6-sip-13.5.1 PyQt6-tools-6.4.2.3.3 altgraph-0.17.3 click-8.1.3 colorama-0.4.6 pefile-2023.2.7 pyinstaller-hooks-contrib-2023.2 pyqt6-plugins-6.4.2.2.3 python-dotenv-1.0.0 pywin32-ctypes-0.2.0 qt6-applications-6.4.3.2.3 qt6-tools-6.4.3.1.3
409 INFO: PyInstaller: 5.10.1
409 INFO: Python: 3.11.3
416 INFO: Platform: Windows-10-10.0.22621-SP0
417 INFO: wrote D:\DEV\5th-age-monster-builder\app.spec
421 INFO: UPX is not available.
421 INFO: Removing temporary files and cleaning cache in C:\Users\titsw\AppData\Local\pyinstaller
438 INFO: Extending PYTHONPATH with paths
['D:\\DEV\\5th-age-monster-builder\\src']
656 INFO: checking Analysis
657 INFO: Building Analysis because Analysis-00.toc is non existent
657 INFO: Initializing module dependency graph...
658 INFO: Caching module graph hooks...
675 INFO: Analyzing base_library.zip ...
2032 INFO: Loading module hook 'hook-heapq.py' from 'D:\\DEV\\5th-age-monster-builder\\venv\\Lib\\site-packages\\PyInstaller\\hooks'...
2093 INFO: Loading module hook 'hook-encodings.py' from 'D:\\DEV\\5th-age-monster-builder\\venv\\Lib\\site-packages\\PyInstaller\\hooks'...
3106 INFO: Loading module hook 'hook-pickle.py' from 'D:\\DEV\\5th-age-monster-builder\\venv\\Lib\\site-packages\\PyInstaller\\hooks'...
4202 INFO: Caching module dependency graph...
4268 INFO: running Analysis Analysis-00.toc
4271 INFO: Adding Microsoft.Windows.Common-Controls to dependent assemblies of final executable
  required by C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.1008.0_x64__qbz5n2kfra8p0\python.exe
4283 WARNING: lib not found: api-ms-win-appmodel-runtime-l1-1-0.dll dependency of C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.1008.0_x64__qbz5n2kfra8p0\python.exe
4316 INFO: Analyzing D:\DEV\5th-age-monster-builder\src\app.py
4360 INFO: Loading module hook 'hook-PyQt6.py' from 'D:\\DEV\\5th-age-monster-builder\\venv\\Lib\\site-packages\\PyInstaller\\hooks'...
4574 INFO: Processing module hooks...
4598 INFO: Loading module hook 'hook-PyQt6.QtCore.py' from 'D:\\DEV\\5th-age-monster-builder\\venv\\Lib\\site-packages\\PyInstaller\\hooks'...
4726 INFO: Loading module hook 'hook-PyQt6.QtGui.py' from 'D:\\DEV\\5th-age-monster-builder\\venv\\Lib\\site-packages\\PyInstaller\\hooks'...
4840 INFO: Loading module hook 'hook-PyQt6.QtWidgets.py' from 'D:\\DEV\\5th-age-monster-builder\\venv\\Lib\\site-packages\\PyInstaller\\hooks'...
4945 INFO: Looking for ctypes DLLs
4951 INFO: Analyzing run-time hooks ...
4953 INFO: Including run-time hook 'D:\\DEV\\5th-age-monster-builder\\venv\\Lib\\site-packages\\PyInstaller\\hooks\\rthooks\\pyi_rth_inspect.py'
4954 INFO: Including run-time hook 'D:\\DEV\\5th-age-monster-builder\\venv\\Lib\\site-packages\\PyInstaller\\hooks\\rthooks\\pyi_rth_pyqt6.py'
4955 INFO: Including run-time hook 'D:\\DEV\\5th-age-monster-builder\\venv\\Lib\\site-packages\\PyInstaller\\hooks\\rthooks\\pyi_rth_pkgutil.py'
4958 INFO: Looking for dynamic libraries
233 INFO: Extra DLL search directories (AddDllDirectory): ['D:\\DEV\\5th-age-monster-builder\\venv\\Lib\\site-packages\\PyQt6\\Qt6\\bin']
233 INFO: Extra DLL search directories (PATH): ['D:\\DEV\\5th-age-monster-builder\\venv\\Lib\\site-packages\\PyQt6\\Qt6\\bin', 'D:\\DEV\\5th-age-monster-builder\\venv\\Scripts', 'C:\\Program Files (x86)\\NVIDIA Corporation\\PhysX\\Common', 'C:\\WINDOWS\\system32', 'C:\\WINDOWS', 'C:\\WINDOWS\\System32\\Wbem', 'C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\', 'C:\\WINDOWS\\System32\\OpenSSH\\', 'C:\\Program Files\\Microsoft VS Code\\bin', 'C:\\ProgramData\\chocolatey\\bin', 'C:\\Program Files\\dotnet\\', 'C:\\Program Files\\Git\\cmd', 'C:\\Program Files\\Git\\mingw64\\bin', 'C:\\Program Files\\Git\\usr\\bin', 'C:\\Program Files\\Docker\\Docker\\resources\\bin', 'C:\\Program Files\\1Password CLI', 'C:\\Users\\titsw\\AppData\\Local\\Microsoft\\WindowsApps']
597 WARNING: lib not found: api-ms-win-shcore-scaling-l1-1-1.dll dependency of D:\DEV\5th-age-monster-builder\venv\Lib\site-packages\PyQt6\Qt6\plugins\platforms\qwindows.dll
6015 INFO: Looking for eggs
6015 INFO: Using Python library C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.1008.0_x64__qbz5n2kfra8p0\python311.dll
6016 INFO: Found binding redirects:
[]
6017 INFO: Warnings written to D:\DEV\5th-age-monster-builder\build\app\warn-app.txt                                                                                                                                                                                                                             6029 INFO: Graph cross-reference written to D:\DEV\5th-age-monster-builder\build\app\xref-app.html                                                                                                                                                                                                               6055 INFO: checking PYZ                                                                                                                                                                                                                                                                                          6055 INFO: Building PYZ because PYZ-00.toc is non existent                                                                                                                                                                                                                                                       6056 INFO: Building PYZ (ZlibArchive) D:\DEV\5th-age-monster-builder\build\app\PYZ-00.pyz                                                                                                                                                                                                                        
6241 INFO: Building PYZ (ZlibArchive) D:\DEV\5th-age-monster-builder\build\app\PYZ-00.pyz completed successfully.
6251 INFO: checking PKG
6251 INFO: Building PKG because PKG-00.toc is non existent
6252 INFO: Building PKG (CArchive) app.pkg
14090 INFO: Building PKG (CArchive) app.pkg completed successfully.
14092 INFO: Bootloader D:\DEV\5th-age-monster-builder\venv\Lib\site-packages\PyInstaller\bootloader\Windows-64bit-intel\runw.exe
14092 INFO: checking EXE
14092 INFO: Building EXE because EXE-00.toc is non existent
14092 INFO: Building EXE from EXE-00.toc
14092 INFO: Copying bootloader EXE to D:\DEV\5th-age-monster-builder\dist\app.exe.notanexecutable
14136 INFO: Copying icon to EXE
14139 INFO: Copying icons from ['D:\\DEV\\5th-age-monster-builder\\venv\\Lib\\site-packages\\PyInstaller\\bootloader\\images\\icon-windowed.ico']
14159 INFO: Writing RT_GROUP_ICON 0 resource with 104 bytes
14159 INFO: Writing RT_ICON 1 resource with 3752 bytes
14159 INFO: Writing RT_ICON 2 resource with 2216 bytes
14160 INFO: Writing RT_ICON 3 resource with 1384 bytes
14160 INFO: Writing RT_ICON 4 resource with 38188 bytes
14160 INFO: Writing RT_ICON 5 resource with 9640 bytes
14160 INFO: Writing RT_ICON 6 resource with 4264 bytes
14160 INFO: Writing RT_ICON 7 resource with 1128 bytes
14161 INFO: Copying 0 resources to EXE
14161 INFO: Embedding manifest in EXE
14162 INFO: Updating manifest in D:\DEV\5th-age-monster-builder\dist\app.exe.notanexecutable
14186 INFO: Updating resource type 24 name 1 language 0
14188 INFO: Appending PKG archive to EXE
14206 INFO: Fixing EXE headers
17506 INFO: Building EXE from EXE-00.toc completed successfully.
```
