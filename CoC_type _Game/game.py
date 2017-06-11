import sys

from character import Character
from monster import Dragon
from monster import Goblin
from monster import Troll


class Game:
    def setup(self):
        self.player = Character()
        self.monsters = [Dragon(),
                         Goblin(),
                         Troll()
                         ]
        self.monster = self.get_next_monster()

    def get_next_monster(self):
        try:
            return self.monsters.pop(0)
        except IndexError:
            return None

    def monster_turn(self):
        if self.monster.attack():
            print('{} is attacking right NOW!!'.format(self.monster))

            if input("DODGE? Y/n ").lower() == 'y':
                if self.player.dodge():
                    print("you doged the attack.")

                else:
                    print("You got hit anyway.")
                    self.player.hit_points -= 1
                    print(self.player)
            else:
                print("{} hit you for 1 point.".format(self.monster))
                self.player.hit_points -= 1
                print(self.player)
        else:
            print("{} isn't attacking this turn.".format(self.monster))


            # check to see if monster attacks ...done
            # if so, tell to player ...done
            # check if player wants to dodge ....done
            # if yes, then dodge if that succesfu;; then move on ...done
            # if dodge not successfull then remove one hitpoint ...done
            # if monster is not attacking  then tell player that too. ...done

    def player_turn(self):
        player_choice = input("What do you want to do? [A]ttack, [R]est or [Q]uit.").lower()

        if player_choice == 'a':
            if self.player.attack():
                if self.monster.dodge():
                    print("{} doged your attack".format(self.monster))
                else:
                    if self.player.level_up():
                        self.monster.hit_points -= 2
                    else:
                        self.monster.hit_points -= 1
                    print("You attack {} with your {}.".format(self.monster, self.player.weapon))
            else:
                print("You Missed it!!")
        elif player_choice == 'r':
            self.player.rest()
        elif player_choice == 'q':
            # exits out of the interpreter that runs our python script. #
            sys.exit()
        else:
            self.player_turn()

            # let the player attack, rest or quit
            # if they attack(players)
            # see if the attack suucessfull ie return True
            #  if true see if monster dodges if yes print taht monster dodged
            # if not dodged then, subtract right num from monster hit_ponts
            #  if its not a good attack then, tell the player
            #  if they rest :
            #   call the player rest() method
            #  if they quit, then exit the game
            #  if they pick anything else then re-run this method
            # ...done all#

    def cleanup(self):
        if self.monster.hit_points <= 0:
            self.player.xp += self.monster.xp
            print("You killed {}!!".format(self.monster))
            self.monster = self.get_next_monster()

            # if the monster has nomore hit+points :
            # then up the player's experience :xp
            # print the message
            # get a new monster  ...done all#

    def __init__(self):
        self.setup()
        # while we have the player hitpoints  and still have
        #  some monster or monsters in the list

        while self.player.hit_points and (self.monsters or self.monster):
            print('\n' + "==" * 20)
            print(self.player)
            self.monster_turn()
            print('-' * 20)
            self.player_turn()
            print('-' * 20)
            self.cleanup()
        if self.player.hit_points:
            print("YOU WIN!!")
        elif self.monster and self.monster:
            print("YOU LOOSE!!")
        else:
            print("NOBODY LEFT. --Match Draw=--")
            # ask if the player wants to  play again or not.s
        sys.exit()


Game()
