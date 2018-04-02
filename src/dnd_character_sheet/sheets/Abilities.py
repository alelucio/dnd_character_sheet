class Abilities:
    strength = 1
    dexterity = 1
    constitution = 1
    intelligence = 1
    wisdom = 1
    charisma = 1

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

class AbilitySkillsStrength:
    savingThrowsStrength = 0
    athletics = 0

class AbilitySkillsDexterity:
    savingThrowsDexterity = 0
    acrobatics = 0
    sleight_of_hand = 0
    stealth = 0

class AbilitySkillsConstitution:
    savingThrowsConstitution = 0

class AbilitySkillsIntelligence:
    savingThrowIntelligence = 0
    arcana = 0
    history = 0
    investigation = 0
    nature = 0
    religion = 0

class AbilitySkillsWisdom:
    savingThrowsWisdom = 0
    animalHandling = 0
    insight = 0
    medicine = 0
    perception = 0
    survival = 0

class AbilitySkillsCharisma:
    savingThrowCharisma = 0
    deception = 0
    intimidation = 0
    performance = 0
    persuasion = 0

