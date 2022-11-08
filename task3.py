from task2 import logger


class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.counter = 0
        self.listcounter = 0
        return self

    @logger('iteration.log')
    def __next__(self):
        if self.counter >= len(self.list_of_list):
            raise StopIteration
        result = self.list_of_list[self.counter]
        if self.listcounter < len(result) - 1:
            item = result[self.listcounter]
            self.listcounter += 1
        else:
            item = result[self.listcounter]
            self.counter += 1
            self.listcounter = 0

        return item

list_of_lists = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
]