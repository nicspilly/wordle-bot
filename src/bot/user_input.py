def get_word() -> str:
    word = ''
    while len(word) != 5:
        word = input("Please enter a 5 letter word: ")
        # TODO - Sanitize input from user
    return word