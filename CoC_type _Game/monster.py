import random

from combat import Combat

COLORS = ["RED", "BLUE", "GREEN", "WHITE", "BLACK", "YELLOW", "PURPLE"]


class Monster(Combat):
    min_hit_points = 1
    max_hit_points = 2
    min_xp = 1
    max_xp = 2
    sound = "roar"

    # this is the dunder init method/function these type of methods generally called magic
    # methods
    def __init__(self, **kwargs):
        self.hit_points = random.randint(self.min_hit_points, self.max_hit_points)
        self.xp = random.randint(self.min_xp, self.min_xp)
        self.color = random.choice(COLORS)

        for key, value in kwargs.items():
            setattr(self, key, value)

    # this dunder str method basically similar to init method
    # it helps to manipulate the string printing format
    # means how we
    # want to print the required information
    # what happens when our object makes a string out of object

    def __str__(self):
        # this method is called whenever something converted to a string
        return 'This is a {}{} having HP:{} and XP:{}'.format(self.color.lower(),
                                                              self.__class__.__name__,
                                                              self.hit_points,
                                                              self.xp)

    def battle_cry(self):
        return self.sound.upper()


class Goblin(Monster):
    min_hit_points = 1
    max_hit_points = 5
    min_xp = 1
    max_xp = 5
    sound = "icki"


class Dragon(Monster):
    min_hit_points = 1
    max_hit_points = 10
    min_xp = 1
    max_xp = 10
    sound = "rrrraaaaaaarrr"


class Troll(Monster):
    min_hit_points = 1
    max_hit_points = 7
    min_xp = 1
    max_xp = 7
    sound = "bleep"
