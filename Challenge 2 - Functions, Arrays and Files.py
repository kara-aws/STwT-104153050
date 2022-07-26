print("Greetings, Caves & Lizards Club!\nWelcome to your dice roll simulator.") #welcome message

import random

roll_list = []

while True:
    num_rolls = int(input("\nHow many rolls do you need?\n")) #number of rolls

    for roll in range(0, num_rolls): #0 classed as first roll
        dice_value = random.randint(1,6) #randomised value
        print(f"You rolled a {dice_value}") #roll result
        roll_list.append(dice_value)
    reroll = input("\nRoll again? Enter 'Y' or 'N'\n").upper()
    if reroll != "Y": #response other than 'Y' will end program
        break

def Average(roll_list):
    return sum(roll_list) / len(roll_list) #total value divided by number of rolls
average_value = Average(roll_list)

total_value = sum(roll_list) #add up all dice values

#final prints
print(f"\nAverage roll value: {average_value}")
print(f"Total value of all rolls: {total_value}")
print(f"\nYour rolls (in order) were:\n{roll_list}") 
print("\nFarewell!") #goodbye message