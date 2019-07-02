import  datetime
class Dog():
    count = 0
    def __init__(self,weight):
        Dog.count += 1
        self.__weight = weight

    @property
    def weight(self):
        return  self.__weight

    @weight.setter
    def weight(self, input_weight):
        self.__weight = input_weight
    @classmethod
    def dog_num(cls):
        print('we have ', cls.count,'dogs')
    @staticmethod
    def birthday():
        return  datetime.datetime.now()
    def __str__(self):
        return "这是一只狗"

    def __repr__(self):
        return  'Dog属性'

    def __eq__(self, other):
        return  self.__weight == other.__weight

dog = Dog(34)

dog3 = Dog(43)

Dog.dog_num()

