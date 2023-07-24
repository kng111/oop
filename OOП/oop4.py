import pygame
import random

# Инициализация Pygame
pygame.init()

# Определение размеров экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Заголовок окна
pygame.display.set_caption("Игра с машиной и искусственным интеллектом")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Скорость машины игрока
PLAYER_SPEED = 5

# Класс для машины
class Car(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED

# Класс для искусственного интеллекта
class AI(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        # Искусственный интеллект двигается случайным образом
        self.rect.y += random.randint(1, 5)

# Создание групп спрайтов для машин и искусственного интеллекта
all_sprites = pygame.sprite.Group()
cars = pygame.sprite.Group()
ais = pygame.sprite.Group()

# Создание машин и искусственного интеллекта
player_car = Car(WIDTH // 2, HEIGHT - 50)
all_sprites.add(player_car)
cars.add(player_car)

def spawn_ai_cars():
    for i in range(10):
        ai_car = AI(random.randint(100, WIDTH - 100), random.randint(-1000, -50))
        all_sprites.add(ai_car)
        ais.add(ai_car)

# Задаем таймер, чтобы каждые 10 секунд вызывалась функция spawn_ai_cars
pygame.time.set_timer(pygame.USEREVENT, 4000)

# Главный цикл игры
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.USEREVENT:
            # Вызываем функцию для создания новых машин
            spawn_ai_cars()

    # Обновление спрайтов
    all_sprites.update()

    # Проверка столкновений машин и искусственного интеллекта
    collisions = pygame.sprite.spritecollide(player_car, ais, False)
    if collisions:
        running = False

    # Очистка экрана
    screen.fill(BLACK)

    # Отрисовка всех спрайтов
    all_sprites.draw(screen)

    # Обновление экрана
    pygame.display.flip()

    # Показываем счетчик FPS в окне заголовка
    pygame.display.set_caption(f"Игра с машиной и искусственным интеллектом | FPS: {int(clock.get_fps())}")

    # Ограничение FPS
    clock.tick(75)

pygame.quit()
