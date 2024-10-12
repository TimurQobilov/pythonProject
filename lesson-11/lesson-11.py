def get_choice(player):
    print(f"{player}, выберите: камень, ножницы или бумага.")
    return input().lower()


def determine_winner(choice1, choice2):
    if choice1 == choice2:
        return "Ничья!"
    elif (choice1 == "камень" and choice2 == "ножницы") or \
            (choice1 == "ножницы" and choice2 == "бумага") or \
            (choice1 == "бумага" and choice2 == "камень"):
        return "Игрок 1 победил!"
    else:
        return "Игрок 2 победил!"


def play_game():
    print("Игра: Камень, Ножницы, Бумага")
    player1_choice = get_choice("Игрок 1")
    player2_choice = get_choice("Игрок 2")

    result = determine_winner(player1_choice, player2_choice)
    print(result)


play_game()
