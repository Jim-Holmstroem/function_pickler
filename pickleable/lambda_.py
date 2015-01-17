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
        self._lambda = lambda_
        self._context = context

    def __getattr__(self, name):
        """Transparency
        """
        return getattr(self._lambda, name)

    def __call__(self, *args, **kwargs):
        return self._lambda(*args, **kwargs)

    def __getstate__(self):
        state = State(
            code=Code(self.func_code),
            name=self.func_name,
            argdefs=self.func_defaults,
            context=self._context,
        )

        return state

    def __setstate__(self, state):
        self._lambda = types.LambdaType(
            code=state.code._code,
            globals=state.context,
            name=state.name,
            argdefs=state.argdefs,
            closure=None,  # TODO is this needed for np/pd to work?
        )
