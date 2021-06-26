from dice_roller import DiceRoller as dr

dice = dr()
total = 0
die_number = 1

print(f"Welcome to the Dice Roller\n")

print("Die type: ")
for key in dice.dice_type:
    print(dice.dice_type[key])

dice_type = input(f"\nPlease enter the type of dice you would like to roll: ")

try:
    dice_amt = int(input(f"Please choose how many dice you would like to roll: "))
    
except ValueError:
    print("Sorry the number you have entered for amount is not a positive number. Please try again.")

else: 
    if(dice_type == 'd2'):
        while(dice_amt != 0):
            roll = dr.two_sided_roll()
            print(f"Die number {die_number}: {roll}")
            total += roll
            die_number += 1
            dice_amt -= 1
        print(f"Your total for this roll was: {total}")

    if(dice_type == 'd4'):
        while(dice_amt != 0):
            roll = dr.four_sided_roll()
            print(f"Die number {die_number}: {roll}")
            total += roll
            die_number += 1
            dice_amt -= 1
        print(f"Your total for this roll was: {total}")

    if(dice_type == 'd6'):
        while(dice_amt != 0):
            roll = dr.six_sided_roll()
            print(f"Die number {die_number}: {roll}")
            total += roll
            die_number += 1
            dice_amt -= 1
        print(f"Your total for this roll was: {total}")

    if(dice_type == 'd10'):
        while(dice_amt != 0):
            roll = dr.ten_sided_roll()
            print(f"Die number {die_number}: {roll}")
            total += roll
            die_number += 1
            dice_amt -= 1
        print(f"Your total for this roll was: {total}")

    if(dice_type == 'd12'):
        while(dice_amt != 0):
            roll = dr.twelve_sided_roll()
            print(f"Die number {die_number}: {roll}")
            total += roll
            die_number += 1
            dice_amt -= 1
        print(f"Your total for this roll was: {total}")

    if(dice_type == 'd20'):
        while(dice_amt != 0):
            roll = dr.twenty_sided_roll()
            print(f"Die number {die_number}: {roll}")
            total += roll
            die_number += 1
            dice_amt -= 1
        print(f"Your total for this roll was: {total}")

