danno = 10


class Health:
    maxHealthPoint = 84

    def actualHealthPoint(self, danno):
        self.maxHealthPoint = self.maxHealthPoint - danno
        print(Health.maxHealthPoint)
