import random
import json

white_possibles = list(range(1, 70))  # range number to 69
red_possibles = list(range(1, 27))  # range number to 26

ticket_price = 2
tickets_per_draw = int(input("How much ticket(s)?"))
num_draws = int(input("How much draw(s)?"))

total_spent = 0
earnings = 0

times_won = {  # a dictionary
    "5+P": 0,
    "5": 0,
    "4+P": 0,
    "4": 0,
    "3+P": 0,
    "3": 0,
    "2+P": 0,
    "1+P": 0,
    "P": 0,
    "0": 0,
}


def calc_win_amount(my_numbers, winning_numbers):
    win_amount = 0

    white_matches = len(my_numbers["whites"].intersection(
        winning_numbers["whites"]))
    power_match = my_numbers["red"] == winning_numbers["red"]

    if white_matches == 5:
        if power_match:
            win_amount = 2_000_000_000
            times_won["5+P"] += 1
        else:
            win_amount = 1_000_000_000
            times_won["5"] += 1
    elif white_matches == 4:
        if power_match:
            win_amount = 50_000
            times_won["4+P"] += 1
        else:
            win_amount = 100
            times_won["4"] += 1
    elif white_matches == 3:
        if power_match:
            win_amount = 100
            times_won["3+P"] += 1
        else:
            win_amount = 7
            times_won["3"] += 1
    elif white_matches == 2 and power_match:
        win_amount = 7
        times_won["2+P"] += 1
    elif white_matches == 1 and power_match:
        win_amount = 4
        times_won["1+P"] += 1
    elif power_match:
        win_amount = 4
        times_won["P"] += 1
    else:
        times_won["0"] += 1

    return win_amount


for draw in range(num_draws):
    white_draw = set(random.sample(white_possibles, k=5))
    red_draw = random.choice(red_possibles)

    winning_numbers = {
        "whites": white_draw,
        "red": red_draw,
    }
    for ticket in range(tickets_per_draw):
        total_spent += ticket_price
        my_whites = set(random.sample(white_possibles, k=5))
        my_red = random.choice(red_possibles)

        my_numbers = {"whites": my_whites, "red": my_red}
        win_amount = calc_win_amount(my_numbers, winning_numbers)
        earnings += win_amount

print(f"Spent: ${total_spent}")
print(f"Earnings: ${earnings}")

print(json.dumps(times_won, indent=2))