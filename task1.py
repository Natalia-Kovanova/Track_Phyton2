import doctest


class Book:

    def __init__(self, title: str, author: str, pages: int) -> None:
        """
        Создание объекта "Книга"

        :param title: Название книги
        :param author: Автор книги
        :param pages: Количество страниц

        Примеры:
        >>> book = Book("1984", "Orwell", 328)
        """
        if not isinstance(title, str):
            raise TypeError("Название должно быть строкой")
        if title == "":
            raise ValueError("Название не может быть пустым")
        self.title = title

        if not isinstance(author, str):
            raise TypeError("Автор должен быть строкой")
        if author == "":
            raise ValueError("Автор не может быть пустым")
        self.author = author

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть больше 0")
        self.pages = pages

    def open_book(self, page: int) -> None:
        """
        Открыть книгу на странице.

        :param page: Номер страницы
        :raise ValueError: Если страницы не существует

        Примеры:
        >>> book = Book("1984", "Orwell", 328)
        >>> book.open_book(10)
        """
        if not isinstance(page, int):
            raise TypeError("Номер страницы должен быть int")
        if page < 1 or page > self.pages:
            raise ValueError("Такой страницы нет")
        ...

    def read_book(self, count: int) -> None:
        """
        Прочитать несколько страниц.

        :param count: Количество страниц
        :raise ValueError: Если указано слишком большое количество страниц

        Примеры:
        >>> book = Book("1984", "Orwell", 328)
        >>> book.read_book(20)
        """
        if not isinstance(count, int):
            raise TypeError("Количество страниц должно быть int")
        if count <= 0:
            raise ValueError("Количество страниц должно быть больше 0")
        if count > self.pages:
            raise ValueError("Нельзя прочитать больше страниц, чем есть в книге")
        ...

    def close_book(self) -> None:
        """
        Закрыть книгу.

        Примеры:
        >>> book = Book("1984", "Orwell", 328)
        >>> book.close_book()
        """
        if self.title == "":
            raise ValueError("Книга должна иметь название")
        ...


class Car:

    def __init__(self, brand: str, fuel: float, speed: int) -> None:
        """
        Создание объекта "Автомобиль"

        :param brand: Марка автомобиля
        :param fuel: Количество топлива
        :param speed: Скорость

        Примеры:
        >>> car = Car("Toyota", 40, 0)
        """
        if not isinstance(brand, str):
            raise TypeError("Марка должна быть строкой")
        if brand == "":
            raise ValueError("Марка не может быть пустой")
        self.brand = brand

        if not isinstance(fuel, (int, float)):
            raise TypeError("Топливо должно быть числом")
        if fuel < 0:
            raise ValueError("Топливо не может быть отрицательным")
        self.fuel = fuel

        if not isinstance(speed, int):
            raise TypeError("Скорость должна быть int")
        if speed < 0:
            raise ValueError("Скорость не может быть отрицательной")
        self.speed = speed

    def start_engine(self) -> None:
        """
        Запустить двигатель.

        Примеры:
        >>> car = Car("Toyota", 40, 0)
        >>> car.start_engine()
        """
        if self.fuel == 0:
            raise ValueError("Нельзя завести автомобиль без топлива")
        ...

    def drive(self, new_speed: int) -> None:
        """
        Начать движение.

        :param new_speed: Новая скорость

        Примеры:
        >>> car = Car("Toyota", 40, 0)
        >>> car.drive(60)
        """
        if not isinstance(new_speed, int):
            raise TypeError("Скорость должна быть int")
        if new_speed < 0:
            raise ValueError("Скорость не может быть отрицательной")
        if self.fuel == 0:
            raise ValueError("Нельзя ехать без топлива")
        ...

    def refuel(self, liters: float) -> None:
        """
        Заправить автомобиль.

        :param liters: Количество топлива

        Примеры:
        >>> car = Car("Toyota", 40, 0)
        >>> car.refuel(10)
        """
        if not isinstance(liters, (int, float)):
            raise TypeError("Количество топлива должно быть числом")
        if liters <= 0:
            raise ValueError("Количество топлива должно быть больше 0")
        if self.fuel + liters > 100:
            raise ValueError("Слишком много топлива")
        ...

    def __str__(self) -> str:
        return f"Car: {self.brand}, fuel={self.fuel}, speed={self.speed}"


class Student:

    def __init__(self, name: str, age: int, course: int) -> None:
        """
        Создание объекта "Студент"

        :param name: Имя студента
        :param age: Возраст
        :param course: Курс

        Примеры:
        >>> student = Student("Anna", 20, 2)
        """
        if not isinstance(name, str):
            raise TypeError("Имя должно быть строкой")
        if name == "":
            raise ValueError("Имя не может быть пустым")
        self.name = name

        if not isinstance(age, int):
            raise TypeError("Возраст должен быть int")
        if age <= 0:
            raise ValueError("Возраст должен быть больше 0")
        self.age = age

        if not isinstance(course, int):
            raise TypeError("Курс должен быть int")
        if course < 1 or course > 6:
            raise ValueError("Курс должен быть от 1 до 6")
        self.course = course

    def study(self, hours: int) -> None:
        """
        Учеба студента.

        :param hours: Количество часов

        Примеры:
        >>> student = Student("Anna", 20, 2)
        >>> student.study(3)
        """
        if not isinstance(hours, int):
            raise TypeError("Количество часов должно быть int")
        if hours <= 0:
            raise ValueError("Количество часов должно быть больше 0")
        if self.course < 1:
            raise ValueError("Некорректный курс")
        ...

    def attend_class(self, subject: str) -> None:
        """
        Посетить занятие.

        :param subject: Предмет

        Примеры:
        >>> student = Student("Anna", 20, 2)
        >>> student.attend_class("Math")
        """
        if not isinstance(subject, str):
            raise TypeError("Название предмета должно быть строкой")
        if subject == "":
            raise ValueError("Название предмета не может быть пустым")
        if self.age < 16:
            raise ValueError("Студент слишком мал для обучения в вузе")
        ...

    def take_exam(self, subject: str) -> None:
        """
        Сдать экзамен.

        :param subject: Предмет

        Примеры:
        >>> student = Student("Anna", 20, 2)
        >>> student.take_exam("Physics")
        """
        if not isinstance(subject, str):
            raise TypeError("Название предмета должно быть строкой")
        if subject == "":
            raise ValueError("Название предмета не может быть пустым")
        if self.course < 1:
            raise ValueError("Студент не зачислен на курс")
        ...

    def __str__(self) -> str:
        return f"Student: {self.name}, age={self.age}, course={self.course}"


if __name__ == "__main__":
    doctest.testmod()
