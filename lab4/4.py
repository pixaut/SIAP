class Animal:
    # Атрибут класса (общий для всех экземпляров)
    kingdom = "Животные"

    def __init__(self, name, age):
        # Атрибуты экземпляра
        self.name = name
        self.age = age

    # Метод экземпляра (обычный)
    def speak(self):
        return f"{self.name} издает звук!"

    # Статический метод (не зависит ни от класса, ни от экземпляра)
    @staticmethod
    def is_alive():
        return True

    # Метод класса (работает с самим классом, а не с экземплярами)
    @classmethod
    def get_kingdom(cls):
        return f"Все {cls.__name__} принадлежат к царству '{cls.kingdom}'"


if __name__ == '__main__':
    # Создаём экземпляры
    cat = Animal("Барсик", 3)
    dog = Animal("Шарик", 5)

    # Методы экземпляра
    print(cat.speak())   # Барсик издает звук!
    print(dog.speak())   # Шарик издает звук!

    # Статический метод
    print(Animal.is_alive())  # True

    # Метод класса
    print(Animal.get_kingdom())  # Все Animal принадлежат к царству 'Животные'
        