#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import pytest
from dnd_character_sheet.sheets.Abilities import Abilities #classe
from unittest.mock import Mock

__author__ = "Alessandro Luciani"
__copyright__ = "Alessandro Luciani"
__license__ = "mit"


def test_modifier_abilities():
    abilities = Abilities()
    assert abilities.getModifierAbility(1) == -5, " 1 punti equivalgono a -5 score"
    assert abilities.getModifierAbility(15) == 2, " 15 punti equivalgono a 2 score"
    assert abilities.getModifierAbility(30) == 10, " 30 punti equivalgono a 10 score"
    assert abilities.getModifierAbility(32) == None, " 32 punti equivalgono a 10 score"
    assert abilities.getModifierAbility(0) == None, " 0 punti equivalgono a -5 score"

def test_abilities():
    abilities = Abilities()
    assert abilities.getModifierStrength() == -5
    abilities.strength = 10
    assert abilities.getModifierStrength() == 0
    assert abilities.getModifierDexterity() == -5
    assert abilities.getModifierConstitution() == -5
    assert abilities.getModifierIntelligence() == -5
    assert abilities.getModifierWisdom() == -5
    assert abilities.getModifierCharisma() == -5

def test_skills_strength():

    # Creo un dado tarocco che mi restituice sempre 15
    # Si... Die è dado in inglese

    die = Mock()
    die.return_value = 15

    # Creo Abilities impostando il dado tarocco
    abilities = Abilities(die)

    abilities.strength = 10
    abilities.savingThrowsStrength = False
    # mock dado
    assert abilities.trowSavingTrowsStrength() == 15
    abilities.strength = 10
    abilities.savingThrowsStrength = True
    # proficiencyBonus = 4
    # mock dado
    assert abilities.trowSavingTrowsStrength() == 15









