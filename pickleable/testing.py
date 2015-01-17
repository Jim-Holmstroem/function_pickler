from __future__ import division, print_function

from itertools import product, starmap


picklers = map(
    __import__,
    [
        "pickle",
        "cPickle",
    ]
)

protocols = range(3)


class Pickling(object):
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

    def __repr__(self):
        return "{}({}, {})".format(
            self.__class__.__name__,
            "{}={}".format(
                "pickler",
                self.pickler,
            ),
            "{}={}".format(
                "protocol",
                self.protocol,
            ),
        )

    def __str__(self):
        return self.__repr__()


picklings = list(starmap(
    Pickling,
    product(
        picklers,
        protocols
    )
))
