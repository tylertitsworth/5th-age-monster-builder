# Form implementation generated from reading ui file '.\monsterBuilderv1.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_role(object):
    def setupUi(self, role):
        role.setObjectName("role")
        role.resize(975, 753)
        self.centralwidget = QtWidgets.QWidget(parent=role)
        self.centralwidget.setObjectName("centralwidget")
        self.creatureSize = QtWidgets.QComboBox(parent=self.centralwidget)
        self.creatureSize.setGeometry(QtCore.QRect(140, 80, 81, 22))
        self.creatureSize.setObjectName("size")
        self.creatureSize.addItem("")
        self.creatureSize.addItem("")
        self.creatureSize.addItem("")
        self.creatureSize.addItem("")
        self.creatureSize.addItem("")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 80, 101, 21))
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 101, 21))
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.name = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.name.setGeometry(QtCore.QRect(140, 20, 171, 22))
        self.name.setObjectName("name")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 101, 21))
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.level = QtWidgets.QComboBox(parent=self.centralwidget)
        self.level.setGeometry(QtCore.QRect(140, 50, 41, 22))
        self.level.setObjectName("level")
        self.level.addItem("")
        self.level.addItem("")
        self.level.addItem("")
        self.level.addItem("")
        self.level.addItem("")
        self.level.addItem("")
        self.level.addItem("")
        self.level.addItem("")
        self.level.addItem("")
        self.level.addItem("")
        self.level.addItem("")
        self.level.addItem("")
        self.level.addItem("")
        self.level.addItem("")
        self.level.addItem("")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 110, 101, 21))
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.strength = QtWidgets.QComboBox(parent=self.centralwidget)
        self.strength.setGeometry(QtCore.QRect(140, 110, 71, 22))
        self.strength.setObjectName("strength")
        self.strength.addItem("")
        self.strength.addItem("")
        self.strength.addItem("")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 140, 101, 21))
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.type = QtWidgets.QComboBox(parent=self.centralwidget)
        self.type.setGeometry(QtCore.QRect(140, 140, 111, 22))
        self.type.setObjectName("type")
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 170, 101, 21))
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.role = QtWidgets.QComboBox(parent=self.centralwidget)
        self.role.setGeometry(QtCore.QRect(140, 170, 81, 22))
        self.role.setObjectName("role")
        self.role.addItem("")
        self.role.addItem("")
        self.role.addItem("")
        self.role.addItem("")
        self.role.addItem("")
        self.role.addItem("")
        self.role.addItem("")
        self.role.addItem("")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 200, 101, 21))
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.favored_defense = QtWidgets.QListWidget(parent=self.centralwidget)
        self.favored_defense.setGeometry(QtCore.QRect(140, 200, 41, 41))
        self.favored_defense.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.MultiSelection)
        self.favored_defense.setObjectName("favored_defense")
        item = QtWidgets.QListWidgetItem()
        self.favored_defense.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.favored_defense.addItem(item)
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 250, 101, 21))
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.initiative_modifier = QtWidgets.QComboBox(parent=self.centralwidget)
        self.initiative_modifier.setGeometry(QtCore.QRect(140, 250, 191, 22))
        self.initiative_modifier.setObjectName("initiative_modifier")
        self.initiative_modifier.addItem("")
        self.initiative_modifier.addItem("")
        self.initiative_modifier.addItem("")
        self.initiative_modifier.addItem("")
        self.initiative_modifier.addItem("")
        self.initiative_modifier.addItem("")
        self.initiative_modifier.addItem("")
        self.initiative_modifier.addItem("")
        self.initiative_modifier.addItem("")
        self.initiative_modifier.addItem("")
        self.initiative_modifier.addItem("")
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 280, 101, 21))
        self.label_9.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_9.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.template = QtWidgets.QComboBox(parent=self.centralwidget)
        self.template.setGeometry(QtCore.QRect(140, 280, 91, 22))
        self.template.setObjectName("template")
        self.template.addItem("")
        self.template.addItem("")
        self.template.addItem("")
        self.template.addItem("")
        self.template.addItem("")
        self.template.addItem("")
        self.template.addItem("")
        self.template.addItem("")
        self.label_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 310, 101, 16))
        self.label_10.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_10.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(140, 310, 101, 16))
        self.label_11.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_11.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.immunities = QtWidgets.QListWidget(parent=self.centralwidget)
        self.immunities.setGeometry(QtCore.QRect(30, 330, 81, 191))
        self.immunities.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.MultiSelection)
        self.immunities.setObjectName("immunities")
        item = QtWidgets.QListWidgetItem()
        self.immunities.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.immunities.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.immunities.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.immunities.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.immunities.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.immunities.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.immunities.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.immunities.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.immunities.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.immunities.addItem(item)
        self.vulnerabilities = QtWidgets.QListWidget(parent=self.centralwidget)
        self.vulnerabilities.setGeometry(QtCore.QRect(140, 330, 81, 191))
        self.vulnerabilities.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.MultiSelection)
        self.vulnerabilities.setObjectName("vulnerabilities")
        item = QtWidgets.QListWidgetItem()
        self.vulnerabilities.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.vulnerabilities.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.vulnerabilities.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.vulnerabilities.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.vulnerabilities.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.vulnerabilities.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.vulnerabilities.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.vulnerabilities.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.vulnerabilities.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.vulnerabilities.addItem(item)
        self.displayOutput = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.displayOutput.setGeometry(QtCore.QRect(350, 20, 611, 291))
        self.displayOutput.setObjectName("displayOutput")
        self.generateButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.generateButton.setGeometry(QtCore.QRect(440, 320, 75, 24))
        self.generateButton.setObjectName("generateButton")
        self.resetButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.resetButton.setGeometry(QtCore.QRect(350, 320, 75, 24))
        self.resetButton.setObjectName("resetButton")
        self.label_12 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(240, 320, 101, 21))
        self.label_12.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_12.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(80, 530, 101, 21))
        self.label_13.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_13.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.addAttackButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.addAttackButton.setGeometry(QtCore.QRect(50, 530, 21, 24))
        self.addAttackButton.setObjectName("addAttackButton")
        self.addAbilityButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.addAbilityButton.setGeometry(QtCore.QRect(270, 320, 21, 24))
        self.addAbilityButton.setObjectName("addAbilityButton")
        self.abilityGridLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.abilityGridLayoutWidget.setGeometry(QtCore.QRect(260, 350, 701, 191))
        self.abilityGridLayoutWidget.setObjectName("abilityGridLayoutWidget")
        self.abilityGridLayout = QtWidgets.QGridLayout(self.abilityGridLayoutWidget)
        self.abilityGridLayout.setContentsMargins(0, 0, 0, 0)
        self.abilityGridLayout.setObjectName("abilityGridLayout")
        self.attackGridLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.attackGridLayoutWidget.setGeometry(QtCore.QRect(10, 560, 951, 171))
        self.attackGridLayoutWidget.setObjectName("attackGridLayoutWidget")
        self.attackGridLayout = QtWidgets.QGridLayout(self.attackGridLayoutWidget)
        self.attackGridLayout.setContentsMargins(0, 0, 0, 0)
        self.attackGridLayout.setColumnStretch(6, 6)
        self.attackGridLayout.setObjectName("attackGridLayout")
        role.setCentralWidget(self.centralwidget)

        self.retranslateUi(role)
        self.creatureSize.setCurrentIndex(2)
        self.level.setCurrentIndex(0)
        self.strength.setCurrentIndex(0)
        self.type.setCurrentIndex(8)
        self.role.setCurrentIndex(0)
        self.favored_defense.setCurrentRow(0)
        self.initiative_modifier.setCurrentIndex(1)
        self.template.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(role)

    def retranslateUi(self, role):
        _translate = QtCore.QCoreApplication.translate
        role.setWindowTitle(_translate("role", "5th Age Monster Builder"))
        self.creatureSize.setCurrentText(_translate("role", "Medium"))
        self.creatureSize.setItemText(0, _translate("role", "Tiny"))
        self.creatureSize.setItemText(1, _translate("role", "Small"))
        self.creatureSize.setItemText(2, _translate("role", "Medium"))
        self.creatureSize.setItemText(3, _translate("role", "Large"))
        self.creatureSize.setItemText(4, _translate("role", "Huge"))
        self.label.setText(_translate("role", "Size"))
        self.label_2.setText(_translate("role", "Name"))
        self.label_3.setText(_translate("role", "Level"))
        self.level.setCurrentText(_translate("role", "0"))
        self.level.setItemText(0, _translate("role", "0"))
        self.level.setItemText(1, _translate("role", "1"))
        self.level.setItemText(2, _translate("role", "2"))
        self.level.setItemText(3, _translate("role", "3"))
        self.level.setItemText(4, _translate("role", "4"))
        self.level.setItemText(5, _translate("role", "5"))
        self.level.setItemText(6, _translate("role", "6"))
        self.level.setItemText(7, _translate("role", "7"))
        self.level.setItemText(8, _translate("role", "8"))
        self.level.setItemText(9, _translate("role", "9"))
        self.level.setItemText(10, _translate("role", "10"))
        self.level.setItemText(11, _translate("role", "11"))
        self.level.setItemText(12, _translate("role", "12"))
        self.level.setItemText(13, _translate("role", "13"))
        self.level.setItemText(14, _translate("role", "14"))
        self.label_4.setText(_translate("role", "Strength"))
        self.strength.setCurrentText(_translate("role", "Normal"))
        self.strength.setItemText(0, _translate("role", "Normal"))
        self.strength.setItemText(1, _translate("role", "Double"))
        self.strength.setItemText(2, _translate("role", "Triple"))
        self.label_5.setText(_translate("role", "Type"))
        self.type.setCurrentText(_translate("role", "Humanoid"))
        self.type.setItemText(0, _translate("role", "Aberration"))
        self.type.setItemText(1, _translate("role", "Beast"))
        self.type.setItemText(2, _translate("role", "Celestial"))
        self.type.setItemText(3, _translate("role", "Construct"))
        self.type.setItemText(4, _translate("role", "Dragon"))
        self.type.setItemText(5, _translate("role", "Elemental"))
        self.type.setItemText(6, _translate("role", "Fiend"))
        self.type.setItemText(7, _translate("role", "Giant"))
        self.type.setItemText(8, _translate("role", "Humanoid"))
        self.type.setItemText(9, _translate("role", "Monstrosity"))
        self.type.setItemText(10, _translate("role", "Ooze"))
        self.type.setItemText(11, _translate("role", "Plant"))
        self.type.setItemText(12, _translate("role", "Undead"))
        self.label_6.setText(_translate("role", "Role"))
        self.role.setCurrentText(_translate("role", "Mook"))
        self.role.setItemText(0, _translate("role", "Mook"))
        self.role.setItemText(1, _translate("role", "Archer"))
        self.role.setItemText(2, _translate("role", "Blocker"))
        self.role.setItemText(3, _translate("role", "Caster"))
        self.role.setItemText(4, _translate("role", "Leader"))
        self.role.setItemText(5, _translate("role", "Spoiler"))
        self.role.setItemText(6, _translate("role", "Troop"))
        self.role.setItemText(7, _translate("role", "Wrecker"))
        self.label_7.setText(_translate("role", "Favored Defense"))
        __sortingEnabled = self.favored_defense.isSortingEnabled()
        self.favored_defense.setSortingEnabled(False)
        item = self.favored_defense.item(0)
        item.setText(_translate("role", "MD"))
        item = self.favored_defense.item(1)
        item.setText(_translate("role", "PD"))
        self.favored_defense.setSortingEnabled(__sortingEnabled)
        self.label_8.setText(_translate("role", "Initiative Modifer"))
        self.initiative_modifier.setCurrentText(_translate("role", "Slow and clumsy"))
        self.initiative_modifier.setItemText(0, _translate("role", "Super-slow and utterly clumsy"))
        self.initiative_modifier.setItemText(1, _translate("role", "Slow and clumsy"))
        self.initiative_modifier.setItemText(2, _translate("role", "Awkward or small"))
        self.initiative_modifier.setItemText(3, _translate("role", "Average"))
        self.initiative_modifier.setItemText(4, _translate("role", "Just above average"))
        self.initiative_modifier.setItemText(5, _translate("role", "Quick"))
        self.initiative_modifier.setItemText(6, _translate("role", "Fast"))
        self.initiative_modifier.setItemText(7, _translate("role", "Really fast"))
        self.initiative_modifier.setItemText(8, _translate("role", "Fast like a fast PC"))
        self.initiative_modifier.setItemText(9, _translate("role", "Blindingly fast"))
        self.initiative_modifier.setItemText(10, _translate("role", "Competing with the rogue"))
        self.label_9.setText(_translate("role", "Template"))
        self.template.setCurrentText(_translate("role", "None"))
        self.template.setItemText(0, _translate("role", "None"))
        self.template.setItemText(1, _translate("role", "Scrapper"))
        self.template.setItemText(2, _translate("role", "Offensive"))
        self.template.setItemText(3, _translate("role", "Oaf"))
        self.template.setItemText(4, _translate("role", "Defensive"))
        self.template.setItemText(5, _translate("role", "Lunk"))
        self.template.setItemText(6, _translate("role", "Brittle"))
        self.template.setItemText(7, _translate("role", "Leader"))
        self.label_10.setText(_translate("role", "Immunities"))
        self.label_11.setText(_translate("role", "Vulnerabilities"))
        __sortingEnabled = self.immunities.isSortingEnabled()
        self.immunities.setSortingEnabled(False)
        item = self.immunities.item(0)
        item.setText(_translate("role", "Acid"))
        item = self.immunities.item(1)
        item.setText(_translate("role", "Cold"))
        item = self.immunities.item(2)
        item.setText(_translate("role", "Fire"))
        item = self.immunities.item(3)
        item.setText(_translate("role", "Force"))
        item = self.immunities.item(4)
        item.setText(_translate("role", "Lightning"))
        item = self.immunities.item(5)
        item.setText(_translate("role", "Necrotic"))
        item = self.immunities.item(6)
        item.setText(_translate("role", "Poison"))
        item = self.immunities.item(7)
        item.setText(_translate("role", "Psychic"))
        item = self.immunities.item(8)
        item.setText(_translate("role", "Radiant"))
        item = self.immunities.item(9)
        item.setText(_translate("role", "Thunder"))
        self.immunities.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.vulnerabilities.isSortingEnabled()
        self.vulnerabilities.setSortingEnabled(False)
        item = self.vulnerabilities.item(0)
        item.setText(_translate("role", "Acid"))
        item = self.vulnerabilities.item(1)
        item.setText(_translate("role", "Cold"))
        item = self.vulnerabilities.item(2)
        item.setText(_translate("role", "Fire"))
        item = self.vulnerabilities.item(3)
        item.setText(_translate("role", "Force"))
        item = self.vulnerabilities.item(4)
        item.setText(_translate("role", "Lightning"))
        item = self.vulnerabilities.item(5)
        item.setText(_translate("role", "Necrotic"))
        item = self.vulnerabilities.item(6)
        item.setText(_translate("role", "Poison"))
        item = self.vulnerabilities.item(7)
        item.setText(_translate("role", "Psychic"))
        item = self.vulnerabilities.item(8)
        item.setText(_translate("role", "Radiant"))
        item = self.vulnerabilities.item(9)
        item.setText(_translate("role", "Thunder"))
        self.vulnerabilities.setSortingEnabled(__sortingEnabled)
        self.generateButton.setText(_translate("role", "Generate"))
        self.resetButton.setText(_translate("role", "Reset"))
        self.label_12.setText(_translate("role", "Abilities"))
        self.label_13.setText(_translate("role", "Attacks"))
        self.addAttackButton.setText(_translate("role", "+"))
        self.addAbilityButton.setText(_translate("role", "+"))
