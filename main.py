from hangman_pics import HANGMAN_PICS
from typing import List
import random
RUSSIAN_CHARS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


class HangmanGame:
    def __init__(self):
        self.max_mistakes = len(HANGMAN_PICS) - 1
        self.word = ""
        self.user_word = []
        self.used_letters = []
        self.mistakes = 0


    def get_word(self) -> None:
        try:
            with open("words.txt", "r", encoding='utf-8') as f:
                words = [line.strip() for line in f if line.strip()]
                self.word = random.choice(words)
        except FileNotFoundError:
            print("Файл words.txt не найден.")
            exit()


    def find_letter_positions(self, letter : str) -> List[int]:
        return [i for i, char in enumerate(self.word) if char == letter]


    def display_game_state(self) -> None:
        print(HANGMAN_PICS[self.mistakes])
        print("Слово:", ' '.join(self.user_word))
        print("Ошибки:", self.mistakes, "/ 8")
        print("Использованные буквы:", ', '.join(self.used_letters))


    def get_letter_input(self) -> str:
    
        while True:
            letter = input("Введите букву: ").strip().lower()

            if len(letter) != 1 or letter not in RUSSIAN_CHARS:
                print("Неправильный ввод. Введите одну русскую букву.")

            elif letter in self.used_letters:
                print("Вы уже вводили эту букву.")

            else:
                return letter


    def play_round(self) -> None:
        self.get_word()
        self.user_word = ['_' for _ in self.word]
        self.used_letters = []
        self.mistakes = 0

        while self.mistakes < self.max_mistakes and ''.join(self.user_word) != self.word:
            self.display_game_state()
            letter = self.get_letter_input()
            self.used_letters.append(letter)

            if letter in self.word:
                positions = self.find_letter_positions(letter)

                for i in positions:
                    self.user_word[i] = letter

            else:
                self.mistakes += 1

        self.display_game_state()

        if ''.join(self.user_word) == self.word:
            print("Победа! Загаданное слово:", self.word)
        else:
            print("Проигрыш. Было слово:", self.word)


class GameController:
    def __init__(self):
        self.game = HangmanGame()


    def get_game_command(self) -> str:
        while True:
            cmd = input("Введите 'с' (старт) или 'в' (выход): ").strip().lower()
            if cmd in ['с', 'в']:
                return cmd
            print("Неверный ввод. Введите 'с' или 'в'.")


    def main(self) -> None:
        print("Добро пожаловать в игру!")
        while True:
            command = self.get_game_command()
            if command == "с":
                self.game.play_round()
            else:
                print("Конец!")
                break


if __name__ == "__main__":
    controller = GameController()
    controller.main()