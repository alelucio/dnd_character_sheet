#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from dnd_character_sheet.sheets.Character import Character, CharacterClass

__author__ = "Alessandro Luciani"
__copyright__ = "Alessandro Luciani"
__license__ = "mit"


def test_new_character():
    character = Character()
    assert character.getExperience() == 0, "A new character has 0 experience, aka adventurer in 'cass integration'"
    assert character.getLevel() == 1, "A new character starts from level 1"
    assert character.getClass() == CharacterClass.NO_CLASS, "A new character has no class"


def test_character_experience_gain():
    character = Character()
    character.setClass(CharacterClass.MONK)
    assert character.getClass() == CharacterClass.MONK
    character.addExperience(100)
    assert character.getLevel() == 2, "When the character reaches 100 experience, level increases to 2"
    character.addExperience(399)
    assert character.getLevel() == 2, "When the character reaches 499 experience, level is still 2"
    character.addExperience(1)
    assert character.getLevel() == 3, "When the character reaches 500 experience, level rises to 3"


def test_unvalid_character_levels():
    character = Character()
    character.addExperience(100000)
    assert character.getLevel() is None, "A character can't go over 99999, over-experienced warriors can't find a job"
