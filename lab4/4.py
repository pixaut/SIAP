class Animal:
   
    kingdom = "Животные"

    def __init__(self, name, age):
        
        self.name = name
        self.age = age

    
    def speak(self):
        f"{self.name} издает звук!"

    
    @staticmethod
    def is_alive():
        return True

    
    @classmethod
    def get_kingdom(cls):
        return f"Все {cls.__name__} принадлежат к царству '{cls.kingdom}'"


if __name__ == '__main__':
    
    cat = Animal("Барсик", 3)
    dog = Animal("Шарик", 5)

    
    print(cat.speak())   # Барсик издает звук!
    print(dog.speak())   # Шарик издает звук!

    
    print(Animal.is_alive())  # True

    
    print(Animal.get_kingdom())  # Все Animal принадлежат к царству 'Животные'
        