import random

class RandomStringGenerator:
    def __init__(self, file_path):
        # Конструктор класса. Принимает путь к текстовому документу.
        self.file_path = file_path
        self.words = []

    def load_words(self):
        # Метод для загрузки слов из текстового документа.
        with open(self.file_path, "r", encoding="utf-8") as file:
            self.words = file.read().split()

    def generate_random_string(self, length):
        # Метод для генерации случайной строки из текстового документа заданной длины.
        return ' '.join(random.choices(self.words, k=length))

if __name__ == "__main__":
    # Путь к текстовому документу, из которого будем генерировать случайную строку.
    file_path = "text_document.txt"

    # Создаем экземпляр класса RandomStringGenerator и загружаем слова из текстового документа.
    generator = RandomStringGenerator(file_path)
    generator.load_words()

    # Задаем длину случайной строки (в количестве слов).
    string_length = 10

    # Генерируем случайную строку.
    random_string = generator.generate_random_string(string_length)

    # Выводим результат.
    print(f"Случайная строка из текстового документа:\n{random_string}")
