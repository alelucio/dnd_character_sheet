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


class CharacterAlignment(Enum):
    NO_ALIGNMENT = 0
    LAWFUL_GOOD = 1
    NEUTRAL_GOOD = 2
    CHAOTIC_GOOD = 3
    LAWFUL_NEUTRAL = 4
    NEUTRAL = 5
    CHAOTIC_NEUTRAL = 6
    LAWFUL_EVIL = 7
    NEUTRAL_EVIL = 8
    CHAOTIC_EVIL = 9


class CharacterRace(Enum):
    NO_RACE = 0
    DWARF = 1
    ELF = 2
    HALFLING = 3
    HUMAN = 4
    DRAGONBORN = 5
    GNOME = 6
    HALF_ELF = 7
    HALF_ORC = 8
    TIEFLING = 9


damage = 10


# Per ora questa classe può rimanere senza costruttore
# La miglioreremo quando ti sentirai a tuo agio con le classi
class Character:
    LEVELS = [0, 300, 900, 2700, 6500, 14000, 23000, 34000, 48000, 64000, 85000, 100000, 120000, 140000, 165000, 195000,
              225000, 265000, 305000, 355000]  # Questa è una costante quindi il nome sarà tutto maiuscolo

    _experience = 0  # Esperienza iniziale del personaggio

    _characterClass = CharacterClass.NO_CLASS

    _characterAlignment = CharacterAlignment.NO_ALIGNMENT

    _characterRace = CharacterRace.NO_RACE

    _characterEnergy = 100

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

    def getAlignment(self):
        return self._characterAlignment

    def setAlignment(self, newAlignment):
        self._characterAlignment = newAlignment

    def getRace(self):
        return self._characterRace

    def setRace(self, newRace):
        self._characterRace = newRace

    def applyDamage(self, damage):
        self._characterEnergy = self._characterEnergy - damage

    def getEnergy(self):
        return self._characterEnergy
