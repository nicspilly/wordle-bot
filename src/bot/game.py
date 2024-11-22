import user_input


def check_word(entered_guess: str, goal_guess: str) -> bool:
    user_guess = entered_guess.lower()
    word_to_guess = goal_guess.lower()
    if user_guess == word_to_guess:
        print(f"You got it!! The word was {word_to_guess}")
        return True
    # Initialize result string and a list to track which letters from the word_to_guess have been used
    result = ["x","x","x","x","x"]
    letter_matches = [False] * 5  # To mark letters already matched in the target word

    # First pass: Check for correct positions (Green)
    for i in range(5):
        if user_guess[i] == word_to_guess[i]:
            result[i] = "g"  # Correct letter and position
            letter_matches[i] = True  # Mark this letter as used

    # Second pass: Check for correct letters in wrong positions (Yellow)
    for i in range(5):
        if result[i] == "g":  # Skip already matched (Green) letters
            continue

        for j in range(5):
            # If the letter is in the word and hasn't been used yet
            if not letter_matches[j] and user_guess[i] == word_to_guess[j]:
                result[i] = "y"  # Correct letter, wrong position
                letter_matches[j] = True  # Mark this letter as used
                break  # No need to check further once it's matched

    # Convert the result list back to a string and print for debugging
    result_str = ''.join(result)
    print(f"Result of your guess: {result_str}")

    return result_str == "ggggg"  # If all letters are correct and in the right place, return True


def play_game() -> None:
    word_to_guess: str = user_input.get_word()
    for guess_number in range(1, 7):
        print(f"Time for guess #{guess_number}!")
        user_guess: str = user_input.get_word()
        if check_word(user_guess, word_to_guess):
            break