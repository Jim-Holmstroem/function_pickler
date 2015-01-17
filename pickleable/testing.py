from __future__ import division, print_function

from itertools import product, starmap
from functools import wraps

from nose.tools import (
    nottest,
)

from pickleable.utils import Base


pickle_modules = map(
    __import__,
    [
        "pickle",
        "cPickle",
    ]
)

protocols = range(3)


class Pickler(Base):
    def __init__(self, pickler, protocol):
        self.pickler = pickler
        self.protocol = protocol

    def __call__(self, test_subject):
        return self.pickler.loads(
            self.pickler.dumps(
                test_subject,
                protocol=self.protocol,
            )
        )


picklers = list(starmap(
    Pickler,
    product(
        pickle_modules,
        protocols
    )
))


@nottest
def testify(f):
    @wraps(f)
    def _f(*args, **kwargs):
        for test in f(*args, **kwargs):
            yield test

    return _f
