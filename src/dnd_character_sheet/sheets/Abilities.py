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
