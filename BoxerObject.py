#!usr/bin/python
#JulioGomezJae
#Boxer.py
#This contains the Boxer object
#

from random import randint

class Boxer:
    """
    This is the Boxer that the user will be using
    """
    #this is the boxers name
    boxer_name = None

    #this is the boxers health
    boxer_health =None

    #this is the boxers damage
    boxer_stamina =None

    #this is the boxers stamina
    boxer_strength =None

    def __init__(self,name=None, health=None, stamina=None, strength=None):
        """
        :param name:
        :param health:
        :param damage:
        :param stamina:
        :return:
        """

        self.boxer_name = name
        self.boxer_health = health
        self.boxer_stamina = stamina
        self.boxer_strength = strength

    def remove_health(self,amount):
        """
        this will remove health, therefore the boxer is getting punched
        :param amount: the amount left
        :return: the amount of health taken away
        """
        #checks  if the amount to remove is greater than the health left
        if amount > self.boxer_health:
            amount = self.boxer_health

        #this will remove the amount of health from the boxer
        self.boxer_health -= amount


    def remove_stamina(self, amount):
        """
        this will remove stamina
        :param amount: the amount of stamina we will remove
        :return:
        """
        if amount > self.boxer_stamina:
            amount = self.boxer_stamina

        self.boxer_stamina -= amount

    def attempt_block(self):
        """
        this will attempt to block a punch
        :return:
        """
        block = randint(0,1)
        if block == 1:
            return True
        else:
            return False

    def calculate_damage(self,opponents_health):
        """
        this will calculate the damage
        :param opponents_health:
        :return:
        """
        damage = randint(0,self.boxer_strength + self.boxer_stamina)

        #this will check if the damage is bigger than the remainder of the opponent
        if damage > opponents_health:
            damage = opponents_health

        return damage
