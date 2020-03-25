import random


# Write your game of chance functions here

def coin_flip(bet, side):
    num = random.randint(1, 10)
    current_amount = bet_money
    if bet > current_amount:
        raise Exception("Not enough funds!!")
    if bet < 0:
        raise Exception("Bets need to be greater than 0!!")
    if not ((side == "Heads") or (side == "Tails")):
        raise Exception('Side should be \'Heads\' or \'Tails\'!!')
    if num % 2 == 0:
        result = "Heads"
    else:
        result = "Tails"

    if side == result:
        print("Won")
        return bet

    else:
        print("Lost")
        return -bet


def two_dice(bet, output):
    current_amount = bet_money
    if bet > current_amount:
        raise Exception("Not enough funds!!")
    if bet < 0:
        raise Exception("Bets need to be greater than 0!!")
    if not ((output == 'Odd') or (output == 'Even')):
        raise Exception("Should be 'Odd' or 'Even'!!")
    die1_score = random.randint(1, 6)
    die2_score = random.randint(1, 6)

    total = die1_score + die2_score

    if total % 2 == 0:
        side = "Even"
    else:
        side = "Odd"

    if side == output:
        print("Won")
        return bet
    else:
        print("Lost")
        return -bet


def card_pick(bet, player1):
    current_amount = bet_money
    if bet > current_amount:
        raise Exception("Not enough funds!!")
    if bet < 0:
        raise Exception("Bets need to be greater than 0!!")
    card_rand = random.randint(1, 13)

    if player1 > card_rand:
        print("Won")
        return bet
    elif player1 == card_rand:
        print("Draw")
        return 0
    elif player1 < card_rand:
        print("Lost")
        return -bet


def roulette(bet, output):
    current_amount = bet_money
    if bet > current_amount:
        raise Exception("Not enough funds!!")
    if bet < 0:
        raise Exception("Bets need to be greater than 0!!")
    random_outnumber = random.randint(0, 3)
    potential_results = ["Odd", "Even", 0, 00]
    result = potential_results[random_outnumber]
    if output == result:
        print("Won")
        return bet
    else:
        print("Lost")
        return -bet


play_on = "Yes"

bet_money = int(input("How much money would you like to bet?"))

while play_on == "Yes" or play_on == "Y":

    game_num = int(input(
        "Which game would you like to play? Select 1 for Coinflip, 2 for Two Dice, 3 for Card Pick, 4 for Roulette."))

    if game_num == 1:
        bet_money += coin_flip(50, "Heads")
        print("Currently have " + str(bet_money) + " left.")
    elif game_num == 2:
        bet_money += two_dice(70, "Odd")
        print("Currently have " + str(bet_money) + " left.")
    elif game_num == 3:
        bet_money += card_pick(20, random.randint(1, 13))
        print("Currently have " + str(bet_money) + " left.")
    elif game_num == 4:
        bet_money += roulette(30, 0)
        print("Currently have " + str(bet_money) + " left.")

    play_on = input("Play another game??")

print("Ended this casino session with " + str(bet_money))
