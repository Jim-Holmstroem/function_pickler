from __future__ import print_function, division

from collections import namedtuple
import types

from pickleable.utils import Base
from pickleable.code import Code


State = namedtuple(
    'State',
    (
        'code',
        'name',
        'argdefs',
        'context',
    )
)


class Lambda(Base):
    def __init__(self, lambda_, context={}):
        self.lambda_ = lambda_
        self.context = context

    def __getattr__(self, name):
        """Transparency
        """
        return getattr(self.lambda_, name)

    def __call__(self, *args, **kwargs):
        print(self.__dict__)
        return self.lambda_(*args, **kwargs)

    def __getstate__(self):
        state = State(
            code=Code(self.func_code),
            name=self.func_name,
            argdefs=self.func_defaults,
            context=self.context,
        )

        return state

    def __setstate__(self, state):
        self.lambda_ = types.LambdaType(
            code=state.code.code,
            globals=state.context,
            name=state.name,
            argdefs=state.argdefs,
            closure=None,  # TODO is this needed for np/pd to work?
        )
