import random

from combat import Combat


class Character(Combat):
    # overriding the variable from combat file Combat class
    attack_limit = 10
    base_hit_points = 10
    xp = 0

    # overriding the method from combat file Combat class attack() method
    def attack(self):
        roll = random.randint(1, self.attack_limit)
        if self.weapon == "Sword":
            roll += 1
        elif self.weapon == "Axe":
            roll += 2
        elif self.weapon == "Bow_and_Arrows":
            roll += 3
        return roll > 4

    # this is just a simple get_weapon method returns weapon of choice
    def get_weapon(self):
        weapon_choice = input("[S]word, [A]xe, [B]ow_and_[A]rrows : ").lower()

        if weapon_choice in 'sab':
            if weapon_choice == 's':
                return "Sword"
            elif weapon_choice == 'a':
                return "Axe"
            else:
                return "Bow_and_Arrows"
        else:
            return self.get_weapon()

    def __init__(self, **kwargs):


        self.name = input("Name :: ")
        self.weapon = self.get_weapon()
        self.hit_points = self.base_hit_points
        for key, value in kwargs.items():
            setattr(self, key, value)


    def __str__(self):
        return 'Hi {} you have HP::{} and XP::{}.'.format(self.name,self.hit_points,self.xp)

    def rest(self):
        if self.hit_points < self.base_hit_points:
            self.hit_points += 1

    def level_up(self):
        return self.xp >= 5
