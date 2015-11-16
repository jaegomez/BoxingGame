#!/usr/bin/python
#JulioGomezJae
#
#this is a boxing game
#

from BoxerObject import Boxer
from random import randint


def actions(players_boxer,computers_boxer):
    """
    this is the function that will do actions
    :param players_boxer: the name of the player
    :param computers_boxer: comp name
    :return:
    """
    #loop until player or computer hits 0 health
    while players_boxer.boxer_health > 0 and computers_boxer.boxer_health > 0:

        player_options = {"[0]": " Stats", "[1]": " Punch", "[2]": " Block"}
        list_of_player_options = player_options.keys()

        for key in list_of_player_options:
            print key + player_options.get(key)

        pick_choice = raw_input("Enter your choice: ")

        if pick_choice == '0':
            print "--------STATS-------"
            print "HEALTH: " + str(players_boxer.boxer_health)
            print "STAMINA: " + str(players_boxer.boxer_stamina)
            print "STRENGTH: " + str(players_boxer.boxer_strength)
            print "---OPPONENT STATS---"
            print "HEALTH: " + str(computers_boxer.boxer_health)
            print "STAMINA: " + str(computers_boxer.boxer_stamina)
            print "STRENGTH: " + str(computers_boxer.boxer_strength)
        elif pick_choice == '1':

            players_boxer.remove_stamina(1)
            players_damage = players_boxer.calculate_damage(computers_boxer.boxer_health)
            computers_damage = computers_boxer.calculate_damage(players_boxer.boxer_health)
            cpu_block_success = False
            who_won =False
            if randint(0,2) == 0:
                    cpu_block_success = computers_boxer.attempt_block()

            if cpu_block_success == False:
                print "You hit the CPU and caused " + str(players_damage) + " damage to it!"
                computers_boxer.remove_health(players_damage)
                print "The CPU hit you and caused " + str(computers_damage) + " damage."
                players_boxer.remove_health(computers_damage)
                computers_boxer.remove_stamina(1)
            else:
                print "CPU blocked your punch!"

        elif pick_choice == '2':
            computers_boxer.remove_stamina(1)
            computers_damage = computers_boxer.calculate_damage(players_boxer.boxer_health)
            player_block_success = False
            if randint(0,2) == 0:
                player_block_success = players_boxer.attempt_block()

            if player_block_success == False:
                print "You blocked it!"

            else:
                print "You missed the block! The CPU caused " + str(computers_damage) + " damage!"
                players_boxer.remove_health(computers_damage)

    if computers_boxer.boxer_health == 0:
        print "You defeated the CPU! You have " + str(players_boxer.boxer_health) + " health left."
    elif players_boxer.boxer_health == 0:
        print "The CPU beat you!"




def main():
    """
    This is the main function.
    :return:
    """
    print "Welcome to the Python Boxing Game"
    boxer_name = raw_input("Whats your name?").title()

    players_boxer = Boxer(boxer_name, 20, 10, 10)
    computers_boxer = None

    list_of_difficulties = ["1", "2", "3"]
    mode = ""

    while mode not in list_of_difficulties:
        mode = raw_input("Easy medium or hard [ 1, 2, 3]:").lower()
        if mode == "1":
            computers_boxer = Boxer("comp", 20, 10, 10)
        elif mode == "2":
            computers_boxer = Boxer("comp", 25, 15, 15)
        elif mode == "3":
            computers_boxer = Boxer("comp", 30, 20, 20)
        elif mode =="exit":
            quit()
        else:
            print "Not valid"

    actions(players_boxer, computers_boxer)

main()