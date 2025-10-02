class Calculator:
    def __init__(self):
        self.a = 0
        self.b = 0

    # Метод для ввода данных
    def input_data(self):
        self.a = float(input("Введите первое число: "))
        self.b = float(input("Введите второе число: "))

    # Методы экземпляра для операций
    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Ошибка: деление на ноль!"

if __name__ == '__main__':
    calc = Calculator()
    calc.input_data()

    print("Сумма:", calc.add())
    print("Разность:", calc.subtract())
    print("Произведение:", calc.multiply())
    print("Частное:", calc.divide())
