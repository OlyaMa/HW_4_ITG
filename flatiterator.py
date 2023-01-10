'''Доработать класс FlatIterator в коде ниже. Должен получиться итератор, который принимает
список списков и возвращает их плоское представление, т.е последовательность состоящую из
вложенных элементов. Функция test в коде ниже также должна отработать без ошибок.'''
class FlatIterator:

    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists

    def __iter__(self):
        self.outer_list_cursor = 0
        self.inner_list_cursor = -1
        return self

    def __next__(self):
        self.inner_list_cursor += 1 # увеличиваем inner_list_cursor
        if self.inner_list_cursor >= len(self.list_of_lists[self.outer_list_cursor]):# если во вложенном списке элементы закончились,
            self.outer_list_cursor += 1 # то переходи на следующий список, увеличив outer_list_cursor,
            self.inner_list_cursor = 0 # и обнуляем inner_list_cursor
        if self.outer_list_cursor >= len(self.list_of_lists):
            raise StopIteration
        return self.list_of_lists[self.outer_list_cursor][self.inner_list_cursor]


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

