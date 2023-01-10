'''Написать генератор аналогичный генератору из задания 2, но обрабатывающий списки с любым уровнем вложенности.'''
import types
from collections.abc import Iterable


def flat_generator(list_of_list):
    for i in list_of_list:
        if isinstance(i, Iterable) and not isinstance(i, (str, bytes)):
            yield from flat_generator(i)
        else:
            yield i


def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)
