import random
import sys

game = 'Rock Paper Scissors Lizard Spock game.'
print('Welcome to', game)

# Create number to choice mapping
mapping = {
    1: "Rock",
    2: "Paper",
    3: "Scissors",
    4: "Lizard",
    5: "Spock"
}

ties = wins = loses = 0

while True:

    # Generate computer choice
    pc_choice = random.randint(1, 5)
    pc_choice_output = "I chose %s." % mapping[pc_choice]

    # Request user choice
    try:
        user_choice = int(input("Choose Rock(1), Paper(2), Scissors(3), Lizard(4), Spock(5), Exit(9): "))
        if user_choice == 9:
            print('Thanks for playing', game)
            print(f'{wins} wins, {loses} loses, & {ties} ties')
            sys.exit(0)
        user_choice_output = "You chose %s." % mapping[user_choice]

    except (ValueError, KeyError):
        print(pc_choice_output)
        print("You chose nothing.")
        print("You lose by default.")
        sys.exit(0)

    # Share choices
    print(pc_choice_output)
    print(user_choice_output)

    # Setup results
    i_win = "%s beats %s - I win!" % (mapping[pc_choice], mapping[user_choice])
    u_win = "%s beats %s - you win!" % (mapping[user_choice], mapping[pc_choice])
    tie = "Tie!"

    result = (user_choice - pc_choice) % 5
    if result == 1 or result == 2:
        wins += 1
    elif result == 3 or result == 4:
        loses += 1
    else:
        ties += 1

    print([tie, u_win, u_win, i_win, i_win][result])
    print()
