from __future__ import division, print_function

from collections import namedtuple

from pickleable.utils import Base
from exceptions import Exception


State = namedtuple(
    'State',
    (
        'fully_qualified_name',
        'get_version',
        'module_version',
        'verify_version',
    )
)


class VersionMismatchException(Exception, Base):
    """
    Parameters
    ----------
    module :: module
        The module for which the mismatch took place

    pre_version :: str
        The version before.

    post_version :: str
        The version after.
    """
    def __init__(self, module, pre_version, post_version):
        self.module = module
        self.pre_version = pre_version
        self.post_version = post_version


def get_version(module):
    return __import__(
        module.__name__.split('.')[0]
    ).__version__


class Module(Base):
    """
    Parameters
    ----------
    module :: module
        The module to wrap

    get_version :: module -> str
        Function to get the version of the module.
        Some base modules are missing the __version__

    verify_version :: bool
       If the version is verified to be the same when pickling as unpickling.
       This is important since code can behave differently between versions.
    """
    def __init__(self, module, get_version=get_version, verify_version=True):
        self._module = module
        self._get_version = get_version
        self._verify_version = verify_version

    def __getattr__(self, name):
        return getattr(self._module, name)

    def __getstate__(self):
        state = State(
            fully_qualified_name=self._module.__name__,
            get_version=self._get_version,
            module_version=self._get_version(self._module),
            verify_version=self._verify_version,
        )

        return state

    def __setstate__(self, state):
        module = __import__(
            state.fully_qualified_name,
            fromlist=['not empty'],
        )

        same_version = (
            state.module_version == state.get_version(module)
        )

        if state.verify_version and not(same_version):
            raise VersionMismatchException(
                state.fully_qualified_name,
                state.module_version,
                state.get_version(module),
            )

        self._module = module
        self._get_version = state.get_version
        self._verify_version = state.verify_version
