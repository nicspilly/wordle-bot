import user_input


def check_word(user_guess: str, word_to_guess: str) -> bool:
    if user_guess == word_to_guess:
        print(f"You got it!! The word was {word_to_guess}")
        return True

    # Initialize result string and a list to track which letters from the word_to_guess have been used
    result = ["x","x","x","x","x"]
    letter_matches = [False] * 5  # To mark letters already matched in the target word

    # First pass: Check for correct positions (Green guesses)
    for i in range(5):
        if user_guess[i] == word_to_guess[i]:
            result[i] = "G"
            letter_matches[i] = True  # Mark this letter as used

    # Second pass: Check for correct letters in wrong positions (Yellow guesses)
    for i in range(5):
        if result[i] == "G":
            continue
        for j in range(5):
            if not letter_matches[j] and user_guess[i] == word_to_guess[j]:
                result[i] = "Y"
                letter_matches[j] = True  # Mark this letter as used
                break  # No need to check further once it's matched

    result_str = ''.join(result)
    print(f"Result: {result_str}")

    return False


def play_game() -> None:
    word_to_guess: str = user_input.get_word()
    for guess_number in range(1, 7):
        print(f"Time for guess #{guess_number}!")
        user_guess: str = user_input.get_word()
        if check_word(user_guess, word_to_guess):
            break