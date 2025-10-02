class Animal:
    _cost:float
    _type:str

    def __init__(self,cost:float,type:str):
        self._cost = cost
        self._type = type

    def go(self):
        print('Animal go!!!!')
    def get_cost(self)->float:
        return self._cost
    

class Bird(Animal):
    def go(self):
        print('Bird fly!')

class Fish(Animal):
    def go(self):
        print('Fish swim!')

class ZooShop:

    animals:list

    def __init__(self,n:int):
        self.animals=list()

        for i in range(n):
            name = input('Введите породу: ')
            cost = int(input('Её стоимость: '))

            is_fish = int(input('Это рыба? (1 - да , 0 - нет): '))
            if is_fish == 1:
                new_animal = Fish(type=name,cost = cost)
            else:
                new_animal = Bird(type=name,cost=cost)

            self.animals.append(new_animal)

    def write_to_file(self,filepath):
        with open(filepath,'w',encoding='utf-8') as f:
            for animal in self.animals:
                print(f'Animal class : {type(animal)}, cost : {animal.get_cost()}, type : {animal._type}',file=f)

    def TopCostInfo(self):
        top = max(self.animals,key=Animal.get_cost)
        print(f'Самая дорогая порода: {top._type}, и её цена: {top.get_cost()}')
        
if __name__ == '__main__':
    shop = ZooShop(2)

    shop.TopCostInfo()

    shop.write_to_file('lab4/animal.txt')
