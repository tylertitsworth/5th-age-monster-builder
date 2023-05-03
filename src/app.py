from utils.classes import Creature
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
        self.attack_ranges = []
        self.attack_types = []

        self.condition_add_buttons = []
        self.condition_buttons = []
        self.condition_conditions = []
        self.condition_descriptions = []
        self.condition_labels = []

        self.abilityRows = ["Hide", "Hide", "Hide", "Hide"]
        self.attackRows = ["Hide", "Hide", "Hide", "Hide", "Hide", "Hide", "Hide", "Hide"]

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
            self.abilityGridLayout.addWidget(self.ability_labels[n], n, 2, 1, 1)

            self.ability_descriptions.append(
                QtWidgets.QLineEdit(parent=self.abilityGridLayoutWidget)
            )
            self.ability_descriptions[n].setObjectName(f"ability_description_{n}")
            self.ability_descriptions[n].setText(
                QtCore.QCoreApplication.translate("role", "Description")
            )
            self.ability_descriptions[n].hide()
            self.abilityGridLayout.addWidget(self.ability_descriptions[n], n, 3, 1, 1)

            self.ability_buttons.append(
                QtWidgets.QPushButton(parent=self.abilityGridLayoutWidget)
            )
            self.ability_buttons[n].setObjectName(f"ability_button_{n}")
            self.ability_buttons[n].setText(
                QtCore.QCoreApplication.translate("role", "-")
            )
            self.abilityGridLayout.addWidget(self.ability_buttons[n], n, 4, 1, 1)
            self.ability_buttons[n].row = n
            self.ability_buttons[n].hide()
            self.ability_buttons[n].clicked.connect(self.removeAbility)

        for n, i in enumerate(self.attackRows):
            if n % 2 == 0:
                self.attack_ranges.append(
                    QtWidgets.QComboBox(parent=self.attackGridLayoutWidget)
                )
                self.attack_ranges[n].setObjectName(f"attack_range_{n}")
                self.attack_ranges[n].addItem("")
                self.attack_ranges[n].addItem("")
                self.attack_ranges[n].addItem("")
                self.attack_ranges[n].setCurrentText(
                    QtCore.QCoreApplication.translate("role", "Melee")
                )
                self.attack_ranges[n].setItemText(
                    0, QtCore.QCoreApplication.translate("role", "Melee")
                )
                self.attack_ranges[n].setItemText(
                    1, QtCore.QCoreApplication.translate("role", "Ranged")
                )
                self.attack_ranges[n].setItemText(
                    2, QtCore.QCoreApplication.translate("role", "Close")
                )
                self.attack_ranges[n].hide()
                self.attackGridLayout.addWidget(self.attack_ranges[n], n, 0, 1, 1)

                self.attack_names.append(
                    QtWidgets.QLineEdit(parent=self.attackGridLayoutWidget)
                )
                self.attack_names[n].setObjectName(f"attack_name_{n}")
                self.attack_names[n].setText(
                    QtCore.QCoreApplication.translate("role", "Attack Name")
                )
                self.attack_names[n].hide()
                self.attackGridLayout.addWidget(self.attack_names[n], n, 1, 1, 1)

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
                self.attack_labels[n].setObjectName(f"attack_label_{n}")
                self.attack_labels[n].setText(
                    QtCore.QCoreApplication.translate("role", "vs.")
                )
                self.attack_labels[n].hide()
                self.attackGridLayout.addWidget(self.attack_labels[n], n, 2, 1, 1)

                self.attack_defenses.append(
                    QtWidgets.QComboBox(parent=self.attackGridLayoutWidget)
                )
                self.attack_defenses[n].setObjectName(f"attack_defense_{n}")
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
                self.attackGridLayout.addWidget(self.attack_defenses[n], n, 3, 1, 1)

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
                self.attack_label1s[n].setObjectName(f"attack_label1_{n}")
                self.attack_label1s[n].setText(
                    QtCore.QCoreApplication.translate("role", ":")
                )
                self.attack_label1s[n].hide()
                self.attackGridLayout.addWidget(self.attack_label1s[n], n, 4, 1, 1)

                self.attack_types.append(
                    QtWidgets.QComboBox(parent=self.attackGridLayoutWidget)
                )
                self.attack_types[n].setCurrentText("")
                self.attack_types[n].setObjectName(f"attack_type_{n}")
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
                self.attackGridLayout.addWidget(self.attack_types[n], n, 5, 1, 1)

                self.attack_descriptions.append(
                    QtWidgets.QLineEdit(parent=self.attackGridLayoutWidget)
                )
                self.attack_descriptions[n].setObjectName(f"attack_description_{n}")
                self.attack_descriptions[n].setText(
                    QtCore.QCoreApplication.translate("role", "Hit effect")
                )
                self.attack_descriptions[n].hide()
                self.attackGridLayout.addWidget(self.attack_descriptions[n], n, 6, 1, 1)

                self.condition_add_buttons.append(
                    QtWidgets.QPushButton(parent=self.attackGridLayoutWidget)
                )
                self.condition_add_buttons[n].setObjectName(f"condition_add_button_{n}")
                self.condition_add_buttons[n].setText(
                    QtCore.QCoreApplication.translate("role", "+ Condition")
                )
                self.condition_add_buttons[n].hide()
                self.condition_add_buttons[n].clicked.connect(self.addCondition)
                self.attackGridLayout.addWidget(
                    self.condition_add_buttons[n], n, 7, 1, 1
                )

                self.attack_buttons.append(
                    QtWidgets.QPushButton(parent=self.attackGridLayoutWidget)
                )
                self.attack_buttons[n].setObjectName(f"attack_button_{n}")
                self.attack_buttons[n].setText(
                    QtCore.QCoreApplication.translate("role", "-")
                )
                self.attackGridLayout.addWidget(self.attack_buttons[n], n, 8, 1, 1)
                self.attack_buttons[n].row = n
                self.attack_buttons[n].hide()
                self.attack_buttons[n].clicked.connect(self.removeAttack)

                self.condition_buttons.append("")
                self.condition_conditions.append("")
                self.condition_descriptions.append("")
                self.condition_labels.append("")

            else:
                self.condition_conditions.append(
                    QtWidgets.QLineEdit(parent=self.attackGridLayoutWidget)
                )
                self.condition_conditions[n].setObjectName(f"condition_condition_{n}")
                self.condition_conditions[n].setText(
                    QtCore.QCoreApplication.translate("role", "even hit")
                )
                self.condition_conditions[n].hide()
                self.attackGridLayout.addWidget(
                    self.condition_conditions[n], n, 1, 1, 1
                )

                self.condition_labels.append(
                    QtWidgets.QLabel(parent=self.attackGridLayoutWidget)
                )
                self.condition_labels[n].setLayoutDirection(
                    QtCore.Qt.LayoutDirection.LeftToRight
                )
                self.condition_labels[n].setAlignment(
                    QtCore.Qt.AlignmentFlag.AlignLeading
                    | QtCore.Qt.AlignmentFlag.AlignLeft
                    | QtCore.Qt.AlignmentFlag.AlignVCenter
                )
                self.condition_labels[n].setObjectName(f"condition_label_{n}")
                self.condition_labels[n].setText(
                    QtCore.QCoreApplication.translate("role", ":")
                )
                self.condition_labels[n].hide()
                self.attackGridLayout.addWidget(self.condition_labels[n], n, 2, 1, 1)

                self.condition_descriptions.append(
                    QtWidgets.QLineEdit(parent=self.attackGridLayoutWidget)
                )
                self.condition_descriptions[n].setObjectName(
                    f"condition_description_{n}"
                )
                self.condition_descriptions[n].setText(
                    QtCore.QCoreApplication.translate("role", "Condition Description")
                )
                self.condition_descriptions[n].hide()
                self.attackGridLayout.addWidget(
                    self.condition_descriptions[n], n, 6, 1, 1
                )

                self.condition_buttons.append(
                    QtWidgets.QPushButton(parent=self.attackGridLayoutWidget)
                )
                self.condition_buttons[n].setObjectName(f"condition_button_{n}")
                self.condition_buttons[n].setText(
                    QtCore.QCoreApplication.translate("role", "-")
                )
                self.attackGridLayout.addWidget(self.condition_buttons[n], n, 8, 1, 1)
                self.condition_buttons[n].row = n
                self.condition_buttons[n].hide()
                self.condition_buttons[n].clicked.connect(self.removeCondition)

                self.attack_buttons.append("")
                self.attack_defenses.append("")
                self.attack_descriptions.append("")
                self.attack_label1s.append("")
                self.attack_labels.append("")
                self.attack_names.append("")
                self.attack_ranges.append("")
                self.attack_types.append("")
                self.condition_add_buttons.append("")

        self.addAttack()

        self.addAbilityButton.clicked.connect(self.addAbility)
        self.addAttackButton.clicked.connect(self.addAttack)
        self.generateButton.clicked.connect(self.generateCreature)
        self.resetButton.clicked.connect(self.displayOutput.clear)

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
            if (idx == 0 or idx % 2 == 0) and row == "Hide":
                self.attackRows[idx] = "Show"
                self.attack_buttons[idx].show()
                self.attack_defenses[idx].show()
                self.attack_descriptions[idx].show()
                self.attack_label1s[idx].show()
                self.attack_labels[idx].show()
                self.attack_names[idx].show()
                self.attack_ranges[idx].show()
                self.attack_types[idx].show()
                self.condition_add_buttons[idx].show()
                break


    def addCondition(self):
        for idx, row in enumerate(self.attackRows):
            if idx % 2 != 0 and row == "Hide":
                self.attackRows[idx] = "Show"
                self.condition_buttons[idx].show()
                self.condition_conditions[idx].show()
                self.condition_descriptions[idx].show()
                self.condition_labels[idx].show()
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
        self.attack_ranges[self.sender().row].hide()
        self.attack_types[self.sender().row].hide()
        self.attack_descriptions[self.sender().row].hide()
        self.attack_buttons[self.sender().row].hide()
        self.condition_add_buttons[self.sender().row].hide()

    def removeCondition(self):
        self.attackRows[self.sender().row] = "Hide"
        self.condition_conditions[self.sender().row].hide()
        self.condition_labels[self.sender().row].hide()
        self.condition_descriptions[self.sender().row].hide()
        self.condition_buttons[self.sender().row].hide()

    def generateCreature(self):
        abilities = []
        attacks = []

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
        for idx, row in enumerate(self.attackRows):
            if row == "Show":
                if not hasattr(self.attack_types[idx], "currentText"):  # No Type
                    if idx % 2 == 0:
                        if self.attackRows[idx + 1] == "Show":  # Yes Condition
                            attacks.append(
                                {
                                    "defense": self.attack_defenses[
                                        idx
                                    ].currentText(),
                                    "description": self.attack_descriptions[
                                        idx
                                    ].text(),
                                    "name": self.attack_names[idx].text(),
                                    "range": self.attack_ranges[idx].currentText(),
                                    "triggers": [
                                        {
                                            "condition": self.condition_conditions[
                                                idx + 1
                                            ].text(),
                                            "description": self.condition_descriptions[
                                                idx + 1
                                            ].text(),
                                        }
                                    ],
                                }
                            )
                        else:  # No Condition
                            attacks.append(
                                {
                                    "defense": self.attack_defenses[idx].currentText(),
                                    "description": self.attack_descriptions[idx].text(),
                                    "name": self.attack_names[idx].text(),
                                    "range": self.attack_ranges[idx].currentText(),
                                }
                            )
                    else:
                        pass
                else:  # Yes Type
                    if idx % 2 == 0:
                        if self.attackRows[idx + 1] == "Show":  # Yes Condition
                            attacks.append(
                                {
                                    "damage_type": self.attack_types[
                                        idx
                                    ].currentText(),
                                    "defense": self.attack_defenses[
                                        idx
                                    ].currentText(),
                                    "description": self.attack_descriptions[
                                        idx
                                    ].text(),
                                    "name": self.attack_names[idx].text(),
                                    "range": self.attack_ranges[idx].currentText(),
                                    "triggers": [
                                        {
                                            "condition": self.condition_conditions[
                                                idx + 1
                                            ].text(),
                                            "description": self.condition_descriptions[
                                                idx + 1
                                            ].text(),
                                        }
                                    ],
                                }
                            )
                        else:  # No Condition
                            attacks.append(
                                {
                                    "damage_type": self.attack_types[idx].currentText(),
                                    "defense": self.attack_defenses[idx].currentText(),
                                    "description": self.attack_descriptions[idx].text(),
                                    "name": self.attack_names[idx].text(),
                                    "range": self.attack_ranges[idx].currentText(),
                                }
                            )
                    else:
                        pass
            else:
                if idx % 2 == 0 and self.attackRows[idx - 2] == "Show" and self.attackRows[idx + 1] == "Show":
                    attacks[idx - 2]["triggers"].append(
                        {
                            "condition": self.condition_conditions[
                                idx + 1
                            ].text(),
                            "description": self.condition_descriptions[
                                idx + 1
                            ].text(),
                        }
                    )
                if idx % 2 == 0 and idx >= 4 and self.attackRows[idx - 4] == "Show" and self.attackRows[idx + 1] == "Show":
                    attacks[idx - 4]["triggers"].append(
                        {
                            "condition": self.condition_conditions[
                                idx + 1
                            ].text(),
                            "description": self.condition_descriptions[
                                idx + 1
                            ].text(),
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
                    favored_defenses=[
                        i.text() for i in self.favored_defense.selectedItems()
                    ],
                    immunities=[i.text() for i in self.immunities.selectedItems()],
                    initiative_type=self.initiative_modifier.currentText(),
                    level=int(self.level.currentText()),
                    role=self.role.currentText(),
                    size=self.creatureSize.currentText(),
                    strength=self.strength.currentText(),
                    template=self.template.currentText(),
                    vulnerabilities=[
                        i.text() for i in self.vulnerabilities.selectedItems()
                    ],
                )
            )
        )


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = MainWindow()

    window.show()
    app.exec()
