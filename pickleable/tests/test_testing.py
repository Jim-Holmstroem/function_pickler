from __future__ import division, print_function

from itertools import (
    product,
    repeat,
    imap,
    chain,
)

from nose.tools import (
    assert_equals,
    assert_true,
)
import inspect

from pickleable import testing


def test_pickle_modules():
    assert_equals(len(testing.pickle_modules), 2)


def test_protocols():
    assert_equals(len(testing.protocols), 3)


def test_picklers():
    assert_equals(
        len(testing.picklers),
        len(testing.pickle_modules) * len(testing.protocols)
    )


def test_testify():
    def test_generator_function(generator_function):
        assert_true(
            inspect.isgeneratorfunction(generator_function)
        )

    def _generator():
        for i in range(3):
            yield i

    def _imap():
        return imap(lambda x: x, range(3))

    def _list():
        return range(3)

    for test_data in [
        _generator,
        _imap,
        _list,
    ]:
        yield test_generator_function, testing.testify(test_data)


@testing.testify
def test_pickler_is_identity():
    test_subjects = [
        1,
        'test',
        None,
        set(),
        {1},
        {},
        {'test', 1},
        [],
        [1, 'test'],
    ]

    def is_identity(pickler, test_subject):
        assert_equals(
            pickler(test_subject),
            test_subject
        )

    return imap(
        lambda *cs: tuple(chain(*cs)),
        repeat((is_identity, )),
        product(
            testing.picklers,
            test_subjects,
        )
    )
