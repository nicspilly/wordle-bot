def get_word() -> str:
    word: str = ''
    while len(word) != 5:
        word = input("Please enter a 5 letter word: ")
        # TODO - Sanitize input from user and verify it's an English word
    return word.lower()