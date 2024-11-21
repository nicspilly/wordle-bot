import user_input

def check_word(user_guess: str) -> None:
    pass

def play_game() -> None:
    word_to_guess = user_input.get_word()
    for guess_number in range(1, 7):
        print(f"Time for guess #{guess_number}!")
        user_guess = user_input.get_word()
        check_word(user_guess)
    pass