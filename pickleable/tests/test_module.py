from __future__ import division, print_function

from itertools import (
    chain,
    imap,
    product,
    repeat,
)
from nose.tools import assert_equals

from pickleable import testing
from pickleable.module import Module


@testing.testify
def test_module():
    real_modules = [
        __import__('pickle'),
        __import__('cPickle'),
    ]
    modules = real_modules

    def valid_pickling(pickler, module):
        assert_equals(
            pickler(Module(module))._module,
            module,
        )

    return imap(
        lambda *cs: tuple(chain(*cs)),
        repeat((valid_pickling, )),
        product(
            testing.picklers,
            modules,
        )
    )
