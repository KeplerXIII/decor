from task1 import test_1
from task2 import test_2
from task3 import FlatIterator, list_of_lists

if __name__ == '__main__':

    # Задание 1
    test_1()

    # Задание 2
    test_2()

    # Задание 3
    # Не уверен, что это можно где-то практически применить, но было интересно, наследуется ли декоратор в экземпляре
    # и залогирует ли каждую итерацию, вот - работает.
    # Лог работы итератора экземпляра класса в файле - iteration.log
    iterator_object = FlatIterator(list_of_lists)
    for i in iterator_object:
        pass
