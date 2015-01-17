from __future__ import division, print_function

from itertools import (
    chain,
    imap,
    product,
    repeat,
)

from nose.tools import (
    assert_equals,
)

from pickleable import testing
from pickleable.lambda_ import Lambda


@testing.testify
def test_no_context_lambda():
    lambdas = [
        lambda x: x,
        lambda x, c=1: c * x,
    ]

    def valid_pickling(pickler, lambda_):
        input_ = 1
        assert_equals(
            pickler(Lambda(lambda_))(input_),
            Lambda(lambda_)(input_),
            lambda_(input_),
        )

    return imap(
        lambda *cs: tuple(chain(*cs)),
        repeat((valid_pickling, )),
        product(
            testing.picklers,
            lambdas,
        )
    )
