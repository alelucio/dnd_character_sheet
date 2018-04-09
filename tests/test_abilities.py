#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import pytest
from dnd_character_sheet.sheets.Abilities import Abilities  # classe
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

    # test trowSavingTrowStrength

    abilities.strength = 10
    abilities.savingThrowsStrength = False
    assert abilities.trowSavingTrowsStrength() == 19
    abilities.strength = 10
    abilities.savingThrowsStrength = True
    assert abilities.trowSavingTrowsStrength() == 15

    # test trowAthletics

    abilities.strength = 10
    abilities.athletics = True
    assert abilities.trowAthletics() == 15
    abilities.strength = 10
    abilities.athletics = False
    assert abilities.trowAthletics() == 19


def test_skills_dexterity():
    die = Mock()
    die.return_value = 15
    abilities = Abilities(die)

    # test savingTrowsDexterity

    abilities.dexterity = 10
    abilities.savingTrowsDexterity = True
    assert abilities.trowSavingThrowsDexterity() == 15
    abilities.dexterity = 10
    abilities.savingTrowsDexterity = False
    assert abilities.trowSavingThrowsDexterity() == 19

    # test acrobatics

    abilities.dexterity = 10
    abilities.acrobatics = True
    assert abilities.trowAcrobatics() == 15
    abilities.dexterity = 10
    abilities.acrobatics = False
    assert abilities.trowAcrobatics() == 19

    # test sleight of hand

    abilities.dexterity = 10
    abilities.sleight_of_hand = True
    assert abilities.trowSleightOfHand() == 15
    abilities.dexterity = 10
    abilities.sleight_of_hand = False
    assert abilities.trowSleightOfHand() == 19

    # test stealth

    abilities.dexterity = 10
    abilities.stealth = True
    assert abilities.trowStealth() == 15
    abilities.dexterity = 10
    abilities.stealth = False
    assert abilities.trowStealth() == 19


def test_skills_constitution():
    die = Mock()
    die.return_value = 15
    abilities = Abilities(die)

    # test savingTrowConstitution

    abilities.constitution = 10
    abilities.savingThrowsConstitution = True
    assert abilities.trowSavingThrowsConstitution() == 15
    abilities.constitution = 10
    abilities.savingThrowsConstitution = False
    assert abilities.trowSavingThrowsConstitution() == 19


def test_skills_intelligence():
    die = Mock()
    die.return_value = 15
    abilities = Abilities(die)

    # test savingTrowIntelligence

    abilities.intelligence = 10
    abilities.savingThrowIntelligence = True
    assert abilities.trowSavingThrowsIntelligence() == 15
    abilities.intelligence = 10
    abilities.savingThrowIntelligence = False
    assert abilities.trowSavingThrowsIntelligence() == 19

    # test arcana

    abilities.intelligence = 10
    abilities.arcana = True
    assert abilities.trowArcana() == 15
    abilities.intelligence = 10
    abilities.arcana = False
    assert abilities.trowArcana() == 19

    # test history

    abilities.intelligence = 10
    abilities.history = True
    assert abilities.trowHistory() == 15
    abilities.intelligence = 10
    abilities.history = False
    assert abilities.trowHistory() == 19

    # test investigation

    abilities.intelligence = 10
    abilities.investigation = True
    assert abilities.trowInvestigation() == 15
    abilities.intelligence = 10
    abilities.investigation = False
    assert abilities.trowInvestigation() == 19

    # test nature

    abilities.intelligence = 10
    abilities.nature = True
    assert abilities.trowNature() == 15
    abilities.intelligence = 10
    abilities.nature = False
    assert abilities.trowNature() == 19

    # test religion

    abilities.intelligence = 10
    abilities.religion = True
    assert abilities.trowReligion() == 15
    abilities.intelligence = 10
    abilities.religion = False
    assert abilities.trowReligion() == 19


def test_skills_wisdom():
    die = Mock()
    die.return_value = 15
    abilities = Abilities(die)

    # test savingTrowWisdom

    abilities.wisdom = 10
    abilities.savingThrowsWisdom = True
    assert abilities.trowSavingTrowWisdom() == 15
    abilities.wisdom = 10
    abilities.savingThrowsWisdom = False
    assert abilities.trowSavingTrowWisdom() == 19

    # test animalHandling

    abilities.wisdom = 10
    abilities.animalHandling = True
    assert abilities.trowAnimalHandling() == 15
    abilities.wisdom = 10
    abilities.animalHandling = False
    assert abilities.trowAnimalHandling() == 19

    # test insight

    abilities.wisdom = 10
    abilities.insight = True
    assert abilities.trowInsight() == 15
    abilities.wisdom = 10
    abilities.insight = False
    assert abilities.trowInsight() == 19

    # test medicine

    abilities.wisdom = 10
    abilities.medicine = True
    assert abilities.trowMedicine() == 15
    abilities.wisdom = 10
    abilities.medicine = False
    assert abilities.trowMedicine() == 19

    # test perception

    abilities.wisdom = 10
    abilities.perception = True
    assert abilities.trowPerception() == 15
    abilities.wisdom = 10
    abilities.perception = False
    assert abilities.trowPerception() == 19

    # test survival

    abilities.wisdom = 10
    abilities.survival = True
    assert abilities.trowSurvival() == 15
    abilities.wisdom = 10
    abilities.survival = False
    assert abilities.trowSurvival() == 19


def test_skills_charisma():
    die = Mock()
    die.return_value = 15
    abilities = Abilities(die)

    # test savingTrowCharisma

    abilities.charisma = 10
    abilities.savingThrowCharisma = True
    assert abilities.trowSavingTrowCharisma() == 15
    abilities.charisma = 10
    abilities.savingThrowCharisma = False
    assert abilities.trowSavingTrowCharisma() == 19

    # test deception

    abilities.charisma = 10
    abilities.deception = True
    assert abilities.trowDeception() == 15
    abilities.charisma = 10
    abilities.deception = False
    assert abilities.trowDeception() == 19

    # test intimidation

    abilities.charisma = 10
    abilities.intimidation = True
    assert abilities.trowIntimidation() == 15
    abilities.charisma = 10
    abilities.intimidation = False
    assert abilities.trowIntimidation() == 19

    # test performance

    abilities.charisma = 10
    abilities.performance = True
    assert abilities.trowPerformance() == 15
    abilities.charisma = 10
    abilities.performance = False
    assert abilities.trowPerformance() == 19

    # test persuasion

    abilities.charisma = 10
    abilities.persuasion = True
    assert abilities.trowPersuasion() == 15
    abilities.charisma = 10
    abilities.persuasion = False
    assert abilities.trowPersuasion() == 19


    # test CA

def test_getArmorClass():
    abilities = Abilities()
    abilities.dexterity = 10
    abilities.wisdom = 10
    assert abilities.getArmorClass() == 10

    # test initiative

def test_getInitiative():
    abilities = Abilities()
    abilities.dexterity = 10
    assert abilities.getInitiative() == 0















