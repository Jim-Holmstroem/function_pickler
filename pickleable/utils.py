from __future__ import division, print_function


class Base(object):
    def __repr__(self):
        return "{class_name}({state})".format(
            class_name=self.__class__.__name__,
            state=", ".join(
                map(
                    "{}={}".format,
                    map(repr, self.__dict__.keys()),
                    map(repr, self.__dict__.values()),
                )
            )
        )

    def __str__(self):
        return self.__repr__()
