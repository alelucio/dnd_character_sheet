#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from dnd_character_sheet.sheets.Character import Character, CharacterClass , CharacterAlignment, CharacterRace

__author__ = "Alessandro Luciani"
__copyright__ = "Alessandro Luciani"
__license__ = "mit"


def test_new_character():
    character = Character()
    assert character.getExperience() == 0, "A new character has 0 experience, aka adventurer in 'cass integration'"
    assert character.getLevel() == 1, "A new character starts from level 1"
    assert character.getClass() == CharacterClass.NO_CLASS, "A new character has no class"
    assert character.getAlignment() == CharacterAlignment.NO_ALIGNMENT, " A new character has no alignment"
    assert character.getRace() == CharacterRace.NO_RACE, " A new character has no race"

def test_character_experience_gain():
    character = Character()
    character.setClass(CharacterClass.MONK)
    assert character.getClass() == CharacterClass.MONK
    character.addExperience(300)
    assert character.getLevel() == 2, "When the character reaches 300 experience, level increases to 2"
    character.addExperience(599)
    assert character.getLevel() == 2, "When the character reaches 899 experience, level is still 2"
    character.addExperience(1)
    assert character.getLevel() == 3, "When the character reaches 900 experience, level rises to 3"


def test_unvalid_character_levels():
    character = Character()
    character.addExperience(380000)
    assert character.getLevel() is None, "A character can't go over 355000, over-experienced warriors can't find a job"

def test_energy():
    character = Character()
    character.characterEnergy = 100
    damage = 10
    assert character.actualEnergy() == 90
