from utils.classes import Creature
import qtmodern.styles, qtmodern.windows
from builderUI import Ui_role
from PyQt6 import QtWidgets, QtCore, QtGui


class MainWindow(QtWidgets.QMainWindow, Ui_role):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.ability_buttons = []
        self.ability_dcs = []
        self.ability_descriptions = []
        self.ability_labels = []
        self.ability_names = []

        self.attack_buttons = []
        self.attack_defenses = []
        self.attack_descriptions = []
        self.attack_label1s = []
        self.attack_labels = []
        self.attack_names = []
        self.attack_types = []

        self.abilityRows = ["Hide", "Hide", "Hide", "Hide", "Hide"]
        self.attackRows = ["Hide", "Hide", "Hide", "Hide", "Hide", "Hide", "Hide"]

        self.setupAttacks()
        self.setupAbilities()

        self.addAbilityButton.clicked.connect(self.addAbility)
        self.addAttackButton.clicked.connect(self.addAttack)
        self.generateButton.clicked.connect(self.generateCreature)
        self.resetButton.clicked.connect(self.displayOutput.clear)

    def setupAttacks(self):
        for n, i in enumerate(self.attackRows):
            self.attack_names.append(
                QtWidgets.QLineEdit(parent=self.attackGridLayoutWidget)
            )
            self.attack_names[n].setObjectName(f"attack_names{[n]}")
            self.attack_names[n].setText(
                QtCore.QCoreApplication.translate("role", "Attack Name")
            )
            self.attack_names[n].hide()
            self.attackGridLayout.addWidget(self.attack_names[n], n, 0, 1, 1)

            self.attack_labels.append(
                QtWidgets.QLabel(parent=self.attackGridLayoutWidget)
            )
            self.attack_labels[n].setLayoutDirection(
                QtCore.Qt.LayoutDirection.LeftToRight
            )
            self.attack_labels[n].setAlignment(
                QtCore.Qt.AlignmentFlag.AlignLeading
                | QtCore.Qt.AlignmentFlag.AlignLeft
                | QtCore.Qt.AlignmentFlag.AlignVCenter
            )
            self.attack_labels[n].setObjectName(f"attack_labels{[n]}")
            self.attack_labels[n].setText(
                QtCore.QCoreApplication.translate("role", "vs.")
            )
            self.attack_labels[n].hide()
            self.attackGridLayout.addWidget(self.attack_labels[n], n, 1, 1, 1)

            self.attack_defenses.append(
                QtWidgets.QComboBox(parent=self.attackGridLayoutWidget)
            )
            self.attack_defenses[n].setObjectName(f"attack_defenses{[n]}")
            self.attack_defenses[n].addItem("")
            self.attack_defenses[n].addItem("")
            self.attack_defenses[n].addItem("")
            self.attack_defenses[n].setCurrentText(
                QtCore.QCoreApplication.translate("role", "AC")
            )
            self.attack_defenses[n].setItemText(
                0, QtCore.QCoreApplication.translate("role", "AC")
            )
            self.attack_defenses[n].setItemText(
                1, QtCore.QCoreApplication.translate("role", "PD")
            )
            self.attack_defenses[n].setItemText(
                2, QtCore.QCoreApplication.translate("role", "MD")
            )
            self.attack_defenses[n].hide()
            self.attackGridLayout.addWidget(self.attack_defenses[n], n, 2, 1, 1)

            self.attack_label1s.append(
                QtWidgets.QLabel(parent=self.attackGridLayoutWidget)
            )
            self.attack_label1s[n].setLayoutDirection(
                QtCore.Qt.LayoutDirection.LeftToRight
            )
            self.attack_label1s[n].setAlignment(
                QtCore.Qt.AlignmentFlag.AlignLeading
                | QtCore.Qt.AlignmentFlag.AlignLeft
                | QtCore.Qt.AlignmentFlag.AlignVCenter
            )
            self.attack_label1s[n].setObjectName(f"attack_label1s{[n]}")
            self.attack_label1s[n].setText(
                QtCore.QCoreApplication.translate("role", ":")
            )
            self.attack_label1s[n].hide()
            self.attackGridLayout.addWidget(self.attack_label1s[n], n, 3, 1, 1)

            self.attack_types.append(
                QtWidgets.QComboBox(parent=self.attackGridLayoutWidget)
            )
            self.attack_types[n].setCurrentText("")
            self.attack_types[n].setObjectName(f"attack_types{[n]}")
            self.attack_types[n].addItem("")
            self.attack_types[n].setItemText(0, "")
            self.attack_types[n].addItem("")
            self.attack_types[n].addItem("")
            self.attack_types[n].addItem("")
            self.attack_types[n].addItem("")
            self.attack_types[n].addItem("")
            self.attack_types[n].addItem("")
            self.attack_types[n].addItem("")
            self.attack_types[n].addItem("")
            self.attack_types[n].addItem("")
            self.attack_types[n].addItem("")
            self.attack_types[n].setItemText(
                1, QtCore.QCoreApplication.translate("role", "Acid")
            )
            self.attack_types[n].setItemText(
                2, QtCore.QCoreApplication.translate("role", "Cold")
            )
            self.attack_types[n].setItemText(
                3, QtCore.QCoreApplication.translate("role", "Fire")
            )
            self.attack_types[n].setItemText(
                4, QtCore.QCoreApplication.translate("role", "Force")
            )
            self.attack_types[n].setItemText(
                5, QtCore.QCoreApplication.translate("role", "Lightning")
            )
            self.attack_types[n].setItemText(
                6, QtCore.QCoreApplication.translate("role", "Necrotic")
            )
            self.attack_types[n].setItemText(
                7, QtCore.QCoreApplication.translate("role", "Poison")
            )
            self.attack_types[n].setItemText(
                8, QtCore.QCoreApplication.translate("role", "Psychic")
            )
            self.attack_types[n].setItemText(
                9, QtCore.QCoreApplication.translate("role", "Radiant")
            )
            self.attack_types[n].setItemText(
                10, QtCore.QCoreApplication.translate("role", "Thunder")
            )
            self.attack_types[n].hide()
            self.attackGridLayout.addWidget(self.attack_types[n], n, 4, 1, 1)

            self.attack_descriptions.append(
                QtWidgets.QLineEdit(parent=self.attackGridLayoutWidget)
            )
            self.attack_descriptions[n].setObjectName(f"attack_descriptions{[n]}")
            self.attack_descriptions[n].setText(
                QtCore.QCoreApplication.translate("role", "Description")
            )
            self.attack_descriptions[n].hide()
            self.attackGridLayout.addWidget(self.attack_descriptions[n], n, 5, 1, 1)

            self.attack_buttons.append(
                QtWidgets.QPushButton(parent=self.attackGridLayoutWidget)
            )
            self.attack_buttons[n].setObjectName(f"attack_button_{n}")
            self.attack_buttons[n].setText(
                QtCore.QCoreApplication.translate("role", "-")
            )
            self.attackGridLayout.addWidget(self.attack_buttons[n], n, 6, 1, 1)
            self.attack_buttons[n].row = n
            self.attack_buttons[n].hide()
            self.attack_buttons[n].clicked.connect(self.removeAttack)
            if n == 0:
                self.addAttack()

    def setupAbilities(self):
        for n, i in enumerate(self.abilityRows):
            self.ability_names.append(
                QtWidgets.QLineEdit(parent=self.abilityGridLayoutWidget)
            )
            self.ability_names[n].setObjectName(f"ability_name_{n}")
            self.ability_names[n].setText(
                QtCore.QCoreApplication.translate("role", "Ability Name")
            )
            self.ability_names[n].hide()
            self.abilityGridLayout.addWidget(self.ability_names[n], n, 0, 1, 1)

            self.ability_dcs.append(
                QtWidgets.QLineEdit(parent=self.abilityGridLayoutWidget)
            )
            self.ability_dcs[n].setObjectName(f"ability_dc_{n}")
            self.ability_dcs[n].setText(QtCore.QCoreApplication.translate("role", "DC"))
            self.ability_dcs[n].hide()
            self.abilityGridLayout.addWidget(self.ability_dcs[n], n, 1, 1, 1)

            self.ability_labels.append(
                QtWidgets.QLabel(parent=self.abilityGridLayoutWidget)
            )
            self.ability_labels[n].setLayoutDirection(
                QtCore.Qt.LayoutDirection.LeftToRight
            )
            self.ability_labels[n].setAlignment(
                QtCore.Qt.AlignmentFlag.AlignRight
                | QtCore.Qt.AlignmentFlag.AlignTrailing
                | QtCore.Qt.AlignmentFlag.AlignVCenter
            )
            self.ability_labels[n].setObjectName(f"ability_label_{n}")
            self.ability_labels[n].setText(
                QtCore.QCoreApplication.translate("role", ":")
            )
            self.ability_labels[n].hide()
            self.abilityGridLayout.addWidget(self.ability_labels[n], n, 5, 1, 1)

            self.ability_descriptions.append(
                QtWidgets.QLineEdit(parent=self.abilityGridLayoutWidget)
            )
            self.ability_descriptions[n].setObjectName(f"ability_description_{n}")
            self.ability_descriptions[n].setText(
                QtCore.QCoreApplication.translate("role", "Description")
            )
            self.ability_descriptions[n].hide()
            self.abilityGridLayout.addWidget(self.ability_descriptions[n], n, 6, 1, 1)

            self.ability_buttons.append(
                QtWidgets.QPushButton(parent=self.abilityGridLayoutWidget)
            )
            self.ability_buttons[n].setObjectName(f"ability_button_{n}")
            self.ability_buttons[n].setText(
                QtCore.QCoreApplication.translate("role", "-")
            )
            self.abilityGridLayout.addWidget(self.ability_buttons[n], n, 7, 1, 1)
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

    def addAttack(self):
        for idx, row in enumerate(self.attackRows):
            if row == "Hide":
                self.attackRows[idx] = "Show"
                self.attack_names[idx].show()
                self.attack_defenses[idx].show()
                self.attack_label1s[idx].show()
                self.attack_labels[idx].show()
                self.attack_types[idx].show()
                self.attack_descriptions[idx].show()
                self.attack_buttons[idx].show()
                break

    def removeAbility(self):
        self.abilityRows[self.sender().row] = "Hide"
        self.ability_names[self.sender().row].hide()
        self.ability_dcs[self.sender().row].hide()
        self.ability_labels[self.sender().row].hide()
        self.ability_descriptions[self.sender().row].hide()
        self.ability_buttons[self.sender().row].hide()

    def removeAttack(self):
        self.attackRows[self.sender().row] = "Hide"
        self.attack_names[self.sender().row].hide()
        self.attack_defenses[self.sender().row].hide()
        self.attack_label1s[self.sender().row].hide()
        self.attack_labels[self.sender().row].hide()
        self.attack_types[self.sender().row].hide()
        self.attack_descriptions[self.sender().row].hide()
        self.attack_buttons[self.sender().row].hide()

    def generateCreature(self):
        # test = Creature(name="Half-Orc Commander",
        #                 abilities=[{"name": "Orcish Command", "description": "When a nearby ally of the half-orc commander scores a critical hit, that ally can roll a save against a save ends effect as a free action."}, {"name": "Lethal Swing", "description": "Once per battle, a half-orc can reroll a melee attack and use the result it prefers"}],
        #                 attacks=[{"name": "Jagged Longsword", "defense": "AC", "triggers": [{"condition": "even hit", "description": "One nearby lower-level mook makes an attack as a free action."}]}, {"name": "Thrown Javelin", "defense": "AC", "range": "Ranged", "triggers": [{"condition": "even hit", "description": "The half-orc commander gains 20 temporary hit points."}]}],
        #                 creature_type="Humanoid",
        #                 favored_defenses=["PD"],
        #                 initiative_type="Fast",
        #                 level=8,
        #                 role="Leader",
        #                 size="Medium",
        #                 strength="Normal",
        #                 template="Leader"
        # )
        # print(test)
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = MainWindow()

    qtmodern.styles.dark(app)
    mw = qtmodern.windows.ModernWindow(window)
    mw.show()
    app.exec()
