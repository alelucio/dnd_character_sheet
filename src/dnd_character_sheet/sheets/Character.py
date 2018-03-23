from enum import Enum


class CharacterClass(Enum):
    NO_CLASS = 0
    BARBARIAN = 1
    BARD = 2
    CLERIC = 3
    DRUID = 4
    FIGHTER = 5
    MONK = 6
    PALADIN = 7
    RANGER = 8
    ROGUE = 9
    SORCER = 10
    WARLOCK = 11
    WIZARD = 12


# Per ora questa classe può rimanere senza costruttore
# La miglioreremo quando ti sentirai a tuo agio con le classi
class Character:
    LEVELS = [0, 100, 500, 1000, 10000, 100000]  # Questa è una costante quindi il nome sarà tutto maiuscolo

    _experience = 0  # Esperienza iniziale del personaggio

    _characterClass = CharacterClass.NO_CLASS

    def getLevel(self):
        for currentLevel, nextLevelPoints in enumerate(self.LEVELS):
            if self._experience < nextLevelPoints:
                return currentLevel
        return None

    def addExperience(self, amount):
        self._experience += amount

    def getExperience(self):
        return self._experience

    def getClass(self):
        return self._characterClass

    def setClass(self, newCharacterClass):
        self._characterClass = newCharacterClass
