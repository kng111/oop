import random


# self - это ссылка на текущий объект (экземпляр класса), который создается при вызове конструктора __init__.
class RandomNumberGenerator:
    def __init__(self, count=10, min_value=1, max_value=100):
        # Инициализация объекта класса с параметрами: количество чисел, минимальное и максимальное значение
        self.count = count
        # В строке self.count = count, self является ссылкой на текущий экземпляр класса (объект).
        self.min_value = min_value
        self.max_value = max_value
        self.numbers = []

    def generate_numbers(self):
        # Генерация списка случайных чисел в заданном диапазоне
        self.numbers = [random.randint(self.min_value, self.max_value) for _ in range(self.count)]

    def get_minimum(self):
        # Получение минимального значения из списка чисел
        return min(self.numbers)

    def get_maximum(self):
        # Получение максимального значения из списка чисел
        return max(self.numbers)

    def get_average(self):
        # Получение среднего значения списка чисел
        return sum(self.numbers) / len(self.numbers)

if __name__ == "__main__":
    # Создание объекта класса и генерация списка случайных чисел
    rng = RandomNumberGenerator(count=20, min_value=1, max_value=100)
    rng.generate_numbers()

    # Вывод результатов анализа списка чисел
    print(f"Сгенерированные числа: {rng.numbers}")
    print(f"Минимальное значение: {rng.get_minimum()}")
    print(f"Максимальное значение: {rng.get_maximum()}")
    print(f"Среднее значение: {rng.get_average()}")
