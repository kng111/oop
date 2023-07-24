import random

class NumberGuesser:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def guess_number(self):
        while True:
            guess = random.randint(self.min_value, self.max_value)
            print(f"Предполагаю, что вы загадали число: {guess}")

            response = input("Больше (b), меньше (m) или угадал (u) число? ").lower()

            if response == 'b':
                self.min_value = guess + 1
            elif response == 'm':
                self.max_value = guess - 1
            elif response == 'u':
                print(f"Ура! Число {guess} угадано.")
                break
            else:
                print("Некорректный ввод. Попробуйте снова.")

if __name__ == "__main__":
    min_value = 1
    max_value = 100
    print("Загадайте число от 1 до 100.")
    guesser = NumberGuesser(min_value, max_value)
    guesser.guess_number()
