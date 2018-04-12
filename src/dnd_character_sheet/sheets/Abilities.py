from dnd_character_sheet.sheets.Dice import d

proficiencyBonus = 4


class Abilities:
    strength = 1
    dexterity = 1
    constitution = 1
    intelligence = 1
    wisdom = 1
    charisma = 1

    def __init__(self, die=d):
        self.die = die

    def getModifierStrength(self):
        return self.getModifierAbility(self.strength)

    def getModifierDexterity(self):
        return self.getModifierAbility(self.dexterity)

    def getModifierConstitution(self):
        return self.getModifierAbility(self.constitution)

    def getModifierIntelligence(self):
        return self.getModifierAbility(self.intelligence)

    def getModifierWisdom(self):
        return self.getModifierAbility(self.wisdom)

    def getModifierCharisma(self):
        return self.getModifierAbility(self.charisma)

    def getModifierAbility(self, value):
        if value > 30 or value < 1:
            return None
        else:
            return -5 + (int(value / 2))

    # STRENGTH SKILLS

    savingThrowsStrength = False

    def trowSavingTrowsStrength(self):
        if self.savingThrowsStrength:
            return self.die(20) + self.getModifierStrength()
        else:
            return self.die(20) + self.getModifierStrength() + proficiencyBonus

    athletics = False

    def trowAthletics(self):
        if self.athletics:
            return self.die(20) + self.getModifierStrength()
        else:
            return self.die(20) + self.getModifierStrength() + proficiencyBonus

    # DEXTERITY SKILLS

    savingTrowsDexterity = False

    def trowSavingThrowsDexterity(self):
        if self.savingTrowsDexterity:
            return self.die(20) + self.getModifierDexterity()
        else:
            return self.die(20) + self.getModifierDexterity() + proficiencyBonus

    acrobatics = False

    def trowAcrobatics(self):
        if self.acrobatics:
            return self.die(20) + self.getModifierDexterity()
        else:
            return self.die(20) + self.getModifierDexterity() + proficiencyBonus

    sleight_of_hand = False

    def trowSleightOfHand(self):
        if self.sleight_of_hand:
            return self.die(20) + self.getModifierDexterity()
        else:
            return self.die(20) + self.getModifierDexterity() + proficiencyBonus

    stealth = False

    def trowStealth(self):
        if self.stealth:
            return self.die(20) + self.getModifierDexterity()
        else:
            return self.die(20) + self.getModifierDexterity() + proficiencyBonus

    # CONSTITUTION SKILLS

    savingThrowsConstitution = False

    def trowSavingThrowsConstitution(self):
        if self.savingThrowsConstitution:
            return self.die(20) + self.getModifierConstitution()
        else:
            return self.die(20) + self.getModifierConstitution() + proficiencyBonus

    # INTELLIGENCE SKILLS

    savingThrowIntelligence = False

    def trowSavingThrowsIntelligence(self):
        if self.savingThrowIntelligence:
            return self.die(20) + self.getModifierIntelligence()
        else:
            return self.die(20) + self.getModifierIntelligence() + proficiencyBonus

    arcana = False

    def trowArcana(self):
        if self.arcana:
            return self.die(20) + self.getModifierIntelligence()
        else:
            return self.die(20) + self.getModifierIntelligence() + proficiencyBonus

    history = False

    def trowHistory(self):
        if self.history:
            return self.die(20) + self.getModifierIntelligence()
        else:
            return self.die(20) + self.getModifierIntelligence() + proficiencyBonus

    investigation = False

    def trowInvestigation(self):
        if self.investigation:
            return self.die(20) + self.getModifierIntelligence()
        else:
            return self.die(20) + self.getModifierIntelligence() + proficiencyBonus

    nature = False

    def trowNature(self):
        if self.nature:
            return self.die(20) + self.getModifierIntelligence()
        else:
            return self.die(20) + self.getModifierIntelligence() + proficiencyBonus

    religion = False

    def trowReligion(self):
        if self.religion:
            return self.die(20) + self.getModifierIntelligence()
        else:
            return self.die(20) + self.getModifierIntelligence() + proficiencyBonus

    # WISDOM SKILLS

    savingThrowsWisdom = False

    def trowSavingTrowWisdom(self):
        if self.savingThrowsWisdom:
            return self.die(20) + self.getModifierWisdom()
        else:
            return self.die(20) + self.getModifierWisdom() + proficiencyBonus

    animalHandling = False

    def trowAnimalHandling(self):
        if self.animalHandling:
            return self.die(20) + self.getModifierWisdom()
        else:
            return self.die(20) + self.getModifierWisdom() + proficiencyBonus

    insight = False

    def trowInsight(self):
        if self.insight:
            return self.die(20) + self.getModifierWisdom()
        else:
            return self.die(20) + self.getModifierWisdom() + proficiencyBonus

    medicine = False

    def trowMedicine(self):
        if self.medicine:
            return self.die(20) + self.getModifierWisdom()
        else:
            return self.die(20) + self.getModifierWisdom() + proficiencyBonus

    perception = False

    def trowPerception(self):
        if self.perception:
            return self.die(20) + self.getModifierWisdom()
        else:
            return self.die(20) + self.getModifierWisdom() + proficiencyBonus

    survival = False

    def trowSurvival(self):
        if self.survival:
            return self.die(20) + self.getModifierWisdom()
        else:
            return self.die(20) + self.getModifierWisdom() + proficiencyBonus

    # CHARISMA SKILLS

    savingThrowCharisma = False

    def trowSavingTrowCharisma(self):
        if self.savingThrowCharisma:
            return self.die(20) + self.getModifierCharisma()
        else:
            return self.die(20) + self.getModifierCharisma() + proficiencyBonus

    deception = False

    def trowDeception(self):
        if self.deception:
            return self.die(20) + self.getModifierCharisma()
        else:
            return self.die(20) + self.getModifierCharisma() + proficiencyBonus

    intimidation = False

    def trowIntimidation(self):
        if self.intimidation:
            return self.die(20) + self.getModifierCharisma()
        else:
            return self.die(20) + self.getModifierCharisma() + proficiencyBonus

    performance = False

    def trowPerformance(self):
        if self.performance:
            return self.die(20) + self.getModifierCharisma()
        else:
            return self.die(20) + self.getModifierCharisma() + proficiencyBonus

    persuasion = False

    def trowPersuasion(self):
        if self.persuasion:
            return self.die(20) + self.getModifierCharisma()
        else:
            return self.die(20) + self.getModifierCharisma() + proficiencyBonus

    # questa CA vale solo per il monaco... da mettere a posto piu avanti

    def getArmorClass(self):
        return 10 + self.getModifierDexterity() + self.getModifierWisdom()

    def getInitiative(self):
        return self.getModifierDexterity()


