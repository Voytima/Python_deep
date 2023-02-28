"""
📌 Доработаем задачи 5-6. Создайте класс-фабрику.
    ○ Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
    ○ Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
"""
from abc import ABCMeta, abstractmethod


class IAnimal(metaclass=ABCMeta):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def do_something(self):
        pass


class Bird(IAnimal):

    def __init__(self, name, age):
        super().__init__(name, age)

    def do_something(self):
        print(f"Bird: {self.name}, age: {self.age} years and it can fly!")


class Dog(IAnimal):

    def __init__(self, name, age):
        super().__init__(name, age)

    def do_something(self):
        print(f"Dog: {self.name}, age: {self.age} years and it can woof!")


class Fish(IAnimal):

    def __init__(self, name, age):
        super().__init__(name, age)

    def do_something(self):
        print(f"Fish: {self.name}, age: {self.age} years and it can swim fast!")


class AnimalFactory:

    @staticmethod
    def get_animal(animal_type):
        name = input('Enter name: ')
        age = input("Enter age in years: ")

        if animal_type == 'Bird':
            return Bird(name, age)
        if animal_type == 'Dog':
            return Dog(name, age)
        if animal_type == 'Fish':
            return Fish(name, age)
        print("Invalid animal type")

        return -1


if __name__ == '__main__':
    choice = input("What type of animal do you want to create?\nBird, Dog, Fish\n>>> ")
    animal = AnimalFactory.get_animal(choice)
    animal.do_something()
    print()
    choice = input("What type of animal do you want to create?\nBird, Dog, Fish\n>>> ")
    animal2 = AnimalFactory.get_animal(choice)
    animal2.do_something()
