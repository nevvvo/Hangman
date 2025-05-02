import random

RUSSIAN_CHARS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

HANGMAN_PICS = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """,
    """
       -----
       |   |
      [O   |
      /|\\  |
      / \\  |
           |
    =========
    """,
    """
       -----
       |   |
      [O]  |
      /|\\  |
      / \\  |
           |
    =========
    """
]


def get_game_command():
    while True:
        cmd = input("Введите 'с' (старт) или 'в' (выход): ").strip().lower()
        if cmd in ['с', 'в']:
            return cmd
        print("Неверный ввод. Введите 'с' или 'в'.")


def get_letter_input(used_letters):
    while True:
        letter = input("Введите букву: ").strip().lower()
        if len(letter) != 1 or letter not in RUSSIAN_CHARS:
            print("Неправильный ввод. Введите ОДНУ русскую букву.")
        elif letter in used_letters:
            print("Вы уже вводили эту букву.")
        else:
            return letter


def get_word():
    with open("words.txt", "r", encoding='utf-8') as f:
        words = f.readline().split(", ")
        return random.choice(words)


def find_letter_positions(word, letter):
    return [i for i, char in enumerate(word) if char == letter]


def display_game_state(user_word, mistakes, used_letters):
    print(HANGMAN_PICS[mistakes])
    print("Слово:", ' '.join(user_word))
    print("Ошибки:", mistakes, "/ 8")
    print("Использованные буквы:", ', '.join(used_letters))


def play_round():
    word = get_word()
    user_word = ['_' for _ in word]
    used_letters = []
    mistakes = 0

    while mistakes < 9 and ''.join(user_word) != word:
        display_game_state(user_word, mistakes, used_letters)
        letter = get_letter_input(used_letters)
        used_letters.append(letter)

        if letter in word:
            positions = find_letter_positions(word, letter)
            for i in positions:
                user_word[i] = letter
        else:
            mistakes += 1

    display_game_state(user_word, mistakes, used_letters)

    if ''.join(user_word) == word:
        print("🎉 Победа! Загаданное слово:", word)
    else:
        print("💀 Поражение. Было слово:", word)


def main():
    print("Добро пожаловать в игру ВИСЕЛИЦА!")
    while True:
        command = get_game_command()
        if command == "с":
            play_round()
        else:
            print("До свидания!")
            break


if __name__ == "__main__":
    main()
