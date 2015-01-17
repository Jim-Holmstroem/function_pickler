from __future__ import division, print_function

from collections import namedtuple
import types


class Code(object):
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

    def __init__(self, code):
        self.code = code

    def __getatttr__(self, name):
        """Transparency
        """
        return getattr(self.code, name)

    def __getstate__(self):
        state = Code.State(
            argcount=self.co_argcount,
            nlocals=self.co_nlocals,
            stacksize=self.co_stacksize,
            flags=self.co_flags,
            codestring=self.co_code,
            constants=self.co_consts,
            names=self.co_names,
            varnames=self.varnames,
            filename=self.co_filename,
            name=self.co_name,
            firstlineno=self.co_firstlineno,
            lnotab=self.co_lnotab,
        )

        return state

    def __setstate__(self, state):
        self.code = types.CodeType(
            argcount=state.argcount,
            nlocals=state.nlocals,
            stacksize=state.stacksize,
            flags=state.flags,
            codestring=state.codestring,
            constants=state.constants,
            names=state.names,
            varnames=state.varnames,
            filename=state.filename,
            name=state.name,
            firstlineno=state.firstlineno,
            lnotab=state.lnotab,
            freevars=(),  # TODO are these needed for np/pd to work?
            cellvars=(),
        )
