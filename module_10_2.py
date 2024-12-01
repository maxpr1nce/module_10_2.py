import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemy_count = 100  # Общее количество врагов
        self.days = 0

    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.enemy_count > 0:
            time.sleep(1)  # Задержка в 1 секунду
            self.enemy_count -= self.power
            self.days += 1
            if self.enemy_count < 0:
                self.enemy_count = 0
            print(f"{self.name} сражается {self.days}..., осталось {self.enemy_count} воинов.")
        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")

# Создание и запуск потоков для двух рыцарей
knight1 = Knight("Рыцарь Артур", 30)
knight2 = Knight("Рыцарь Ланселот", 25)

knight1.start()
knight2.start()

# Ожидание завершения битвы
knight1.join()
knight2.join()

print("Битвы окончены.")