class Car:
    """Базовый класс автомобиля."""

    def __init__(self, brand: str, speed: int) -> None:
        """Создает автомобиль."""
        self.brand = brand
        self._speed = speed

    def __str__(self) -> str:
        """Строковое представление автомобиля."""
        return f"Автомобиль {self.brand}, скорость {self._speed} км/ч"

    def __repr__(self) -> str:
        """Представление объекта для разработчика."""
        return f"Car('{self.brand}', {self._speed})"

    def drive(self) -> str:
        """Описывает движение автомобиля."""
        return f"{self.brand} едет со скоростью {self._speed} км/ч"

    def get_speed(self) -> int:
        """Возвращает скорость."""
        return self._speed


class Truck(Car):
    """Грузовой автомобиль."""

    def __init__(self, brand: str, speed: int, capacity: int) -> None:
        """Создает грузовик."""
        super().__init__(brand, speed)
        self.capacity = capacity

    def __str__(self) -> str:
        """Строковое представление грузовика."""
        return f"Грузовик {self.brand}, скорость {self._speed} км/ч, груз {self.capacity} кг"

    def __repr__(self) -> str:
        """Представление объекта для разработчика."""
        return f"Truck('{self.brand}', {self._speed}, {self.capacity})"

    def drive(self) -> str:
        """Переопределенный метод движения."""
        return f"Грузовик {self.brand} везет груз и едет {self._speed} км/ч"

    def load(self) -> str:
        """Показывает грузоподъемность."""
        return f"Можно загрузить до {self.capacity} кг"


if __name__ == "__main__":
    car = Car("Toyota", 120)
    truck = Truck("Volvo", 90, 5000)

    print(car)
    print(car.drive())

    print()

    print(truck)
    print(truck.drive())
    print(truck.load())
    