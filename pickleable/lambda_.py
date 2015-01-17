from __future__ import print_function, division

from collections import namedtuple
import types

from pickleable.code import Code


class Lambda(object):
    State = namedtuple(
        'State',
        (
            'code',
            'name',
            'argdefs',
            'context',
        )
    )

    def __init__(self, lambda_, context={}):
        self.lambda_ = lambda_
        self.context = context

    def __getatttr__(self, name):
        """Transparency
        """
        return getattr(self.lambda_, name)

    def __getstate__(self):
        state = Lambda.State(
            code=Code(self.func_code),
            name=self.func_name,
            argdefs=self.func_defaults,
            context=self.context,
        )

        return state

    def __setstate__(self, state):
        self._lambda = types.LambdaType(
            code=state.code,
            globals=state.context,
            name=state.name,
            argdefs=state.argdefs,
            closure=None,  # TODO is this needed for np/pd to work?
        )
