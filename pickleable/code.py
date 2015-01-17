from __future__ import division, print_function

from collections import namedtuple
import types

from pickleable.utils import Base


State = namedtuple(
    'State',
    (
        'argcount',
        'nlocals',
        'stacksize',
        'flags',
        'codestring',
        'constants',
        'names',
        'varnames',
        'filename',
        'name',
        'firstlineno',
        'lnotab',
    )
)


class Code(Base):
    def __init__(self, code):
        self._code = code

    def __getattr__(self, name):
        """Transparency
        """
        return getattr(self._code, name)

    def __getstate__(self):
        state = State(
            argcount=self.co_argcount,
            nlocals=self.co_nlocals,
            stacksize=self.co_stacksize,
            flags=self.co_flags,
            codestring=self.co_code,
            constants=self.co_consts,
            names=self.co_names,
            varnames=self.co_varnames,
            filename=self.co_filename,
            name=self.co_name,
            firstlineno=self.co_firstlineno,
            lnotab=self.co_lnotab,
        )

        return state

    def __setstate__(self, state):
        self._code = types.CodeType(
            state.argcount,
            state.nlocals,
            state.stacksize,
            state.flags,
            state.codestring,
            state.constants,
            state.names,
            state.varnames,
            state.filename,
            state.name,
            state.firstlineno,
            state.lnotab,
            (),  # TODO are these needed for np/pd to work?
            (),  # NOTE does not support keyword arguments (and the exception message is not showing it properly)
        )
