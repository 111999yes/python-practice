import random

seed = int(input("seed: "))
num_upper = int(input("num_upper: "))
player_one_win = 0
player_two_win = 0

random.seed(seed)

def gen_ran_num():
    return random.randint(1, num_upper)

def run_game():
    round = 0
    ans = gen_ran_num()
    print("A new secret number has been generated.")
    while True:
        round += 1
        guess = input()
        if guess == "q":
            return -1
        guess = int(guess)
        if guess > num_upper or guess < 1:
            print(f"Invalid guess! Please enter a number between 1 and {num_upper}.")
        elif guess > ans:
            print("Too high!")
        elif guess < ans:
            print("Too low!")
        else:
            player_num = 2
            if round % 2 == 1:
                player_num = 1
            print(f"Correct! Player {player_num} wins!")
            return player_num

while True:
    winner = run_game()
    if winner == -1:
        if player_one_win + player_two_win != 0:
            print("Final Results:")
            print(f"Player 1: {player_one_win} Wins")
            print(f"Player 2: {player_two_win} Wins")
        print("Bye Bye!")
        break
    elif winner == 1:
        player_one_win += 1
    else:
        player_two_win += 1
    
    print(f"Game stats: {player_one_win + player_two_win} rounds, player1 {player_one_win} wins, player2 {player_two_win} wins.\n")