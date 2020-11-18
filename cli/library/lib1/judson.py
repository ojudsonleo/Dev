# TODO: finshed
"""Lib"""
import time
import os
import collections
from collections import Counter
from collections import namedtuple
import inspect
from time import *
import random

"""os imports"""
import abc
import sys
import stat as st


def printlist():
    while True:
        inp = input("")

        inpk = input("")

        inpkk = input("")

        inpkkkk = input("")

        list = [inp, inpk, inpkk, inpkkkk]

        def listname():
            print(list)

        listname()


def jsys():
    # encoding: utf-8
    # module sys
    # from (built-in)
    # by generator 1.147
    """
    This module provides access to some objects used or maintained by the
    interpreter and to functions that interact strongly with the interpreter.

    Dynamic objects:

    argv -- command line arguments; argv[0] is the script pathname if known
    path -- module search path; path[0] is the script directory, else ''
    modules -- dictionary of loaded modules

    displayhook -- called to show results in an interactive session
    excepthook -- called to handle any uncaught exception other than SystemExit
      To customize printing in an interactive session or to install a custom
      top-level exception handler, assign other functions to replace these.

    stdin -- standard input file object; used by input()
    stdout -- standard output file object; used by print()
    stderr -- standard error object; used for error messages
      By assigning other file objects (or objects that behave like files)
      to these, it is possible to redirect all of the interpreter's I/O.

    last_type -- type of last uncaught exception
    last_value -- value of last uncaught exception
    last_traceback -- traceback of last uncaught exception
      These three are only available in an interactive session after a
      traceback has been printed.

    Static objects:

    builtin_module_names -- tuple of module names built into this interpreter
    copyright -- copyright notice pertaining to this interpreter
    exec_prefix -- prefix used to find the machine-specific Python library
    executable -- absolute path of the executable binary of the Python interpreter
    float_info -- a named tuple with information about the float implementation.
    float_repr_style -- string indicating the style of repr() output for floats
    hash_info -- a named tuple with information about the hash algorithm.
    hexversion -- version information encoded as a single integer
    implementation -- Python implementation information.
    int_info -- a named tuple with information about the int implementation.
    maxsize -- the largest supported length of containers.
    maxunicode -- the value of the largest Unicode code point
    platform -- platform identifier
    prefix -- prefix used to find the Python library
    thread_info -- a named tuple with information about the thread implementation.
    version -- the version of this interpreter as a string
    version_info -- version information as a named tuple
    __stdin__ -- the original stdin; don't touch!
    __stdout__ -- the original stdout; don't touch!
    __stderr__ -- the original stderr; don't touch!
    __displayhook__ -- the original displayhook; don't touch!
    __excepthook__ -- the original excepthook; don't touch!

    Functions:

    displayhook() -- print an object to the screen, and save it in builtins._
    excepthook() -- print an exception and its traceback to sys.stderr
    exc_info() -- return thread-safe information about the current exception
    exit() -- exit the interpreter by raising SystemExit
    getdlopenflags() -- returns flags to be used for dlopen() calls
    getprofile() -- get the global profiling function
    getrefcount() -- return the reference count for an object (plus one :-)
    getrecursionlimit() -- return the max recursion depth for the interpreter
    getsizeof() -- return the size of an object in bytes
    gettrace() -- get the global debug tracing function
    setcheckinterval() -- control how often the interpreter checks for events
    setdlopenflags() -- set the flags to be used for dlopen() calls
    setprofile() -- set the global profiling function
    setrecursionlimit() -- set the max recursion depth for the interpreter
    settrace() -- set the global debug tracing function
    """
    # no imports

    # Variables with simple values

    abiflags = ''

    api_version = 1013

    base_exec_prefix = '/home/obedotto/anaconda3/envs/joeljebitto'

    base_prefix = '/home/obedotto/anaconda3/envs/joeljebitto'

    byteorder = 'little'

    copyright = 'Copyright (c) 2001-2020 Python Software Foundation.\nAll Rights Reserved.\n\nCopyright (c) 2000 BeOpen.com.\nAll Rights Reserved.\n\nCopyright (c) 1995-2001 Corporation for National Research Initiatives.\nAll Rights Reserved.\n\nCopyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.\nAll Rights Reserved.'

    dont_write_bytecode = True

    executable = '/home/obedotto/anaconda3/envs/joeljebitto/bin/python'

    exec_prefix = '/home/obedotto/anaconda3/envs/joeljebitto'

    float_repr_style = 'short'

    hexversion = 50856944

    maxsize = 9223372036854775807
    maxunicode = 1114111

    platform = 'linux'

    prefix = '/home/obedotto/anaconda3/envs/joeljebitto'

    pycache_prefix = None

    version = '3.8.3 | packaged by conda-forge | (default, Jun  1 2020, 17:43:00) \n[GCC 7.5.0]'

    _base_executable = '/home/obedotto/anaconda3/envs/joeljebitto/bin/python'

    _framework = ''

    _home = None

    # functions

    def addaudithook(*args, **kwargs):  # real signature unknown
        """ Adds a new audit hook callback. """
        pass

    def audit(event, *args):  # real signature unknown; restored from __doc__
        """
        audit(event, *args)

        Passes the event to any audit hooks that are attached.
        """
        pass

    def breakpointhook(*args, **kws):  # real signature unknown; restored from __doc__
        """
        breakpointhook(*args, **kws)

        This hook function is called by built-in breakpoint().
        """
        pass

    def callstats(*args, **kwargs):  # real signature unknown
        """
        Return a tuple of function call statistics.

        A tuple is returned only if CALL_PROFILE was defined when Python was
        built.  Otherwise, this returns None.

        When enabled, this function returns detailed, implementation-specific
        details about the number of function calls executed. The return value
        is a 11-tuple where the entries in the tuple are counts of:
        0. all function calls
        1. calls to PyFunction_Type objects
        2. PyFunction calls that do not create an argument tuple
        3. PyFunction calls that do not create an argument tuple
           and bypass PyEval_EvalCodeEx()
        4. PyMethod calls
        5. PyMethod calls on bound methods
        6. PyType calls
        7. PyCFunction calls
        8. generator calls
        9. All other calls
        10. Number of stack pops performed by call_function()
        """
        pass

    def call_tracing(*args, **kwargs):  # real signature unknown
        """
        Call func(*args), while tracing is enabled.

        The tracing state is saved, and restored afterwards.  This is intended
        to be called from a debugger from a checkpoint, to recursively debug
        some other code.
        """
        pass

    def displayhook(*args, **kwargs):  # real signature unknown
        """ Print an object to sys.stdout and also save it in builtins._ """
        pass

    def excepthook(*args, **kwargs):  # real signature unknown
        """ Handle an exception by displaying it with a traceback on sys.stderr. """
        pass

    def exc_info(*args, **kwargs):  # real signature unknown
        """
        Return current exception information: (type, value, traceback).

        Return information about the most recent exception caught by an except
        clause in the current stack frame or in an older stack frame.
        """
        pass

    def exit(*args, **kwargs):  # real signature unknown
        """
        Exit the interpreter by raising SystemExit(status).

        If the status is omitted or None, it defaults to zero (i.e., success).
        If the status is an integer, it will be used as the system exit status.
        If it is another kind of object, it will be printed and the system
        exit status will be one (i.e., failure).
        """
        pass

    def getallocatedblocks(*args, **kwargs):  # real signature unknown
        """ Return the number of memory blocks currently allocated. """
        pass

    def getcheckinterval(*args, **kwargs):  # real signature unknown
        """ Return the current check interval; see sys.setcheckinterval(). """
        pass

    def getdefaultencoding(*args, **kwargs):  # real signature unknown
        """ Return the current default encoding used by the Unicode implementation. """
        pass

    def getdlopenflags(*args, **kwargs):  # real signature unknown
        """
        Return the current value of the flags that are used for dlopen calls.

        The flag constants are defined in the os module.
        """
        pass

    def getfilesystemencodeerrors(*args, **kwargs):  # real signature unknown
        """ Return the error mode used Unicode to OS filename conversion. """
        pass

    def getfilesystemencoding(*args, **kwargs):  # real signature unknown
        """ Return the encoding used to convert Unicode filenames to OS filenames. """
        pass

    def getprofile(*args, **kwargs):  # real signature unknown
        """
        Return the profiling function set with sys.setprofile.

        See the profiler chapter in the library manual.
        """
        pass

    def getrecursionlimit(*args, **kwargs):  # real signature unknown
        """
        Return the current value of the recursion limit.

        The recursion limit is the maximum depth of the Python interpreter
        stack.  This limit prevents infinite recursion from causing an overflow
        of the C stack and crashing Python.
        """
        pass

    def getrefcount():  # real signature unknown; restored from __doc__
        """
        Return the reference count of object.

        The count returned is generally one higher than you might expect,
        because it includes the (temporary) reference as an argument to
        getrefcount().
        """
        pass

    def getsizeof(p_object, default=None):  # real signature unknown; restored from __doc__
        """
        getsizeof(object [, default]) -> int

        Return the size of object in bytes.
        """
        return 0

    def getswitchinterval(*args, **kwargs):  # real signature unknown
        """ Return the current thread switch interval; see sys.setswitchinterval(). """
        pass

    def gettrace(*args, **kwargs):  # real signature unknown
        """
        Return the global debug tracing function set with sys.settrace.

        See the debugger chapter in the library manual.
        """
        pass

    def get_asyncgen_hooks(*args, **kwargs):  # real signature unknown
        """
        Return the installed asynchronous generators hooks.

        This returns a namedtuple of the form (firstiter, finalizer).
        """
        pass

    def get_coroutine_origin_tracking_depth(*args, **kwargs):  # real signature unknown
        """ Check status of origin tracking for coroutine objects in this thread. """
        pass

    def intern(*args, **kwargs):  # real signature unknown
        """
        ``Intern'' the given string.

        This enters the string in the (global) table of interned strings whose
        purpose is to speed up dictionary lookups. Return the string itself or
        the previously interned string object with the same value.
        """
        pass

    def is_finalizing(*args, **kwargs):  # real signature unknown
        """ Return True if Python is exiting. """
        pass

    def setcheckinterval(*args, **kwargs):  # real signature unknown
        """
        Set the async event check interval to n instructions.

        This tells the Python interpreter to check for asynchronous events
        every n instructions.

        This also affects how often thread switches occur.
        """
        pass

    def setdlopenflags(*args, **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        Set the flags used by the interpreter for dlopen calls.

        This is used, for example, when the interpreter loads extension
        modules. Among other things, this will enable a lazy resolving of
        symbols when importing a module, if called as sys.setdlopenflags(0).
        To share symbols across extension modules, call as
        sys.setdlopenflags(os.RTLD_GLOBAL).  Symbolic names for the flag
        modules can be found in the os module (RTLD_xxx constants, e.g.
        os.RTLD_LAZY).
        """
        pass

    def setprofile(function):  # real signature unknown; restored from __doc__
        """
        setprofile(function)

        Set the profiling function.  It will be called on each function call
        and return.  See the profiler chapter in the library manual.
        """
        pass

    def setrecursionlimit(*args, **kwargs):  # real signature unknown
        """
        Set the maximum depth of the Python interpreter stack to n.

        This limit prevents infinite recursion from causing an overflow of the C
        stack and crashing Python.  The highest possible limit is platform-
        dependent.
        """
        pass

    def setswitchinterval(*args, **kwargs):  # real signature unknown
        """
        Set the ideal thread switching delay inside the Python interpreter.

        The actual frequency of switching threads can be lower if the
        interpreter executes long sequences of uninterruptible code
        (this is implementation-specific and workload-dependent).

        The parameter must represent the desired switching delay in seconds
        A typical value is 0.005 (5 milliseconds).
        """
        pass

    def settrace(function):  # real signature unknown; restored from __doc__
        """
        settrace(function)

        Set the global debug tracing function.  It will be called on each
        function call.  See the debugger chapter in the library manual.
        """
        pass

    def set_asyncgen_hooks(*args, **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        set_asyncgen_hooks(* [, firstiter] [, finalizer])

        Set a finalizer for async generators objects.
        """
        pass

    def set_coroutine_origin_tracking_depth(*args, **kwargs):  # real signature unknown
        """
        Enable or disable origin tracking for coroutine objects in this thread.

        Coroutine objects will track 'depth' frames of traceback information
        about where they came from, available in their cr_origin attribute.

        Set a depth of 0 to disable.
        """
        pass

    def unraisablehook(*args, **kwargs):  # real signature unknown
        """
        Handle an unraisable exception.

        The unraisable argument has the following attributes:

        * exc_type: Exception type.
        * exc_value: Exception value, can be None.
        * exc_traceback: Exception traceback, can be None.
        * err_msg: Error message, can be None.
        * object: Object causing the exception, can be None.
        """
        pass

    def _clear_type_cache(*args, **kwargs):  # real signature unknown
        """ Clear the internal type lookup cache. """
        pass

    def _current_frames(*args, **kwargs):  # real signature unknown
        """
        Return a dict mapping each thread's thread id to its current stack frame.

        This function should be used for specialized purposes only.
        """
        pass

    def _debugmallocstats(*args, **kwargs):  # real signature unknown
        """
        Print summary info to stderr about the state of pymalloc's structures.

        In Py_DEBUG mode, also perform some expensive internal consistency
        checks.
        """
        pass

    def _getframe(*args, **kwargs):  # real signature unknown
        """
        Return a frame object from the call stack.

        If optional integer depth is given, return the frame object that many
        calls below the top of the stack.  If that is deeper than the call
        stack, ValueError is raised.  The default for depth is zero, returning
        the frame at the top of the call stack.

        This function should be used for internal and specialized purposes
        only.
        """
        pass

    def __breakpointhook__(*args, **kwargs):  # real signature unknown
        """
        breakpointhook(*args, **kws)

        This hook function is called by built-in breakpoint().
        """
        pass

    def __displayhook__(*args, **kwargs):  # real signature unknown
        """ Print an object to sys.stdout and also save it in builtins._ """
        pass

    def __excepthook__(*args, **kwargs):  # real signature unknown
        """ Handle an exception by displaying it with a traceback on sys.stderr. """
        pass

    def __interactivehook__():  # reliably restored by inspect
        # no doc
        pass

    def __unraisablehook__(*args, **kwargs):  # real signature unknown
        """
        Handle an unraisable exception.

        The unraisable argument has the following attributes:

        * exc_type: Exception type.
        * exc_value: Exception value, can be None.
        * exc_traceback: Exception traceback, can be None.
        * err_msg: Error message, can be None.
        * object: Object causing the exception, can be None.
        """
        pass

    # classes

    class __loader__(object):
        """
        Meta path import for built-in modules.

            All methods are either class or static methods to avoid the need to
            instantiate the class.
        """

        @classmethod
        def create_module(cls, *args, **kwargs):  # real signature unknown
            """ Create a built-in module """
            pass

        @classmethod
        def exec_module(cls, *args, **kwargs):  # real signature unknown
            """ Exec a built-in module """
            pass

        @classmethod
        def find_module(cls, *args, **kwargs):  # real signature unknown
            """
            Find the built-in module.

                    If 'path' is ever specified then the search is considered a failure.

                    This method is deprecated.  Use find_spec() instead.
            """
            pass

        @classmethod
        def find_spec(cls, *args, **kwargs):  # real signature unknown
            pass

        @classmethod
        def get_code(cls, *args, **kwargs):  # real signature unknown
            """ Return None as built-in modules do not have code objects. """
            pass

        @classmethod
        def get_source(cls, *args, **kwargs):  # real signature unknown
            """ Return None as built-in modules do not have source code. """
            pass

        @classmethod
        def is_package(cls, *args, **kwargs):  # real signature unknown
            """ Return False as built-in modules are never packages. """
            pass

        @classmethod
        def load_module(cls, *args, **kwargs):  # real signature unknown
            """
            Load the specified module into sys.modules and return it.

                This method is deprecated.  Use loader.exec_module instead.
            """
            pass

        def module_repr(module):  # reliably restored by inspect
            """
            Return repr for the module.

                    The method is deprecated.  The import machinery does the job itself.
            """
            pass

        def __init__(self, *args, **kwargs):  # real signature unknown
            pass

        __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
        """list of weak references to the object (if defined)"""

        __dict__ = None  # (!) real value is "mappingproxy({'__module__': '_frozen_importlib', '__doc__': 'Meta path import for built-in modules.\\n\\n    All methods are either class or static methods to avoid the need to\\n    instantiate the class.\\n\\n    ', 'module_repr': <staticmethod object at 0x7f5ae0fac430>, 'find_spec': <classmethod object at 0x7f5ae0fac460>, 'find_module': <classmethod object at 0x7f5ae0fac490>, 'create_module': <classmethod object at 0x7f5ae0fac4c0>, 'exec_module': <classmethod object at 0x7f5ae0fac4f0>, 'get_code': <classmethod object at 0x7f5ae0fac580>, 'get_source': <classmethod object at 0x7f5ae0fac610>, 'is_package': <classmethod object at 0x7f5ae0fac6a0>, 'load_module': <classmethod object at 0x7f5ae0fac6d0>, '__dict__': <attribute '__dict__' of 'BuiltinImporter' objects>, '__weakref__': <attribute '__weakref__' of 'BuiltinImporter' objects>})"

    # variables with complex values

    argv = []  # real value of type <class 'list'> skipped

    builtin_module_names = ()  # real value of type <class 'tuple'> skipped

    flags = (
        0,
        0,
        0,
        0,
        1,
        0,
        0,
        0,
        0,
        0,
        0,
        1,
        0,
        False,
        0,
    )

    float_info = (
        1.7976931348623157e+308,
        1024,
        308,
        2.2250738585072014e-308,
        -1021,
        -307,
        15,
        53,
        2.220446049250313e-16,
        2,
        1,
    )

    hash_info = (
        64,
        2305843009213693951,
        314159,
        0,
        1000003,
        'siphash24',
        64,
        128,
        0,
    )

    implementation = None  # (!) real value is "namespace(_multiarch='x86_64-linux-gnu', cache_tag='cpython-38', hexversion=50856944, name='cpython', version=sys.version_info(major=3, minor=8, micro=3, releaselevel='final', serial=0))"

    int_info = (
        30,
        4,
    )

    meta_path = [
        __loader__,
        None,  # (!) real value is "<class '_frozen_importlib.FrozenImporter'>"
        None,  # (!) real value is "<class '_frozen_importlib_external.PathFinder'>"
        None,  # (!) real value is '<six._SixMetaPathImporter object at 0x7f5adf545460>'
    ]

    modules = {}  # real value of type <class 'dict'> skipped

    path = [
        '/home/obedotto/pycharm-2020.1.2/plugins/python/helpers',
        '/home/obedotto/pycharm-2020.1.2/plugins/python/helpers/generator3',
        '/home/obedotto/anaconda3/envs/joeljebitto/lib/python38.zip',
        '/home/obedotto/anaconda3/envs/joeljebitto/lib/python3.8',
        '/home/obedotto/anaconda3/envs/joeljebitto/lib/python3.8/lib-dynload',
        '/home/obedotto/anaconda3/envs/joeljebitto/lib/python3.8/site-packages',
        '/home/obedotto/pycharm-2020.1.2/plugins/python/helpers/typeshed/stdlib/3.7',
        '/home/obedotto/pycharm-2020.1.2/plugins/python/helpers/typeshed/stdlib/3',
        '/home/obedotto/pycharm-2020.1.2/plugins/python/helpers/typeshed/stdlib/2and3',
        '/home/obedotto/pycharm-2020.1.2/plugins/python/helpers/typeshed/third_party/3',
        '/home/obedotto/pycharm-2020.1.2/plugins/python/helpers/typeshed/third_party/2and3',
    ]

    path_hooks = [
        None,  # (!) real value is "<class 'zipimport.zipimporter'>"
        None,  # (!) real value is '<function FileFinder.path_hook.<locals>.path_hook_for_FileFinder at 0x7f5ae0f61160>'
    ]

    path_importer_cache = {}  # real value of type <class 'dict'> skipped

    stderr = None  # (!) real value is "<_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'>"

    stdin = None  # (!) real value is "<_io.TextIOWrapper name=6 mode='r' encoding='UTF-8'>"

    stdout = None  # (!) forward: __stdout__, real value is "<_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>"

    thread_info = (
        'pthread',
        'semaphore',
        'NPTL 2.23',
    )

    version_info = (
        3,
        8,
        3,
        'final',
        0,
    )

    warnoptions = []

    _git = (
        'CPython',
        '',
        '',
    )

    _xoptions = {}

    __spec__ = None  # (!) real value is "ModuleSpec(name='sys', loader=<class '_frozen_importlib.BuiltinImporter'>)"

    __stderr__ = stderr

    __stdin__ = None  # (!) real value is "<_io.TextIOWrapper name='<stdin>' mode='r' encoding='utf-8'>"

    __stdout__ = None  # (!) real value is "<_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>"

    # intermittent names
    exc_value = Exception()
    exc_traceback = None


def jpickel():
    """Create portable serialized representations of Python objects.

    See module copyreg for a mechanism for registering custom picklers.
    See module pickletools source for extensive comments.

    Classes:

        Pickler
        Unpickler

    Functions:

        dump(object, file)
        dumps(object) -> string
        load(file) -> object
        loads(string) -> object

    Misc variables:

        __version__
        format_version
        compatible_formats

    """

    from types import FunctionType
    from copyreg import dispatch_table
    from copyreg import _extension_registry, _inverted_registry, _extension_cache
    from itertools import islice
    from functools import partial
    import sys
    from sys import maxsize
    from struct import pack, unpack
    import re
    import io
    import codecs
    import _compat_pickle

    __all__ = ["PickleError", "PicklingError", "UnpicklingError", "Pickler",
               "Unpickler", "dump", "dumps", "load", "loads"]

    try:
        from _pickle import PickleBuffer
        __all__.append("PickleBuffer")
        _HAVE_PICKLE_BUFFER = True
    except ImportError:
        _HAVE_PICKLE_BUFFER = False

    # Shortcut for use in isinstance testing
    bytes_types = (bytes, bytearray)

    # These are purely informational; no code uses these.
    format_version = "4.0"  # File format version we write
    compatible_formats = ["1.0",  # Original protocol 0
                          "1.1",  # Protocol 0 with INST added
                          "1.2",  # Original protocol 1
                          "1.3",  # Protocol 1 with BINFLOAT added
                          "2.0",  # Protocol 2
                          "3.0",  # Protocol 3
                          "4.0",  # Protocol 4
                          "5.0",  # Protocol 5
                          ]  # Old format versions we can read

    # This is the highest protocol number we know how to read.
    HIGHEST_PROTOCOL = 5

    # The protocol we write by default.  May be less than HIGHEST_PROTOCOL.
    # Only bump this if the oldest still supported version of Python already
    # includes it.
    DEFAULT_PROTOCOL = 4

    class PickleError(Exception):
        """A common base class for the other pickling exceptions."""
        pass

    class PicklingError(PickleError):
        """This exception is raised when an unpicklable object is passed to the
        dump() method.

        """
        pass

    class UnpicklingError(PickleError):
        """This exception is raised when there is a problem unpickling an object,
        such as a security violation.

        Note that other exceptions may also be raised during unpickling, including
        (but not necessarily limited to) AttributeError, EOFError, ImportError,
        and IndexError.

        """
        pass

    # An instance of _Stop is raised by Unpickler.load_stop() in response to
    # the STOP opcode, passing the object that is the result of unpickling.
    class _Stop(Exception):
        def __init__(self, value):
            self.value = value

    # Jython has PyStringMap; it's a dict subclass with string keys
    try:
        from org.python.core import PyStringMap
    except ImportError:
        PyStringMap = None

    # Pickle opcodes.  See pickletools.py for extensive docs.  The listing
    # here is in kind-of alphabetical order of 1-character pickle code.
    # pickletools groups them by purpose.

    MARK = b'('  # push special markobject on stack
    STOP = b'.'  # every pickle ends with STOP
    POP = b'0'  # discard topmost stack item
    POP_MARK = b'1'  # discard stack top through topmost markobject
    DUP = b'2'  # duplicate top stack item
    FLOAT = b'F'  # push float object; decimal string argument
    INT = b'I'  # push integer or bool; decimal string argument
    BININT = b'J'  # push four-byte signed int
    BININT1 = b'K'  # push 1-byte unsigned int
    LONG = b'L'  # push long; decimal string argument
    BININT2 = b'M'  # push 2-byte unsigned int
    NONE = b'N'  # push None
    PERSID = b'P'  # push persistent object; id is taken from string arg
    BINPERSID = b'Q'  # "       "         "  ;  "  "   "     "  stack
    REDUCE = b'R'  # apply callable to argtuple, both on stack
    STRING = b'S'  # push string; NL-terminated string argument
    BINSTRING = b'T'  # push string; counted binary string argument
    SHORT_BINSTRING = b'U'  # "     "   ;    "      "       "      " < 256 bytes
    UNICODE = b'V'  # push Unicode string; raw-unicode-escaped'd argument
    BINUNICODE = b'X'  # "     "       "  ; counted UTF-8 string argument
    APPEND = b'a'  # append stack top to list below it
    BUILD = b'b'  # call __setstate__ or __dict__.update()
    GLOBAL = b'c'  # push self.find_class(modname, name); 2 string args
    DICT = b'd'  # build a dict from stack items
    EMPTY_DICT = b'}'  # push empty dict
    APPENDS = b'e'  # extend list on stack by topmost stack slice
    GET = b'g'  # push item from memo on stack; index is string arg
    BINGET = b'h'  # "    "    "    "   "   "  ;   "    " 1-byte arg
    INST = b'i'  # build & push class instance
    LONG_BINGET = b'j'  # push item from memo on stack; index is 4-byte arg
    LIST = b'l'  # build list from topmost stack items
    EMPTY_LIST = b']'  # push empty list
    OBJ = b'o'  # build & push class instance
    PUT = b'p'  # store stack top in memo; index is string arg
    BINPUT = b'q'  # "     "    "   "   " ;   "    " 1-byte arg
    LONG_BINPUT = b'r'  # "     "    "   "   " ;   "    " 4-byte arg
    SETITEM = b's'  # add key+value pair to dict
    TUPLE = b't'  # build tuple from topmost stack items
    EMPTY_TUPLE = b')'  # push empty tuple
    SETITEMS = b'u'  # modify dict by adding topmost key+value pairs
    BINFLOAT = b'G'  # push float; arg is 8-byte float encoding

    TRUE = b'I01\n'  # not an opcode; see INT docs in pickletools.py
    FALSE = b'I00\n'  # not an opcode; see INT docs in pickletools.py

    # Protocol 2

    PROTO = b'\x80'  # identify pickle protocol
    NEWOBJ = b'\x81'  # build object by applying cls.__new__ to argtuple
    EXT1 = b'\x82'  # push object from extension registry; 1-byte index
    EXT2 = b'\x83'  # ditto, but 2-byte index
    EXT4 = b'\x84'  # ditto, but 4-byte index
    TUPLE1 = b'\x85'  # build 1-tuple from stack top
    TUPLE2 = b'\x86'  # build 2-tuple from two topmost stack items
    TUPLE3 = b'\x87'  # build 3-tuple from three topmost stack items
    NEWTRUE = b'\x88'  # push True
    NEWFALSE = b'\x89'  # push False
    LONG1 = b'\x8a'  # push long from < 256 bytes
    LONG4 = b'\x8b'  # push really big long

    _tuplesize2code = [EMPTY_TUPLE, TUPLE1, TUPLE2, TUPLE3]

    # Protocol 3 (Python 3.x)

    BINBYTES = b'B'  # push bytes; counted binary string argument
    SHORT_BINBYTES = b'C'  # "     "   ;    "      "       "      " < 256 bytes

    # Protocol 4

    SHORT_BINUNICODE = b'\x8c'  # push short string; UTF-8 length < 256 bytes
    BINUNICODE8 = b'\x8d'  # push very long string
    BINBYTES8 = b'\x8e'  # push very long bytes string
    EMPTY_SET = b'\x8f'  # push empty set on the stack
    ADDITEMS = b'\x90'  # modify set by adding topmost stack items
    FROZENSET = b'\x91'  # build frozenset from topmost stack items
    NEWOBJ_EX = b'\x92'  # like NEWOBJ but work with keyword only arguments
    STACK_GLOBAL = b'\x93'  # same as GLOBAL but using names on the stacks
    MEMOIZE = b'\x94'  # store top of the stack in memo
    FRAME = b'\x95'  # indicate the beginning of a new frame

    # Protocol 5

    BYTEARRAY8 = b'\x96'  # push bytearray
    NEXT_BUFFER = b'\x97'  # push next out-of-band buffer
    READONLY_BUFFER = b'\x98'  # make top of stack readonly

    __all__.extend([x for x in dir() if re.match("[A-Z][A-Z0-9_]+$", x)])

    class _Framer:

        _FRAME_SIZE_MIN = 4
        _FRAME_SIZE_TARGET = 64 * 1024

        def __init__(self, file_write):
            self.file_write = file_write
            self.current_frame = None

        def start_framing(self):
            self.current_frame = io.BytesIO()

        def end_framing(self):
            if self.current_frame and self.current_frame.tell() > 0:
                self.commit_frame(force=True)
                self.current_frame = None

        def commit_frame(self, force=False):
            if self.current_frame:
                f = self.current_frame
                if f.tell() >= self._FRAME_SIZE_TARGET or force:
                    data = f.getbuffer()
                    write = self.file_write
                    if len(data) >= self._FRAME_SIZE_MIN:
                        # Issue a single call to the write method of the underlying
                        # file object for the frame opcode with the size of the
                        # frame. The concatenation is expected to be less expensive
                        # than issuing an additional call to write.
                        write(FRAME + pack("<Q", len(data)))

                    # Issue a separate call to write to append the frame
                    # contents without concatenation to the above to avoid a
                    # memory copy.
                    write(data)

                    # Start the new frame with a new io.BytesIO instance so that
                    # the file object can have delayed access to the previous frame
                    # contents via an unreleased memoryview of the previous
                    # io.BytesIO instance.
                    self.current_frame = io.BytesIO()

        def write(self, data):
            if self.current_frame:
                return self.current_frame.write(data)
            else:
                return self.file_write(data)

        def write_large_bytes(self, header, payload):
            write = self.file_write
            if self.current_frame:
                # Terminate the current frame and flush it to the file.
                self.commit_frame(force=True)

            # Perform direct write of the header and payload of the large binary
            # object. Be careful not to concatenate the header and the payload
            # prior to calling 'write' as we do not want to allocate a large
            # temporary bytes object.
            # We intentionally do not insert a protocol 4 frame opcode to make
            # it possible to optimize file.read calls in the loader.
            write(header)
            write(payload)

    class _Unframer:

        def __init__(self, file_read, file_readline, file_tell=None):
            self.file_read = file_read
            self.file_readline = file_readline
            self.current_frame = None

        def readinto(self, buf):
            if self.current_frame:
                n = self.current_frame.readinto(buf)
                if n == 0 and len(buf) != 0:
                    self.current_frame = None
                    n = len(buf)
                    buf[:] = self.file_read(n)
                    return n
                if n < len(buf):
                    raise UnpicklingError(
                        "pickle exhausted before end of frame")
                return n
            else:
                n = len(buf)
                buf[:] = self.file_read(n)
                return n

        def read(self, n):
            if self.current_frame:
                data = self.current_frame.read(n)
                if not data and n != 0:
                    self.current_frame = None
                    return self.file_read(n)
                if len(data) < n:
                    raise UnpicklingError(
                        "pickle exhausted before end of frame")
                return data
            else:
                return self.file_read(n)

        def readline(self):
            if self.current_frame:
                data = self.current_frame.readline()
                if not data:
                    self.current_frame = None
                    return self.file_readline()
                if data[-1] != b'\n'[0]:
                    raise UnpicklingError(
                        "pickle exhausted before end of frame")
                return data
            else:
                return self.file_readline()

        def load_frame(self, frame_size):
            if self.current_frame and self.current_frame.read() != b'':
                raise UnpicklingError(
                    "beginning of a new frame before end of current frame")
            self.current_frame = io.BytesIO(self.file_read(frame_size))

    # Tools used for pickling.

    def _getattribute(obj, name):
        for subpath in name.split('.'):
            if subpath == '<locals>':
                raise AttributeError("Can't get local attribute {!r} on {!r}"
                                     .format(name, obj))
            try:
                parent = obj
                obj = getattr(obj, subpath)
            except AttributeError:
                raise AttributeError("Can't get attribute {!r} on {!r}"
                                     .format(name, obj)) from None
        return obj, parent

    def whichmodule(obj, name):
        """Find the module an object belong to."""
        module_name = getattr(obj, '__module__', None)
        if module_name is not None:
            return module_name
        # Protect the iteration by using a list copy of sys.modules against dynamic
        # modules that trigger imports of other modules upon calls to getattr.
        for module_name, module in list(sys.modules.items()):
            if module_name == '__main__' or module is None:
                continue
            try:
                if _getattribute(module, name)[0] is obj:
                    return module_name
            except AttributeError:
                pass
        return '__main__'

    def encode_long(x):
        r"""Encode a long to a two's complement little-endian binary string.
        Note that 0 is a special case, returning an empty string, to save a
        byte in the LONG1 pickling context.

        >>> encode_long(0)
        b''
        >>> encode_long(255)
        b'\xff\x00'
        >>> encode_long(32767)
        b'\xff\x7f'
        >>> encode_long(-256)
        b'\x00\xff'
        >>> encode_long(-32768)
        b'\x00\x80'
        >>> encode_long(-128)
        b'\x80'
        >>> encode_long(127)
        b'\x7f'
        >>>
        """
        if x == 0:
            return b''
        nbytes = (x.bit_length() >> 3) + 1
        result = x.to_bytes(nbytes, byteorder='little', signed=True)
        if x < 0 and nbytes > 1:
            if result[-1] == 0xff and (result[-2] & 0x80) != 0:
                result = result[:-1]
        return result

    def decode_long(data):
        r"""Decode a long from a two's complement little-endian binary string.

        >>> decode_long(b'')
        0
        >>> decode_long(b"\xff\x00")
        255
        >>> decode_long(b"\xff\x7f")
        32767
        >>> decode_long(b"\x00\xff")
        -256
        >>> decode_long(b"\x00\x80")
        -32768
        >>> decode_long(b"\x80")
        -128
        >>> decode_long(b"\x7f")
        127
        """
        return int.from_bytes(data, byteorder='little', signed=True)

    # Pickling machinery

    class _Pickler:

        def __init__(self, file, protocol=None, *, fix_imports=True,
                     buffer_callback=None):
            """This takes a binary file for writing a pickle data stream.

            The optional *protocol* argument tells the pickler to use the
            given protocol; supported protocols are 0, 1, 2, 3, 4 and 5.
            The default protocol is 4. It was introduced in Python 3.4, and
            is incompatible with previous versions.

            Specifying a negative protocol version selects the highest
            protocol version supported.  The higher the protocol used, the
            more recent the version of Python needed to read the pickle
            produced.

            The *file* argument must have a write() method that accepts a
            single bytes argument. It can thus be a file object opened for
            binary writing, an io.BytesIO instance, or any other custom
            object that meets this interface.

            If *fix_imports* is True and *protocol* is less than 3, pickle
            will try to map the new Python 3 names to the old module names
            used in Python 2, so that the pickle data stream is readable
            with Python 2.

            If *buffer_callback* is None (the default), buffer views are
            serialized into *file* as part of the pickle stream.

            If *buffer_callback* is not None, then it can be called any number
            of times with a buffer view.  If the callback returns a false value
            (such as None), the given buffer is out-of-band; otherwise the
            buffer is serialized in-band, i.e. inside the pickle stream.

            It is an error if *buffer_callback* is not None and *protocol*
            is None or smaller than 5.
            """
            if protocol is None:
                protocol = DEFAULT_PROTOCOL
            if protocol < 0:
                protocol = HIGHEST_PROTOCOL
            elif not 0 <= protocol <= HIGHEST_PROTOCOL:
                raise ValueError("pickle protocol must be <= %d" % HIGHEST_PROTOCOL)
            if buffer_callback is not None and protocol < 5:
                raise ValueError("buffer_callback needs protocol >= 5")
            self._buffer_callback = buffer_callback
            try:
                self._file_write = file.write
            except AttributeError:
                raise TypeError("file must have a 'write' attribute")
            self.framer = _Framer(self._file_write)
            self.write = self.framer.write
            self._write_large_bytes = self.framer.write_large_bytes
            self.memo = {}
            self.proto = int(protocol)
            self.bin = protocol >= 1
            self.fast = 0
            self.fix_imports = fix_imports and protocol < 3

        def clear_memo(self):
            """Clears the pickler's "memo".

            The memo is the data structure that remembers which objects the
            pickler has already seen, so that shared or recursive objects
            are pickled by reference and not by value.  This method is
            useful when re-using picklers.
            """
            self.memo.clear()

        def dump(self, obj):
            """Write a pickled representation of obj to the open file."""
            # Check whether Pickler was initialized correctly. This is
            # only needed to mimic the behavior of _pickle.Pickler.dump().
            if not hasattr(self, "_file_write"):
                raise PicklingError("Pickler.__init__() was not called by "
                                    "%s.__init__()" % (self.__class__.__name__,))
            if self.proto >= 2:
                self.write(PROTO + pack("<B", self.proto))
            if self.proto >= 4:
                self.framer.start_framing()
            self.save(obj)
            self.write(STOP)
            self.framer.end_framing()

        def memoize(self, obj):
            """Store an object in the memo."""

            # The Pickler memo is a dictionary mapping object ids to 2-tuples
            # that contain the Unpickler memo key and the object being memoized.
            # The memo key is written to the pickle and will become
            # the key in the Unpickler's memo.  The object is stored in the
            # Pickler memo so that transient objects are kept alive during
            # pickling.

            # The use of the Unpickler memo length as the memo key is just a
            # convention.  The only requirement is that the memo values be unique.
            # But there appears no advantage to any other scheme, and this
            # scheme allows the Unpickler memo to be implemented as a plain (but
            # growable) array, indexed by memo key.
            if self.fast:
                return
            assert id(obj) not in self.memo
            idx = len(self.memo)
            self.write(self.put(idx))
            self.memo[id(obj)] = idx, obj

        # Return a PUT (BINPUT, LONG_BINPUT) opcode string, with argument i.
        def put(self, idx):
            if self.proto >= 4:
                return MEMOIZE
            elif self.bin:
                if idx < 256:
                    return BINPUT + pack("<B", idx)
                else:
                    return LONG_BINPUT + pack("<I", idx)
            else:
                return PUT + repr(idx).encode("ascii") + b'\n'

        # Return a GET (BINGET, LONG_BINGET) opcode string, with argument i.
        def get(self, i):
            if self.bin:
                if i < 256:
                    return BINGET + pack("<B", i)
                else:
                    return LONG_BINGET + pack("<I", i)

            return GET + repr(i).encode("ascii") + b'\n'

        def save(self, obj, save_persistent_id=True):
            self.framer.commit_frame()

            # Check for persistent id (defined by a subclass)
            pid = self.persistent_id(obj)
            if pid is not None and save_persistent_id:
                self.save_pers(pid)
                return

            # Check the memo
            x = self.memo.get(id(obj))
            if x is not None:
                self.write(self.get(x[0]))
                return

            rv = NotImplemented
            reduce = getattr(self, "reducer_override", None)
            if reduce is not None:
                rv = reduce(obj)

            if rv is NotImplemented:
                # Check the type dispatch table
                t = type(obj)
                f = self.dispatch.get(t)
                if f is not None:
                    f(self, obj)  # Call unbound method with explicit self
                    return

                # Check private dispatch table if any, or else
                # copyreg.dispatch_table
                reduce = getattr(self, 'dispatch_table', dispatch_table).get(t)
                if reduce is not None:
                    rv = reduce(obj)
                else:
                    # Check for a class with a custom metaclass; treat as regular
                    # class
                    if issubclass(t, type):
                        self.save_global(obj)
                        return

                    # Check for a __reduce_ex__ method, fall back to __reduce__
                    reduce = getattr(obj, "__reduce_ex__", None)
                    if reduce is not None:
                        rv = reduce(self.proto)
                    else:
                        reduce = getattr(obj, "__reduce__", None)
                        if reduce is not None:
                            rv = reduce()
                        else:
                            raise PicklingError("Can't pickle %r object: %r" %
                                                (t.__name__, obj))

            # Check for string returned by reduce(), meaning "save as global"
            if isinstance(rv, str):
                self.save_global(obj, rv)
                return

            # Assert that reduce() returned a tuple
            if not isinstance(rv, tuple):
                raise PicklingError("%s must return string or tuple" % reduce)

            # Assert that it returned an appropriately sized tuple
            l = len(rv)
            if not (2 <= l <= 6):
                raise PicklingError("Tuple returned by %s must have "
                                    "two to six elements" % reduce)

            # Save the reduce() output and finally memoize the object
            self.save_reduce(obj=obj, *rv)

        def persistent_id(self, obj):
            # This exists so a subclass can override it
            return None

        def save_pers(self, pid):
            # Save a persistent id reference
            if self.bin:
                self.save(pid, save_persistent_id=False)
                self.write(BINPERSID)
            else:
                try:
                    self.write(PERSID + str(pid).encode("ascii") + b'\n')
                except UnicodeEncodeError:
                    raise PicklingError(
                        "persistent IDs in protocol 0 must be ASCII strings")

        def save_reduce(self, func, args, state=None, listitems=None,
                        dictitems=None, state_setter=None, obj=None):
            # This API is called by some subclasses

            if not isinstance(args, tuple):
                raise PicklingError("args from save_reduce() must be a tuple")
            if not callable(func):
                raise PicklingError("func from save_reduce() must be callable")

            save = self.save
            write = self.write

            func_name = getattr(func, "__name__", "")
            if self.proto >= 2 and func_name == "__newobj_ex__":
                cls, args, kwargs = args
                if not hasattr(cls, "__new__"):
                    raise PicklingError("args[0] from {} args has no __new__"
                                        .format(func_name))
                if obj is not None and cls is not obj.__class__:
                    raise PicklingError("args[0] from {} args has the wrong class"
                                        .format(func_name))
                if self.proto >= 4:
                    save(cls)
                    save(args)
                    save(kwargs)
                    write(NEWOBJ_EX)
                else:
                    func = partial(cls.__new__, cls, *args, **kwargs)
                    save(func)
                    save(())
                    write(REDUCE)
            elif self.proto >= 2 and func_name == "__newobj__":
                # A __reduce__ implementation can direct protocol 2 or newer to
                # use the more efficient NEWOBJ opcode, while still
                # allowing protocol 0 and 1 to work normally.  For this to
                # work, the function returned by __reduce__ should be
                # called __newobj__, and its first argument should be a
                # class.  The implementation for __newobj__
                # should be as follows, although pickle has no way to
                # verify this:
                #
                # def __newobj__(cls, *args):
                #     return cls.__new__(cls, *args)
                #
                # Protocols 0 and 1 will pickle a reference to __newobj__,
                # while protocol 2 (and above) will pickle a reference to
                # cls, the remaining args tuple, and the NEWOBJ code,
                # which calls cls.__new__(cls, *args) at unpickling time
                # (see load_newobj below).  If __reduce__ returns a
                # three-tuple, the state from the third tuple item will be
                # pickled regardless of the protocol, calling __setstate__
                # at unpickling time (see load_build below).
                #
                # Note that no standard __newobj__ implementation exists;
                # you have to provide your own.  This is to enforce
                # compatibility with Python 2.2 (pickles written using
                # protocol 0 or 1 in Python 2.3 should be unpicklable by
                # Python 2.2).
                cls = args[0]
                if not hasattr(cls, "__new__"):
                    raise PicklingError(
                        "args[0] from __newobj__ args has no __new__")
                if obj is not None and cls is not obj.__class__:
                    raise PicklingError(
                        "args[0] from __newobj__ args has the wrong class")
                args = args[1:]
                save(cls)
                save(args)
                write(NEWOBJ)
            else:
                save(func)
                save(args)
                write(REDUCE)

            if obj is not None:
                # If the object is already in the memo, this means it is
                # recursive. In this case, throw away everything we put on the
                # stack, and fetch the object back from the memo.
                if id(obj) in self.memo:
                    write(POP + self.get(self.memo[id(obj)][0]))
                else:
                    self.memoize(obj)

            # More new special cases (that work with older protocols as
            # well): when __reduce__ returns a tuple with 4 or 5 items,
            # the 4th and 5th item should be iterators that provide list
            # items and dict items (as (key, value) tuples), or None.

            if listitems is not None:
                self._batch_appends(listitems)

            if dictitems is not None:
                self._batch_setitems(dictitems)

            if state is not None:
                if state_setter is None:
                    save(state)
                    write(BUILD)
                else:
                    # If a state_setter is specified, call it instead of load_build
                    # to update obj's with its previous state.
                    # First, push state_setter and its tuple of expected arguments
                    # (obj, state) onto the stack.
                    save(state_setter)
                    save(obj)  # simple BINGET opcode as obj is already memoized.
                    save(state)
                    write(TUPLE2)
                    # Trigger a state_setter(obj, state) function call.
                    write(REDUCE)
                    # The purpose of state_setter is to carry-out an
                    # inplace modification of obj. We do not care about what the
                    # method might return, so its output is eventually removed from
                    # the stack.
                    write(POP)

        # Methods below this point are dispatched through the dispatch table

        dispatch = {}

        def save_none(self, obj):
            self.write(NONE)

        dispatch[type(None)] = save_none

        def save_bool(self, obj):
            if self.proto >= 2:
                self.write(NEWTRUE if obj else NEWFALSE)
            else:
                self.write(TRUE if obj else FALSE)

        dispatch[bool] = save_bool

        def save_long(self, obj):
            if self.bin:
                # If the int is small enough to fit in a signed 4-byte 2's-comp
                # format, we can store it more efficiently than the general
                # case.
                # First one- and two-byte unsigned ints:
                if obj >= 0:
                    if obj <= 0xff:
                        self.write(BININT1 + pack("<B", obj))
                        return
                    if obj <= 0xffff:
                        self.write(BININT2 + pack("<H", obj))
                        return
                # Next check for 4-byte signed ints:
                if -0x80000000 <= obj <= 0x7fffffff:
                    self.write(BININT + pack("<i", obj))
                    return
            if self.proto >= 2:
                encoded = encode_long(obj)
                n = len(encoded)
                if n < 256:
                    self.write(LONG1 + pack("<B", n) + encoded)
                else:
                    self.write(LONG4 + pack("<i", n) + encoded)
                return
            if -0x80000000 <= obj <= 0x7fffffff:
                self.write(INT + repr(obj).encode("ascii") + b'\n')
            else:
                self.write(LONG + repr(obj).encode("ascii") + b'L\n')

        dispatch[int] = save_long

        def save_float(self, obj):
            if self.bin:
                self.write(BINFLOAT + pack('>d', obj))
            else:
                self.write(FLOAT + repr(obj).encode("ascii") + b'\n')

        dispatch[float] = save_float

        def save_bytes(self, obj):
            if self.proto < 3:
                if not obj:  # bytes object is empty
                    self.save_reduce(bytes, (), obj=obj)
                else:
                    self.save_reduce(codecs.encode,
                                     (str(obj, 'latin1'), 'latin1'), obj=obj)
                return
            n = len(obj)
            if n <= 0xff:
                self.write(SHORT_BINBYTES + pack("<B", n) + obj)
            elif n > 0xffffffff and self.proto >= 4:
                self._write_large_bytes(BINBYTES8 + pack("<Q", n), obj)
            elif n >= self.framer._FRAME_SIZE_TARGET:
                self._write_large_bytes(BINBYTES + pack("<I", n), obj)
            else:
                self.write(BINBYTES + pack("<I", n) + obj)
            self.memoize(obj)

        dispatch[bytes] = save_bytes

        def save_bytearray(self, obj):
            if self.proto < 5:
                if not obj:  # bytearray is empty
                    self.save_reduce(bytearray, (), obj=obj)
                else:
                    self.save_reduce(bytearray, (bytes(obj),), obj=obj)
                return
            n = len(obj)
            if n >= self.framer._FRAME_SIZE_TARGET:
                self._write_large_bytes(BYTEARRAY8 + pack("<Q", n), obj)
            else:
                self.write(BYTEARRAY8 + pack("<Q", n) + obj)

        dispatch[bytearray] = save_bytearray

        if _HAVE_PICKLE_BUFFER:
            def save_picklebuffer(self, obj):
                if self.proto < 5:
                    raise PicklingError("PickleBuffer can only pickled with "
                                        "protocol >= 5")
                with obj.raw() as m:
                    if not m.contiguous:
                        raise PicklingError("PickleBuffer can not be pickled when "
                                            "pointing to a non-contiguous buffer")
                    in_band = True
                    if self._buffer_callback is not None:
                        in_band = bool(self._buffer_callback(obj))
                    if in_band:
                        # Write data in-band
                        # XXX The C implementation avoids a copy here
                        if m.readonly:
                            self.save_bytes(m.tobytes())
                        else:
                            self.save_bytearray(m.tobytes())
                    else:
                        # Write data out-of-band
                        self.write(NEXT_BUFFER)
                        if m.readonly:
                            self.write(READONLY_BUFFER)

            dispatch[PickleBuffer] = save_picklebuffer

        def save_str(self, obj):
            if self.bin:
                encoded = obj.encode('utf-8', 'surrogatepass')
                n = len(encoded)
                if n <= 0xff and self.proto >= 4:
                    self.write(SHORT_BINUNICODE + pack("<B", n) + encoded)
                elif n > 0xffffffff and self.proto >= 4:
                    self._write_large_bytes(BINUNICODE8 + pack("<Q", n), encoded)
                elif n >= self.framer._FRAME_SIZE_TARGET:
                    self._write_large_bytes(BINUNICODE + pack("<I", n), encoded)
                else:
                    self.write(BINUNICODE + pack("<I", n) + encoded)
            else:
                obj = obj.replace("\\", "\\u005c")
                obj = obj.replace("\0", "\\u0000")
                obj = obj.replace("\n", "\\u000a")
                obj = obj.replace("\r", "\\u000d")
                obj = obj.replace("\x1a", "\\u001a")  # EOF on DOS
                self.write(UNICODE + obj.encode('raw-unicode-escape') +
                           b'\n')
            self.memoize(obj)

        dispatch[str] = save_str

        def save_tuple(self, obj):
            if not obj:  # tuple is empty
                if self.bin:
                    self.write(EMPTY_TUPLE)
                else:
                    self.write(MARK + TUPLE)
                return

            n = len(obj)
            save = self.save
            memo = self.memo
            if n <= 3 and self.proto >= 2:
                for element in obj:
                    save(element)
                # Subtle.  Same as in the big comment below.
                if id(obj) in memo:
                    get = self.get(memo[id(obj)][0])
                    self.write(POP * n + get)
                else:
                    self.write(_tuplesize2code[n])
                    self.memoize(obj)
                return

            # proto 0 or proto 1 and tuple isn't empty, or proto > 1 and tuple
            # has more than 3 elements.
            write = self.write
            write(MARK)
            for element in obj:
                save(element)

            if id(obj) in memo:
                # Subtle.  d was not in memo when we entered save_tuple(), so
                # the process of saving the tuple's elements must have saved
                # the tuple itself:  the tuple is recursive.  The proper action
                # now is to throw away everything we put on the stack, and
                # simply GET the tuple (it's already constructed).  This check
                # could have been done in the "for element" loop instead, but
                # recursive tuples are a rare thing.
                get = self.get(memo[id(obj)][0])
                if self.bin:
                    write(POP_MARK + get)
                else:  # proto 0 -- POP_MARK not available
                    write(POP * (n + 1) + get)
                return

            # No recursion.
            write(TUPLE)
            self.memoize(obj)

        dispatch[tuple] = save_tuple

        def save_list(self, obj):
            if self.bin:
                self.write(EMPTY_LIST)
            else:  # proto 0 -- can't use EMPTY_LIST
                self.write(MARK + LIST)

            self.memoize(obj)
            self._batch_appends(obj)

        dispatch[list] = save_list

        _BATCHSIZE = 1000

        def _batch_appends(self, items):
            # Helper to batch up APPENDS sequences
            save = self.save
            write = self.write

            if not self.bin:
                for x in items:
                    save(x)
                    write(APPEND)
                return

            it = iter(items)
            while True:
                tmp = list(islice(it, self._BATCHSIZE))
                n = len(tmp)
                if n > 1:
                    write(MARK)
                    for x in tmp:
                        save(x)
                    write(APPENDS)
                elif n:
                    save(tmp[0])
                    write(APPEND)
                # else tmp is empty, and we're done
                if n < self._BATCHSIZE:
                    return

        def save_dict(self, obj):
            if self.bin:
                self.write(EMPTY_DICT)
            else:  # proto 0 -- can't use EMPTY_DICT
                self.write(MARK + DICT)

            self.memoize(obj)
            self._batch_setitems(obj.items())

        dispatch[dict] = save_dict
        if PyStringMap is not None:
            dispatch[PyStringMap] = save_dict

        def _batch_setitems(self, items):
            # Helper to batch up SETITEMS sequences; proto >= 1 only
            save = self.save
            write = self.write

            if not self.bin:
                for k, v in items:
                    save(k)
                    save(v)
                    write(SETITEM)
                return

            it = iter(items)
            while True:
                tmp = list(islice(it, self._BATCHSIZE))
                n = len(tmp)
                if n > 1:
                    write(MARK)
                    for k, v in tmp:
                        save(k)
                        save(v)
                    write(SETITEMS)
                elif n:
                    k, v = tmp[0]
                    save(k)
                    save(v)
                    write(SETITEM)
                # else tmp is empty, and we're done
                if n < self._BATCHSIZE:
                    return

        def save_set(self, obj):
            save = self.save
            write = self.write

            if self.proto < 4:
                self.save_reduce(set, (list(obj),), obj=obj)
                return

            write(EMPTY_SET)
            self.memoize(obj)

            it = iter(obj)
            while True:
                batch = list(islice(it, self._BATCHSIZE))
                n = len(batch)
                if n > 0:
                    write(MARK)
                    for item in batch:
                        save(item)
                    write(ADDITEMS)
                if n < self._BATCHSIZE:
                    return

        dispatch[set] = save_set

        def save_frozenset(self, obj):
            save = self.save
            write = self.write

            if self.proto < 4:
                self.save_reduce(frozenset, (list(obj),), obj=obj)
                return

            write(MARK)
            for item in obj:
                save(item)

            if id(obj) in self.memo:
                # If the object is already in the memo, this means it is
                # recursive. In this case, throw away everything we put on the
                # stack, and fetch the object back from the memo.
                write(POP_MARK + self.get(self.memo[id(obj)][0]))
                return

            write(FROZENSET)
            self.memoize(obj)

        dispatch[frozenset] = save_frozenset

        def save_global(self, obj, name=None):
            write = self.write
            memo = self.memo

            if name is None:
                name = getattr(obj, '__qualname__', None)
            if name is None:
                name = obj.__name__

            module_name = whichmodule(obj, name)
            try:
                __import__(module_name, level=0)
                module = sys.modules[module_name]
                obj2, parent = _getattribute(module, name)
            except (ImportError, KeyError, AttributeError):
                raise PicklingError(
                    "Can't pickle %r: it's not found as %s.%s" %
                    (obj, module_name, name)) from None
            else:
                if obj2 is not obj:
                    raise PicklingError(
                        "Can't pickle %r: it's not the same object as %s.%s" %
                        (obj, module_name, name))

            if self.proto >= 2:
                code = _extension_registry.get((module_name, name))
                if code:
                    assert code > 0
                    if code <= 0xff:
                        write(EXT1 + pack("<B", code))
                    elif code <= 0xffff:
                        write(EXT2 + pack("<H", code))
                    else:
                        write(EXT4 + pack("<i", code))
                    return
            lastname = name.rpartition('.')[2]
            if parent is module:
                name = lastname
            # Non-ASCII identifiers are supported only with protocols >= 3.
            if self.proto >= 4:
                self.save(module_name)
                self.save(name)
                write(STACK_GLOBAL)
            elif parent is not module:
                self.save_reduce(getattr, (parent, lastname))
            elif self.proto >= 3:
                write(GLOBAL + bytes(module_name, "utf-8") + b'\n' +
                      bytes(name, "utf-8") + b'\n')
            else:
                if self.fix_imports:
                    r_name_mapping = _compat_pickle.REVERSE_NAME_MAPPING
                    r_import_mapping = _compat_pickle.REVERSE_IMPORT_MAPPING
                    if (module_name, name) in r_name_mapping:
                        module_name, name = r_name_mapping[(module_name, name)]
                    elif module_name in r_import_mapping:
                        module_name = r_import_mapping[module_name]
                try:
                    write(GLOBAL + bytes(module_name, "ascii") + b'\n' +
                          bytes(name, "ascii") + b'\n')
                except UnicodeEncodeError:
                    raise PicklingError(
                        "can't pickle global identifier '%s.%s' using "
                        "pickle protocol %i" % (module, name, self.proto)) from None

            self.memoize(obj)

        def save_type(self, obj):
            if obj is type(None):
                return self.save_reduce(type, (None,), obj=obj)
            elif obj is type(NotImplemented):
                return self.save_reduce(type, (NotImplemented,), obj=obj)
            elif obj is type(...):
                return self.save_reduce(type, (...,), obj=obj)
            return self.save_global(obj)

        dispatch[FunctionType] = save_global
        dispatch[type] = save_type

    # Unpickling machinery

    class _Unpickler:

        def __init__(self, file, *, fix_imports=True,
                     encoding="ASCII", errors="strict", buffers=None):
            """This takes a binary file for reading a pickle data stream.

            The protocol version of the pickle is detected automatically, so
            no proto argument is needed.

            The argument *file* must have two methods, a read() method that
            takes an integer argument, and a readline() method that requires
            no arguments.  Both methods should return bytes.  Thus *file*
            can be a binary file object opened for reading, an io.BytesIO
            object, or any other custom object that meets this interface.

            The file-like object must have two methods, a read() method
            that takes an integer argument, and a readline() method that
            requires no arguments.  Both methods should return bytes.
            Thus file-like object can be a binary file object opened for
            reading, a BytesIO object, or any other custom object that
            meets this interface.

            If *buffers* is not None, it should be an iterable of buffer-enabled
            objects that is consumed each time the pickle stream references
            an out-of-band buffer view.  Such buffers have been given in order
            to the *buffer_callback* of a Pickler object.

            If *buffers* is None (the default), then the buffers are taken
            from the pickle stream, assuming they are serialized there.
            It is an error for *buffers* to be None if the pickle stream
            was produced with a non-None *buffer_callback*.

            Other optional arguments are *fix_imports*, *encoding* and
            *errors*, which are used to control compatibility support for
            pickle stream generated by Python 2.  If *fix_imports* is True,
            pickle will try to map the old Python 2 names to the new names
            used in Python 3.  The *encoding* and *errors* tell pickle how
            to decode 8-bit string instances pickled by Python 2; these
            default to 'ASCII' and 'strict', respectively. *encoding* can be
            'bytes' to read theses 8-bit string instances as bytes objects.
            """
            self._buffers = iter(buffers) if buffers is not None else None
            self._file_readline = file.readline
            self._file_read = file.read
            self.memo = {}
            self.encoding = encoding
            self.errors = errors
            self.proto = 0
            self.fix_imports = fix_imports

        def load(self):
            """Read a pickled object representation from the open file.

            Return the reconstituted object hierarchy specified in the file.
            """
            # Check whether Unpickler was initialized correctly. This is
            # only needed to mimic the behavior of _pickle.Unpickler.dump().
            if not hasattr(self, "_file_read"):
                raise UnpicklingError("Unpickler.__init__() was not called by "
                                      "%s.__init__()" % (self.__class__.__name__,))
            self._unframer = _Unframer(self._file_read, self._file_readline)
            self.read = self._unframer.read
            self.readinto = self._unframer.readinto
            self.readline = self._unframer.readline
            self.metastack = []
            self.stack = []
            self.append = self.stack.append
            self.proto = 0
            read = self.read
            dispatch = self.dispatch
            try:
                while True:
                    key = read(1)
                    if not key:
                        raise EOFError
                    assert isinstance(key, bytes_types)
                    dispatch[key[0]](self)
            except _Stop as stopinst:
                return stopinst.value

        # Return a list of items pushed in the stack after last MARK instruction.
        def pop_mark(self):
            items = self.stack
            self.stack = self.metastack.pop()
            self.append = self.stack.append
            return items

        def persistent_load(self, pid):
            raise UnpicklingError("unsupported persistent id encountered")

        dispatch = {}

        def load_proto(self):
            proto = self.read(1)[0]
            if not 0 <= proto <= HIGHEST_PROTOCOL:
                raise ValueError("unsupported pickle protocol: %d" % proto)
            self.proto = proto

        dispatch[PROTO[0]] = load_proto

        def load_frame(self):
            frame_size, = unpack('<Q', self.read(8))
            if frame_size > sys.maxsize:
                raise ValueError("frame size > sys.maxsize: %d" % frame_size)
            self._unframer.load_frame(frame_size)

        dispatch[FRAME[0]] = load_frame

        def load_persid(self):
            try:
                pid = self.readline()[:-1].decode("ascii")
            except UnicodeDecodeError:
                raise UnpicklingError(
                    "persistent IDs in protocol 0 must be ASCII strings")
            self.append(self.persistent_load(pid))

        dispatch[PERSID[0]] = load_persid

        def load_binpersid(self):
            pid = self.stack.pop()
            self.append(self.persistent_load(pid))

        dispatch[BINPERSID[0]] = load_binpersid

        def load_none(self):
            self.append(None)

        dispatch[NONE[0]] = load_none

        def load_false(self):
            self.append(False)

        dispatch[NEWFALSE[0]] = load_false

        def load_true(self):
            self.append(True)

        dispatch[NEWTRUE[0]] = load_true

        def load_int(self):
            data = self.readline()
            if data == FALSE[1:]:
                val = False
            elif data == TRUE[1:]:
                val = True
            else:
                val = int(data, 0)
            self.append(val)

        dispatch[INT[0]] = load_int

        def load_binint(self):
            self.append(unpack('<i', self.read(4))[0])

        dispatch[BININT[0]] = load_binint

        def load_binint1(self):
            self.append(self.read(1)[0])

        dispatch[BININT1[0]] = load_binint1

        def load_binint2(self):
            self.append(unpack('<H', self.read(2))[0])

        dispatch[BININT2[0]] = load_binint2

        def load_long(self):
            val = self.readline()[:-1]
            if val and val[-1] == b'L'[0]:
                val = val[:-1]
            self.append(int(val, 0))

        dispatch[LONG[0]] = load_long

        def load_long1(self):
            n = self.read(1)[0]
            data = self.read(n)
            self.append(decode_long(data))

        dispatch[LONG1[0]] = load_long1

        def load_long4(self):
            n, = unpack('<i', self.read(4))
            if n < 0:
                # Corrupt or hostile pickle -- we never write one like this
                raise UnpicklingError("LONG pickle has negative byte count")
            data = self.read(n)
            self.append(decode_long(data))

        dispatch[LONG4[0]] = load_long4

        def load_float(self):
            self.append(float(self.readline()[:-1]))

        dispatch[FLOAT[0]] = load_float

        def load_binfloat(self):
            self.append(unpack('>d', self.read(8))[0])

        dispatch[BINFLOAT[0]] = load_binfloat

        def _decode_string(self, value):
            # Used to allow strings from Python 2 to be decoded either as
            # bytes or Unicode strings.  This should be used only with the
            # STRING, BINSTRING and SHORT_BINSTRING opcodes.
            if self.encoding == "bytes":
                return value
            else:
                return value.decode(self.encoding, self.errors)

        def load_string(self):
            data = self.readline()[:-1]
            # Strip outermost quotes
            if len(data) >= 2 and data[0] == data[-1] and data[0] in b'"\'':
                data = data[1:-1]
            else:
                raise UnpicklingError("the STRING opcode argument must be quoted")
            self.append(self._decode_string(codecs.escape_decode(data)[0]))

        dispatch[STRING[0]] = load_string

        def load_binstring(self):
            # Deprecated BINSTRING uses signed 32-bit length
            len, = unpack('<i', self.read(4))
            if len < 0:
                raise UnpicklingError("BINSTRING pickle has negative byte count")
            data = self.read(len)
            self.append(self._decode_string(data))

        dispatch[BINSTRING[0]] = load_binstring

        def load_binbytes(self):
            len, = unpack('<I', self.read(4))
            if len > maxsize:
                raise UnpicklingError("BINBYTES exceeds system's maximum size "
                                      "of %d bytes" % maxsize)
            self.append(self.read(len))

        dispatch[BINBYTES[0]] = load_binbytes

        def load_unicode(self):
            self.append(str(self.readline()[:-1], 'raw-unicode-escape'))

        dispatch[UNICODE[0]] = load_unicode

        def load_binunicode(self):
            len, = unpack('<I', self.read(4))
            if len > maxsize:
                raise UnpicklingError("BINUNICODE exceeds system's maximum size "
                                      "of %d bytes" % maxsize)
            self.append(str(self.read(len), 'utf-8', 'surrogatepass'))

        dispatch[BINUNICODE[0]] = load_binunicode

        def load_binunicode8(self):
            len, = unpack('<Q', self.read(8))
            if len > maxsize:
                raise UnpicklingError("BINUNICODE8 exceeds system's maximum size "
                                      "of %d bytes" % maxsize)
            self.append(str(self.read(len), 'utf-8', 'surrogatepass'))

        dispatch[BINUNICODE8[0]] = load_binunicode8

        def load_binbytes8(self):
            len, = unpack('<Q', self.read(8))
            if len > maxsize:
                raise UnpicklingError("BINBYTES8 exceeds system's maximum size "
                                      "of %d bytes" % maxsize)
            self.append(self.read(len))

        dispatch[BINBYTES8[0]] = load_binbytes8

        def load_bytearray8(self):
            len, = unpack('<Q', self.read(8))
            if len > maxsize:
                raise UnpicklingError("BYTEARRAY8 exceeds system's maximum size "
                                      "of %d bytes" % maxsize)
            b = bytearray(len)
            self.readinto(b)
            self.append(b)

        dispatch[BYTEARRAY8[0]] = load_bytearray8

        def load_next_buffer(self):
            if self._buffers is None:
                raise UnpicklingError("pickle stream refers to out-of-band data "
                                      "but no *buffers* argument was given")
            try:
                buf = next(self._buffers)
            except StopIteration:
                raise UnpicklingError("not enough out-of-band buffers")
            self.append(buf)

        dispatch[NEXT_BUFFER[0]] = load_next_buffer

        def load_readonly_buffer(self):
            buf = self.stack[-1]
            with memoryview(buf) as m:
                if not m.readonly:
                    self.stack[-1] = m.toreadonly()

        dispatch[READONLY_BUFFER[0]] = load_readonly_buffer

        def load_short_binstring(self):
            len = self.read(1)[0]
            data = self.read(len)
            self.append(self._decode_string(data))

        dispatch[SHORT_BINSTRING[0]] = load_short_binstring

        def load_short_binbytes(self):
            len = self.read(1)[0]
            self.append(self.read(len))

        dispatch[SHORT_BINBYTES[0]] = load_short_binbytes

        def load_short_binunicode(self):
            len = self.read(1)[0]
            self.append(str(self.read(len), 'utf-8', 'surrogatepass'))

        dispatch[SHORT_BINUNICODE[0]] = load_short_binunicode

        def load_tuple(self):
            items = self.pop_mark()
            self.append(tuple(items))

        dispatch[TUPLE[0]] = load_tuple

        def load_empty_tuple(self):
            self.append(())

        dispatch[EMPTY_TUPLE[0]] = load_empty_tuple

        def load_tuple1(self):
            self.stack[-1] = (self.stack[-1],)

        dispatch[TUPLE1[0]] = load_tuple1

        def load_tuple2(self):
            self.stack[-2:] = [(self.stack[-2], self.stack[-1])]

        dispatch[TUPLE2[0]] = load_tuple2

        def load_tuple3(self):
            self.stack[-3:] = [(self.stack[-3], self.stack[-2], self.stack[-1])]

        dispatch[TUPLE3[0]] = load_tuple3

        def load_empty_list(self):
            self.append([])

        dispatch[EMPTY_LIST[0]] = load_empty_list

        def load_empty_dictionary(self):
            self.append({})

        dispatch[EMPTY_DICT[0]] = load_empty_dictionary

        def load_empty_set(self):
            self.append(set())

        dispatch[EMPTY_SET[0]] = load_empty_set

        def load_frozenset(self):
            items = self.pop_mark()
            self.append(frozenset(items))

        dispatch[FROZENSET[0]] = load_frozenset

        def load_list(self):
            items = self.pop_mark()
            self.append(items)

        dispatch[LIST[0]] = load_list

        def load_dict(self):
            items = self.pop_mark()
            d = {items[i]: items[i + 1]
                 for i in range(0, len(items), 2)}
            self.append(d)

        dispatch[DICT[0]] = load_dict

        # INST and OBJ differ only in how they get a class object.  It's not
        # only sensible to do the rest in a common routine, the two routines
        # previously diverged and grew different bugs.
        # klass is the class to instantiate, and k points to the topmost mark
        # object, following which are the arguments for klass.__init__.
        def _instantiate(self, klass, args):
            if (args or not isinstance(klass, type) or
                    hasattr(klass, "__getinitargs__")):
                try:
                    value = klass(*args)
                except TypeError as err:
                    raise TypeError("in constructor for %s: %s" %
                                    (klass.__name__, str(err)), sys.exc_info()[2])
            else:
                value = klass.__new__(klass)
            self.append(value)

        def load_inst(self):
            module = self.readline()[:-1].decode("ascii")
            name = self.readline()[:-1].decode("ascii")
            klass = self.find_class(module, name)
            self._instantiate(klass, self.pop_mark())

        dispatch[INST[0]] = load_inst

        def load_obj(self):
            # Stack is ... markobject classobject arg1 arg2 ...
            args = self.pop_mark()
            cls = args.pop(0)
            self._instantiate(cls, args)

        dispatch[OBJ[0]] = load_obj

        def load_newobj(self):
            args = self.stack.pop()
            cls = self.stack.pop()
            obj = cls.__new__(cls, *args)
            self.append(obj)

        dispatch[NEWOBJ[0]] = load_newobj

        def load_newobj_ex(self):
            kwargs = self.stack.pop()
            args = self.stack.pop()
            cls = self.stack.pop()
            obj = cls.__new__(cls, *args, **kwargs)
            self.append(obj)

        dispatch[NEWOBJ_EX[0]] = load_newobj_ex

        def load_global(self):
            module = self.readline()[:-1].decode("utf-8")
            name = self.readline()[:-1].decode("utf-8")
            klass = self.find_class(module, name)
            self.append(klass)

        dispatch[GLOBAL[0]] = load_global

        def load_stack_global(self):
            name = self.stack.pop()
            module = self.stack.pop()
            if type(name) is not str or type(module) is not str:
                raise UnpicklingError("STACK_GLOBAL requires str")
            self.append(self.find_class(module, name))

        dispatch[STACK_GLOBAL[0]] = load_stack_global

        def load_ext1(self):
            code = self.read(1)[0]
            self.get_extension(code)

        dispatch[EXT1[0]] = load_ext1

        def load_ext2(self):
            code, = unpack('<H', self.read(2))
            self.get_extension(code)

        dispatch[EXT2[0]] = load_ext2

        def load_ext4(self):
            code, = unpack('<i', self.read(4))
            self.get_extension(code)

        dispatch[EXT4[0]] = load_ext4

        def get_extension(self, code):
            nil = []
            obj = _extension_cache.get(code, nil)
            if obj is not nil:
                self.append(obj)
                return
            key = _inverted_registry.get(code)
            if not key:
                if code <= 0:  # note that 0 is forbidden
                    # Corrupt or hostile pickle.
                    raise UnpicklingError("EXT specifies code <= 0")
                raise ValueError("unregistered extension code %d" % code)
            obj = self.find_class(*key)
            _extension_cache[code] = obj
            self.append(obj)

        def find_class(self, module, name):
            # Subclasses may override this.
            sys.audit('pickle.find_class', module, name)
            if self.proto < 3 and self.fix_imports:
                if (module, name) in _compat_pickle.NAME_MAPPING:
                    module, name = _compat_pickle.NAME_MAPPING[(module, name)]
                elif module in _compat_pickle.IMPORT_MAPPING:
                    module = _compat_pickle.IMPORT_MAPPING[module]
            __import__(module, level=0)
            if self.proto >= 4:
                return _getattribute(sys.modules[module], name)[0]
            else:
                return getattr(sys.modules[module], name)

        def load_reduce(self):
            stack = self.stack
            args = stack.pop()
            func = stack[-1]
            stack[-1] = func(*args)

        dispatch[REDUCE[0]] = load_reduce

        def load_pop(self):
            if self.stack:
                del self.stack[-1]
            else:
                self.pop_mark()

        dispatch[POP[0]] = load_pop

        def load_pop_mark(self):
            self.pop_mark()

        dispatch[POP_MARK[0]] = load_pop_mark

        def load_dup(self):
            self.append(self.stack[-1])

        dispatch[DUP[0]] = load_dup

        def load_get(self):
            i = int(self.readline()[:-1])
            self.append(self.memo[i])

        dispatch[GET[0]] = load_get

        def load_binget(self):
            i = self.read(1)[0]
            self.append(self.memo[i])

        dispatch[BINGET[0]] = load_binget

        def load_long_binget(self):
            i, = unpack('<I', self.read(4))
            self.append(self.memo[i])

        dispatch[LONG_BINGET[0]] = load_long_binget

        def load_put(self):
            i = int(self.readline()[:-1])
            if i < 0:
                raise ValueError("negative PUT argument")
            self.memo[i] = self.stack[-1]

        dispatch[PUT[0]] = load_put

        def load_binput(self):
            i = self.read(1)[0]
            if i < 0:
                raise ValueError("negative BINPUT argument")
            self.memo[i] = self.stack[-1]

        dispatch[BINPUT[0]] = load_binput

        def load_long_binput(self):
            i, = unpack('<I', self.read(4))
            if i > maxsize:
                raise ValueError("negative LONG_BINPUT argument")
            self.memo[i] = self.stack[-1]

        dispatch[LONG_BINPUT[0]] = load_long_binput

        def load_memoize(self):
            memo = self.memo
            memo[len(memo)] = self.stack[-1]

        dispatch[MEMOIZE[0]] = load_memoize

        def load_append(self):
            stack = self.stack
            value = stack.pop()
            list = stack[-1]
            list.append(value)

        dispatch[APPEND[0]] = load_append

        def load_appends(self):
            items = self.pop_mark()
            list_obj = self.stack[-1]
            try:
                extend = list_obj.extend
            except AttributeError:
                pass
            else:
                extend(items)
                return
            # Even if the PEP 307 requires extend() and append() methods,
            # fall back on append() if the object has no extend() method
            # for backward compatibility.
            append = list_obj.append
            for item in items:
                append(item)

        dispatch[APPENDS[0]] = load_appends

        def load_setitem(self):
            stack = self.stack
            value = stack.pop()
            key = stack.pop()
            dict = stack[-1]
            dict[key] = value

        dispatch[SETITEM[0]] = load_setitem

        def load_setitems(self):
            items = self.pop_mark()
            dict = self.stack[-1]
            for i in range(0, len(items), 2):
                dict[items[i]] = items[i + 1]

        dispatch[SETITEMS[0]] = load_setitems

        def load_additems(self):
            items = self.pop_mark()
            set_obj = self.stack[-1]
            if isinstance(set_obj, set):
                set_obj.update(items)
            else:
                add = set_obj.add
                for item in items:
                    add(item)

        dispatch[ADDITEMS[0]] = load_additems

        def load_build(self):
            stack = self.stack
            state = stack.pop()
            inst = stack[-1]
            setstate = getattr(inst, "__setstate__", None)
            if setstate is not None:
                setstate(state)
                return
            slotstate = None
            if isinstance(state, tuple) and len(state) == 2:
                state, slotstate = state
            if state:
                inst_dict = inst.__dict__
                intern = sys.intern
                for k, v in state.items():
                    if type(k) is str:
                        inst_dict[intern(k)] = v
                    else:
                        inst_dict[k] = v
            if slotstate:
                for k, v in slotstate.items():
                    setattr(inst, k, v)

        dispatch[BUILD[0]] = load_build

        def load_mark(self):
            self.metastack.append(self.stack)
            self.stack = []
            self.append = self.stack.append

        dispatch[MARK[0]] = load_mark

        def load_stop(self):
            value = self.stack.pop()
            raise _Stop(value)

        dispatch[STOP[0]] = load_stop

    # Shorthands

    def _dump(obj, file, protocol=None, *, fix_imports=True, buffer_callback=None):
        _Pickler(file, protocol, fix_imports=fix_imports,
                 buffer_callback=buffer_callback).dump(obj)

    def _dumps(obj, protocol=None, *, fix_imports=True, buffer_callback=None):
        f = io.BytesIO()
        _Pickler(f, protocol, fix_imports=fix_imports,
                 buffer_callback=buffer_callback).dump(obj)
        res = f.getvalue()
        assert isinstance(res, bytes_types)
        return res

    def _load(file, *, fix_imports=True, encoding="ASCII", errors="strict",
              buffers=None):
        return _Unpickler(file, fix_imports=fix_imports, buffers=buffers,
                          encoding=encoding, errors=errors).load()

    def _loads(s, *, fix_imports=True, encoding="ASCII", errors="strict",
               buffers=None):
        if isinstance(s, str):
            raise TypeError("Can't load pickle from unicode string")
        file = io.BytesIO(s)
        return _Unpickler(file, fix_imports=fix_imports, buffers=buffers,
                          encoding=encoding, errors=errors).load()

    # Use the faster _pickle if possible
    try:
        from _pickle import (
            PickleError,
            PicklingError,
            UnpicklingError,
            Pickler,
            Unpickler,
            dump,
            dumps,
            load,
            loads
        )
    except ImportError:
        Pickler, Unpickler = _Pickler, _Unpickler
        dump, dumps, load, loads = _dump, _dumps, _load, _loads

    # Doctest
    def _test():
        import doctest
        return doctest.testmod()

    if __name__ == "__main__":
        import argparse
        parser = argparse.ArgumentParser(
            description='display contents of the pickle files')
        parser.add_argument(
            'pickle_file', type=argparse.FileType('br'),
            nargs='*', help='the pickle file')
        parser.add_argument(
            '-t', '--test', action='store_true',
            help='run self-test suite')
        parser.add_argument(
            '-v', action='store_true',
            help='run verbosely; only affects self-test run')
        args = parser.parse_args()
        if args.test:
            _test()
        else:
            if not args.pickle_file:
                parser.print_help()
            else:
                import pprint
                for f in args.pickle_file:
                    obj = load(f)
                    pprint.pprint(obj)


def jposix():
    # encoding: utf-8
    # module posix
    # from (built-in)
    # by generator 1.147
    """
    This module provides access to operating system functionality that is
    standardized by the C Standard and the POSIX standard (a thinly
    disguised Unix interface).  Refer to the library manual and
    corresponding Unix manual entries for more information on calls.
    """
    # no imports

    # Variables with simple values

    CLD_CONTINUED = 6
    CLD_DUMPED = 3
    CLD_EXITED = 1
    CLD_TRAPPED = 4

    EX_CANTCREAT = 73
    EX_CONFIG = 78
    EX_DATAERR = 65
    EX_IOERR = 74
    EX_NOHOST = 68
    EX_NOINPUT = 66
    EX_NOPERM = 77
    EX_NOUSER = 67
    EX_OK = 0
    EX_OSERR = 71
    EX_OSFILE = 72
    EX_PROTOCOL = 76
    EX_SOFTWARE = 70
    EX_TEMPFAIL = 75
    EX_UNAVAILABLE = 69
    EX_USAGE = 64

    F_LOCK = 1
    F_OK = 0
    F_TEST = 3
    F_TLOCK = 2
    F_ULOCK = 0

    NGROUPS_MAX = 65536

    O_ACCMODE = 3
    O_APPEND = 1024
    O_ASYNC = 8192
    O_CLOEXEC = 524288
    O_CREAT = 64
    O_DIRECT = 16384
    O_DIRECTORY = 65536
    O_DSYNC = 4096
    O_EXCL = 128
    O_LARGEFILE = 0
    O_NDELAY = 2048
    O_NOATIME = 262144
    O_NOCTTY = 256
    O_NOFOLLOW = 131072
    O_NONBLOCK = 2048
    O_RDONLY = 0
    O_RDWR = 2
    O_RSYNC = 1052672
    O_SYNC = 1052672
    O_TRUNC = 512
    O_WRONLY = 1

    POSIX_FADV_DONTNEED = 4
    POSIX_FADV_NOREUSE = 5
    POSIX_FADV_NORMAL = 0
    POSIX_FADV_RANDOM = 1
    POSIX_FADV_SEQUENTIAL = 2
    POSIX_FADV_WILLNEED = 3

    POSIX_SPAWN_CLOSE = 1
    POSIX_SPAWN_DUP2 = 2
    POSIX_SPAWN_OPEN = 0

    PRIO_PGRP = 1
    PRIO_PROCESS = 0
    PRIO_USER = 2

    P_ALL = 0
    P_PGID = 2
    P_PID = 1

    RTLD_DEEPBIND = 8
    RTLD_GLOBAL = 256
    RTLD_LAZY = 1
    RTLD_LOCAL = 0
    RTLD_NODELETE = 4096
    RTLD_NOLOAD = 4
    RTLD_NOW = 2

    R_OK = 4

    SCHED_BATCH = 3
    SCHED_FIFO = 1
    SCHED_IDLE = 5
    SCHED_OTHER = 0

    SCHED_RESET_ON_FORK = 1073741824

    SCHED_RR = 2

    ST_APPEND = 256
    ST_MANDLOCK = 64
    ST_NOATIME = 1024
    ST_NODEV = 4
    ST_NODIRATIME = 2048
    ST_NOEXEC = 8
    ST_NOSUID = 2
    ST_RDONLY = 1
    ST_RELATIME = 4096
    ST_SYNCHRONOUS = 16
    ST_WRITE = 128

    TMP_MAX = 238328

    WCONTINUED = 8

    WEXITED = 4

    WNOHANG = 1
    WNOWAIT = 16777216

    WSTOPPED = 2

    WUNTRACED = 2

    W_OK = 2

    XATTR_CREATE = 1
    XATTR_REPLACE = 2

    XATTR_SIZE_MAX = 65536

    X_OK = 1

    # functions

    def abort(*args, **kwargs):  # real signature unknown
        """
        Abort the interpreter immediately.

        This function 'dumps core' or otherwise fails in the hardest way possible
        on the hosting operating system.  This function never returns.
        """
        pass

    def access(*args, **kwargs):  # real signature unknown
        """
        Use the real uid/gid to test for access to a path.

          path
            Path to be tested; can be string, bytes, or a path-like object.
          mode
            Operating-system mode bitfield.  Can be F_OK to test existence,
            or the inclusive-OR of R_OK, W_OK, and X_OK.
          dir_fd
            If not None, it should be a file descriptor open to a directory,
            and path should be relative; path will then be relative to that
            directory.
          effective_ids
            If True, access will use the effective uid/gid instead of
            the real uid/gid.
          follow_symlinks
            If False, and the last element of the path is a symbolic link,
            access will examine the symbolic link itself instead of the file
            the link points to.

        dir_fd, effective_ids, and follow_symlinks may not be implemented
          on your platform.  If they are unavailable, using them will raise a
          NotImplementedError.

        Note that most operations will use the effective uid/gid, therefore this
          routine can be used in a suid/sgid environment to test if the invoking user
          has the specified access to the path.
        """
        pass

    def chdir(*args, **kwargs):  # real signature unknown
        """
        Change the current working directory to the specified path.

        path may always be specified as a string.
        On some platforms, path may also be specified as an open file descriptor.
          If this functionality is unavailable, using it raises an exception.
        """
        pass

    def chmod(*args, **kwargs):  # real signature unknown
        """
        Change the access permissions of a file.

          path
            Path to be modified.  May always be specified as a str, bytes, or a path-like object.
            On some platforms, path may also be specified as an open file descriptor.
            If this functionality is unavailable, using it raises an exception.
          mode
            Operating-system mode bitfield.
          dir_fd
            If not None, it should be a file descriptor open to a directory,
            and path should be relative; path will then be relative to that
            directory.
          follow_symlinks
            If False, and the last element of the path is a symbolic link,
            chmod will modify the symbolic link itself instead of the file
            the link points to.

        It is an error to use dir_fd or follow_symlinks when specifying path as
          an open file descriptor.
        dir_fd and follow_symlinks may not be implemented on your platform.
          If they are unavailable, using them will raise a NotImplementedError.
        """
        pass

    def chown(*args, **kwargs):  # real signature unknown
        """
        Change the owner and group id of path to the numeric uid and gid.\

          path
            Path to be examined; can be string, bytes, a path-like object, or open-file-descriptor int.
          dir_fd
            If not None, it should be a file descriptor open to a directory,
            and path should be relative; path will then be relative to that
            directory.
          follow_symlinks
            If False, and the last element of the path is a symbolic link,
            stat will examine the symbolic link itself instead of the file
            the link points to.

        path may always be specified as a string.
        On some platforms, path may also be specified as an open file descriptor.
          If this functionality is unavailable, using it raises an exception.
        If dir_fd is not None, it should be a file descriptor open to a directory,
          and path should be relative; path will then be relative to that directory.
        If follow_symlinks is False, and the last element of the path is a symbolic
          link, chown will modify the symbolic link itself instead of the file the
          link points to.
        It is an error to use dir_fd or follow_symlinks when specifying path as
          an open file descriptor.
        dir_fd and follow_symlinks may not be implemented on your platform.
          If they are unavailable, using them will raise a NotImplementedError.
        """
        pass

    def chroot(*args, **kwargs):  # real signature unknown
        """ Change root directory to path. """
        pass

    def close(*args, **kwargs):  # real signature unknown
        """ Close a file descriptor. """
        pass

    def closerange(*args, **kwargs):  # real signature unknown
        """ Closes all file descriptors in [fd_low, fd_high), ignoring errors. """
        pass

    def confstr(*args, **kwargs):  # real signature unknown
        """ Return a string-valued system configuration variable. """
        pass

    def cpu_count(*args, **kwargs):  # real signature unknown
        """
        Return the number of CPUs in the system; return None if indeterminable.

        This number is not equivalent to the number of CPUs the current process can
        use.  The number of usable CPUs can be obtained with
        ``len(os.sched_getaffinity(0))``
        """
        pass

    def ctermid(*args, **kwargs):  # real signature unknown
        """ Return the name of the controlling terminal for this process. """
        pass

    def device_encoding(*args, **kwargs):  # real signature unknown
        """
        Return a string describing the encoding of a terminal's file descriptor.

        The file descriptor must be attached to a terminal.
        If the device is not a terminal, return None.
        """
        pass

    def dup(*args, **kwargs):  # real signature unknown
        """ Return a duplicate of a file descriptor. """
        pass

    def dup2(*args, **kwargs):  # real signature unknown
        """ Duplicate file descriptor. """
        pass

    def execv(*args, **kwargs):  # real signature unknown
        """
        Execute an executable path with arguments, replacing current process.

          path
            Path of executable file.
          argv
            Tuple or list of strings.
        """
        pass

    def execve(*args, **kwargs):  # real signature unknown
        """
        Execute an executable path with arguments, replacing current process.

          path
            Path of executable file.
          argv
            Tuple or list of strings.
          env
            Dictionary of strings mapping to strings.
        """
        pass

    def fchdir(*args, **kwargs):  # real signature unknown
        """
        Change to the directory of the given file descriptor.

        fd must be opened on a directory, not a file.
        Equivalent to os.chdir(fd).
        """
        pass

    def fchmod(*args, **kwargs):  # real signature unknown
        """
        Change the access permissions of the file given by file descriptor fd.

        Equivalent to os.chmod(fd, mode).
        """
        pass

    def fchown(*args, **kwargs):  # real signature unknown
        """
        Change the owner and group id of the file specified by file descriptor.

        Equivalent to os.chown(fd, uid, gid).
        """
        pass

    def fdatasync(*args, **kwargs):  # real signature unknown
        """ Force write of fd to disk without forcing update of metadata. """
        pass

    def fork(*args, **kwargs):  # real signature unknown
        """
        Fork a child process.

        Return 0 to child process and PID of child to parent process.
        """
        pass

    def forkpty(*args, **kwargs):  # real signature unknown
        """
        Fork a new process with a new pseudo-terminal as controlling tty.

        Returns a tuple of (pid, master_fd).
        Like fork(), return pid of 0 to the child process,
        and pid of child to the parent process.
        To both, return fd of newly opened pseudo-terminal.
        """
        pass

    def fpathconf(*args, **kwargs):  # real signature unknown
        """
        Return the configuration limit name for the file descriptor fd.

        If there is no limit, return -1.
        """
        pass

    def fspath(*args, **kwargs):  # real signature unknown
        """
        Return the file system path representation of the object.

        If the object is str or bytes, then allow it to pass through as-is. If the
        object defines __fspath__(), then return the result of that method. All other
        types raise a TypeError.
        """
        pass

    def fstat(*args, **kwargs):  # real signature unknown
        """
        Perform a stat system call on the given file descriptor.

        Like stat(), but for an open file descriptor.
        Equivalent to os.stat(fd).
        """
        pass

    def fstatvfs(*args, **kwargs):  # real signature unknown
        """
        Perform an fstatvfs system call on the given fd.

        Equivalent to statvfs(fd).
        """
        pass

    def fsync(*args, **kwargs):  # real signature unknown
        """ Force write of fd to disk. """
        pass

    def ftruncate(*args, **kwargs):  # real signature unknown
        """ Truncate a file, specified by file descriptor, to a specific length. """
        pass

    def getcwd(*args, **kwargs):  # real signature unknown
        """ Return a unicode string representing the current working directory. """
        pass

    def getcwdb(*args, **kwargs):  # real signature unknown
        """ Return a bytes string representing the current working directory. """
        pass

    def getegid(*args, **kwargs):  # real signature unknown
        """ Return the current process's effective group id. """
        pass

    def geteuid(*args, **kwargs):  # real signature unknown
        """ Return the current process's effective user id. """
        pass

    def getgid(*args, **kwargs):  # real signature unknown
        """ Return the current process's group id. """
        pass

    def getgrouplist(user, group):  # real signature unknown; restored from __doc__
        """
        getgrouplist(user, group) -> list of groups to which a user belongs

        Returns a list of groups to which a user belongs.

            user: username to lookup
            group: base group id of the user
        """
        return []

    def getgroups(*args, **kwargs):  # real signature unknown
        """ Return list of supplemental group IDs for the process. """
        pass

    def getloadavg(*args, **kwargs):  # real signature unknown
        """
        Return average recent system load information.

        Return the number of processes in the system run queue averaged over
        the last 1, 5, and 15 minutes as a tuple of three floats.
        Raises OSError if the load average was unobtainable.
        """
        pass

    def getlogin(*args, **kwargs):  # real signature unknown
        """ Return the actual login name. """
        pass

    def getpgid():  # real signature unknown; restored from __doc__
        """ Call the system call getpgid(), and return the result. """
        pass

    def getpgrp(*args, **kwargs):  # real signature unknown
        """ Return the current process group id. """
        pass

    def getpid(*args, **kwargs):  # real signature unknown
        """ Return the current process id. """
        pass

    def getppid(*args, **kwargs):  # real signature unknown
        """
        Return the parent's process id.

        If the parent process has already exited, Windows machines will still
        return its id; others systems will return the id of the 'init' process (1).
        """
        pass

    def getpriority(*args, **kwargs):  # real signature unknown
        """ Return program scheduling priority. """
        pass

    def getresgid(*args, **kwargs):  # real signature unknown
        """ Return a tuple of the current process's real, effective, and saved group ids. """
        pass

    def getresuid(*args, **kwargs):  # real signature unknown
        """ Return a tuple of the current process's real, effective, and saved user ids. """
        pass

    def getsid(pid):  # real signature unknown; restored from __doc__
        """ Call the system call getsid(pid) and return the result. """
        pass

    def getuid(*args, **kwargs):  # real signature unknown
        """ Return the current process's user id. """
        pass

    def getxattr(*args, **kwargs):  # real signature unknown
        """
        Return the value of extended attribute attribute on path.

        path may be either a string, a path-like object, or an open file descriptor.
        If follow_symlinks is False, and the last element of the path is a symbolic
          link, getxattr will examine the symbolic link itself instead of the file
          the link points to.
        """
        pass

    def get_blocking(*args, **kwargs):  # real signature unknown
        """
        Get the blocking mode of the file descriptor.

        Return False if the O_NONBLOCK flag is set, True if the flag is cleared.
        """
        pass

    def get_inheritable(*args, **kwargs):  # real signature unknown
        """ Get the close-on-exe flag of the specified file descriptor. """
        pass

    def get_terminal_size(*args, **kwargs):  # real signature unknown
        """
        Return the size of the terminal window as (columns, lines).

        The optional argument fd (default standard output) specifies
        which file descriptor should be queried.

        If the file descriptor is not connected to a terminal, an OSError
        is thrown.

        This function will only be defined if an implementation is
        available for this system.

        shutil.get_terminal_size is the high-level function which should
        normally be used, os.get_terminal_size is the low-level implementation.
        """
        pass

    def initgroups(username, gid):  # real signature unknown; restored from __doc__
        """
        initgroups(username, gid) -> None

        Call the system initgroups() to initialize the group access list with all of
        the groups of which the specified username is a member, plus the specified
        group id.
        """
        pass

    def isatty(*args, **kwargs):  # real signature unknown
        """
        Return True if the fd is connected to a terminal.

        Return True if the file descriptor is an open file descriptor
        connected to the slave end of a terminal.
        """
        pass

    def kill(*args, **kwargs):  # real signature unknown
        """ Kill a process with a signal. """
        pass

    def killpg(*args, **kwargs):  # real signature unknown
        """ Kill a process group with a signal. """
        pass

    def lchown(*args, **kwargs):  # real signature unknown
        """
        Change the owner and group id of path to the numeric uid and gid.

        This function will not follow symbolic links.
        Equivalent to os.chown(path, uid, gid, follow_symlinks=False).
        """
        pass

    def link(*args, **kwargs):  # real signature unknown
        """
        Create a hard link to a file.

        If either src_dir_fd or dst_dir_fd is not None, it should be a file
          descriptor open to a directory, and the respective path string (src or dst)
          should be relative; the path will then be relative to that directory.
        If follow_symlinks is False, and the last element of src is a symbolic
          link, link will create a link to the symbolic link itself instead of the
          file the link points to.
        src_dir_fd, dst_dir_fd, and follow_symlinks may not be implemented on your
          platform.  If they are unavailable, using them will raise a
          NotImplementedError.
        """
        pass

    def listdir(*args, **kwargs):  # real signature unknown
        """
        Return a list containing the names of the files in the directory.

        path can be specified as either str, bytes, or a path-like object.  If path is bytes,
          the filenames returned will also be bytes; in all other circumstances
          the filenames returned will be str.
        If path is None, uses the path='.'.
        On some platforms, path may also be specified as an open file descriptor;\
          the file descriptor must refer to a directory.
          If this functionality is unavailable, using it raises NotImplementedError.

        The list is in arbitrary order.  It does not include the special
        entries '.' and '..' even if they are present in the directory.
        """
        pass

    def listxattr(*args, **kwargs):  # real signature unknown
        """
        Return a list of extended attributes on path.

        path may be either None, a string, a path-like object, or an open file descriptor.
        if path is None, listxattr will examine the current directory.
        If follow_symlinks is False, and the last element of the path is a symbolic
          link, listxattr will examine the symbolic link itself instead of the file
          the link points to.
        """
        pass

    def lockf(*args, **kwargs):  # real signature unknown
        """
        Apply, test or remove a POSIX lock on an open file descriptor.

          fd
            An open file descriptor.
          command
            One of F_LOCK, F_TLOCK, F_ULOCK or F_TEST.
          length
            The number of bytes to lock, starting at the current position.
        """
        pass

    def lseek(*args, **kwargs):  # real signature unknown
        """
        Set the position of a file descriptor.  Return the new position.

        Return the new cursor position in number of bytes
        relative to the beginning of the file.
        """
        pass

    def lstat(*args, **kwargs):  # real signature unknown
        """
        Perform a stat system call on the given path, without following symbolic links.

        Like stat(), but do not follow symbolic links.
        Equivalent to stat(path, follow_symlinks=False).
        """
        pass

    def major(*args, **kwargs):  # real signature unknown
        """ Extracts a device major number from a raw device number. """
        pass

    def makedev(*args, **kwargs):  # real signature unknown
        """ Composes a raw device number from the major and minor device numbers. """
        pass

    def minor(*args, **kwargs):  # real signature unknown
        """ Extracts a device minor number from a raw device number. """
        pass

    def mkdir(*args, **kwargs):  # real signature unknown
        """
        Create a directory.

        If dir_fd is not None, it should be a file descriptor open to a directory,
          and path should be relative; path will then be relative to that directory.
        dir_fd may not be implemented on your platform.
          If it is unavailable, using it will raise a NotImplementedError.

        The mode argument is ignored on Windows.
        """
        pass

    def mkfifo(*args, **kwargs):  # real signature unknown
        """
        Create a "fifo" (a POSIX named pipe).

        If dir_fd is not None, it should be a file descriptor open to a directory,
          and path should be relative; path will then be relative to that directory.
        dir_fd may not be implemented on your platform.
          If it is unavailable, using it will raise a NotImplementedError.
        """
        pass

    def mknod(*args, **kwargs):  # real signature unknown
        """
        Create a node in the file system.

        Create a node in the file system (file, device special file or named pipe)
        at path.  mode specifies both the permissions to use and the
        type of node to be created, being combined (bitwise OR) with one of
        S_IFREG, S_IFCHR, S_IFBLK, and S_IFIFO.  If S_IFCHR or S_IFBLK is set on mode,
        device defines the newly created device special file (probably using
        os.makedev()).  Otherwise device is ignored.

        If dir_fd is not None, it should be a file descriptor open to a directory,
          and path should be relative; path will then be relative to that directory.
        dir_fd may not be implemented on your platform.
          If it is unavailable, using it will raise a NotImplementedError.
        """
        pass

    def nice(*args, **kwargs):  # real signature unknown
        """ Add increment to the priority of process and return the new priority. """
        pass

    def open(*args, **kwargs):  # real signature unknown
        """
        Open a file for low level IO.  Returns a file descriptor (integer).

        If dir_fd is not None, it should be a file descriptor open to a directory,
          and path should be relative; path will then be relative to that directory.
        dir_fd may not be implemented on your platform.
          If it is unavailable, using it will raise a NotImplementedError.
        """
        pass

    def openpty(*args, **kwargs):  # real signature unknown
        """
        Open a pseudo-terminal.

        Return a tuple of (master_fd, slave_fd) containing open file descriptors
        for both the master and slave ends.
        """
        pass

    def pathconf(*args, **kwargs):  # real signature unknown
        """
        Return the configuration limit name for the file or directory path.

        If there is no limit, return -1.
        On some platforms, path may also be specified as an open file descriptor.
          If this functionality is unavailable, using it raises an exception.
        """
        pass

    def pipe(*args, **kwargs):  # real signature unknown
        """
        Create a pipe.

        Returns a tuple of two file descriptors:
          (read_fd, write_fd)
        """
        pass

    def pipe2(*args, **kwargs):  # real signature unknown
        """
        Create a pipe with flags set atomically.

        Returns a tuple of two file descriptors:
          (read_fd, write_fd)

        flags can be constructed by ORing together one or more of these values:
        O_NONBLOCK, O_CLOEXEC.
        """
        pass

    def posix_fadvise(*args, **kwargs):  # real signature unknown
        """
        Announce an intention to access data in a specific pattern.

        Announce an intention to access data in a specific pattern, thus allowing
        the kernel to make optimizations.
        The advice applies to the region of the file specified by fd starting at
        offset and continuing for length bytes.
        advice is one of POSIX_FADV_NORMAL, POSIX_FADV_SEQUENTIAL,
        POSIX_FADV_RANDOM, POSIX_FADV_NOREUSE, POSIX_FADV_WILLNEED, or
        POSIX_FADV_DONTNEED.
        """
        pass

    def posix_fallocate(*args, **kwargs):  # real signature unknown
        """
        Ensure a file has allocated at least a particular number of bytes on disk.

        Ensure that the file specified by fd encompasses a range of bytes
        starting at offset bytes from the beginning and continuing for length bytes.
        """
        pass

    def posix_spawn(*args, **kwargs):  # real signature unknown
        """
        Execute the program specified by path in a new process.

          path
            Path of executable file.
          argv
            Tuple or list of strings.
          env
            Dictionary of strings mapping to strings.
          file_actions
            A sequence of file action tuples.
          setpgroup
            The pgroup to use with the POSIX_SPAWN_SETPGROUP flag.
          resetids
            If the value is `true` the POSIX_SPAWN_RESETIDS will be activated.
          setsid
            If the value is `true` the POSIX_SPAWN_SETSID or POSIX_SPAWN_SETSID_NP will be activated.
          setsigmask
            The sigmask to use with the POSIX_SPAWN_SETSIGMASK flag.
          setsigdef
            The sigmask to use with the POSIX_SPAWN_SETSIGDEF flag.
          scheduler
            A tuple with the scheduler policy (optional) and parameters.
        """
        pass

    def posix_spawnp(*args, **kwargs):  # real signature unknown
        """
        Execute the program specified by path in a new process.

          path
            Path of executable file.
          argv
            Tuple or list of strings.
          env
            Dictionary of strings mapping to strings.
          file_actions
            A sequence of file action tuples.
          setpgroup
            The pgroup to use with the POSIX_SPAWN_SETPGROUP flag.
          resetids
            If the value is `True` the POSIX_SPAWN_RESETIDS will be activated.
          setsid
            If the value is `True` the POSIX_SPAWN_SETSID or POSIX_SPAWN_SETSID_NP will be activated.
          setsigmask
            The sigmask to use with the POSIX_SPAWN_SETSIGMASK flag.
          setsigdef
            The sigmask to use with the POSIX_SPAWN_SETSIGDEF flag.
          scheduler
            A tuple with the scheduler policy (optional) and parameters.
        """
        pass

    def pread(*args, **kwargs):  # real signature unknown
        """
        Read a number of bytes from a file descriptor starting at a particular offset.

        Read length bytes from file descriptor fd, starting at offset bytes from
        the beginning of the file.  The file offset remains unchanged.
        """
        pass

    def preadv(*args, **kwargs):  # real signature unknown
        """
        Reads from a file descriptor into a number of mutable bytes-like objects.

        Combines the functionality of readv() and pread(). As readv(), it will
        transfer data into each buffer until it is full and then move on to the next
        buffer in the sequence to hold the rest of the data. Its fourth argument,
        specifies the file offset at which the input operation is to be performed. It
        will return the total number of bytes read (which can be less than the total
        capacity of all the objects).

        The flags argument contains a bitwise OR of zero or more of the following flags:

        - RWF_HIPRI
        - RWF_NOWAIT

        Using non-zero flags requires Linux 4.6 or newer.
        """
        pass

    def putenv(*args, **kwargs):  # real signature unknown
        """ Change or add an environment variable. """
        pass

    def pwrite(*args, **kwargs):  # real signature unknown
        """
        Write bytes to a file descriptor starting at a particular offset.

        Write buffer to fd, starting at offset bytes from the beginning of
        the file.  Returns the number of bytes writte.  Does not change the
        current file offset.
        """
        pass

    def pwritev(*args, **kwargs):  # real signature unknown
        """
        Writes the contents of bytes-like objects to a file descriptor at a given offset.

        Combines the functionality of writev() and pwrite(). All buffers must be a sequence
        of bytes-like objects. Buffers are processed in array order. Entire contents of first
        buffer is written before proceeding to second, and so on. The operating system may
        set a limit (sysconf() value SC_IOV_MAX) on the number of buffers that can be used.
        This function writes the contents of each object to the file descriptor and returns
        the total number of bytes written.

        The flags argument contains a bitwise OR of zero or more of the following flags:

        - RWF_DSYNC
        - RWF_SYNC

        Using non-zero flags requires Linux 4.7 or newer.
        """
        pass

    def read(*args, **kwargs):  # real signature unknown
        """ Read from a file descriptor.  Returns a bytes object. """
        pass

    def readlink(*args, **kwargs):  # real signature unknown
        """
        Return a string representing the path to which the symbolic link points.

        If dir_fd is not None, it should be a file descriptor open to a directory,
        and path should be relative; path will then be relative to that directory.

        dir_fd may not be implemented on your platform.  If it is unavailable,
        using it will raise a NotImplementedError.
        """
        pass

    def readv(*args, **kwargs):  # real signature unknown
        """
        Read from a file descriptor fd into an iterable of buffers.

        The buffers should be mutable buffers accepting bytes.
        readv will transfer data into each buffer until it is full
        and then move on to the next buffer in the sequence to hold
        the rest of the data.

        readv returns the total number of bytes read,
        which may be less than the total capacity of all the buffers.
        """
        pass

    def register_at_fork(*args, **kwargs):  # real signature unknown
        """
        Register callables to be called when forking a new process.

          before
            A callable to be called in the parent before the fork() syscall.
          after_in_child
            A callable to be called in the child after fork().
          after_in_parent
            A callable to be called in the parent after fork().

        'before' callbacks are called in reverse order.
        'after_in_child' and 'after_in_parent' callbacks are called in order.
        """
        pass

    def remove(*args, **kwargs):  # real signature unknown
        """
        Remove a file (same as unlink()).

        If dir_fd is not None, it should be a file descriptor open to a directory,
          and path should be relative; path will then be relative to that directory.
        dir_fd may not be implemented on your platform.
          If it is unavailable, using it will raise a NotImplementedError.
        """
        pass

    def removexattr(*args, **kwargs):  # real signature unknown
        """
        Remove extended attribute attribute on path.

        path may be either a string, a path-like object, or an open file descriptor.
        If follow_symlinks is False, and the last element of the path is a symbolic
          link, removexattr will modify the symbolic link itself instead of the file
          the link points to.
        """
        pass

    def rename(*args, **kwargs):  # real signature unknown
        """
        Rename a file or directory.

        If either src_dir_fd or dst_dir_fd is not None, it should be a file
          descriptor open to a directory, and the respective path string (src or dst)
          should be relative; the path will then be relative to that directory.
        src_dir_fd and dst_dir_fd, may not be implemented on your platform.
          If they are unavailable, using them will raise a NotImplementedError.
        """
        pass

    def replace(*args, **kwargs):  # real signature unknown
        """
        Rename a file or directory, overwriting the destination.

        If either src_dir_fd or dst_dir_fd is not None, it should be a file
          descriptor open to a directory, and the respective path string (src or dst)
          should be relative; the path will then be relative to that directory.
        src_dir_fd and dst_dir_fd, may not be implemented on your platform.
          If they are unavailable, using them will raise a NotImplementedError.
        """
        pass

    def rmdir(*args, **kwargs):  # real signature unknown
        """
        Remove a directory.

        If dir_fd is not None, it should be a file descriptor open to a directory,
          and path should be relative; path will then be relative to that directory.
        dir_fd may not be implemented on your platform.
          If it is unavailable, using it will raise a NotImplementedError.
        """
        pass

    def scandir(*args, **kwargs):  # real signature unknown
        """
        Return an iterator of DirEntry objects for given path.

        path can be specified as either str, bytes, or a path-like object.  If path
        is bytes, the names of yielded DirEntry objects will also be bytes; in
        all other circumstances they will be str.

        If path is None, uses the path='.'.
        """
        pass

    def sched_getaffinity(*args, **kwargs):  # real signature unknown
        """
        Return the affinity of the process identified by pid (or the current process if zero).

        The affinity is returned as a set of CPU identifiers.
        """
        pass

    def sched_getparam(*args, **kwargs):  # real signature unknown
        """
        Returns scheduling parameters for the process identified by pid.

        If pid is 0, returns parameters for the calling process.
        Return value is an instance of sched_param.
        """
        pass

    def sched_getscheduler(*args, **kwargs):  # real signature unknown
        """
        Get the scheduling policy for the process identifiedy by pid.

        Passing 0 for pid returns the scheduling policy for the calling process.
        """
        pass

    def sched_get_priority_max(*args, **kwargs):  # real signature unknown
        """ Get the maximum scheduling priority for policy. """
        pass

    def sched_get_priority_min(*args, **kwargs):  # real signature unknown
        """ Get the minimum scheduling priority for policy. """
        pass

    def sched_rr_get_interval(*args, **kwargs):  # real signature unknown
        """
        Return the round-robin quantum for the process identified by pid, in seconds.

        Value returned is a float.
        """
        pass

    def sched_setaffinity(*args, **kwargs):  # real signature unknown
        """
        Set the CPU affinity of the process identified by pid to mask.

        mask should be an iterable of integers identifying CPUs.
        """
        pass

    def sched_setparam(*args, **kwargs):  # real signature unknown
        """
        Set scheduling parameters for the process identified by pid.

        If pid is 0, sets parameters for the calling process.
        param should be an instance of sched_param.
        """
        pass

    def sched_setscheduler(*args, **kwargs):  # real signature unknown
        """
        Set the scheduling policy for the process identified by pid.

        If pid is 0, the calling process is changed.
        param is an instance of sched_param.
        """
        pass

    def sched_yield(*args, **kwargs):  # real signature unknown
        """ Voluntarily relinquish the CPU. """
        pass

    def sendfile(out, in_, offset, count):  # real signature unknown; restored from __doc__
        """
        sendfile(out, in, offset, count) -> byteswritten
        sendfile(out, in, offset, count[, headers][, trailers], flags=0)
                    -> byteswritten
        Copy count bytes from file descriptor in to file descriptor out.
        """
        pass

    def setegid(*args, **kwargs):  # real signature unknown
        """ Set the current process's effective group id. """
        pass

    def seteuid(*args, **kwargs):  # real signature unknown
        """ Set the current process's effective user id. """
        pass

    def setgid(*args, **kwargs):  # real signature unknown
        """ Set the current process's group id. """
        pass

    def setgroups(*args, **kwargs):  # real signature unknown
        """ Set the groups of the current process to list. """
        pass

    def setpgid(pid, pgrp):  # real signature unknown; restored from __doc__
        """ Call the system call setpgid(pid, pgrp). """
        pass

    def setpgrp(*args, **kwargs):  # real signature unknown
        """ Make the current process the leader of its process group. """
        pass

    def setpriority(*args, **kwargs):  # real signature unknown
        """ Set program scheduling priority. """
        pass

    def setregid(*args, **kwargs):  # real signature unknown
        """ Set the current process's real and effective group ids. """
        pass

    def setresgid(*args, **kwargs):  # real signature unknown
        """ Set the current process's real, effective, and saved group ids. """
        pass

    def setresuid(*args, **kwargs):  # real signature unknown
        """ Set the current process's real, effective, and saved user ids. """
        pass

    def setreuid(*args, **kwargs):  # real signature unknown
        """ Set the current process's real and effective user ids. """
        pass

    def setsid():  # real signature unknown; restored from __doc__
        """ Call the system call setsid(). """
        pass

    def setuid(*args, **kwargs):  # real signature unknown
        """ Set the current process's user id. """
        pass

    def setxattr(*args, **kwargs):  # real signature unknown
        """
        Set extended attribute attribute on path to value.

        path may be either a string, a path-like object,  or an open file descriptor.
        If follow_symlinks is False, and the last element of the path is a symbolic
          link, setxattr will modify the symbolic link itself instead of the file
          the link points to.
        """
        pass

    def set_blocking(*args, **kwargs):  # real signature unknown
        """
        Set the blocking mode of the specified file descriptor.

        Set the O_NONBLOCK flag if blocking is False,
        clear the O_NONBLOCK flag otherwise.
        """
        pass

    def set_inheritable(*args, **kwargs):  # real signature unknown
        """ Set the inheritable flag of the specified file descriptor. """
        pass

    def stat(*args, **kwargs):  # real signature unknown
        """
        Perform a stat system call on the given path.

          path
            Path to be examined; can be string, bytes, a path-like object or
            open-file-descriptor int.
          dir_fd
            If not None, it should be a file descriptor open to a directory,
            and path should be a relative string; path will then be relative to
            that directory.
          follow_symlinks
            If False, and the last element of the path is a symbolic link,
            stat will examine the symbolic link itself instead of the file
            the link points to.

        dir_fd and follow_symlinks may not be implemented
          on your platform.  If they are unavailable, using them will raise a
          NotImplementedError.

        It's an error to use dir_fd or follow_symlinks when specifying path as
          an open file descriptor.
        """
        pass

    def statvfs(*args, **kwargs):  # real signature unknown
        """
        Perform a statvfs system call on the given path.

        path may always be specified as a string.
        On some platforms, path may also be specified as an open file descriptor.
          If this functionality is unavailable, using it raises an exception.
        """
        pass

    def strerror(*args, **kwargs):  # real signature unknown
        """ Translate an error code to a message string. """
        pass

    def symlink(*args, **kwargs):  # real signature unknown
        """
        Create a symbolic link pointing to src named dst.

        target_is_directory is required on Windows if the target is to be
          interpreted as a directory.  (On Windows, symlink requires
          Windows 6.0 or greater, and raises a NotImplementedError otherwise.)
          target_is_directory is ignored on non-Windows platforms.

        If dir_fd is not None, it should be a file descriptor open to a directory,
          and path should be relative; path will then be relative to that directory.
        dir_fd may not be implemented on your platform.
          If it is unavailable, using it will raise a NotImplementedError.
        """
        pass

    def sync(*args, **kwargs):  # real signature unknown
        """ Force write of everything to disk. """
        pass

    def sysconf(*args, **kwargs):  # real signature unknown
        """ Return an integer-valued system configuration variable. """
        pass

    def system(*args, **kwargs):  # real signature unknown
        """ Execute the command in a subshell. """
        pass

    def tcgetpgrp(*args, **kwargs):  # real signature unknown
        """ Return the process group associated with the terminal specified by fd. """
        pass

    def tcsetpgrp(*args, **kwargs):  # real signature unknown
        """ Set the process group associated with the terminal specified by fd. """
        pass

    def times(*args, **kwargs):  # real signature unknown
        """
        Return a collection containing process timing information.

        The object returned behaves like a named tuple with these fields:
          (utime, stime, cutime, cstime, elapsed_time)
        All fields are floating point numbers.
        """
        pass

    def truncate(*args, **kwargs):  # real signature unknown
        """
        Truncate a file, specified by path, to a specific length.

        On some platforms, path may also be specified as an open file descriptor.
          If this functionality is unavailable, using it raises an exception.
        """
        pass

    def ttyname(*args, **kwargs):  # real signature unknown
        """
        Return the name of the terminal device connected to 'fd'.

          fd
            Integer file descriptor handle.
        """
        pass

    def umask(*args, **kwargs):  # real signature unknown
        """ Set the current numeric umask and return the previous umask. """
        pass

    def uname(*args, **kwargs):  # real signature unknown
        """
        Return an object identifying the current operating system.

        The object behaves like a named tuple with the following fields:
          (sysname, nodename, release, version, machine)
        """
        pass

    def unlink(*args, **kwargs):  # real signature unknown
        """
        Remove a file (same as remove()).

        If dir_fd is not None, it should be a file descriptor open to a directory,
          and path should be relative; path will then be relative to that directory.
        dir_fd may not be implemented on your platform.
          If it is unavailable, using it will raise a NotImplementedError.
        """
        pass

    def unsetenv(*args, **kwargs):  # real signature unknown
        """ Delete an environment variable. """
        pass

    def urandom(*args, **kwargs):  # real signature unknown
        """ Return a bytes object containing random bytes suitable for cryptographic use. """
        pass

    def utime(*args, **kwargs):  # real signature unknown
        """
        Set the access and modified time of path.

        path may always be specified as a string.
        On some platforms, path may also be specified as an open file descriptor.
          If this functionality is unavailable, using it raises an exception.

        If times is not None, it must be a tuple (atime, mtime);
            atime and mtime should be expressed as float seconds since the epoch.
        If ns is specified, it must be a tuple (atime_ns, mtime_ns);
            atime_ns and mtime_ns should be expressed as integer nanoseconds
            since the epoch.
        If times is None and ns is unspecified, utime uses the current time.
        Specifying tuples for both times and ns is an error.

        If dir_fd is not None, it should be a file descriptor open to a directory,
          and path should be relative; path will then be relative to that directory.
        If follow_symlinks is False, and the last element of the path is a symbolic
          link, utime will modify the symbolic link itself instead of the file the
          link points to.
        It is an error to use dir_fd or follow_symlinks when specifying path
          as an open file descriptor.
        dir_fd and follow_symlinks may not be available on your platform.
          If they are unavailable, using them will raise a NotImplementedError.
        """
        pass

    def wait(*args, **kwargs):  # real signature unknown
        """
        Wait for completion of a child process.

        Returns a tuple of information about the child process:
            (pid, status)
        """
        pass

    def wait3(*args, **kwargs):  # real signature unknown
        """
        Wait for completion of a child process.

        Returns a tuple of information about the child process:
          (pid, status, rusage)
        """
        pass

    def wait4(*args, **kwargs):  # real signature unknown
        """
        Wait for completion of a specific child process.

        Returns a tuple of information about the child process:
          (pid, status, rusage)
        """
        pass

    def waitid(*args, **kwargs):  # real signature unknown
        """
        Returns the result of waiting for a process or processes.

          idtype
            Must be one of be P_PID, P_PGID or P_ALL.
          id
            The id to wait on.
          options
            Constructed from the ORing of one or more of WEXITED, WSTOPPED
            or WCONTINUED and additionally may be ORed with WNOHANG or WNOWAIT.

        Returns either waitid_result or None if WNOHANG is specified and there are
        no children in a waitable state.
        """
        pass

    def waitpid(*args, **kwargs):  # real signature unknown
        """
        Wait for completion of a given child process.

        Returns a tuple of information regarding the child process:
            (pid, status)

        The options argument is ignored on Windows.
        """
        pass

    def WCOREDUMP(*args, **kwargs):  # real signature unknown
        """ Return True if the process returning status was dumped to a core file. """
        pass

    def WEXITSTATUS(*args, **kwargs):  # real signature unknown
        """ Return the process return code from status. """
        pass

    def WIFCONTINUED(*args, **kwargs):  # real signature unknown
        """
        Return True if a particular process was continued from a job control stop.

        Return True if the process returning status was continued from a
        job control stop.
        """
        pass

    def WIFEXITED(*args, **kwargs):  # real signature unknown
        """ Return True if the process returning status exited via the exit() system call. """
        pass

    def WIFSIGNALED(*args, **kwargs):  # real signature unknown
        """ Return True if the process returning status was terminated by a signal. """
        pass

    def WIFSTOPPED(*args, **kwargs):  # real signature unknown
        """ Return True if the process returning status was stopped. """
        pass

    def write(*args, **kwargs):  # real signature unknown
        """ Write a bytes object to a file descriptor. """
        pass

    def writev(*args, **kwargs):  # real signature unknown
        """
        Iterate over buffers, and write the contents of each to a file descriptor.

        Returns the total number of bytes written.
        buffers must be a sequence of bytes-like objects.
        """
        pass

    def WSTOPSIG(*args, **kwargs):  # real signature unknown
        """ Return the signal that stopped the process that provided the status value. """
        pass

    def WTERMSIG(*args, **kwargs):  # real signature unknown
        """ Return the signal that terminated the process that provided the status value. """
        pass

    def _exit(*args, **kwargs):  # real signature unknown
        """ Exit to the system with specified status, without normal exit processing. """
        pass

    # classes

    class DirEntry(object):
        # no doc
        def inode(self, *args, **kwargs):  # real signature unknown
            """ Return inode of the entry; cached per entry. """
            pass

        def is_dir(self, *args, **kwargs):  # real signature unknown
            """ Return True if the entry is a directory; cached per entry. """
            pass

        def is_file(self, *args, **kwargs):  # real signature unknown
            """ Return True if the entry is a file; cached per entry. """
            pass

        def is_symlink(self, *args, **kwargs):  # real signature unknown
            """ Return True if the entry is a symbolic link; cached per entry. """
            pass

        def stat(self, *args, **kwargs):  # real signature unknown
            """ Return stat_result object for the entry; cached per entry. """
            pass

        def __fspath__(self, *args, **kwargs):  # real signature unknown
            """ Returns the path for the entry. """
            pass

        def __init__(self, *args, **kwargs):  # real signature unknown
            pass

        def __repr__(self, *args, **kwargs):  # real signature unknown
            """ Return repr(self). """
            pass

        name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
        """the entry's base filename, relative to scandir() "path" argument"""

        path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
        """the entry's full path name; equivalent to os.path.join(scandir_path, entry.name)"""

    class error(Exception):
        """ Base class for I/O related errors. """

        def __init__(self, *args, **kwargs):  # real signature unknown
            pass

        @staticmethod  # known case of __new__
        def __new__(*args, **kwargs):  # real signature unknown
            """ Create and return a new object.  See help(type) for accurate signature. """
            pass

        def __reduce__(self, *args, **kwargs):  # real signature unknown
            pass

        def __str__(self, *args, **kwargs):  # real signature unknown
            """ Return str(self). """
            pass

        characters_written = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

        errno = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
        """POSIX exception code"""

        filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
        """exception filename"""

        filename2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
        """second exception filename"""

        strerror = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
        """exception strerror"""

    class sched_param(tuple):
        """
        Current has only one field: sched_priority");

          sched_priority
            A scheduling parameter.
        """

        def __init__(self, *args, **kwargs):  # real signature unknown
            pass

        @staticmethod  # known case of __new__
        def __new__(*args, **kwargs):  # real signature unknown
            """ Create and return a new object.  See help(type) for accurate signature. """
            pass

        def __reduce__(self, *args, **kwargs):  # real signature unknown
            pass

        def __repr__(self, *args, **kwargs):  # real signature unknown
            """ Return repr(self). """
            pass

        sched_priority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
        """the scheduling priority"""

        n_fields = 1
        n_sequence_fields = 1
        n_unnamed_fields = 0

    class statvfs_result(tuple):
        """
        statvfs_result: Result from statvfs or fstatvfs.

        This object may be accessed either as a tuple of
          (bsize, frsize, blocks, bfree, bavail, files, ffree, favail, flag, namemax),
        or via the attributes f_bsize, f_frsize, f_blocks, f_bfree, and so on.

        See os.statvfs for more information.
        """

        def __init__(self, *args, **kwargs):  # real signature unknown
            pass

        @staticmethod  # known case of __new__
        def __new__(*args, **kwargs):  # real signature unknown
            """ Create and return a new object.  See help(type) for accurate signature. """
            pass

        def __reduce__(self, *args, **kwargs):  # real signature unknown
            pass

        def __repr__(self, *args, **kwargs):  # real signature unknown
            """ Return repr(self). """
            pass

        f_bavail = property(lambda self: 0)
        """:type: int"""

        f_bfree = property(lambda self: 0)
        """:type: int"""

        f_blocks = property(lambda self: 0)
        """:type: int"""

        f_bsize = property(lambda self: 0)
        """:type: int"""

        f_favail = property(lambda self: 0)
        """:type: int"""

        f_ffree = property(lambda self: 0)
        """:type: int"""

        f_files = property(lambda self: 0)
        """:type: int"""

        f_flag = property(lambda self: 0)
        """:type: int"""

        f_frsize = property(lambda self: 0)
        """:type: int"""

        f_fsid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

        f_namemax = property(lambda self: 0)
        """:type: int"""

        n_fields = 11
        n_sequence_fields = 10
        n_unnamed_fields = 0

    class stat_result(tuple):
        """
        stat_result: Result from stat, fstat, or lstat.

        This object may be accessed either as a tuple of
          (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime)
        or via the attributes st_mode, st_ino, st_dev, st_nlink, st_uid, and so on.

        Posix/windows: If your platform supports st_blksize, st_blocks, st_rdev,
        or st_flags, they are available as attributes only.

        See os.stat for more information.
        """

        def __init__(self, *args, **kwargs):  # real signature unknown
            pass

        @staticmethod  # known case of __new__
        def __new__(*args, **kwargs):  # real signature unknown
            """ Create and return a new object.  See help(type) for accurate signature. """
            pass

        def __reduce__(self, *args, **kwargs):  # real signature unknown
            pass

        def __repr__(self, *args, **kwargs):  # real signature unknown
            """ Return repr(self). """
            pass

        st_atime = property(lambda self: 0)
        """time of last access

        :type: int
        """

        st_atime_ns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
        """time of last access in nanoseconds"""

        st_blksize = property(lambda self: 0)
        """blocksize for filesystem I/O

        :type: int
        """

        st_blocks = property(lambda self: 0)
        """number of blocks allocated

        :type: int
        """

        st_ctime = property(lambda self: 0)
        """time of last change

        :type: int
        """

        st_ctime_ns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
        """time of last change in nanoseconds"""

        st_dev = property(lambda self: 0)
        """device

        :type: int
        """

        st_gid = property(lambda self: 0)
        """group ID of owner

        :type: int
        """

        st_ino = property(lambda self: 0)
        """inode

        :type: int
        """

        st_mode = property(lambda self: 0)
        """protection bits

        :type: int
        """

        st_mtime = property(lambda self: 0)
        """time of last modification

        :type: int
        """

        st_mtime_ns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
        """time of last modification in nanoseconds"""

        st_nlink = property(lambda self: 0)
        """number of hard links

        :type: int
        """

        st_rdev = property(lambda self: 0)
        """device type (if inode device)

        :type: int
        """

        st_size = property(lambda self: 0)
        """total size, in bytes

        :type: int
        """

        st_uid = property(lambda self: 0)
        """user ID of owner

        :type: int
        """

        n_fields = 19
        n_sequence_fields = 10
        n_unnamed_fields = 3

    class terminal_size(tuple):
        """ A tuple of (columns, lines) for holding terminal window size """

        def __init__(self, *args, **kwargs):  # real signature unknown
            pass

        @staticmethod  # known case of __new__
        def __new__(*args, **kwargs):  # real signature unknown
            """ Create and return a new object.  See help(type) for accurate signature. """
            pass

        def __reduce__(self, *args, **kwargs):  # real signature unknown
            pass

        def __repr__(self, *args, **kwargs):  # real signature unknown
            """ Return repr(self). """
            pass

        columns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
        """width of the terminal window in characters"""

        lines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
        """height of the terminal window in characters"""

        n_fields = 2
        n_sequence_fields = 2
        n_unnamed_fields = 0

    class times_result(tuple):
        """
        times_result: Result from os.times().

        This object may be accessed either as a tuple of
          (user, system, children_user, children_system, elapsed),
        or via the attributes user, system, children_user, children_system,
        and elapsed.

        See os.times for more information.
        """

        def __init__(self, *args, **kwargs):  # real signature unknown
            pass

        @staticmethod  # known case of __new__
        def __new__(*args, **kwargs):  # real signature unknown
            """ Create and return a new object.  See help(type) for accurate signature. """
            pass

        def __reduce__(self, *args, **kwargs):  # real signature unknown
            pass

        def __repr__(self, *args, **kwargs):  # real signature unknown
            """ Return repr(self). """
            pass

        children_system = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
        """system time of children"""

        children_user = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
        """user time of children"""

        elapsed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
        """elapsed time since an arbitrary point in the past"""

        system = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
        """system time"""

        user = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
        """user time"""

        n_fields = 5
        n_sequence_fields = 5
        n_unnamed_fields = 0

    class uname_result(tuple):
        """
        uname_result: Result from os.uname().

        This object may be accessed either as a tuple of
          (sysname, nodename, release, version, machine),
        or via the attributes sysname, nodename, release, version, and machine.

        See os.uname for more information.
        """

        def __init__(self, *args, **kwargs):  # real signature unknown
            pass

        @staticmethod  # known case of __new__
        def __new__(*args, **kwargs):  # real signature unknown
            """ Create and return a new object.  See help(type) for accurate signature. """
            pass

        def __reduce__(self, *args, **kwargs):  # real signature unknown
            pass

        def __repr__(self, *args, **kwargs):  # real signature unknown
            """ Return repr(self). """
            pass

        machine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
        """hardware identifier"""

        nodename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
        """name of machine on network (implementation-defined)"""

        release = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
        """operating system release"""

        sysname = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
        """operating system name"""

        version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
        """operating system version"""

        n_fields = 5
        n_sequence_fields = 5
        n_unnamed_fields = 0

    class waitid_result(tuple):
        """
        waitid_result: Result from waitid.

        This object may be accessed either as a tuple of
          (si_pid, si_uid, si_signo, si_status, si_code),
        or via the attributes si_pid, si_uid, and so on.

        See os.waitid for more information.
        """

        def __init__(self, *args, **kwargs):  # real signature unknown
            pass

        @staticmethod  # known case of __new__
        def __new__(*args, **kwargs):  # real signature unknown
            """ Create and return a new object.  See help(type) for accurate signature. """
            pass

        def __reduce__(self, *args, **kwargs):  # real signature unknown
            pass

        def __repr__(self, *args, **kwargs):  # real signature unknown
            """ Return repr(self). """
            pass

        si_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

        si_pid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

        si_signo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

        si_status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

        si_uid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

        n_fields = 5
        n_sequence_fields = 5
        n_unnamed_fields = 0

    class __loader__(object):
        """
        Meta path import for built-in modules.

            All methods are either class or static methods to avoid the need to
            instantiate the class.
        """

        @classmethod
        def create_module(cls, *args, **kwargs):  # real signature unknown
            """ Create a built-in module """
            pass

        @classmethod
        def exec_module(cls, *args, **kwargs):  # real signature unknown
            """ Exec a built-in module """
            pass

        @classmethod
        def find_module(cls, *args, **kwargs):  # real signature unknown
            """
            Find the built-in module.

                    If 'path' is ever specified then the search is considered a failure.

                    This method is deprecated.  Use find_spec() instead.
            """
            pass

        @classmethod
        def find_spec(cls, *args, **kwargs):  # real signature unknown
            pass

        @classmethod
        def get_code(cls, *args, **kwargs):  # real signature unknown
            """ Return None as built-in modules do not have code objects. """
            pass

        @classmethod
        def get_source(cls, *args, **kwargs):  # real signature unknown
            """ Return None as built-in modules do not have source code. """
            pass

        @classmethod
        def is_package(cls, *args, **kwargs):  # real signature unknown
            """ Return False as built-in modules are never packages. """
            pass

        @classmethod
        def load_module(cls, *args, **kwargs):  # real signature unknown
            """
            Load the specified module into sys.modules and return it.

                This method is deprecated.  Use loader.exec_module instead.
            """
            pass

        def module_repr(module):  # reliably restored by inspect
            """
            Return repr for the module.

                    The method is deprecated.  The import machinery does the job itself.
            """
            pass

        def __init__(self, *args, **kwargs):  # real signature unknown
            pass

        __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
        """list of weak references to the object (if defined)"""

        __dict__ = None  # (!) real value is "mappingproxy({'__module__': '_frozen_importlib', '__doc__': 'Meta path import for built-in modules.\\n\\n    All methods are either class or static methods to avoid the need to\\n    instantiate the class.\\n\\n    ', 'module_repr': <staticmethod object at 0x7f5ae0fac430>, 'find_spec': <classmethod object at 0x7f5ae0fac460>, 'find_module': <classmethod object at 0x7f5ae0fac490>, 'create_module': <classmethod object at 0x7f5ae0fac4c0>, 'exec_module': <classmethod object at 0x7f5ae0fac4f0>, 'get_code': <classmethod object at 0x7f5ae0fac580>, 'get_source': <classmethod object at 0x7f5ae0fac610>, 'is_package': <classmethod object at 0x7f5ae0fac6a0>, 'load_module': <classmethod object at 0x7f5ae0fac6d0>, '__dict__': <attribute '__dict__' of 'BuiltinImporter' objects>, '__weakref__': <attribute '__weakref__' of 'BuiltinImporter' objects>})"

    # variables with complex values

    confstr_names = {
        'CS_GNU_LIBC_VERSION': 2,
        'CS_GNU_LIBPTHREAD_VERSION': 3,
        'CS_LFS64_CFLAGS': 1004,
        'CS_LFS64_LDFLAGS': 1005,
        'CS_LFS64_LIBS': 1006,
        'CS_LFS64_LINTFLAGS': 1007,
        'CS_LFS_CFLAGS': 1000,
        'CS_LFS_LDFLAGS': 1001,
        'CS_LFS_LIBS': 1002,
        'CS_LFS_LINTFLAGS': 1003,
        'CS_PATH': 0,
        'CS_XBS5_ILP32_OFF32_CFLAGS': 1100,
        'CS_XBS5_ILP32_OFF32_LDFLAGS': 1101,
        'CS_XBS5_ILP32_OFF32_LIBS': 1102,
        'CS_XBS5_ILP32_OFF32_LINTFLAGS': 1103,
        'CS_XBS5_ILP32_OFFBIG_CFLAGS': 1104,
        'CS_XBS5_ILP32_OFFBIG_LDFLAGS': 1105,
        'CS_XBS5_ILP32_OFFBIG_LIBS': 1106,
        'CS_XBS5_ILP32_OFFBIG_LINTFLAGS': 1107,
        'CS_XBS5_LP64_OFF64_CFLAGS': 1108,
        'CS_XBS5_LP64_OFF64_LDFLAGS': 1109,
        'CS_XBS5_LP64_OFF64_LIBS': 1110,
        'CS_XBS5_LP64_OFF64_LINTFLAGS': 1111,
        'CS_XBS5_LPBIG_OFFBIG_CFLAGS': 1112,
        'CS_XBS5_LPBIG_OFFBIG_LDFLAGS': 1113,
        'CS_XBS5_LPBIG_OFFBIG_LIBS': 1114,
        'CS_XBS5_LPBIG_OFFBIG_LINTFLAGS': 1115,
    }

    environ = {}  # real value of type <class 'dict'> skipped

    pathconf_names = {
        'PC_ALLOC_SIZE_MIN': 18,
        'PC_ASYNC_IO': 10,
        'PC_CHOWN_RESTRICTED': 6,
        'PC_FILESIZEBITS': 13,
        'PC_LINK_MAX': 0,
        'PC_MAX_CANON': 1,
        'PC_MAX_INPUT': 2,
        'PC_NAME_MAX': 3,
        'PC_NO_TRUNC': 7,
        'PC_PATH_MAX': 4,
        'PC_PIPE_BUF': 5,
        'PC_PRIO_IO': 11,
        'PC_REC_INCR_XFER_SIZE': 14,
        'PC_REC_MAX_XFER_SIZE': 15,
        'PC_REC_MIN_XFER_SIZE': 16,
        'PC_REC_XFER_ALIGN': 17,
        'PC_SOCK_MAXBUF': 12,
        'PC_SYMLINK_MAX': 19,
        'PC_SYNC_IO': 9,
        'PC_VDISABLE': 8,
    }

    sysconf_names = {
        'SC_2_CHAR_TERM': 95,
        'SC_2_C_BIND': 47,
        'SC_2_C_DEV': 48,
        'SC_2_C_VERSION': 96,
        'SC_2_FORT_DEV': 49,
        'SC_2_FORT_RUN': 50,
        'SC_2_LOCALEDEF': 52,
        'SC_2_SW_DEV': 51,
        'SC_2_UPE': 97,
        'SC_2_VERSION': 46,
        'SC_AIO_LISTIO_MAX': 23,
        'SC_AIO_MAX': 24,
        'SC_AIO_PRIO_DELTA_MAX': 25,
        'SC_ARG_MAX': 0,
        'SC_ASYNCHRONOUS_IO': 12,
        'SC_ATEXIT_MAX': 87,
        'SC_AVPHYS_PAGES': 86,
        'SC_BC_BASE_MAX': 36,
        'SC_BC_DIM_MAX': 37,
        'SC_BC_SCALE_MAX': 38,
        'SC_BC_STRING_MAX': 39,
        'SC_CHARCLASS_NAME_MAX': 45,
        'SC_CHAR_BIT': 101,
        'SC_CHAR_MAX': 102,
        'SC_CHAR_MIN': 103,
        'SC_CHILD_MAX': 1,
        'SC_CLK_TCK': 2,
        'SC_COLL_WEIGHTS_MAX': 40,
        'SC_DELAYTIMER_MAX': 26,
        'SC_EQUIV_CLASS_MAX': 41,
        'SC_EXPR_NEST_MAX': 42,
        'SC_FSYNC': 15,
        'SC_GETGR_R_SIZE_MAX': 69,
        'SC_GETPW_R_SIZE_MAX': 70,
        'SC_INT_MAX': 104,
        'SC_INT_MIN': 105,
        'SC_IOV_MAX': 60,
        'SC_JOB_CONTROL': 7,
        'SC_LINE_MAX': 43,
        'SC_LOGIN_NAME_MAX': 71,
        'SC_LONG_BIT': 106,
        'SC_MAPPED_FILES': 16,
        'SC_MB_LEN_MAX': 108,
        'SC_MEMLOCK': 17,
        'SC_MEMLOCK_RANGE': 18,
        'SC_MEMORY_PROTECTION': 19,
        'SC_MESSAGE_PASSING': 20,
        'SC_MQ_OPEN_MAX': 27,
        'SC_MQ_PRIO_MAX': 28,
        'SC_NGROUPS_MAX': 3,
        'SC_NL_ARGMAX': 119,
        'SC_NL_LANGMAX': 120,
        'SC_NL_MSGMAX': 121,
        'SC_NL_NMAX': 122,
        'SC_NL_SETMAX': 123,
        'SC_NL_TEXTMAX': 124,
        'SC_NPROCESSORS_CONF': 83,
        'SC_NPROCESSORS_ONLN': 84,
        'SC_NZERO': 109,
        'SC_OPEN_MAX': 4,
        'SC_PAGESIZE': 30,
        'SC_PAGE_SIZE': 30,
        'SC_PASS_MAX': 88,
        'SC_PHYS_PAGES': 85,
        'SC_PII': 53,
        'SC_PII_INTERNET': 56,
        'SC_PII_INTERNET_DGRAM': 62,
        'SC_PII_INTERNET_STREAM': 61,
        'SC_PII_OSI': 57,
        'SC_PII_OSI_CLTS': 64,
        'SC_PII_OSI_COTS': 63,
        'SC_PII_OSI_M': 65,
        'SC_PII_SOCKET': 55,
        'SC_PII_XTI': 54,
        'SC_POLL': 58,
        'SC_PRIORITIZED_IO': 13,
        'SC_PRIORITY_SCHEDULING': 10,
        'SC_REALTIME_SIGNALS': 9,
        'SC_RE_DUP_MAX': 44,
        'SC_RTSIG_MAX': 31,
        'SC_SAVED_IDS': 8,
        'SC_SCHAR_MAX': 111,
        'SC_SCHAR_MIN': 112,
        'SC_SELECT': 59,
        'SC_SEMAPHORES': 21,
        'SC_SEM_NSEMS_MAX': 32,
        'SC_SEM_VALUE_MAX': 33,
        'SC_SHARED_MEMORY_OBJECTS': 22,
        'SC_SHRT_MAX': 113,
        'SC_SHRT_MIN': 114,
        'SC_SIGQUEUE_MAX': 34,
        'SC_SSIZE_MAX': 110,
        'SC_STREAM_MAX': 5,
        'SC_SYNCHRONIZED_IO': 14,
        'SC_THREADS': 67,
        'SC_THREAD_ATTR_STACKADDR': 77,
        'SC_THREAD_ATTR_STACKSIZE': 78,
        'SC_THREAD_DESTRUCTOR_ITERATIONS': 73,
        'SC_THREAD_KEYS_MAX': 74,
        'SC_THREAD_PRIORITY_SCHEDULING': 79,
        'SC_THREAD_PRIO_INHERIT': 80,
        'SC_THREAD_PRIO_PROTECT': 81,
        'SC_THREAD_PROCESS_SHARED': 82,
        'SC_THREAD_SAFE_FUNCTIONS': 68,
        'SC_THREAD_STACK_MIN': 75,
        'SC_THREAD_THREADS_MAX': 76,
        'SC_TIMERS': 11,
        'SC_TIMER_MAX': 35,
        'SC_TTY_NAME_MAX': 72,
        'SC_TZNAME_MAX': 6,
        'SC_T_IOV_MAX': 66,
        'SC_UCHAR_MAX': 115,
        'SC_UINT_MAX': 116,
        'SC_UIO_MAXIOV': 60,
        'SC_ULONG_MAX': 117,
        'SC_USHRT_MAX': 118,
        'SC_VERSION': 29,
        'SC_WORD_BIT': 107,
        'SC_XBS5_ILP32_OFF32': 125,
        'SC_XBS5_ILP32_OFFBIG': 126,
        'SC_XBS5_LP64_OFF64': 127,
        'SC_XBS5_LPBIG_OFFBIG': 128,
        'SC_XOPEN_CRYPT': 92,
        'SC_XOPEN_ENH_I18N': 93,
        'SC_XOPEN_LEGACY': 129,
        'SC_XOPEN_REALTIME': 130,
        'SC_XOPEN_REALTIME_THREADS': 131,
        'SC_XOPEN_SHM': 94,
        'SC_XOPEN_UNIX': 91,
        'SC_XOPEN_VERSION': 89,
        'SC_XOPEN_XCU_VERSION': 90,
        'SC_XOPEN_XPG2': 98,
        'SC_XOPEN_XPG3': 99,
        'SC_XOPEN_XPG4': 100,
    }

    _have_functions = [
        'HAVE_FACCESSAT',
        'HAVE_FCHDIR',
        'HAVE_FCHMOD',
        'HAVE_FCHMODAT',
        'HAVE_FCHOWN',
        'HAVE_FCHOWNAT',
        'HAVE_FEXECVE',
        'HAVE_FDOPENDIR',
        'HAVE_FPATHCONF',
        'HAVE_FSTATAT',
        'HAVE_FSTATVFS',
        'HAVE_FTRUNCATE',
        'HAVE_FUTIMENS',
        'HAVE_FUTIMES',
        'HAVE_FUTIMESAT',
        'HAVE_LINKAT',
        'HAVE_LCHOWN',
        'HAVE_LSTAT',
        'HAVE_LUTIMES',
        'HAVE_MKDIRAT',
        'HAVE_MKFIFOAT',
        'HAVE_MKNODAT',
        'HAVE_OPENAT',
        'HAVE_READLINKAT',
        'HAVE_RENAMEAT',
        'HAVE_SYMLINKAT',
        'HAVE_UNLINKAT',
        'HAVE_UTIMENSAT',
    ]

    __spec__ = None  # (!) real value is "ModuleSpec(name='posix', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"


def jcollections_abs():
    # Copyright 2007 Google, Inc. All Rights Reserved.
    # Licensed to PSF under a Contributor Agreement.

    """Abstract Base Classes (ABCs) for collections, according to PEP 3119.

    Unit tests are in test_collections.
    """

    from abc import ABCMeta, abstractmethod
    import sys

    __all__ = ["Awaitable", "Coroutine",
               "AsyncIterable", "AsyncIterator", "AsyncGenerator",
               "Hashable", "Iterable", "Iterator", "Generator", "Reversible",
               "Sized", "Container", "Callable", "Collection",
               "Set", "MutableSet",
               "Mapping", "MutableMapping",
               "MappingView", "KeysView", "ItemsView", "ValuesView",
               "Sequence", "MutableSequence",
               "ByteString",
               ]

    # This module has been renamed from collections.abc to _collections_abc to
    # speed up interpreter startup. Some of the types such as MutableMapping are
    # required early but collections module imports a lot of other modules.
    # See issue #19218
    __name__ = "collections.abc"

    # Private list of types that we want to register with the various ABCs
    # so that they will pass tests like:
    #       it = iter(somebytearray)
    #       assert isinstance(it, Iterable)
    # Note:  in other implementations, these types might not be distinct
    # and they may have their own implementation specific types that
    # are not included on this list.
    bytes_iterator = type(iter(b''))
    bytearray_iterator = type(iter(bytearray()))
    # callable_iterator = ???
    dict_keyiterator = type(iter({}.keys()))
    dict_valueiterator = type(iter({}.values()))
    dict_itemiterator = type(iter({}.items()))
    list_iterator = type(iter([]))
    list_reverseiterator = type(iter(reversed([])))
    range_iterator = type(iter(range(0)))
    longrange_iterator = type(iter(range(1 << 1000)))
    set_iterator = type(iter(set()))
    str_iterator = type(iter(""))
    tuple_iterator = type(iter(()))
    zip_iterator = type(iter(zip()))
    ## views ##
    dict_keys = type({}.keys())
    dict_values = type({}.values())
    dict_items = type({}.items())
    ## misc ##
    mappingproxy = type(type.__dict__)
    generator = type((lambda: (yield))())

    ## coroutine ##
    async def _coro():
        pass

    _coro = _coro()
    coroutine = type(_coro)
    _coro.close()  # Prevent ResourceWarning
    del _coro

    ## asynchronous generator ##
    async def _ag():
        yield

    _ag = _ag()
    async_generator = type(_ag)
    del _ag

    ### ONE-TRICK PONIES ###

    def _check_methods(C, *methods):
        mro = C.__mro__
        for method in methods:
            for B in mro:
                if method in B.__dict__:
                    if B.__dict__[method] is None:
                        return NotImplemented
                    break
            else:
                return NotImplemented
        return True

    class Hashable(metaclass=ABCMeta):

        __slots__ = ()

        @abstractmethod
        def __hash__(self):
            return 0

        @classmethod
        def __subclasshook__(cls, C):
            if cls is Hashable:
                return _check_methods(C, "__hash__")
            return NotImplemented

    class Awaitable(metaclass=ABCMeta):

        __slots__ = ()

        @abstractmethod
        def __await__(self):
            yield

        @classmethod
        def __subclasshook__(cls, C):
            if cls is Awaitable:
                return _check_methods(C, "__await__")
            return NotImplemented

    class Coroutine(Awaitable):

        __slots__ = ()

        @abstractmethod
        def send(self, value):
            """Send a value into the coroutine.
            Return next yielded value or raise StopIteration.
            """
            raise StopIteration

        @abstractmethod
        def throw(self, typ, val=None, tb=None):
            """Raise an exception in the coroutine.
            Return next yielded value or raise StopIteration.
            """
            if val is None:
                if tb is None:
                    raise typ
                val = typ()
            if tb is not None:
                val = val.with_traceback(tb)
            raise val

        def close(self):
            """Raise GeneratorExit inside coroutine.
            """
            try:
                self.throw(GeneratorExit)
            except (GeneratorExit, StopIteration):
                pass
            else:
                raise RuntimeError("coroutine ignored GeneratorExit")

        @classmethod
        def __subclasshook__(cls, C):
            if cls is Coroutine:
                return _check_methods(C, '__await__', 'send', 'throw', 'close')
            return NotImplemented

    Coroutine.register(coroutine)

    class AsyncIterable(metaclass=ABCMeta):

        __slots__ = ()

        @abstractmethod
        def __aiter__(self):
            return AsyncIterator()

        @classmethod
        def __subclasshook__(cls, C):
            if cls is AsyncIterable:
                return _check_methods(C, "__aiter__")
            return NotImplemented

    class AsyncIterator(AsyncIterable):

        __slots__ = ()

        @abstractmethod
        async def __anext__(self):
            """Return the next item or raise StopAsyncIteration when exhausted."""
            raise StopAsyncIteration

        def __aiter__(self):
            return self

        @classmethod
        def __subclasshook__(cls, C):
            if cls is AsyncIterator:
                return _check_methods(C, "__anext__", "__aiter__")
            return NotImplemented

    class AsyncGenerator(AsyncIterator):

        __slots__ = ()

        async def __anext__(self):
            """Return the next item from the asynchronous generator.
            When exhausted, raise StopAsyncIteration.
            """
            return await self.asend(None)

        @abstractmethod
        async def asend(self, value):
            """Send a value into the asynchronous generator.
            Return next yielded value or raise StopAsyncIteration.
            """
            raise StopAsyncIteration

        @abstractmethod
        async def athrow(self, typ, val=None, tb=None):
            """Raise an exception in the asynchronous generator.
            Return next yielded value or raise StopAsyncIteration.
            """
            if val is None:
                if tb is None:
                    raise typ
                val = typ()
            if tb is not None:
                val = val.with_traceback(tb)
            raise val

        async def aclose(self):
            """Raise GeneratorExit inside coroutine.
            """
            try:
                await self.athrow(GeneratorExit)
            except (GeneratorExit, StopAsyncIteration):
                pass
            else:
                raise RuntimeError("asynchronous generator ignored GeneratorExit")

        @classmethod
        def __subclasshook__(cls, C):
            if cls is AsyncGenerator:
                return _check_methods(C, '__aiter__', '__anext__',
                                      'asend', 'athrow', 'aclose')
            return NotImplemented

    AsyncGenerator.register(async_generator)

    class Iterable(metaclass=ABCMeta):

        __slots__ = ()

        @abstractmethod
        def __iter__(self):
            while False:
                yield None

        @classmethod
        def __subclasshook__(cls, C):
            if cls is Iterable:
                return _check_methods(C, "__iter__")
            return NotImplemented

    class Iterator(Iterable):

        __slots__ = ()

        @abstractmethod
        def __next__(self):
            'Return the next item from the iterator. When exhausted, raise StopIteration'
            raise StopIteration

        def __iter__(self):
            return self

        @classmethod
        def __subclasshook__(cls, C):
            if cls is Iterator:
                return _check_methods(C, '__iter__', '__next__')
            return NotImplemented

    Iterator.register(bytes_iterator)
    Iterator.register(bytearray_iterator)
    # Iterator.register(callable_iterator)
    Iterator.register(dict_keyiterator)
    Iterator.register(dict_valueiterator)
    Iterator.register(dict_itemiterator)
    Iterator.register(list_iterator)
    Iterator.register(list_reverseiterator)
    Iterator.register(range_iterator)
    Iterator.register(longrange_iterator)
    Iterator.register(set_iterator)
    Iterator.register(str_iterator)
    Iterator.register(tuple_iterator)
    Iterator.register(zip_iterator)

    class Reversible(Iterable):

        __slots__ = ()

        @abstractmethod
        def __reversed__(self):
            while False:
                yield None

        @classmethod
        def __subclasshook__(cls, C):
            if cls is Reversible:
                return _check_methods(C, "__reversed__", "__iter__")
            return NotImplemented

    class Generator(Iterator):

        __slots__ = ()

        def __next__(self):
            """Return the next item from the generator.
            When exhausted, raise StopIteration.
            """
            return self.send(None)

        @abstractmethod
        def send(self, value):
            """Send a value into the generator.
            Return next yielded value or raise StopIteration.
            """
            raise StopIteration

        @abstractmethod
        def throw(self, typ, val=None, tb=None):
            """Raise an exception in the generator.
            Return next yielded value or raise StopIteration.
            """
            if val is None:
                if tb is None:
                    raise typ
                val = typ()
            if tb is not None:
                val = val.with_traceback(tb)
            raise val

        def close(self):
            """Raise GeneratorExit inside generator.
            """
            try:
                self.throw(GeneratorExit)
            except (GeneratorExit, StopIteration):
                pass
            else:
                raise RuntimeError("generator ignored GeneratorExit")

        @classmethod
        def __subclasshook__(cls, C):
            if cls is Generator:
                return _check_methods(C, '__iter__', '__next__',
                                      'send', 'throw', 'close')
            return NotImplemented

    Generator.register(generator)

    class Sized(metaclass=ABCMeta):

        __slots__ = ()

        @abstractmethod
        def __len__(self):
            return 0

        @classmethod
        def __subclasshook__(cls, C):
            if cls is Sized:
                return _check_methods(C, "__len__")
            return NotImplemented

    class Container(metaclass=ABCMeta):

        __slots__ = ()

        @abstractmethod
        def __contains__(self, x):
            return False

        @classmethod
        def __subclasshook__(cls, C):
            if cls is Container:
                return _check_methods(C, "__contains__")
            return NotImplemented

    class Collection(Sized, Iterable, Container):

        __slots__ = ()

        @classmethod
        def __subclasshook__(cls, C):
            if cls is Collection:
                return _check_methods(C, "__len__", "__iter__", "__contains__")
            return NotImplemented

    class Callable(metaclass=ABCMeta):

        __slots__ = ()

        @abstractmethod
        def __call__(self, *args, **kwds):
            return False

        @classmethod
        def __subclasshook__(cls, C):
            if cls is Callable:
                return _check_methods(C, "__call__")
            return NotImplemented

    ### SETS ###

    class Set(Collection):

        """A set is a finite, iterable container.

        This class provides concrete generic implementations of all
        methods except for __contains__, __iter__ and __len__.

        To override the comparisons (presumably for speed, as the
        semantics are fixed), redefine __le__ and __ge__,
        then the other operations will automatically follow suit.
        """

        __slots__ = ()

        def __le__(self, other):
            if not isinstance(other, Set):
                return NotImplemented
            if len(self) > len(other):
                return False
            for elem in self:
                if elem not in other:
                    return False
            return True

        def __lt__(self, other):
            if not isinstance(other, Set):
                return NotImplemented
            return len(self) < len(other) and self.__le__(other)

        def __gt__(self, other):
            if not isinstance(other, Set):
                return NotImplemented
            return len(self) > len(other) and self.__ge__(other)

        def __ge__(self, other):
            if not isinstance(other, Set):
                return NotImplemented
            if len(self) < len(other):
                return False
            for elem in other:
                if elem not in self:
                    return False
            return True

        def __eq__(self, other):
            if not isinstance(other, Set):
                return NotImplemented
            return len(self) == len(other) and self.__le__(other)

        @classmethod
        def _from_iterable(cls, it):
            '''Construct an instance of the class from any iterable input.

            Must override this method if the class constructor signature
            does not accept an iterable for an input.
            '''
            return cls(it)

        def __and__(self, other):
            if not isinstance(other, Iterable):
                return NotImplemented
            return self._from_iterable(value for value in other if value in self)

        __rand__ = __and__

        def isdisjoint(self, other):
            'Return True if two sets have a null intersection.'
            for value in other:
                if value in self:
                    return False
            return True

        def __or__(self, other):
            if not isinstance(other, Iterable):
                return NotImplemented
            chain = (e for s in (self, other) for e in s)
            return self._from_iterable(chain)

        __ror__ = __or__

        def __sub__(self, other):
            if not isinstance(other, Set):
                if not isinstance(other, Iterable):
                    return NotImplemented
                other = self._from_iterable(other)
            return self._from_iterable(value for value in self
                                       if value not in other)

        def __rsub__(self, other):
            if not isinstance(other, Set):
                if not isinstance(other, Iterable):
                    return NotImplemented
                other = self._from_iterable(other)
            return self._from_iterable(value for value in other
                                       if value not in self)

        def __xor__(self, other):
            if not isinstance(other, Set):
                if not isinstance(other, Iterable):
                    return NotImplemented
                other = self._from_iterable(other)
            return (self - other) | (other - self)

        __rxor__ = __xor__

        def _hash(self):
            """Compute the hash value of a set.

            Note that we don't define __hash__: not all sets are hashable.
            But if you define a hashable set type, its __hash__ should
            call this function.

            This must be compatible __eq__.

            All sets ought to compare equal if they contain the same
            elements, regardless of how they are implemented, and
            regardless of the order of the elements; so there's not much
            freedom for __eq__ or __hash__.  We match the algorithm used
            by the built-in frozenset type.
            """
            MAX = sys.maxsize
            MASK = 2 * MAX + 1
            n = len(self)
            h = 1927868237 * (n + 1)
            h &= MASK
            for x in self:
                hx = hash(x)
                h ^= (hx ^ (hx << 16) ^ 89869747) * 3644798167
                h &= MASK
            h = h * 69069 + 907133923
            h &= MASK
            if h > MAX:
                h -= MASK + 1
            if h == -1:
                h = 590923713
            return h

    Set.register(frozenset)

    class MutableSet(Set):
        """A mutable set is a finite, iterable container.

        This class provides concrete generic implementations of all
        methods except for __contains__, __iter__, __len__,
        add(), and discard().

        To override the comparisons (presumably for speed, as the
        semantics are fixed), all you have to do is redefine __le__ and
        then the other operations will automatically follow suit.
        """

        __slots__ = ()

        @abstractmethod
        def add(self, value):
            """Add an element."""
            raise NotImplementedError

        @abstractmethod
        def discard(self, value):
            """Remove an element.  Do not raise an exception if absent."""
            raise NotImplementedError

        def remove(self, value):
            """Remove an element. If not a member, raise a KeyError."""
            if value not in self:
                raise KeyError(value)
            self.discard(value)

        def pop(self):
            """Return the popped value.  Raise KeyError if empty."""
            it = iter(self)
            try:
                value = next(it)
            except StopIteration:
                raise KeyError from None
            self.discard(value)
            return value

        def clear(self):
            """This is slow (creates N new iterators!) but effective."""
            try:
                while True:
                    self.pop()
            except KeyError:
                pass

        def __ior__(self, it):
            for value in it:
                self.add(value)
            return self

        def __iand__(self, it):
            for value in (self - it):
                self.discard(value)
            return self

        def __ixor__(self, it):
            if it is self:
                self.clear()
            else:
                if not isinstance(it, Set):
                    it = self._from_iterable(it)
                for value in it:
                    if value in self:
                        self.discard(value)
                    else:
                        self.add(value)
            return self

        def __isub__(self, it):
            if it is self:
                self.clear()
            else:
                for value in it:
                    self.discard(value)
            return self

    MutableSet.register(set)

    ### MAPPINGS ###

    class Mapping(Collection):

        __slots__ = ()

        """A Mapping is a generic container for associating key/value
        pairs.

        This class provides concrete generic implementations of all
        methods except for __getitem__, __iter__, and __len__.

        """

        @abstractmethod
        def __getitem__(self, key):
            raise KeyError

        def get(self, key, default=None):
            'D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.'
            try:
                return self[key]
            except KeyError:
                return default

        def __contains__(self, key):
            try:
                self[key]
            except KeyError:
                return False
            else:
                return True

        def keys(self):
            "D.keys() -> a set-like object providing a view on D's keys"
            return KeysView(self)

        def items(self):
            "D.items() -> a set-like object providing a view on D's items"
            return ItemsView(self)

        def values(self):
            "D.values() -> an object providing a view on D's values"
            return ValuesView(self)

        def __eq__(self, other):
            if not isinstance(other, Mapping):
                return NotImplemented
            return dict(self.items()) == dict(other.items())

        __reversed__ = None

    Mapping.register(mappingproxy)

    class MappingView(Sized):

        __slots__ = '_mapping',

        def __init__(self, mapping):
            self._mapping = mapping

        def __len__(self):
            return len(self._mapping)

        def __repr__(self):
            return '{0.__class__.__name__}({0._mapping!r})'.format(self)

    class KeysView(MappingView, Set):

        __slots__ = ()

        @classmethod
        def _from_iterable(self, it):
            return set(it)

        def __contains__(self, key):
            return key in self._mapping

        def __iter__(self):
            yield from self._mapping

    KeysView.register(dict_keys)

    class ItemsView(MappingView, Set):

        __slots__ = ()

        @classmethod
        def _from_iterable(self, it):
            return set(it)

        def __contains__(self, item):
            key, value = item
            try:
                v = self._mapping[key]
            except KeyError:
                return False
            else:
                return v is value or v == value

        def __iter__(self):
            for key in self._mapping:
                yield (key, self._mapping[key])

    ItemsView.register(dict_items)

    class ValuesView(MappingView, Collection):

        __slots__ = ()

        def __contains__(self, value):
            for key in self._mapping:
                v = self._mapping[key]
                if v is value or v == value:
                    return True
            return False

        def __iter__(self):
            for key in self._mapping:
                yield self._mapping[key]

    ValuesView.register(dict_values)

    class MutableMapping(Mapping):

        __slots__ = ()

        """A MutableMapping is a generic container for associating
        key/value pairs.

        This class provides concrete generic implementations of all
        methods except for __getitem__, __setitem__, __delitem__,
        __iter__, and __len__.

        """

        @abstractmethod
        def __setitem__(self, key, value):
            raise KeyError

        @abstractmethod
        def __delitem__(self, key):
            raise KeyError

        __marker = object()

        def pop(self, key, default=__marker):
            '''D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
              If key is not found, d is returned if given, otherwise KeyError is raised.
            '''
            try:
                value = self[key]
            except KeyError:
                if default is self.__marker:
                    raise
                return default
            else:
                del self[key]
                return value

        def popitem(self):
            '''D.popitem() -> (k, v), remove and return some (key, value) pair
               as a 2-tuple; but raise KeyError if D is empty.
            '''
            try:
                key = next(iter(self))
            except StopIteration:
                raise KeyError from None
            value = self[key]
            del self[key]
            return key, value

        def clear(self):
            'D.clear() -> None.  Remove all items from D.'
            try:
                while True:
                    self.popitem()
            except KeyError:
                pass

        def update(self, other=(), /, **kwds):
            ''' D.update([E, ]**F) -> None.  Update D from mapping/iterable E and F.
                If E present and has a .keys() method, does:     for k in E: D[k] = E[k]
                If E present and lacks .keys() method, does:     for (k, v) in E: D[k] = v
                In either case, this is followed by: for k, v in F.items(): D[k] = v
            '''
            if isinstance(other, Mapping):
                for key in other:
                    self[key] = other[key]
            elif hasattr(other, "keys"):
                for key in other.keys():
                    self[key] = other[key]
            else:
                for key, value in other:
                    self[key] = value
            for key, value in kwds.items():
                self[key] = value

        def setdefault(self, key, default=None):
            'D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D'
            try:
                return self[key]
            except KeyError:
                self[key] = default
            return default

    MutableMapping.register(dict)

    ### SEQUENCES ###

    class Sequence(Reversible, Collection):

        """All the operations on a read-only sequence.

        Concrete subclasses must override __new__ or __init__,
        __getitem__, and __len__.
        """

        __slots__ = ()

        @abstractmethod
        def __getitem__(self, index):
            raise IndexError

        def __iter__(self):
            i = 0
            try:
                while True:
                    v = self[i]
                    yield v
                    i += 1
            except IndexError:
                return

        def __contains__(self, value):
            for v in self:
                if v is value or v == value:
                    return True
            return False

        def __reversed__(self):
            for i in reversed(range(len(self))):
                yield self[i]

        def index(self, value, start=0, stop=None):
            '''S.index(value, [start, [stop]]) -> integer -- return first index of value.
               Raises ValueError if the value is not present.

               Supporting start and stop arguments is optional, but
               recommended.
            '''
            if start is not None and start < 0:
                start = max(len(self) + start, 0)
            if stop is not None and stop < 0:
                stop += len(self)

            i = start
            while stop is None or i < stop:
                try:
                    v = self[i]
                    if v is value or v == value:
                        return i
                except IndexError:
                    break
                i += 1
            raise ValueError

        def count(self, value):
            'S.count(value) -> integer -- return number of occurrences of value'
            return sum(1 for v in self if v is value or v == value)

    Sequence.register(tuple)
    Sequence.register(str)
    Sequence.register(range)
    Sequence.register(memoryview)

    class ByteString(Sequence):

        """This unifies bytes and bytearray.

        XXX Should add all their methods.
        """

        __slots__ = ()

    ByteString.register(bytes)
    ByteString.register(bytearray)

    class MutableSequence(Sequence):

        __slots__ = ()

        """All the operations on a read-write sequence.

        Concrete subclasses must provide __new__ or __init__,
        __getitem__, __setitem__, __delitem__, __len__, and insert().

        """

        @abstractmethod
        def __setitem__(self, index, value):
            raise IndexError

        @abstractmethod
        def __delitem__(self, index):
            raise IndexError

        @abstractmethod
        def insert(self, index, value):
            'S.insert(index, value) -- insert value before index'
            raise IndexError

        def append(self, value):
            'S.append(value) -- append value to the end of the sequence'
            self.insert(len(self), value)

        def clear(self):
            'S.clear() -> None -- remove all items from S'
            try:
                while True:
                    self.pop()
            except IndexError:
                pass

        def reverse(self):
            'S.reverse() -- reverse *IN PLACE*'
            n = len(self)
            for i in range(n // 2):
                self[i], self[n - i - 1] = self[n - i - 1], self[i]

        def extend(self, values):
            'S.extend(iterable) -- extend sequence by appending elements from the iterable'
            if values is self:
                values = list(values)
            for v in values:
                self.append(v)

        def pop(self, index=-1):
            '''S.pop([index]) -> item -- remove and return item at index (default last).
               Raise IndexError if list is empty or index is out of range.
            '''
            v = self[index]
            del self[index]
            return v

        def remove(self, value):
            '''S.remove(value) -- remove first occurrence of value.
               Raise ValueError if the value is not present.
            '''
            del self[self.index(value)]

        def __iadd__(self, values):
            self.extend(values)
            return self

    MutableSequence.register(list)
    MutableSequence.register(bytearray)  # Multiply inheriting, see ByteString


def jcollections():
    '''This module implements specialized container datatypes providing
    alternatives to Python's general purpose built-in containers, dict,
    list, set, and tuple.

    * namedtuple   factory function for creating tuple subclasses with named fields
    * deque        list-like container with fast appends and pops on either end
    * ChainMap     dict-like class for creating a single view of multiple mappings
    * Counter      dict subclass for counting hashable objects
    * OrderedDict  dict subclass that remembers the order entries were added
    * defaultdict  dict subclass that calls a factory function to supply missing values
    * UserDict     wrapper around dictionary objects for easier dict subclassing
    * UserList     wrapper around list objects for easier list subclassing
    * UserString   wrapper around string objects for easier string subclassing

    '''

    __all__ = ['deque', 'defaultdict', 'namedtuple', 'UserDict', 'UserList',
               'UserString', 'Counter', 'OrderedDict', 'ChainMap']

    import _collections_abc
    from operator import itemgetter as _itemgetter, eq as _eq
    from keyword import iskeyword as _iskeyword
    import sys as _sys
    import heapq as _heapq
    from _weakref import proxy as _proxy
    from itertools import repeat as _repeat, chain as _chain, starmap as _starmap
    from reprlib import recursive_repr as _recursive_repr

    try:
        from _collections import deque
    except ImportError:
        pass
    else:
        _collections_abc.MutableSequence.register(deque)

    try:
        from _collections import defaultdict
    except ImportError:
        pass

    def __getattr__(name):
        # For backwards compatibility, continue to make the collections ABCs
        # through Python 3.6 available through the collections module.
        # Note, no new collections ABCs were added in Python 3.7
        if name in _collections_abc.__all__:
            obj = getattr(_collections_abc, name)
            import warnings
            warnings.warn("Using or importing the ABCs from 'collections' instead "
                          "of from 'collections.abc' is deprecated since Python 3.3, "
                          "and in 3.9 it will stop working",
                          DeprecationWarning, stacklevel=2)
            globals()[name] = obj
            return obj
        raise AttributeError(f'module {__name__!r} has no attribute {name!r}')

    ################################################################################
    ### OrderedDict
    ################################################################################

    class _OrderedDictKeysView(_collections_abc.KeysView):

        def __reversed__(self):
            yield from reversed(self._mapping)

    class _OrderedDictItemsView(_collections_abc.ItemsView):

        def __reversed__(self):
            for key in reversed(self._mapping):
                yield (key, self._mapping[key])

    class _OrderedDictValuesView(_collections_abc.ValuesView):

        def __reversed__(self):
            for key in reversed(self._mapping):
                yield self._mapping[key]

    class _Link(object):
        __slots__ = 'prev', 'next', 'key', '__weakref__'

    class OrderedDict(dict):
        'Dictionary that remembers insertion order'

        # An inherited dict maps keys to values.
        # The inherited dict provides __getitem__, __len__, __contains__, and get.
        # The remaining methods are order-aware.
        # Big-O running times for all methods are the same as regular dictionaries.

        # The internal self.__map dict maps keys to links in a doubly linked list.
        # The circular doubly linked list starts and ends with a sentinel element.
        # The sentinel element never gets deleted (this simplifies the algorithm).
        # The sentinel is in self.__hardroot with a weakref proxy in self.__root.
        # The prev links are weakref proxies (to prevent circular references).
        # Individual links are kept alive by the hard reference in self.__map.
        # Those hard references disappear when a key is deleted from an OrderedDict.

        def __init__(self, other=(), /, **kwds):
            '''Initialize an ordered dictionary.  The signature is the same as
            regular dictionaries.  Keyword argument order is preserved.
            '''
            try:
                self.__root
            except AttributeError:
                self.__hardroot = _Link()
                self.__root = root = _proxy(self.__hardroot)
                root.prev = root.next = root
                self.__map = {}
            self.__update(other, **kwds)

        def __setitem__(self, key, value,
                        dict_setitem=dict.__setitem__, proxy=_proxy, Link=_Link):
            'od.__setitem__(i, y) <==> od[i]=y'
            # Setting a new item creates a new link at the end of the linked list,
            # and the inherited dictionary is updated with the new key/value pair.
            if key not in self:
                self.__map[key] = link = Link()
                root = self.__root
                last = root.prev
                link.prev, link.next, link.key = last, root, key
                last.next = link
                root.prev = proxy(link)
            dict_setitem(self, key, value)

        def __delitem__(self, key, dict_delitem=dict.__delitem__):
            'od.__delitem__(y) <==> del od[y]'
            # Deleting an existing item uses self.__map to find the link which gets
            # removed by updating the links in the predecessor and successor nodes.
            dict_delitem(self, key)
            link = self.__map.pop(key)
            link_prev = link.prev
            link_next = link.next
            link_prev.next = link_next
            link_next.prev = link_prev
            link.prev = None
            link.next = None

        def __iter__(self):
            'od.__iter__() <==> iter(od)'
            # Traverse the linked list in order.
            root = self.__root
            curr = root.next
            while curr is not root:
                yield curr.key
                curr = curr.next

        def __reversed__(self):
            'od.__reversed__() <==> reversed(od)'
            # Traverse the linked list in reverse order.
            root = self.__root
            curr = root.prev
            while curr is not root:
                yield curr.key
                curr = curr.prev

        def clear(self):
            'od.clear() -> None.  Remove all items from od.'
            root = self.__root
            root.prev = root.next = root
            self.__map.clear()
            dict.clear(self)

        def popitem(self, last=True):
            '''Remove and return a (key, value) pair from the dictionary.

            Pairs are returned in LIFO order if last is true or FIFO order if false.
            '''
            if not self:
                raise KeyError('dictionary is empty')
            root = self.__root
            if last:
                link = root.prev
                link_prev = link.prev
                link_prev.next = root
                root.prev = link_prev
            else:
                link = root.next
                link_next = link.next
                root.next = link_next
                link_next.prev = root
            key = link.key
            del self.__map[key]
            value = dict.pop(self, key)
            return key, value

        def move_to_end(self, key, last=True):
            '''Move an existing element to the end (or beginning if last is false).

            Raise KeyError if the element does not exist.
            '''
            link = self.__map[key]
            link_prev = link.prev
            link_next = link.next
            soft_link = link_next.prev
            link_prev.next = link_next
            link_next.prev = link_prev
            root = self.__root
            if last:
                last = root.prev
                link.prev = last
                link.next = root
                root.prev = soft_link
                last.next = link
            else:
                first = root.next
                link.prev = root
                link.next = first
                first.prev = soft_link
                root.next = link

        def __sizeof__(self):
            sizeof = _sys.getsizeof
            n = len(self) + 1  # number of links including root
            size = sizeof(self.__dict__)  # instance dictionary
            size += sizeof(self.__map) * 2  # internal dict and inherited dict
            size += sizeof(self.__hardroot) * n  # link objects
            size += sizeof(self.__root) * n  # proxy objects
            return size

        update = __update = _collections_abc.MutableMapping.update

        def keys(self):
            "D.keys() -> a set-like object providing a view on D's keys"
            return _OrderedDictKeysView(self)

        def items(self):
            "D.items() -> a set-like object providing a view on D's items"
            return _OrderedDictItemsView(self)

        def values(self):
            "D.values() -> an object providing a view on D's values"
            return _OrderedDictValuesView(self)

        __ne__ = _collections_abc.MutableMapping.__ne__

        __marker = object()

        def pop(self, key, default=__marker):
            '''od.pop(k[,d]) -> v, remove specified key and return the corresponding
            value.  If key is not found, d is returned if given, otherwise KeyError
            is raised.

            '''
            if key in self:
                result = self[key]
                del self[key]
                return result
            if default is self.__marker:
                raise KeyError(key)
            return default

        def setdefault(self, key, default=None):
            '''Insert key with a value of default if key is not in the dictionary.

            Return the value for key if key is in the dictionary, else default.
            '''
            if key in self:
                return self[key]
            self[key] = default
            return default

        @_recursive_repr()
        def __repr__(self):
            'od.__repr__() <==> repr(od)'
            if not self:
                return '%s()' % (self.__class__.__name__,)
            return '%s(%r)' % (self.__class__.__name__, list(self.items()))

        def __reduce__(self):
            'Return state information for pickling'
            inst_dict = vars(self).copy()
            for k in vars(OrderedDict()):
                inst_dict.pop(k, None)
            return self.__class__, (), inst_dict or None, None, iter(self.items())

        def copy(self):
            'od.copy() -> a shallow copy of od'
            return self.__class__(self)

        @classmethod
        def fromkeys(cls, iterable, value=None):
            '''Create a new ordered dictionary with keys from iterable and values set to value.
            '''
            self = cls()
            for key in iterable:
                self[key] = value
            return self

        def __eq__(self, other):
            '''od.__eq__(y) <==> od==y.  Comparison to another OD is order-sensitive
            while comparison to a regular mapping is order-insensitive.

            '''
            if isinstance(other, OrderedDict):
                return dict.__eq__(self, other) and all(map(_eq, self, other))
            return dict.__eq__(self, other)

    try:
        from _collections import OrderedDict
    except ImportError:
        # Leave the pure Python version in place.
        pass

    ################################################################################
    ### namedtuple
    ################################################################################

    try:
        from _collections import _tuplegetter
    except ImportError:
        _tuplegetter = lambda index, doc: property(_itemgetter(index), doc=doc)

    def namedtuple(typename, field_names, *, rename=False, defaults=None, module=None):
        """Returns a new subclass of tuple with named fields.

        >>> Point = namedtuple('Point', ['x', 'y'])
        >>> Point.__doc__                   # docstring for the new class
        'Point(x, y)'
        >>> p = Point(11, y=22)             # instantiate with positional args or keywords
        >>> p[0] + p[1]                     # indexable like a plain tuple
        33
        >>> x, y = p                        # unpack like a regular tuple
        >>> x, y
        (11, 22)
        >>> p.x + p.y                       # fields also accessible by name
        33
        >>> d = p._asdict()                 # convert to a dictionary
        >>> d['x']
        11
        >>> Point(**d)                      # convert from a dictionary
        Point(x=11, y=22)
        >>> p._replace(x=100)               # _replace() is like str.replace() but targets named fields
        Point(x=100, y=22)

        """

        # Validate the field names.  At the user's option, either generate an error
        # message or automatically replace the field name with a valid name.
        if isinstance(field_names, str):
            field_names = field_names.replace(',', ' ').split()
        field_names = list(map(str, field_names))
        typename = _sys.intern(str(typename))

        if rename:
            seen = set()
            for index, name in enumerate(field_names):
                if (not name.isidentifier()
                        or _iskeyword(name)
                        or name.startswith('_')
                        or name in seen):
                    field_names[index] = f'_{index}'
                seen.add(name)

        for name in [typename] + field_names:
            if type(name) is not str:
                raise TypeError('Type names and field names must be strings')
            if not name.isidentifier():
                raise ValueError('Type names and field names must be valid '
                                 f'identifiers: {name!r}')
            if _iskeyword(name):
                raise ValueError('Type names and field names cannot be a '
                                 f'keyword: {name!r}')

        seen = set()
        for name in field_names:
            if name.startswith('_') and not rename:
                raise ValueError('Field names cannot start with an underscore: '
                                 f'{name!r}')
            if name in seen:
                raise ValueError(f'Encountered duplicate field name: {name!r}')
            seen.add(name)

        field_defaults = {}
        if defaults is not None:
            defaults = tuple(defaults)
            if len(defaults) > len(field_names):
                raise TypeError('Got more default values than field names')
            field_defaults = dict(reversed(list(zip(reversed(field_names),
                                                    reversed(defaults)))))

        # Variables used in the methods and docstrings
        field_names = tuple(map(_sys.intern, field_names))
        num_fields = len(field_names)
        arg_list = repr(field_names).replace("'", "")[1:-1]
        repr_fmt = '(' + ', '.join(f'{name}=%r' for name in field_names) + ')'
        tuple_new = tuple.__new__
        _dict, _tuple, _len, _map, _zip = dict, tuple, len, map, zip

        # Create all the named tuple methods to be added to the class namespace

        s = f'def __new__(_cls, {arg_list}): return _tuple_new(_cls, ({arg_list}))'
        namespace = {'_tuple_new': tuple_new, '__name__': f'namedtuple_{typename}'}
        # Note: exec() has the side-effect of interning the field names
        exec(s, namespace)
        __new__ = namespace['__new__']
        __new__.__doc__ = f'Create new instance of {typename}({arg_list})'
        if defaults is not None:
            __new__.__defaults__ = defaults

        @classmethod
        def _make(cls, iterable):
            result = tuple_new(cls, iterable)
            if _len(result) != num_fields:
                raise TypeError(f'Expected {num_fields} arguments, got {len(result)}')
            return result

        _make.__func__.__doc__ = (f'Make a new {typename} object from a sequence '
                                  'or iterable')

        def _replace(self, /, **kwds):
            result = self._make(_map(kwds.pop, field_names, self))
            if kwds:
                raise ValueError(f'Got unexpected field names: {list(kwds)!r}')
            return result

        _replace.__doc__ = (f'Return a new {typename} object replacing specified '
                            'fields with new values')

        def __repr__(self):
            'Return a nicely formatted representation string'
            return self.__class__.__name__ + repr_fmt % self

        def _asdict(self):
            'Return a new dict which maps field names to their values.'
            return _dict(_zip(self._fields, self))

        def __getnewargs__(self):
            'Return self as a plain tuple.  Used by copy and pickle.'
            return _tuple(self)

        # Modify function metadata to help with introspection and debugging
        for method in (__new__, _make.__func__, _replace,
                       __repr__, _asdict, __getnewargs__):
            method.__qualname__ = f'{typename}.{method.__name__}'

        # Build-up the class namespace dictionary
        # and use type() to build the result class
        class_namespace = {
            '__doc__': f'{typename}({arg_list})',
            '__slots__': (),
            '_fields': field_names,
            '_field_defaults': field_defaults,
            # alternate spelling for backward compatibility
            '_fields_defaults': field_defaults,
            '__new__': __new__,
            '_make': _make,
            '_replace': _replace,
            '__repr__': __repr__,
            '_asdict': _asdict,
            '__getnewargs__': __getnewargs__,
        }
        for index, name in enumerate(field_names):
            doc = _sys.intern(f'Alias for field number {index}')
            class_namespace[name] = _tuplegetter(index, doc)

        result = type(typename, (tuple,), class_namespace)

        # For pickling to work, the __module__ variable needs to be set to the frame
        # where the named tuple is created.  Bypass this step in environments where
        # sys._getframe is not defined (Jython for example) or sys._getframe is not
        # defined for arguments greater than 0 (IronPython), or where the user has
        # specified a particular module.
        if module is None:
            try:
                module = _sys._getframe(1).f_globals.get('__name__', '__main__')
            except (AttributeError, ValueError):
                pass
        if module is not None:
            result.__module__ = module

        return result

    ########################################################################
    ###  Counter
    ########################################################################

    def _count_elements(mapping, iterable):
        'Tally elements from the iterable.'
        mapping_get = mapping.get
        for elem in iterable:
            mapping[elem] = mapping_get(elem, 0) + 1

    try:  # Load C helper function if available
        from _collections import _count_elements
    except ImportError:
        pass

    class Counter(dict):
        '''Dict subclass for counting hashable items.  Sometimes called a bag
        or multiset.  Elements are stored as dictionary keys and their counts
        are stored as dictionary values.

        >>> c = Counter('abcdeabcdabcaba')  # count elements from a string

        >>> c.most_common(3)                # three most common elements
        [('a', 5), ('b', 4), ('c', 3)]
        >>> sorted(c)                       # list all unique elements
        ['a', 'b', 'c', 'd', 'e']
        >>> ''.join(sorted(c.elements()))   # list elements with repetitions
        'aaaaabbbbcccdde'
        >>> sum(c.values())                 # total of all counts
        15

        >>> c['a']                          # count of letter 'a'
        5
        >>> for elem in 'shazam':           # update counts from an iterable
        ...     c[elem] += 1                # by adding 1 to each element's count
        >>> c['a']                          # now there are seven 'a'
        7
        >>> del c['b']                      # remove all 'b'
        >>> c['b']                          # now there are zero 'b'
        0

        >>> d = Counter('simsalabim')       # make another counter
        >>> c.update(d)                     # add in the second counter
        >>> c['a']                          # now there are nine 'a'
        9

        >>> c.clear()                       # empty the counter
        >>> c
        Counter()

        Note:  If a count is set to zero or reduced to zero, it will remain
        in the counter until the entry is deleted or the counter is cleared:

        >>> c = Counter('aaabbc')
        >>> c['b'] -= 2                     # reduce the count of 'b' by two
        >>> c.most_common()                 # 'b' is still in, but its count is zero
        [('a', 3), ('c', 1), ('b', 0)]

        '''

        # References:
        #   http://en.wikipedia.org/wiki/Multiset
        #   http://www.gnu.org/software/smalltalk/manual-base/html_node/Bag.html
        #   http://www.demo2s.com/Tutorial/Cpp/0380__set-multiset/Catalog0380__set-multiset.htm
        #   http://code.activestate.com/recipes/259174/
        #   Knuth, TAOCP Vol. II section 4.6.3

        def __init__(self, iterable=None, /, **kwds):
            '''Create a new, empty Counter object.  And if given, count elements
            from an input iterable.  Or, initialize the count from another mapping
            of elements to their counts.

            >>> c = Counter()                           # a new, empty counter
            >>> c = Counter('gallahad')                 # a new counter from an iterable
            >>> c = Counter({'a': 4, 'b': 2})           # a new counter from a mapping
            >>> c = Counter(a=4, b=2)                   # a new counter from keyword args

            '''
            super(Counter, self).__init__()
            self.update(iterable, **kwds)

        def __missing__(self, key):
            'The count of elements not in the Counter is zero.'
            # Needed so that self[missing_item] does not raise KeyError
            return 0

        def most_common(self, n=None):
            '''List the n most common elements and their counts from the most
            common to the least.  If n is None, then list all element counts.

            >>> Counter('abracadabra').most_common(3)
            [('a', 5), ('b', 2), ('r', 2)]

            '''
            # Emulate Bag.sortedByCount from Smalltalk
            if n is None:
                return sorted(self.items(), key=_itemgetter(1), reverse=True)
            return _heapq.nlargest(n, self.items(), key=_itemgetter(1))

        def elements(self):
            '''Iterator over elements repeating each as many times as its count.

            >>> c = Counter('ABCABC')
            >>> sorted(c.elements())
            ['A', 'A', 'B', 'B', 'C', 'C']

            # Knuth's example for prime factors of 1836:  2**2 * 3**3 * 17**1
            >>> prime_factors = Counter({2: 2, 3: 3, 17: 1})
            >>> product = 1
            >>> for factor in prime_factors.elements():     # loop over factors
            ...     product *= factor                       # and multiply them
            >>> product
            1836

            Note, if an element's count has been set to zero or is a negative
            number, elements() will ignore it.

            '''
            # Emulate Bag.do from Smalltalk and Multiset.begin from C++.
            return _chain.from_iterable(_starmap(_repeat, self.items()))

        # Override dict methods where necessary

        @classmethod
        def fromkeys(cls, iterable, v=None):
            # There is no equivalent method for counters because the semantics
            # would be ambiguous in cases such as Counter.fromkeys('aaabbc', v=2).
            # Initializing counters to zero values isn't necessary because zero
            # is already the default value for counter lookups.  Initializing
            # to one is easily accomplished with Counter(set(iterable)).  For
            # more exotic cases, create a dictionary first using a dictionary
            # comprehension or dict.fromkeys().
            raise NotImplementedError(
                'Counter.fromkeys() is undefined.  Use Counter(iterable) instead.')

        def update(self, iterable=None, /, **kwds):
            '''Like dict.update() but add counts instead of replacing them.

            Source can be an iterable, a dictionary, or another Counter instance.

            >>> c = Counter('which')
            >>> c.update('witch')           # add elements from another iterable
            >>> d = Counter('watch')
            >>> c.update(d)                 # add elements from another counter
            >>> c['h']                      # four 'h' in which, witch, and watch
            4

            '''
            # The regular dict.update() operation makes no sense here because the
            # replace behavior results in the some of original untouched counts
            # being mixed-in with all of the other counts for a mismash that
            # doesn't have a straight-forward interpretation in most counting
            # contexts.  Instead, we implement straight-addition.  Both the inputs
            # and outputs are allowed to contain zero and negative counts.

            if iterable is not None:
                if isinstance(iterable, _collections_abc.Mapping):
                    if self:
                        self_get = self.get
                        for elem, count in iterable.items():
                            self[elem] = count + self_get(elem, 0)
                    else:
                        super(Counter, self).update(iterable)  # fast path when counter is empty
                else:
                    _count_elements(self, iterable)
            if kwds:
                self.update(kwds)

        def subtract(self, iterable=None, /, **kwds):
            '''Like dict.update() but subtracts counts instead of replacing them.
            Counts can be reduced below zero.  Both the inputs and outputs are
            allowed to contain zero and negative counts.

            Source can be an iterable, a dictionary, or another Counter instance.

            >>> c = Counter('which')
            >>> c.subtract('witch')             # subtract elements from another iterable
            >>> c.subtract(Counter('watch'))    # subtract elements from another counter
            >>> c['h']                          # 2 in which, minus 1 in witch, minus 1 in watch
            0
            >>> c['w']                          # 1 in which, minus 1 in witch, minus 1 in watch
            -1

            '''
            if iterable is not None:
                self_get = self.get
                if isinstance(iterable, _collections_abc.Mapping):
                    for elem, count in iterable.items():
                        self[elem] = self_get(elem, 0) - count
                else:
                    for elem in iterable:
                        self[elem] = self_get(elem, 0) - 1
            if kwds:
                self.subtract(kwds)

        def copy(self):
            'Return a shallow copy.'
            return self.__class__(self)

        def __reduce__(self):
            return self.__class__, (dict(self),)

        def __delitem__(self, elem):
            'Like dict.__delitem__() but does not raise KeyError for missing values.'
            if elem in self:
                super().__delitem__(elem)

        def __repr__(self):
            if not self:
                return '%s()' % self.__class__.__name__
            try:
                items = ', '.join(map('%r: %r'.__mod__, self.most_common()))
                return '%s({%s})' % (self.__class__.__name__, items)
            except TypeError:
                # handle case where values are not orderable
                return '{0}({1!r})'.format(self.__class__.__name__, dict(self))

        # Multiset-style mathematical operations discussed in:
        #       Knuth TAOCP Volume II section 4.6.3 exercise 19
        #       and at http://en.wikipedia.org/wiki/Multiset
        #
        # Outputs guaranteed to only include positive counts.
        #
        # To strip negative and zero counts, add-in an empty counter:
        #       c += Counter()
        #
        # Rich comparison operators for multiset subset and superset tests
        # are deliberately omitted due to semantic conflicts with the
        # existing inherited dict equality method.  Subset and superset
        # semantics ignore zero counts and require that p≤q ∧ p≥q → p=q;
        # however, that would not be the case for p=Counter(a=1, b=0)
        # and q=Counter(a=1) where the dictionaries are not equal.

        def __add__(self, other):
            '''Add counts from two counters.

            >>> Counter('abbb') + Counter('bcc')
            Counter({'b': 4, 'c': 2, 'a': 1})

            '''
            if not isinstance(other, Counter):
                return NotImplemented
            result = Counter()
            for elem, count in self.items():
                newcount = count + other[elem]
                if newcount > 0:
                    result[elem] = newcount
            for elem, count in other.items():
                if elem not in self and count > 0:
                    result[elem] = count
            return result

        def __sub__(self, other):
            ''' Subtract count, but keep only results with positive counts.

            >>> Counter('abbbc') - Counter('bccd')
            Counter({'b': 2, 'a': 1})

            '''
            if not isinstance(other, Counter):
                return NotImplemented
            result = Counter()
            for elem, count in self.items():
                newcount = count - other[elem]
                if newcount > 0:
                    result[elem] = newcount
            for elem, count in other.items():
                if elem not in self and count < 0:
                    result[elem] = 0 - count
            return result

        def __or__(self, other):
            '''Union is the maximum of value in either of the input counters.

            >>> Counter('abbb') | Counter('bcc')
            Counter({'b': 3, 'c': 2, 'a': 1})

            '''
            if not isinstance(other, Counter):
                return NotImplemented
            result = Counter()
            for elem, count in self.items():
                other_count = other[elem]
                newcount = other_count if count < other_count else count
                if newcount > 0:
                    result[elem] = newcount
            for elem, count in other.items():
                if elem not in self and count > 0:
                    result[elem] = count
            return result

        def __and__(self, other):
            ''' Intersection is the minimum of corresponding counts.

            >>> Counter('abbb') & Counter('bcc')
            Counter({'b': 1})

            '''
            if not isinstance(other, Counter):
                return NotImplemented
            result = Counter()
            for elem, count in self.items():
                other_count = other[elem]
                newcount = count if count < other_count else other_count
                if newcount > 0:
                    result[elem] = newcount
            return result

        def __pos__(self):
            'Adds an empty counter, effectively stripping negative and zero counts'
            result = Counter()
            for elem, count in self.items():
                if count > 0:
                    result[elem] = count
            return result

        def __neg__(self):
            '''Subtracts from an empty counter.  Strips positive and zero counts,
            and flips the sign on negative counts.

            '''
            result = Counter()
            for elem, count in self.items():
                if count < 0:
                    result[elem] = 0 - count
            return result

        def _keep_positive(self):
            '''Internal method to strip elements with a negative or zero count'''
            nonpositive = [elem for elem, count in self.items() if not count > 0]
            for elem in nonpositive:
                del self[elem]
            return self

        def __iadd__(self, other):
            '''Inplace add from another counter, keeping only positive counts.

            >>> c = Counter('abbb')
            >>> c += Counter('bcc')
            >>> c
            Counter({'b': 4, 'c': 2, 'a': 1})

            '''
            for elem, count in other.items():
                self[elem] += count
            return self._keep_positive()

        def __isub__(self, other):
            '''Inplace subtract counter, but keep only results with positive counts.

            >>> c = Counter('abbbc')
            >>> c -= Counter('bccd')
            >>> c
            Counter({'b': 2, 'a': 1})

            '''
            for elem, count in other.items():
                self[elem] -= count
            return self._keep_positive()

        def __ior__(self, other):
            '''Inplace union is the maximum of value from either counter.

            >>> c = Counter('abbb')
            >>> c |= Counter('bcc')
            >>> c
            Counter({'b': 3, 'c': 2, 'a': 1})

            '''
            for elem, other_count in other.items():
                count = self[elem]
                if other_count > count:
                    self[elem] = other_count
            return self._keep_positive()

        def __iand__(self, other):
            '''Inplace intersection is the minimum of corresponding counts.

            >>> c = Counter('abbb')
            >>> c &= Counter('bcc')
            >>> c
            Counter({'b': 1})

            '''
            for elem, count in self.items():
                other_count = other[elem]
                if other_count < count:
                    self[elem] = other_count
            return self._keep_positive()

    ########################################################################
    ###  ChainMap
    ########################################################################

    class ChainMap(_collections_abc.MutableMapping):
        ''' A ChainMap groups multiple dicts (or other mappings) together
        to create a single, updateable view.

        The underlying mappings are stored in a list.  That list is public and can
        be accessed or updated using the *maps* attribute.  There is no other
        state.

        Lookups search the underlying mappings successively until a key is found.
        In contrast, writes, updates, and deletions only operate on the first
        mapping.

        '''

        def __init__(self, *maps):
            '''Initialize a ChainMap by setting *maps* to the given mappings.
            If no mappings are provided, a single empty dictionary is used.

            '''
            self.maps = list(maps) or [{}]  # always at least one map

        def __missing__(self, key):
            raise KeyError(key)

        def __getitem__(self, key):
            for mapping in self.maps:
                try:
                    return mapping[key]  # can't use 'key in mapping' with defaultdict
                except KeyError:
                    pass
            return self.__missing__(key)  # support subclasses that define __missing__

        def get(self, key, default=None):
            return self[key] if key in self else default

        def __len__(self):
            return len(set().union(*self.maps))  # reuses stored hash values if possible

        def __iter__(self):
            d = {}
            for mapping in reversed(self.maps):
                d.update(mapping)  # reuses stored hash values if possible
            return iter(d)

        def __contains__(self, key):
            return any(key in m for m in self.maps)

        def __bool__(self):
            return any(self.maps)

        @_recursive_repr()
        def __repr__(self):
            return f'{self.__class__.__name__}({", ".join(map(repr, self.maps))})'

        @classmethod
        def fromkeys(cls, iterable, *args):
            'Create a ChainMap with a single dict created from the iterable.'
            return cls(dict.fromkeys(iterable, *args))

        def copy(self):
            'New ChainMap or subclass with a new copy of maps[0] and refs to maps[1:]'
            return self.__class__(self.maps[0].copy(), *self.maps[1:])

        __copy__ = copy

        def new_child(self, m=None):  # like Django's Context.push()
            '''New ChainMap with a new map followed by all previous maps.
            If no map is provided, an empty dict is used.
            '''
            if m is None:
                m = {}
            return self.__class__(m, *self.maps)

        @property
        def parents(self):  # like Django's Context.pop()
            'New ChainMap from maps[1:].'
            return self.__class__(*self.maps[1:])

        def __setitem__(self, key, value):
            self.maps[0][key] = value

        def __delitem__(self, key):
            try:
                del self.maps[0][key]
            except KeyError:
                raise KeyError('Key not found in the first mapping: {!r}'.format(key))

        def popitem(self):
            'Remove and return an item pair from maps[0]. Raise KeyError is maps[0] is empty.'
            try:
                return self.maps[0].popitem()
            except KeyError:
                raise KeyError('No keys found in the first mapping.')

        def pop(self, key, *args):
            'Remove *key* from maps[0] and return its value. Raise KeyError if *key* not in maps[0].'
            try:
                return self.maps[0].pop(key, *args)
            except KeyError:
                raise KeyError('Key not found in the first mapping: {!r}'.format(key))

        def clear(self):
            'Clear maps[0], leaving maps[1:] intact.'
            self.maps[0].clear()

    ################################################################################
    ### UserDict
    ################################################################################

    class UserDict(_collections_abc.MutableMapping):

        # Start by filling-out the abstract methods
        def __init__(*args, **kwargs):
            if not args:
                raise TypeError("descriptor '__init__' of 'UserDict' object "
                                "needs an argument")
            self, *args = args
            if len(args) > 1:
                raise TypeError('expected at most 1 arguments, got %d' % len(args))
            if args:
                dict = args[0]
            elif 'dict' in kwargs:
                dict = kwargs.pop('dict')
                import warnings
                warnings.warn("Passing 'dict' as keyword argument is deprecated",
                              DeprecationWarning, stacklevel=2)
            else:
                dict = None
            self.data = {}
            if dict is not None:
                self.update(dict)
            if kwargs:
                self.update(kwargs)

        __init__.__text_signature__ = '($self, dict=None, /, **kwargs)'

        def __len__(self):
            return len(self.data)

        def __getitem__(self, key):
            if key in self.data:
                return self.data[key]
            if hasattr(self.__class__, "__missing__"):
                return self.__class__.__missing__(self, key)
            raise KeyError(key)

        def __setitem__(self, key, item):
            self.data[key] = item

        def __delitem__(self, key):
            del self.data[key]

        def __iter__(self):
            return iter(self.data)

        # Modify __contains__ to work correctly when __missing__ is present
        def __contains__(self, key):
            return key in self.data

        # Now, add the methods in dicts but not in MutableMapping
        def __repr__(self):
            return repr(self.data)

        def __copy__(self):
            inst = self.__class__.__new__(self.__class__)
            inst.__dict__.update(self.__dict__)
            # Create a copy and avoid triggering descriptors
            inst.__dict__["data"] = self.__dict__["data"].copy()
            return inst

        def copy(self):
            if self.__class__ is UserDict:
                return UserDict(self.data.copy())
            import copy
            data = self.data
            try:
                self.data = {}
                c = copy.copy(self)
            finally:
                self.data = data
            c.update(self)
            return c

        @classmethod
        def fromkeys(cls, iterable, value=None):
            d = cls()
            for key in iterable:
                d[key] = value
            return d

    ################################################################################
    ### UserList
    ################################################################################

    class UserList(_collections_abc.MutableSequence):
        """A more or less complete user-defined wrapper around list objects."""

        def __init__(self, initlist=None):
            self.data = []
            if initlist is not None:
                # XXX should this accept an arbitrary sequence?
                if type(initlist) == type(self.data):
                    self.data[:] = initlist
                elif isinstance(initlist, UserList):
                    self.data[:] = initlist.data[:]
                else:
                    self.data = list(initlist)

        def __repr__(self):
            return repr(self.data)

        def __lt__(self, other):
            return self.data < self.__cast(other)

        def __le__(self, other):
            return self.data <= self.__cast(other)

        def __eq__(self, other):
            return self.data == self.__cast(other)

        def __gt__(self, other):
            return self.data > self.__cast(other)

        def __ge__(self, other):
            return self.data >= self.__cast(other)

        def __cast(self, other):
            return other.data if isinstance(other, UserList) else other

        def __contains__(self, item):
            return item in self.data

        def __len__(self):
            return len(self.data)

        def __getitem__(self, i):
            if isinstance(i, slice):
                return self.__class__(self.data[i])
            else:
                return self.data[i]

        def __setitem__(self, i, item):
            self.data[i] = item

        def __delitem__(self, i):
            del self.data[i]

        def __add__(self, other):
            if isinstance(other, UserList):
                return self.__class__(self.data + other.data)
            elif isinstance(other, type(self.data)):
                return self.__class__(self.data + other)
            return self.__class__(self.data + list(other))

        def __radd__(self, other):
            if isinstance(other, UserList):
                return self.__class__(other.data + self.data)
            elif isinstance(other, type(self.data)):
                return self.__class__(other + self.data)
            return self.__class__(list(other) + self.data)

        def __iadd__(self, other):
            if isinstance(other, UserList):
                self.data += other.data
            elif isinstance(other, type(self.data)):
                self.data += other
            else:
                self.data += list(other)
            return self

        def __mul__(self, n):
            return self.__class__(self.data * n)

        __rmul__ = __mul__

        def __imul__(self, n):
            self.data *= n
            return self

        def __copy__(self):
            inst = self.__class__.__new__(self.__class__)
            inst.__dict__.update(self.__dict__)
            # Create a copy and avoid triggering descriptors
            inst.__dict__["data"] = self.__dict__["data"][:]
            return inst

        def append(self, item):
            self.data.append(item)

        def insert(self, i, item):
            self.data.insert(i, item)

        def pop(self, i=-1):
            return self.data.pop(i)

        def remove(self, item):
            self.data.remove(item)

        def clear(self):
            self.data.clear()

        def copy(self):
            return self.__class__(self)

        def count(self, item):
            return self.data.count(item)

        def index(self, item, *args):
            return self.data.index(item, *args)

        def reverse(self):
            self.data.reverse()

        def sort(self, /, *args, **kwds):
            self.data.sort(*args, **kwds)

        def extend(self, other):
            if isinstance(other, UserList):
                self.data.extend(other.data)
            else:
                self.data.extend(other)

    ################################################################################
    ### UserString
    ################################################################################

    class UserString(_collections_abc.Sequence):
        def __init__(self, seq):
            if isinstance(seq, str):
                self.data = seq
            elif isinstance(seq, UserString):
                self.data = seq.data[:]
            else:
                self.data = str(seq)

        def __str__(self):
            return str(self.data)

        def __repr__(self):
            return repr(self.data)

        def __int__(self):
            return int(self.data)

        def __float__(self):
            return float(self.data)

        def __complex__(self):
            return complex(self.data)

        def __hash__(self):
            return hash(self.data)

        def __getnewargs__(self):
            return (self.data[:],)

        def __eq__(self, string):
            if isinstance(string, UserString):
                return self.data == string.data
            return self.data == string

        def __lt__(self, string):
            if isinstance(string, UserString):
                return self.data < string.data
            return self.data < string

        def __le__(self, string):
            if isinstance(string, UserString):
                return self.data <= string.data
            return self.data <= string

        def __gt__(self, string):
            if isinstance(string, UserString):
                return self.data > string.data
            return self.data > string

        def __ge__(self, string):
            if isinstance(string, UserString):
                return self.data >= string.data
            return self.data >= string

        def __contains__(self, char):
            if isinstance(char, UserString):
                char = char.data
            return char in self.data

        def __len__(self):
            return len(self.data)

        def __getitem__(self, index):
            return self.__class__(self.data[index])

        def __add__(self, other):
            if isinstance(other, UserString):
                return self.__class__(self.data + other.data)
            elif isinstance(other, str):
                return self.__class__(self.data + other)
            return self.__class__(self.data + str(other))

        def __radd__(self, other):
            if isinstance(other, str):
                return self.__class__(other + self.data)
            return self.__class__(str(other) + self.data)

        def __mul__(self, n):
            return self.__class__(self.data * n)

        __rmul__ = __mul__

        def __mod__(self, args):
            return self.__class__(self.data % args)

        def __rmod__(self, template):
            return self.__class__(str(template) % self)

        # the following methods are defined in alphabetical order:
        def capitalize(self):
            return self.__class__(self.data.capitalize())

        def casefold(self):
            return self.__class__(self.data.casefold())

        def center(self, width, *args):
            return self.__class__(self.data.center(width, *args))

        def count(self, sub, start=0, end=_sys.maxsize):
            if isinstance(sub, UserString):
                sub = sub.data
            return self.data.count(sub, start, end)

        def encode(self, encoding='utf-8', errors='strict'):
            encoding = 'utf-8' if encoding is None else encoding
            errors = 'strict' if errors is None else errors
            return self.data.encode(encoding, errors)

        def endswith(self, suffix, start=0, end=_sys.maxsize):
            return self.data.endswith(suffix, start, end)

        def expandtabs(self, tabsize=8):
            return self.__class__(self.data.expandtabs(tabsize))

        def find(self, sub, start=0, end=_sys.maxsize):
            if isinstance(sub, UserString):
                sub = sub.data
            return self.data.find(sub, start, end)

        def format(self, /, *args, **kwds):
            return self.data.format(*args, **kwds)

        def format_map(self, mapping):
            return self.data.format_map(mapping)

        def index(self, sub, start=0, end=_sys.maxsize):
            return self.data.index(sub, start, end)

        def isalpha(self):
            return self.data.isalpha()

        def isalnum(self):
            return self.data.isalnum()

        def isascii(self):
            return self.data.isascii()

        def isdecimal(self):
            return self.data.isdecimal()

        def isdigit(self):
            return self.data.isdigit()

        def isidentifier(self):
            return self.data.isidentifier()

        def islower(self):
            return self.data.islower()

        def isnumeric(self):
            return self.data.isnumeric()

        def isprintable(self):
            return self.data.isprintable()

        def isspace(self):
            return self.data.isspace()

        def istitle(self):
            return self.data.istitle()

        def isupper(self):
            return self.data.isupper()

        def join(self, seq):
            return self.data.join(seq)

        def ljust(self, width, *args):
            return self.__class__(self.data.ljust(width, *args))

        def lower(self):
            return self.__class__(self.data.lower())

        def lstrip(self, chars=None):
            return self.__class__(self.data.lstrip(chars))

        maketrans = str.maketrans

        def partition(self, sep):
            return self.data.partition(sep)

        def replace(self, old, new, maxsplit=-1):
            if isinstance(old, UserString):
                old = old.data
            if isinstance(new, UserString):
                new = new.data
            return self.__class__(self.data.replace(old, new, maxsplit))

        def rfind(self, sub, start=0, end=_sys.maxsize):
            if isinstance(sub, UserString):
                sub = sub.data
            return self.data.rfind(sub, start, end)

        def rindex(self, sub, start=0, end=_sys.maxsize):
            return self.data.rindex(sub, start, end)

        def rjust(self, width, *args):
            return self.__class__(self.data.rjust(width, *args))

        def rpartition(self, sep):
            return self.data.rpartition(sep)

        def rstrip(self, chars=None):
            return self.__class__(self.data.rstrip(chars))

        def split(self, sep=None, maxsplit=-1):
            return self.data.split(sep, maxsplit)

        def rsplit(self, sep=None, maxsplit=-1):
            return self.data.rsplit(sep, maxsplit)

        def splitlines(self, keepends=False):
            return self.data.splitlines(keepends)

        def startswith(self, prefix, start=0, end=_sys.maxsize):
            return self.data.startswith(prefix, start, end)

        def strip(self, chars=None):
            return self.__class__(self.data.strip(chars))

        def swapcase(self):
            return self.__class__(self.data.swapcase())

        def title(self):
            return self.__class__(self.data.title())

        def translate(self, *args):
            return self.__class__(self.data.translate(*args))

        def upper(self):
            return self.__class__(self.data.upper())

        def zfill(self, width):
            return self.__class__(self.data.zfill(width))


def jabc():
    # Copyright 2007 Google, Inc. All Rights Reserved.
    # Licensed to PSF under a Contributor Agreement.

    """Abstract Base Classes (ABCs) according to PEP 3119."""

    def abstractmethod(funcobj):
        """A decorator indicating abstract methods.

        Requires that the metaclass is ABCMeta or derived from it.  A
        class that has a metaclass derived from ABCMeta cannot be
        instantiated unless all of its abstract methods are overridden.
        The abstract methods can be called using any of the normal
        'super' call mechanisms.  abstractmethod() may be used to declare
        abstract methods for properties and descriptors.

        Usage:

            class C(metaclass=ABCMeta):
                @abstractmethod
                def my_abstract_method(self, ...):
                    ...
        """
        funcobj.__isabstractmethod__ = True
        return funcobj

    class abstractclassmethod(classmethod):
        """A decorator indicating abstract classmethods.

        Deprecated, use 'classmethod' with 'abstractmethod' instead.
        """

        __isabstractmethod__ = True

        def __init__(self, callable):
            callable.__isabstractmethod__ = True
            super().__init__(callable)

    class abstractstaticmethod(staticmethod):
        """A decorator indicating abstract staticmethods.

        Deprecated, use 'staticmethod' with 'abstractmethod' instead.
        """

        __isabstractmethod__ = True

        def __init__(self, callable):
            callable.__isabstractmethod__ = True
            super().__init__(callable)

    class abstractproperty(property):
        """A decorator indicating abstract properties.

        Deprecated, use 'property' with 'abstractmethod' instead.
        """

        __isabstractmethod__ = True

    try:
        from _abc import (get_cache_token, _abc_init, _abc_register,
                          _abc_instancecheck, _abc_subclasscheck, _get_dump,
                          _reset_registry, _reset_caches)
    except ImportError:
        from _py_abc import ABCMeta, get_cache_token
        ABCMeta.__module__ = 'abc'
    else:
        class ABCMeta(type):
            """Metaclass for defining Abstract Base Classes (ABCs).

            Use this metaclass to create an ABC.  An ABC can be subclassed
            directly, and then acts as a mix-in class.  You can also register
            unrelated concrete classes (even built-in classes) and unrelated
            ABCs as 'virtual subclasses' -- these and their descendants will
            be considered subclasses of the registering ABC by the built-in
            issubclass() function, but the registering ABC won't show up in
            their MRO (Method Resolution Order) nor will method
            implementations defined by the registering ABC be callable (not
            even via super()).
            """

            def __new__(mcls, name, bases, namespace, **kwargs):
                cls = super().__new__(mcls, name, bases, namespace, **kwargs)
                _abc_init(cls)
                return cls

            def register(cls, subclass):
                """Register a virtual subclass of an ABC.

                Returns the subclass, to allow usage as a class decorator.
                """
                return _abc_register(cls, subclass)

            def __instancecheck__(cls, instance):
                """Override for isinstance(instance, cls)."""
                return _abc_instancecheck(cls, instance)

            def __subclasscheck__(cls, subclass):
                """Override for issubclass(subclass, cls)."""
                return _abc_subclasscheck(cls, subclass)

            def _dump_registry(cls, file=None):
                """Debug helper to print the ABC registry."""
                print(f"Class: {cls.__module__}.{cls.__qualname__}", file=file)
                print(f"Inv. counter: {get_cache_token()}", file=file)
                (_abc_registry, _abc_cache, _abc_negative_cache,
                 _abc_negative_cache_version) = _get_dump(cls)
                print(f"_abc_registry: {_abc_registry!r}", file=file)
                print(f"_abc_cache: {_abc_cache!r}", file=file)
                print(f"_abc_negative_cache: {_abc_negative_cache!r}", file=file)
                print(f"_abc_negative_cache_version: {_abc_negative_cache_version!r}",
                      file=file)

            def _abc_registry_clear(cls):
                """Clear the registry (for debugging or testing)."""
                _reset_registry(cls)

            def _abc_caches_clear(cls):
                """Clear the caches (for debugging or testing)."""
                _reset_caches(cls)

    class ABC(metaclass=ABCMeta):
        """Helper class that provides a standard way to create an ABC using
        inheritance.
        """
        __slots__ = ()


def jsys():
    # encoding: utf-8
    # module sys
    # from (built-in)
    # by generator 1.147
    """
    This module provides access to some objects used or maintained by the
    interpreter and to functions that interact strongly with the interpreter.

    Dynamic objects:

    argv -- command line arguments; argv[0] is the script pathname if known
    path -- module search path; path[0] is the script directory, else ''
    modules -- dictionary of loaded modules

    displayhook -- called to show results in an interactive session
    excepthook -- called to handle any uncaught exception other than SystemExit
      To customize printing in an interactive session or to install a custom
      top-level exception handler, assign other functions to replace these.

    stdin -- standard input file object; used by input()
    stdout -- standard output file object; used by print()
    stderr -- standard error object; used for error messages
      By assigning other file objects (or objects that behave like files)
      to these, it is possible to redirect all of the interpreter's I/O.

    last_type -- type of last uncaught exception
    last_value -- value of last uncaught exception
    last_traceback -- traceback of last uncaught exception
      These three are only available in an interactive session after a
      traceback has been printed.

    Static objects:

    builtin_module_names -- tuple of module names built into this interpreter
    copyright -- copyright notice pertaining to this interpreter
    exec_prefix -- prefix used to find the machine-specific Python library
    executable -- absolute path of the executable binary of the Python interpreter
    float_info -- a named tuple with information about the float implementation.
    float_repr_style -- string indicating the style of repr() output for floats
    hash_info -- a named tuple with information about the hash algorithm.
    hexversion -- version information encoded as a single integer
    implementation -- Python implementation information.
    int_info -- a named tuple with information about the int implementation.
    maxsize -- the largest supported length of containers.
    maxunicode -- the value of the largest Unicode code point
    platform -- platform identifier
    prefix -- prefix used to find the Python library
    thread_info -- a named tuple with information about the thread implementation.
    version -- the version of this interpreter as a string
    version_info -- version information as a named tuple
    __stdin__ -- the original stdin; don't touch!
    __stdout__ -- the original stdout; don't touch!
    __stderr__ -- the original stderr; don't touch!
    __displayhook__ -- the original displayhook; don't touch!
    __excepthook__ -- the original excepthook; don't touch!

    Functions:

    displayhook() -- print an object to the screen, and save it in builtins._
    excepthook() -- print an exception and its traceback to sys.stderr
    exc_info() -- return thread-safe information about the current exception
    exit() -- exit the interpreter by raising SystemExit
    getdlopenflags() -- returns flags to be used for dlopen() calls
    getprofile() -- get the global profiling function
    getrefcount() -- return the reference count for an object (plus one :-)
    getrecursionlimit() -- return the max recursion depth for the interpreter
    getsizeof() -- return the size of an object in bytes
    gettrace() -- get the global debug tracing function
    setcheckinterval() -- control how often the interpreter checks for events
    setdlopenflags() -- set the flags to be used for dlopen() calls
    setprofile() -- set the global profiling function
    setrecursionlimit() -- set the max recursion depth for the interpreter
    settrace() -- set the global debug tracing function
    """
    # no imports

    # Variables with simple values

    abiflags = ''

    api_version = 1013

    base_exec_prefix = '/home/obedotto/anaconda3/envs/joeljebitto'

    base_prefix = '/home/obedotto/anaconda3/envs/joeljebitto'

    byteorder = 'little'

    copyright = 'Copyright (c) 2001-2020 Python Software Foundation.\nAll Rights Reserved.\n\nCopyright (c) 2000 BeOpen.com.\nAll Rights Reserved.\n\nCopyright (c) 1995-2001 Corporation for National Research Initiatives.\nAll Rights Reserved.\n\nCopyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.\nAll Rights Reserved.'

    dont_write_bytecode = True

    executable = '/home/obedotto/anaconda3/envs/joeljebitto/bin/python'

    exec_prefix = '/home/obedotto/anaconda3/envs/joeljebitto'

    float_repr_style = 'short'

    hexversion = 50856944

    maxsize = 9223372036854775807
    maxunicode = 1114111

    platform = 'linux'

    prefix = '/home/obedotto/anaconda3/envs/joeljebitto'

    pycache_prefix = None

    version = '3.8.3 | packaged by conda-forge | (default, Jun  1 2020, 17:43:00) \n[GCC 7.5.0]'

    _base_executable = '/home/obedotto/anaconda3/envs/joeljebitto/bin/python'

    _framework = ''

    _home = None

    # functions

    def addaudithook(*args, **kwargs):  # real signature unknown
        """ Adds a new audit hook callback. """
        pass

    def audit(event, *args):  # real signature unknown; restored from __doc__
        """
        audit(event, *args)

        Passes the event to any audit hooks that are attached.
        """
        pass

    def breakpointhook(*args, **kws):  # real signature unknown; restored from __doc__
        """
        breakpointhook(*args, **kws)

        This hook function is called by built-in breakpoint().
        """
        pass

    def callstats(*args, **kwargs):  # real signature unknown
        """
        Return a tuple of function call statistics.

        A tuple is returned only if CALL_PROFILE was defined when Python was
        built.  Otherwise, this returns None.

        When enabled, this function returns detailed, implementation-specific
        details about the number of function calls executed. The return value
        is a 11-tuple where the entries in the tuple are counts of:
        0. all function calls
        1. calls to PyFunction_Type objects
        2. PyFunction calls that do not create an argument tuple
        3. PyFunction calls that do not create an argument tuple
           and bypass PyEval_EvalCodeEx()
        4. PyMethod calls
        5. PyMethod calls on bound methods
        6. PyType calls
        7. PyCFunction calls
        8. generator calls
        9. All other calls
        10. Number of stack pops performed by call_function()
        """
        pass

    def call_tracing(*args, **kwargs):  # real signature unknown
        """
        Call func(*args), while tracing is enabled.

        The tracing state is saved, and restored afterwards.  This is intended
        to be called from a debugger from a checkpoint, to recursively debug
        some other code.
        """
        pass

    def displayhook(*args, **kwargs):  # real signature unknown
        """ Print an object to sys.stdout and also save it in builtins._ """
        pass

    def excepthook(*args, **kwargs):  # real signature unknown
        """ Handle an exception by displaying it with a traceback on sys.stderr. """
        pass

    def exc_info(*args, **kwargs):  # real signature unknown
        """
        Return current exception information: (type, value, traceback).

        Return information about the most recent exception caught by an except
        clause in the current stack frame or in an older stack frame.
        """
        pass

    def exit(*args, **kwargs):  # real signature unknown
        """
        Exit the interpreter by raising SystemExit(status).

        If the status is omitted or None, it defaults to zero (i.e., success).
        If the status is an integer, it will be used as the system exit status.
        If it is another kind of object, it will be printed and the system
        exit status will be one (i.e., failure).
        """
        pass

    def getallocatedblocks(*args, **kwargs):  # real signature unknown
        """ Return the number of memory blocks currently allocated. """
        pass

    def getcheckinterval(*args, **kwargs):  # real signature unknown
        """ Return the current check interval; see sys.setcheckinterval(). """
        pass

    def getdefaultencoding(*args, **kwargs):  # real signature unknown
        """ Return the current default encoding used by the Unicode implementation. """
        pass

    def getdlopenflags(*args, **kwargs):  # real signature unknown
        """
        Return the current value of the flags that are used for dlopen calls.

        The flag constants are defined in the os module.
        """
        pass

    def getfilesystemencodeerrors(*args, **kwargs):  # real signature unknown
        """ Return the error mode used Unicode to OS filename conversion. """
        pass

    def getfilesystemencoding(*args, **kwargs):  # real signature unknown
        """ Return the encoding used to convert Unicode filenames to OS filenames. """
        pass

    def getprofile(*args, **kwargs):  # real signature unknown
        """
        Return the profiling function set with sys.setprofile.

        See the profiler chapter in the library manual.
        """
        pass

    def getrecursionlimit(*args, **kwargs):  # real signature unknown
        """
        Return the current value of the recursion limit.

        The recursion limit is the maximum depth of the Python interpreter
        stack.  This limit prevents infinite recursion from causing an overflow
        of the C stack and crashing Python.
        """
        pass

    def getrefcount():  # real signature unknown; restored from __doc__
        """
        Return the reference count of object.

        The count returned is generally one higher than you might expect,
        because it includes the (temporary) reference as an argument to
        getrefcount().
        """
        pass

    def getsizeof(p_object, default=None):  # real signature unknown; restored from __doc__
        """
        getsizeof(object [, default]) -> int

        Return the size of object in bytes.
        """
        return 0

    def getswitchinterval(*args, **kwargs):  # real signature unknown
        """ Return the current thread switch interval; see sys.setswitchinterval(). """
        pass

    def gettrace(*args, **kwargs):  # real signature unknown
        """
        Return the global debug tracing function set with sys.settrace.

        See the debugger chapter in the library manual.
        """
        pass

    def get_asyncgen_hooks(*args, **kwargs):  # real signature unknown
        """
        Return the installed asynchronous generators hooks.

        This returns a namedtuple of the form (firstiter, finalizer).
        """
        pass

    def get_coroutine_origin_tracking_depth(*args, **kwargs):  # real signature unknown
        """ Check status of origin tracking for coroutine objects in this thread. """
        pass

    def intern(*args, **kwargs):  # real signature unknown
        """
        ``Intern'' the given string.

        This enters the string in the (global) table of interned strings whose
        purpose is to speed up dictionary lookups. Return the string itself or
        the previously interned string object with the same value.
        """
        pass

    def is_finalizing(*args, **kwargs):  # real signature unknown
        """ Return True if Python is exiting. """
        pass

    def setcheckinterval(*args, **kwargs):  # real signature unknown
        """
        Set the async event check interval to n instructions.

        This tells the Python interpreter to check for asynchronous events
        every n instructions.

        This also affects how often thread switches occur.
        """
        pass

    def setdlopenflags(*args, **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        Set the flags used by the interpreter for dlopen calls.

        This is used, for example, when the interpreter loads extension
        modules. Among other things, this will enable a lazy resolving of
        symbols when importing a module, if called as sys.setdlopenflags(0).
        To share symbols across extension modules, call as
        sys.setdlopenflags(os.RTLD_GLOBAL).  Symbolic names for the flag
        modules can be found in the os module (RTLD_xxx constants, e.g.
        os.RTLD_LAZY).
        """
        pass

    def setprofile(function):  # real signature unknown; restored from __doc__
        """
        setprofile(function)

        Set the profiling function.  It will be called on each function call
        and return.  See the profiler chapter in the library manual.
        """
        pass

    def setrecursionlimit(*args, **kwargs):  # real signature unknown
        """
        Set the maximum depth of the Python interpreter stack to n.

        This limit prevents infinite recursion from causing an overflow of the C
        stack and crashing Python.  The highest possible limit is platform-
        dependent.
        """
        pass

    def setswitchinterval(*args, **kwargs):  # real signature unknown
        """
        Set the ideal thread switching delay inside the Python interpreter.

        The actual frequency of switching threads can be lower if the
        interpreter executes long sequences of uninterruptible code
        (this is implementation-specific and workload-dependent).

        The parameter must represent the desired switching delay in seconds
        A typical value is 0.005 (5 milliseconds).
        """
        pass

    def settrace(function):  # real signature unknown; restored from __doc__
        """
        settrace(function)

        Set the global debug tracing function.  It will be called on each
        function call.  See the debugger chapter in the library manual.
        """
        pass

    def set_asyncgen_hooks(*args, **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        set_asyncgen_hooks(* [, firstiter] [, finalizer])

        Set a finalizer for async generators objects.
        """
        pass

    def set_coroutine_origin_tracking_depth(*args, **kwargs):  # real signature unknown
        """
        Enable or disable origin tracking for coroutine objects in this thread.

        Coroutine objects will track 'depth' frames of traceback information
        about where they came from, available in their cr_origin attribute.

        Set a depth of 0 to disable.
        """
        pass

    def unraisablehook(*args, **kwargs):  # real signature unknown
        """
        Handle an unraisable exception.

        The unraisable argument has the following attributes:

        * exc_type: Exception type.
        * exc_value: Exception value, can be None.
        * exc_traceback: Exception traceback, can be None.
        * err_msg: Error message, can be None.
        * object: Object causing the exception, can be None.
        """
        pass

    def _clear_type_cache(*args, **kwargs):  # real signature unknown
        """ Clear the internal type lookup cache. """
        pass

    def _current_frames(*args, **kwargs):  # real signature unknown
        """
        Return a dict mapping each thread's thread id to its current stack frame.

        This function should be used for specialized purposes only.
        """
        pass

    def _debugmallocstats(*args, **kwargs):  # real signature unknown
        """
        Print summary info to stderr about the state of pymalloc's structures.

        In Py_DEBUG mode, also perform some expensive internal consistency
        checks.
        """
        pass

    def _getframe(*args, **kwargs):  # real signature unknown
        """
        Return a frame object from the call stack.

        If optional integer depth is given, return the frame object that many
        calls below the top of the stack.  If that is deeper than the call
        stack, ValueError is raised.  The default for depth is zero, returning
        the frame at the top of the call stack.

        This function should be used for internal and specialized purposes
        only.
        """
        pass

    def __breakpointhook__(*args, **kwargs):  # real signature unknown
        """
        breakpointhook(*args, **kws)

        This hook function is called by built-in breakpoint().
        """
        pass

    def __displayhook__(*args, **kwargs):  # real signature unknown
        """ Print an object to sys.stdout and also save it in builtins._ """
        pass

    def __excepthook__(*args, **kwargs):  # real signature unknown
        """ Handle an exception by displaying it with a traceback on sys.stderr. """
        pass

    def __interactivehook__():  # reliably restored by inspect
        # no doc
        pass

    def __unraisablehook__(*args, **kwargs):  # real signature unknown
        """
        Handle an unraisable exception.

        The unraisable argument has the following attributes:

        * exc_type: Exception type.
        * exc_value: Exception value, can be None.
        * exc_traceback: Exception traceback, can be None.
        * err_msg: Error message, can be None.
        * object: Object causing the exception, can be None.
        """
        pass

    # classes

    class __loader__(object):
        """
        Meta path import for built-in modules.

            All methods are either class or static methods to avoid the need to
            instantiate the class.
        """

        @classmethod
        def create_module(cls, *args, **kwargs):  # real signature unknown
            """ Create a built-in module """
            pass

        @classmethod
        def exec_module(cls, *args, **kwargs):  # real signature unknown
            """ Exec a built-in module """
            pass

        @classmethod
        def find_module(cls, *args, **kwargs):  # real signature unknown
            """
            Find the built-in module.

                    If 'path' is ever specified then the search is considered a failure.

                    This method is deprecated.  Use find_spec() instead.
            """
            pass

        @classmethod
        def find_spec(cls, *args, **kwargs):  # real signature unknown
            pass

        @classmethod
        def get_code(cls, *args, **kwargs):  # real signature unknown
            """ Return None as built-in modules do not have code objects. """
            pass

        @classmethod
        def get_source(cls, *args, **kwargs):  # real signature unknown
            """ Return None as built-in modules do not have source code. """
            pass

        @classmethod
        def is_package(cls, *args, **kwargs):  # real signature unknown
            """ Return False as built-in modules are never packages. """
            pass

        @classmethod
        def load_module(cls, *args, **kwargs):  # real signature unknown
            """
            Load the specified module into sys.modules and return it.

                This method is deprecated.  Use loader.exec_module instead.
            """
            pass

        def module_repr(module):  # reliably restored by inspect
            """
            Return repr for the module.

                    The method is deprecated.  The import machinery does the job itself.
            """
            pass

        def __init__(self, *args, **kwargs):  # real signature unknown
            pass

        __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
        """list of weak references to the object (if defined)"""

        __dict__ = None  # (!) real value is "mappingproxy({'__module__': '_frozen_importlib', '__doc__': 'Meta path import for built-in modules.\\n\\n    All methods are either class or static methods to avoid the need to\\n    instantiate the class.\\n\\n    ', 'module_repr': <staticmethod object at 0x7f5ae0fac430>, 'find_spec': <classmethod object at 0x7f5ae0fac460>, 'find_module': <classmethod object at 0x7f5ae0fac490>, 'create_module': <classmethod object at 0x7f5ae0fac4c0>, 'exec_module': <classmethod object at 0x7f5ae0fac4f0>, 'get_code': <classmethod object at 0x7f5ae0fac580>, 'get_source': <classmethod object at 0x7f5ae0fac610>, 'is_package': <classmethod object at 0x7f5ae0fac6a0>, 'load_module': <classmethod object at 0x7f5ae0fac6d0>, '__dict__': <attribute '__dict__' of 'BuiltinImporter' objects>, '__weakref__': <attribute '__weakref__' of 'BuiltinImporter' objects>})"

    # variables with complex values

    argv = []  # real value of type <class 'list'> skipped

    builtin_module_names = ()  # real value of type <class 'tuple'> skipped

    flags = (
        0,
        0,
        0,
        0,
        1,
        0,
        0,
        0,
        0,
        0,
        0,
        1,
        0,
        False,
        0,
    )

    float_info = (
        1.7976931348623157e+308,
        1024,
        308,
        2.2250738585072014e-308,
        -1021,
        -307,
        15,
        53,
        2.220446049250313e-16,
        2,
        1,
    )

    hash_info = (
        64,
        2305843009213693951,
        314159,
        0,
        1000003,
        'siphash24',
        64,
        128,
        0,
    )

    implementation = None  # (!) real value is "namespace(_multiarch='x86_64-linux-gnu', cache_tag='cpython-38', hexversion=50856944, name='cpython', version=sys.version_info(major=3, minor=8, micro=3, releaselevel='final', serial=0))"

    int_info = (
        30,
        4,
    )

    meta_path = [
        __loader__,
        None,  # (!) real value is "<class '_frozen_importlib.FrozenImporter'>"
        None,  # (!) real value is "<class '_frozen_importlib_external.PathFinder'>"
        None,  # (!) real value is '<six._SixMetaPathImporter object at 0x7f5adf545460>'
    ]

    modules = {}  # real value of type <class 'dict'> skipped

    path = [
        '/home/obedotto/pycharm-2020.1.2/plugins/python/helpers',
        '/home/obedotto/pycharm-2020.1.2/plugins/python/helpers/generator3',
        '/home/obedotto/anaconda3/envs/joeljebitto/lib/python38.zip',
        '/home/obedotto/anaconda3/envs/joeljebitto/lib/python3.8',
        '/home/obedotto/anaconda3/envs/joeljebitto/lib/python3.8/lib-dynload',
        '/home/obedotto/anaconda3/envs/joeljebitto/lib/python3.8/site-packages',
        '/home/obedotto/pycharm-2020.1.2/plugins/python/helpers/typeshed/stdlib/3.7',
        '/home/obedotto/pycharm-2020.1.2/plugins/python/helpers/typeshed/stdlib/3',
        '/home/obedotto/pycharm-2020.1.2/plugins/python/helpers/typeshed/stdlib/2and3',
        '/home/obedotto/pycharm-2020.1.2/plugins/python/helpers/typeshed/third_party/3',
        '/home/obedotto/pycharm-2020.1.2/plugins/python/helpers/typeshed/third_party/2and3',
    ]

    path_hooks = [
        None,  # (!) real value is "<class 'zipimport.zipimporter'>"
        None,  # (!) real value is '<function FileFinder.path_hook.<locals>.path_hook_for_FileFinder at 0x7f5ae0f61160>'
    ]

    path_importer_cache = {}  # real value of type <class 'dict'> skipped

    stderr = None  # (!) real value is "<_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'>"

    stdin = None  # (!) real value is "<_io.TextIOWrapper name=6 mode='r' encoding='UTF-8'>"

    stdout = None  # (!) forward: __stdout__, real value is "<_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>"

    thread_info = (
        'pthread',
        'semaphore',
        'NPTL 2.23',
    )

    version_info = (
        3,
        8,
        3,
        'final',
        0,
    )

    warnoptions = []

    _git = (
        'CPython',
        '',
        '',
    )

    _xoptions = {}

    __spec__ = None  # (!) real value is "ModuleSpec(name='sys', loader=<class '_frozen_importlib.BuiltinImporter'>)"

    __stderr__ = stderr

    __stdin__ = None  # (!) real value is "<_io.TextIOWrapper name='<stdin>' mode='r' encoding='utf-8'>"

    __stdout__ = None  # (!) real value is "<_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>"

    # intermittent names
    exc_value = Exception()
    exc_traceback = None


def jtime():
    # encoding: utf-8
    # module time
    # from (built-in)
    # by generator 1.147
    """
    This module provides various functions to manipulate time values.

    There are two standard representations of time.  One is the number
    of seconds since the Epoch, in UTC (a.k.a. GMT).  It may be an integer
    or a floating point number (to represent fractions of seconds).
    The Epoch is system-defined; on Unix, it is generally January 1st, 1970.
    The actual value can be retrieved by calling gmtime(0).

    The other representation is a tuple of 9 integers giving local time.
    The tuple items are:
      year (including century, e.g. 1998)
      month (1-12)
      day (1-31)
      hours (0-23)
      minutes (0-59)
      seconds (0-59)
      weekday (0-6, Monday is 0)
      Julian day (day in the year, 1-366)
      DST (Daylight Savings Time) flag (-1, 0 or 1)
    If the DST flag is 0, the time is given in the regular time zone;
    if it is 1, the time is given in the DST time zone;
    if it is -1, mktime() should guess based on the date and time.
    """
    # no imports

    # Variables with simple values

    altzone = -19800

    CLOCK_MONOTONIC = 1

    CLOCK_MONOTONIC_RAW = 4

    CLOCK_PROCESS_CPUTIME_ID = 2

    CLOCK_REALTIME = 0

    CLOCK_THREAD_CPUTIME_ID = 3

    daylight = 0

    timezone = -19800

    _STRUCT_TM_ITEMS = 11

    # functions

    def asctime(p_tuple=None):  # real signature unknown; restored from __doc__
        """
        asctime([tuple]) -> string

        Convert a time tuple to a string, e.g. 'Sat Jun 06 16:26:11 1998'.
        When the time tuple is not present, current time as returned by localtime()
        is used.
        """
        return ""

    def clock_getres(clk_id):  # real signature unknown; restored from __doc__
        """
        clock_getres(clk_id) -> floating point number

        Return the resolution (precision) of the specified clock clk_id.
        """
        return 0.0

    def clock_gettime(clk_id):  # real signature unknown; restored from __doc__
        """
        clock_gettime(clk_id) -> float

        Return the time of the specified clock clk_id.
        """
        return 0.0

    def clock_gettime_ns(clk_id):  # real signature unknown; restored from __doc__
        """
        clock_gettime_ns(clk_id) -> int

        Return the time of the specified clock clk_id as nanoseconds.
        """
        return 0

    def clock_settime(clk_id, time):  # real signature unknown; restored from __doc__
        """
        clock_settime(clk_id, time)

        Set the time of the specified clock clk_id.
        """
        pass

    def clock_settime_ns(clk_id, time):  # real signature unknown; restored from __doc__
        """
        clock_settime_ns(clk_id, time)

        Set the time of the specified clock clk_id with nanoseconds.
        """
        pass

    def ctime(seconds=None):  # known case of time.ctime
        """
        ctime(seconds) -> string

        Convert a time in seconds since the Epoch to a string in local time.
        This is equivalent to asctime(localtime(seconds)). When the time tuple is
        not present, current time as returned by localtime() is used.
        """
        return ""

    def get_clock_info(name):  # real signature unknown; restored from __doc__
        """
        get_clock_info(name: str) -> dict

        Get information of the specified clock.
        """
        return {}

    def gmtime(seconds=None):  # real signature unknown; restored from __doc__
        """
        gmtime([seconds]) -> (tm_year, tm_mon, tm_mday, tm_hour, tm_min,
                               tm_sec, tm_wday, tm_yday, tm_isdst)

        Convert seconds since the Epoch to a time tuple expressing UTC (a.k.a.
        GMT).  When 'seconds' is not passed in, convert the current time instead.

        If the platform supports the tm_gmtoff and tm_zone, they are available as
        attributes only.
        """
        pass

    def localtime(seconds=None):  # real signature unknown; restored from __doc__
        """
        localtime([seconds]) -> (tm_year,tm_mon,tm_mday,tm_hour,tm_min,
                                  tm_sec,tm_wday,tm_yday,tm_isdst)

        Convert seconds since the Epoch to a time tuple expressing local time.
        When 'seconds' is not passed in, convert the current time instead.
        """
        pass

    def mktime(p_tuple):  # real signature unknown; restored from __doc__
        """
        mktime(tuple) -> floating point number

        Convert a time tuple in local time to seconds since the Epoch.
        Note that mktime(gmtime(0)) will not generally return zero for most
        time zones; instead the returned value will either be equal to that
        of the timezone or altzone attributes on the time module.
        """
        return 0.0

    def monotonic():  # real signature unknown; restored from __doc__
        """
        monotonic() -> float

        Monotonic clock, cannot go backward.
        """
        return 0.0

    def monotonic_ns():  # real signature unknown; restored from __doc__
        """
        monotonic_ns() -> int

        Monotonic clock, cannot go backward, as nanoseconds.
        """
        return 0

    def perf_counter():  # real signature unknown; restored from __doc__
        """
        perf_counter() -> float

        Performance counter for benchmarking.
        """
        return 0.0

    def perf_counter_ns():  # real signature unknown; restored from __doc__
        """
        perf_counter_ns() -> int

        Performance counter for benchmarking as nanoseconds.
        """
        return 0

    def process_time():  # real signature unknown; restored from __doc__
        """
        process_time() -> float

        Process time for profiling: sum of the kernel and user-space CPU time.
        """
        return 0.0

    def process_time_ns(*args, **kwargs):  # real signature unknown
        """
        process_time() -> int

        Process time for profiling as nanoseconds:
        sum of the kernel and user-space CPU time.
        """
        pass

    def pthread_getcpuclockid(thread_id):  # real signature unknown; restored from __doc__
        """
        pthread_getcpuclockid(thread_id) -> int

        Return the clk_id of a thread's CPU time clock.
        """
        return 0

    def sleep(seconds):  # real signature unknown; restored from __doc__
        """
        sleep(seconds)

        Delay execution for a given number of seconds.  The argument may be
        a floating point number for subsecond precision.
        """
        pass

    def strftime(format, p_tuple=None):  # real signature unknown; restored from __doc__
        """
        strftime(format[, tuple]) -> string

        Convert a time tuple to a string according to a format specification.
        See the library reference manual for formatting codes. When the time tuple
        is not present, current time as returned by localtime() is used.

        Commonly used format codes:

        %Y  Year with century as a decimal number.
        %m  Month as a decimal number [01,12].
        %d  Day of the month as a decimal number [01,31].
        %H  Hour (24-hour clock) as a decimal number [00,23].
        %M  Minute as a decimal number [00,59].
        %S  Second as a decimal number [00,61].
        %z  Time zone offset from UTC.
        %a  Locale's abbreviated weekday name.
        %A  Locale's full weekday name.
        %b  Locale's abbreviated month name.
        %B  Locale's full month name.
        %c  Locale's appropriate date and time representation.
        %I  Hour (12-hour clock) as a decimal number [01,12].
        %p  Locale's equivalent of either AM or PM.

        Other codes may be available on your platform.  See documentation for
        the C library strftime function.
        """
        return ""

    def strptime(string, format):  # real signature unknown; restored from __doc__
        """
        strptime(string, format) -> struct_time

        Parse a string to a time tuple according to a format specification.
        See the library reference manual for formatting codes (same as
        strftime()).

        Commonly used format codes:

        %Y  Year with century as a decimal number.
        %m  Month as a decimal number [01,12].
        %d  Day of the month as a decimal number [01,31].
        %H  Hour (24-hour clock) as a decimal number [00,23].
        %M  Minute as a decimal number [00,59].
        %S  Second as a decimal number [00,61].
        %z  Time zone offset from UTC.
        %a  Locale's abbreviated weekday name.
        %A  Locale's full weekday name.
        %b  Locale's abbreviated month name.
        %B  Locale's full month name.
        %c  Locale's appropriate date and time representation.
        %I  Hour (12-hour clock) as a decimal number [01,12].
        %p  Locale's equivalent of either AM or PM.

        Other codes may be available on your platform.  See documentation for
        the C library strftime function.
        """
        return struct_time

    def thread_time():  # real signature unknown; restored from __doc__
        """
        thread_time() -> float

        Thread time for profiling: sum of the kernel and user-space CPU time.
        """
        return 0.0

    def thread_time_ns(*args, **kwargs):  # real signature unknown
        """
        thread_time() -> int

        Thread time for profiling as nanoseconds:
        sum of the kernel and user-space CPU time.
        """
        pass

    def time():  # real signature unknown; restored from __doc__
        """
        time() -> floating point number

        Return the current time in seconds since the Epoch.
        Fractions of a second may be present if the system clock provides them.
        """
        return 0.0

    def time_ns():  # real signature unknown; restored from __doc__
        """
        time_ns() -> int

        Return the current time in nanoseconds since the Epoch.
        """
        return 0

    def tzset():  # real signature unknown; restored from __doc__
        """
        tzset()

        Initialize, or reinitialize, the local timezone to the value stored in
        os.environ['TZ']. The TZ environment variable should be specified in
        standard Unix timezone format as documented in the tzset man page
        (eg. 'US/Eastern', 'Europe/Amsterdam'). Unknown timezones will silently
        fall back to UTC. If the TZ environment variable is not set, the local
        timezone is set to the systems best guess of wallclock time.
        Changing the TZ environment variable without calling tzset *may* change
        the local timezone used by methods such as localtime, but this behaviour
        should not be relied on.
        """
        pass

    # classes

    class struct_time(tuple):
        """
        The time value as returned by gmtime(), localtime(), and strptime(), and
         accepted by asctime(), mktime() and strftime().  May be considered as a
         sequence of 9 integers.

         Note that several fields' values are not the same as those defined by
         the C language standard for struct tm.  For example, the value of the
         field tm_year is the actual year, not year - 1900.  See individual
         fields' descriptions for details.
        """

        def __init__(self, *args, **kwargs):  # real signature unknown
            pass

        @staticmethod  # known case of __new__
        def __new__(*args, **kwargs):  # real signature unknown
            """ Create and return a new object.  See help(type) for accurate signature. """
            pass

        def __reduce__(self, *args, **kwargs):  # real signature unknown
            pass

        def __repr__(self, *args, **kwargs):  # real signature unknown
            """ Return repr(self). """
            pass

        tm_gmtoff = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
        """offset from UTC in seconds"""

        tm_hour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
        """hours, range [0, 23]"""

        tm_isdst = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
        """1 if summer time is in effect, 0 if not, and -1 if unknown"""

        tm_mday = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
        """day of month, range [1, 31]"""

        tm_min = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
        """minutes, range [0, 59]"""

        tm_mon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
        """month of year, range [1, 12]"""

        tm_sec = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
        """seconds, range [0, 61])"""

        tm_wday = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
        """day of week, range [0, 6], Monday is 0"""

        tm_yday = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
        """day of year, range [1, 366]"""

        tm_year = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
        """year, for example, 1993"""

        tm_zone = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
        """abbreviation of timezone name"""

        n_fields = 11
        n_sequence_fields = 9
        n_unnamed_fields = 0

    class __loader__(object):
        """
        Meta path import for built-in modules.

            All methods are either class or static methods to avoid the need to
            instantiate the class.
        """

        @classmethod
        def create_module(cls, *args, **kwargs):  # real signature unknown
            """ Create a built-in module """
            pass

        @classmethod
        def exec_module(cls, *args, **kwargs):  # real signature unknown
            """ Exec a built-in module """
            pass

        @classmethod
        def find_module(cls, *args, **kwargs):  # real signature unknown
            """
            Find the built-in module.

                    If 'path' is ever specified then the search is considered a failure.

                    This method is deprecated.  Use find_spec() instead.
            """
            pass

        @classmethod
        def find_spec(cls, *args, **kwargs):  # real signature unknown
            pass

        @classmethod
        def get_code(cls, *args, **kwargs):  # real signature unknown
            """ Return None as built-in modules do not have code objects. """
            pass

        @classmethod
        def get_source(cls, *args, **kwargs):  # real signature unknown
            """ Return None as built-in modules do not have source code. """
            pass

        @classmethod
        def is_package(cls, *args, **kwargs):  # real signature unknown
            """ Return False as built-in modules are never packages. """
            pass

        @classmethod
        def load_module(cls, *args, **kwargs):  # real signature unknown
            """
            Load the specified module into sys.modules and return it.

                This method is deprecated.  Use loader.exec_module instead.
            """
            pass

        def module_repr(module):  # reliably restored by inspect
            """
            Return repr for the module.

                    The method is deprecated.  The import machinery does the job itself.
            """
            pass

        def __init__(self, *args, **kwargs):  # real signature unknown
            pass

        __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
        """list of weak references to the object (if defined)"""

        __dict__ = None  # (!) real value is "mappingproxy({'__module__': '_frozen_importlib', '__doc__': 'Meta path import for built-in modules.\\n\\n    All methods are either class or static methods to avoid the need to\\n    instantiate the class.\\n\\n    ', 'module_repr': <staticmethod object at 0x7f5ae0fac430>, 'find_spec': <classmethod object at 0x7f5ae0fac460>, 'find_module': <classmethod object at 0x7f5ae0fac490>, 'create_module': <classmethod object at 0x7f5ae0fac4c0>, 'exec_module': <classmethod object at 0x7f5ae0fac4f0>, 'get_code': <classmethod object at 0x7f5ae0fac580>, 'get_source': <classmethod object at 0x7f5ae0fac610>, 'is_package': <classmethod object at 0x7f5ae0fac6a0>, 'load_module': <classmethod object at 0x7f5ae0fac6d0>, '__dict__': <attribute '__dict__' of 'BuiltinImporter' objects>, '__weakref__': <attribute '__weakref__' of 'BuiltinImporter' objects>})"

    # variables with complex values

    tzname = (
        'IST',
        'IST',
    )

    __spec__ = None  # (!) real value is "ModuleSpec(name='time', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"


# '

_names = sys.builtin_module_names

# Note:  more names are added to __all__ later.
__all__ = ["altsep", "curdir", "pardir", "sep", "pathsep", "linesep",
           "defpath", "name", "path", "devnull", "SEEK_SET", "SEEK_CUR",
           "SEEK_END", "fsencode", "fsdecode", "get_exec_path", "fdopen",
           "popen", "extsep"]


def _exists(name):
    return name in globals()


def _get_exports_list(module):
    try:
        return list(module.__all__)
    except AttributeError:
        return [n for n in dir(module) if n[0] != '_']


# Any new dependencies of the os module and/or changes in path separator
# requires updating importlib as well.
if 'posix' in _names:
    name = 'posix'
    linesep = '\n'
    from posix import *

    try:
        from posix import _exit

        __all__.append('_exit')
    except ImportError:
        pass
    import posixpath as path

    try:
        from posix import _have_functions
    except ImportError:
        pass

    import posix

    __all__.extend(_get_exports_list(posix))
    del posix

elif 'nt' in _names:
    name = 'nt'
    linesep = '\r\n'
    from nt import *

    try:
        from nt import _exit

        __all__.append('_exit')
    except ImportError:
        pass
    import ntpath as path

    import nt

    __all__.extend(_get_exports_list(nt))
    del nt

    try:
        from nt import _have_functions
    except ImportError:
        pass

else:
    raise ImportError('no os specific module found')

sys.modules['os.path'] = path
from os.path import (curdir, pardir, sep, pathsep, defpath, extsep, altsep,
                     devnull)

del _names

if _exists("_have_functions"):
    _globals = globals()


    def _add(str, fn):
        if (fn in _globals) and (str in _have_functions):
            _set.add(_globals[fn])


    _set = set()
    _add("HAVE_FACCESSAT", "access")
    _add("HAVE_FCHMODAT", "chmod")
    _add("HAVE_FCHOWNAT", "chown")
    _add("HAVE_FSTATAT", "stat")
    _add("HAVE_FUTIMESAT", "utime")
    _add("HAVE_LINKAT", "link")
    _add("HAVE_MKDIRAT", "mkdir")
    _add("HAVE_MKFIFOAT", "mkfifo")
    _add("HAVE_MKNODAT", "mknod")
    _add("HAVE_OPENAT", "open")
    _add("HAVE_READLINKAT", "readlink")
    _add("HAVE_RENAMEAT", "rename")
    _add("HAVE_SYMLINKAT", "symlink")
    _add("HAVE_UNLINKAT", "unlink")
    _add("HAVE_UNLINKAT", "rmdir")
    _add("HAVE_UTIMENSAT", "utime")
    supports_dir_fd = _set

    _set = set()
    _add("HAVE_FACCESSAT", "access")
    supports_effective_ids = _set

    _set = set()
    _add("HAVE_FCHDIR", "chdir")
    _add("HAVE_FCHMOD", "chmod")
    _add("HAVE_FCHOWN", "chown")
    _add("HAVE_FDOPENDIR", "listdir")
    _add("HAVE_FDOPENDIR", "scandir")
    _add("HAVE_FEXECVE", "execve")
    _set.add(stat)  # fstat always works
    _add("HAVE_FTRUNCATE", "truncate")
    _add("HAVE_FUTIMENS", "utime")
    _add("HAVE_FUTIMES", "utime")
    _add("HAVE_FPATHCONF", "pathconf")
    if _exists("statvfs") and _exists("fstatvfs"):  # mac os x10.3
        _add("HAVE_FSTATVFS", "statvfs")
    supports_fd = _set

    _set = set()
    _add("HAVE_FACCESSAT", "access")
    # Some platforms don't support lchmod().  Often the function exists
    # anyway, as a stub that always returns ENOSUP or perhaps EOPNOTSUPP.
    # (No, I don't know why that's a good design.)  ./configure will detect
    # this and reject it--so HAVE_LCHMOD still won't be defined on such
    # platforms.  This is Very Helpful.
    #
    # However, sometimes platforms without a working lchmod() *do* have
    # fchmodat().  (Examples: Linux kernel 3.2 with glibc 2.15,
    # OpenIndiana 3.x.)  And fchmodat() has a flag that theoretically makes
    # it behave like lchmod().  So in theory it would be a suitable
    # replacement for lchmod().  But when lchmod() doesn't work, fchmodat()'s
    # flag doesn't work *either*.  Sadly ./configure isn't sophisticated
    # enough to detect this condition--it only determines whether or not
    # fchmodat() minimally works.
    #
    # Therefore we simply ignore fchmodat() when deciding whether or not
    # os.chmod supports follow_symlinks.  Just checking lchmod() is
    # sufficient.  After all--if you have a working fchmodat(), your
    # lchmod() almost certainly works too.
    #
    # _add("HAVE_FCHMODAT",   "chmod")
    _add("HAVE_FCHOWNAT", "chown")
    _add("HAVE_FSTATAT", "stat")
    _add("HAVE_LCHFLAGS", "chflags")
    _add("HAVE_LCHMOD", "chmod")
    if _exists("lchown"):  # mac os x10.3
        _add("HAVE_LCHOWN", "chown")
    _add("HAVE_LINKAT", "link")
    _add("HAVE_LUTIMES", "utime")
    _add("HAVE_LSTAT", "stat")
    _add("HAVE_FSTATAT", "stat")
    _add("HAVE_UTIMENSAT", "utime")
    _add("MS_WINDOWS", "stat")
    supports_follow_symlinks = _set

    del _set
    del _have_functions
    del _globals
    del _add

# Python uses fixed values for the SEEK_ constants; they are mapped
# to native constants if necessary in posixmodule.c
# Other possible SEEK values are directly imported from posixmodule.c
SEEK_SET = 0
SEEK_CUR = 1
SEEK_END = 2


# Super directory utilities.
# (Inspired by Eric Raymond; the doc strings are mostly his)

def makedirs(name, mode=0o777, exist_ok=False):
    """makedirs(name [, mode=0o777][, exist_ok=False])

    Super-mkdir; create a leaf directory and all intermediate ones.  Works like
    mkdir, except that any intermediate path segment (not just the rightmost)
    will be created if it does not exist. If the target directory already
    exists, raise an OSError if exist_ok is False. Otherwise no exception is
    raised.  This is recursive.

    """
    head, tail = path.split(name)
    if not tail:
        head, tail = path.split(head)
    if head and tail and not path.exists(head):
        try:
            makedirs(head, exist_ok=exist_ok)
        except FileExistsError:
            # Defeats race condition when another thread created the path
            pass
        cdir = curdir
        if isinstance(tail, bytes):
            cdir = bytes(curdir, 'ASCII')
        if tail == cdir:  # xxx/newdir/. exists if xxx/newdir exists
            return
    try:
        mkdir(name, mode)
    except OSError:
        # Cannot rely on checking for EEXIST, since the operating system
        # could give priority to other errors like EACCES or EROFS
        if not exist_ok or not path.isdir(name):
            raise


def removedirs(name):
    """removedirs(name)

    Super-rmdir; remove a leaf directory and all empty intermediate
    ones.  Works like rmdir except that, if the leaf directory is
    successfully removed, directories corresponding to rightmost path
    segments will be pruned away until either the whole path is
    consumed or an error occurs.  Errors during this latter phase are
    ignored -- they generally mean that a directory was not empty.

    """
    rmdir(name)
    head, tail = path.split(name)
    if not tail:
        head, tail = path.split(head)
    while head and tail:
        try:
            rmdir(head)
        except OSError:
            break
        head, tail = path.split(head)


def renames(old, new):
    """renames(old, new)

    Super-rename; create directories as necessary and delete any left
    empty.  Works like rename, except creation of any intermediate
    directories needed to make the new pathname good is attempted
    first.  After the rename, directories corresponding to rightmost
    path segments of the old name will be pruned until either the
    whole path is consumed or a nonempty directory is found.

    Note: this function can fail with the new directory structure made
    if you lack permissions needed to unlink the leaf directory or
    file.

    """
    head, tail = path.split(new)
    if head and tail and not path.exists(head):
        makedirs(head)
    rename(old, new)
    head, tail = path.split(old)
    if head and tail:
        try:
            removedirs(head)
        except OSError:
            pass


__all__.extend(["makedirs", "removedirs", "renames"])


def walk(top, topdown=True, onerror=None, followlinks=False):
    """Directory tree generator.

    For each directory in the directory tree rooted at top (including top
    itself, but excluding '.' and '..'), yields a 3-tuple

        dirpath, dirnames, filenames

    dirpath is a string, the path to the directory.  dirnames is a list of
    the names of the subdirectories in dirpath (excluding '.' and '..').
    filenames is a list of the names of the non-directory files in dirpath.
    Note that the names in the lists are just names, with no path components.
    To get a full path (which begins with top) to a file or directory in
    dirpath, do os.path.join(dirpath, name).

    If optional arg 'topdown' is true or not specified, the triple for a
    directory is generated before the triples for any of its subdirectories
    (directories are generated top down).  If topdown is false, the triple
    for a directory is generated after the triples for all of its
    subdirectories (directories are generated bottom up).

    When topdown is true, the caller can modify the dirnames list in-place
    (e.g., via del or slice assignment), and walk will only recurse into the
    subdirectories whose names remain in dirnames; this can be used to prune the
    search, or to impose a specific order of visiting.  Modifying dirnames when
    topdown is false has no effect on the behavior of os.walk(), since the
    directories in dirnames have already been generated by the time dirnames
    itself is generated. No matter the value of topdown, the list of
    subdirectories is retrieved before the tuples for the directory and its
    subdirectories are generated.

    By default errors from the os.scandir() call are ignored.  If
    optional arg 'onerror' is specified, it should be a function; it
    will be called with one argument, an OSError instance.  It can
    report the error to continue with the walk, or raise the exception
    to abort the walk.  Note that the filename is available as the
    filename attribute of the exception object.

    By default, os.walk does not follow symbolic links to subdirectories on
    systems that support them.  In order to get this functionality, set the
    optional argument 'followlinks' to true.

    Caution:  if you pass a relative pathname for top, don't change the
    current working directory between resumptions of walk.  walk never
    changes the current directory, and assumes that the client doesn't
    either.

    Example:

    import os
    from os.path import join, getsize
    for root, dirs, files in os.walk('python/Lib/email'):
        print(root, "consumes", end="")
        print(sum(getsize(join(root, name)) for name in files), end="")
        print("bytes in", len(files), "non-directory files")
        if 'CVS' in dirs:
            dirs.remove('CVS')  # don't visit CVS directories

    """
    top = fspath(top)
    dirs = []
    nondirs = []
    walk_dirs = []

    # We may not have read permission for top, in which case we can't
    # get a list of the files the directory contains.  os.walk
    # always suppressed the exception then, rather than blow up for a
    # minor reason when (say) a thousand readable directories are still
    # left to visit.  That logic is copied here.
    try:
        # Note that scandir is global in this module due
        # to earlier import-*.
        scandir_it = scandir(top)
    except OSError as error:
        if onerror is not None:
            onerror(error)
        return

    with scandir_it:
        while True:
            try:
                try:
                    entry = next(scandir_it)
                except StopIteration:
                    break
            except OSError as error:
                if onerror is not None:
                    onerror(error)
                return

            try:
                is_dir = entry.is_dir()
            except OSError:
                # If is_dir() raises an OSError, consider that the entry is not
                # a directory, same behaviour than os.path.isdir().
                is_dir = False

            if is_dir:
                dirs.append(entry.name)
            else:
                nondirs.append(entry.name)

            if not topdown and is_dir:
                # Bottom-up: recurse into sub-directory, but exclude symlinks to
                # directories if followlinks is False
                if followlinks:
                    walk_into = True
                else:
                    try:
                        is_symlink = entry.is_symlink()
                    except OSError:
                        # If is_symlink() raises an OSError, consider that the
                        # entry is not a symbolic link, same behaviour than
                        # os.path.islink().
                        is_symlink = False
                    walk_into = not is_symlink

                if walk_into:
                    walk_dirs.append(entry.path)

    # Yield before recursion if going top down
    if topdown:
        yield top, dirs, nondirs

        # Recurse into sub-directories
        islink, join = path.islink, path.join
        for dirname in dirs:
            new_path = join(top, dirname)
            # Issue #23605: os.path.islink() is used instead of caching
            # entry.is_symlink() result during the loop on os.scandir() because
            # the caller can replace the directory entry during the "yield"
            # above.
            if followlinks or not islink(new_path):
                yield from walk(new_path, topdown, onerror, followlinks)
    else:
        # Recurse into sub-directories
        for new_path in walk_dirs:
            yield from walk(new_path, topdown, onerror, followlinks)
        # Yield after recursion if going bottom up
        yield top, dirs, nondirs


__all__.append("walk")

if {open, stat} <= supports_dir_fd and {scandir, stat} <= supports_fd:

    def fwalk(top=".", topdown=True, onerror=None, *, follow_symlinks=False, dir_fd=None):
        """Directory tree generator.

        This behaves exactly like walk(), except that it yields a 4-tuple

            dirpath, dirnames, filenames, dirfd

        `dirpath`, `dirnames` and `filenames` are identical to walk() output,
        and `dirfd` is a file descriptor referring to the directory `dirpath`.

        The advantage of fwalk() over walk() is that it's safe against symlink
        races (when follow_symlinks is False).

        If dir_fd is not None, it should be a file descriptor open to a directory,
          and top should be relative; top will then be relative to that directory.
          (dir_fd is always supported for fwalk.)

        Caution:
        Since fwalk() yields file descriptors, those are only valid until the
        next iteration step, so you should dup() them if you want to keep them
        for a longer period.

        Example:

        import os
        for root, dirs, files, rootfd in os.fwalk('python/Lib/email'):
            print(root, "consumes", end="")
            print(sum(os.stat(name, dir_fd=rootfd).st_size for name in files),
                  end="")
            print("bytes in", len(files), "non-directory files")
            if 'CVS' in dirs:
                dirs.remove('CVS')  # don't visit CVS directories
        """
        if not isinstance(top, int) or not hasattr(top, '__index__'):
            top = fspath(top)
        # Note: To guard against symlink races, we use the standard
        # lstat()/open()/fstat() trick.
        if not follow_symlinks:
            orig_st = stat(top, follow_symlinks=False, dir_fd=dir_fd)
        topfd = open(top, O_RDONLY, dir_fd=dir_fd)
        try:
            if (follow_symlinks or (st.S_ISDIR(orig_st.st_mode) and
                                    path.samestat(orig_st, stat(topfd)))):
                yield from _fwalk(topfd, top, isinstance(top, bytes),
                                  topdown, onerror, follow_symlinks)
        finally:
            close(topfd)


    def _fwalk(topfd, toppath, isbytes, topdown, onerror, follow_symlinks):
        # Note: This uses O(depth of the directory tree) file descriptors: if
        # necessary, it can be adapted to only require O(1) FDs, see issue
        # #13734.

        scandir_it = scandir(topfd)
        dirs = []
        nondirs = []
        entries = None if topdown or follow_symlinks else []
        for entry in scandir_it:
            name = entry.name
            if isbytes:
                name = fsencode(name)
            try:
                if entry.is_dir():
                    dirs.append(name)
                    if entries is not None:
                        entries.append(entry)
                else:
                    nondirs.append(name)
            except OSError:
                try:
                    # Add dangling symlinks, ignore disappeared files
                    if entry.is_symlink():
                        nondirs.append(name)
                except OSError:
                    pass

        if topdown:
            yield toppath, dirs, nondirs, topfd

        for name in dirs if entries is None else zip(dirs, entries):
            try:
                if not follow_symlinks:
                    if topdown:
                        orig_st = stat(name, dir_fd=topfd, follow_symlinks=False)
                    else:
                        assert entries is not None
                        name, entry = name
                        orig_st = entry.stat(follow_symlinks=False)
                dirfd = open(name, O_RDONLY, dir_fd=topfd)
            except OSError as err:
                if onerror is not None:
                    onerror(err)
                continue
            try:
                if follow_symlinks or path.samestat(orig_st, stat(dirfd)):
                    dirpath = path.join(toppath, name)
                    yield from _fwalk(dirfd, dirpath, isbytes,
                                      topdown, onerror, follow_symlinks)
            finally:
                close(dirfd)

        if not topdown:
            yield toppath, dirs, nondirs, topfd


    __all__.append("fwalk")


def execl(file, *args):
    """execl(file, *args)

    Execute the executable file with argument list args, replacing the
    current process. """
    execv(file, args)


def execle(file, *args):
    """execle(file, *args, env)

    Execute the executable file with argument list args and
    environment env, replacing the current process. """
    env = args[-1]
    execve(file, args[:-1], env)


def execlp(file, *args):
    """execlp(file, *args)

    Execute the executable file (which is searched for along $PATH)
    with argument list args, replacing the current process. """
    execvp(file, args)


def execlpe(file, *args):
    """execlpe(file, *args, env)

    Execute the executable file (which is searched for along $PATH)
    with argument list args and environment env, replacing the current
    process. """
    env = args[-1]
    execvpe(file, args[:-1], env)


def execvp(file, args):
    """execvp(file, args)

    Execute the executable file (which is searched for along $PATH)
    with argument list args, replacing the current process.
    args may be a list or tuple of strings. """
    _execvpe(file, args)


def execvpe(file, args, env):
    """execvpe(file, args, env)

    Execute the executable file (which is searched for along $PATH)
    with argument list args and environment env, replacing the
    current process.
    args may be a list or tuple of strings. """
    _execvpe(file, args, env)


__all__.extend(["execl", "execle", "execlp", "execlpe", "execvp", "execvpe"])


def _execvpe(file, args, env=None):
    if env is not None:
        exec_func = execve
        argrest = (args, env)
    else:
        exec_func = execv
        argrest = (args,)
        env = environ

    if path.dirname(file):
        exec_func(file, *argrest)
        return
    saved_exc = None
    path_list = get_exec_path(env)
    if name != 'nt':
        file = fsencode(file)
        path_list = map(fsencode, path_list)
    for dir in path_list:
        fullname = path.join(dir, file)
        try:
            exec_func(fullname, *argrest)
        except (FileNotFoundError, NotADirectoryError) as e:
            last_exc = e
        except OSError as e:
            last_exc = e
            if saved_exc is None:
                saved_exc = e
    if saved_exc is not None:
        raise saved_exc
    raise last_exc


def get_exec_path(env=None):
    """Returns the sequence of directories that will be searched for the
    named executable (similar to a shell) when launching a process.

    *env* must be an environment variable dict or None.  If *env* is None,
    os.environ will be used.
    """
    # Use a local import instead of a global import to limit the number of
    # modules loaded at startup: the os module is always loaded at startup by
    # Python. It may also avoid a bootstrap issue.
    import warnings

    if env is None:
        env = environ

    # {b'PATH': ...}.get('PATH') and {'PATH': ...}.get(b'PATH') emit a
    # BytesWarning when using python -b or python -bb: ignore the warning
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", BytesWarning)

        try:
            path_list = env.get('PATH')
        except TypeError:
            path_list = None

        if supports_bytes_environ:
            try:
                path_listb = env[b'PATH']
            except (KeyError, TypeError):
                pass
            else:
                if path_list is not None:
                    raise ValueError(
                        "env cannot contain 'PATH' and b'PATH' keys")
                path_list = path_listb

            if path_list is not None and isinstance(path_list, bytes):
                path_list = fsdecode(path_list)

    if path_list is None:
        path_list = defpath
    return path_list.split(pathsep)


# Change environ to automatically call putenv(), unsetenv if they exist.
from _collections_abc import MutableMapping


class _Environ(MutableMapping):
    def __init__(self, data, encodekey, decodekey, encodevalue, decodevalue, putenv, unsetenv):
        self.encodekey = encodekey
        self.decodekey = decodekey
        self.encodevalue = encodevalue
        self.decodevalue = decodevalue
        self.putenv = putenv
        self.unsetenv = unsetenv
        self._data = data

    def __getitem__(self, key):
        try:
            value = self._data[self.encodekey(key)]
        except KeyError:
            # raise KeyError with the original key value
            raise KeyError(key) from None
        return self.decodevalue(value)

    def __setitem__(self, key, value):
        key = self.encodekey(key)
        value = self.encodevalue(value)
        self.putenv(key, value)
        self._data[key] = value

    def __delitem__(self, key):
        encodedkey = self.encodekey(key)
        self.unsetenv(encodedkey)
        try:
            del self._data[encodedkey]
        except KeyError:
            # raise KeyError with the original key value
            raise KeyError(key) from None

    def __iter__(self):
        # list() from dict object is an atomic operation
        keys = list(self._data)
        for key in keys:
            yield self.decodekey(key)

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return 'environ({{{}}})'.format(', '.join(
            ('{!r}: {!r}'.format(self.decodekey(key), self.decodevalue(value))
             for key, value in self._data.items())))

    def copy(self):
        return dict(self)

    def setdefault(self, key, value):
        if key not in self:
            self[key] = value
        return self[key]


try:
    _putenv = putenv
except NameError:
    _putenv = lambda key, value: None
else:
    if "putenv" not in __all__:
        __all__.append("putenv")

try:
    _unsetenv = unsetenv
except NameError:
    _unsetenv = lambda key: _putenv(key, "")
else:
    if "unsetenv" not in __all__:
        __all__.append("unsetenv")


def _createenviron():
    if name == 'nt':
        # Where Env Var Names Must Be UPPERCASE
        def check_str(value):
            if not isinstance(value, str):
                raise TypeError("str expected, not %s" % type(value).__name__)
            return value

        encode = check_str
        decode = str

        def encodekey(key):
            return encode(key).upper()

        data = {}
        for key, value in environ.items():
            data[encodekey(key)] = value
    else:
        # Where Env Var Names Can Be Mixed Case
        encoding = sys.getfilesystemencoding()

        def encode(value):
            if not isinstance(value, str):
                raise TypeError("str expected, not %s" % type(value).__name__)
            return value.encode(encoding, 'surrogateescape')

        def decode(value):
            return value.decode(encoding, 'surrogateescape')

        encodekey = encode
        data = environ
    return _Environ(data,
                    encodekey, decode,
                    encode, decode,
                    _putenv, _unsetenv)


# unicode environ
environ = _createenviron()
del _createenviron


def getenv(key, default=None):
    """Get an environment variable, return None if it doesn't exist.
    The optional second argument can specify an alternate default.
    key, default and the result are str."""
    return environ.get(key, default)


supports_bytes_environ = (name != 'nt')
__all__.extend(("getenv", "supports_bytes_environ"))

if supports_bytes_environ:
    def _check_bytes(value):
        if not isinstance(value, bytes):
            raise TypeError("bytes expected, not %s" % type(value).__name__)
        return value


    # bytes environ
    environb = _Environ(environ._data,
                        _check_bytes, bytes,
                        _check_bytes, bytes,
                        _putenv, _unsetenv)
    del _check_bytes


    def getenvb(key, default=None):
        """Get an environment variable, return None if it doesn't exist.
        The optional second argument can specify an alternate default.
        key, default and the result are bytes."""
        return environb.get(key, default)


    __all__.extend(("environb", "getenvb"))


def _fscodec():
    encoding = sys.getfilesystemencoding()
    errors = sys.getfilesystemencodeerrors()

    def fsencode(filename):
        """Encode filename (an os.PathLike, bytes, or str) to the filesystem
        encoding with 'surrogateescape' error handler, return bytes unchanged.
        On Windows, use 'strict' error handler if the file system encoding is
        'mbcs' (which is the default encoding).
        """
        filename = fspath(filename)  # Does type-checking of `filename`.
        if isinstance(filename, str):
            return filename.encode(encoding, errors)
        else:
            return filename

    def fsdecode(filename):
        """Decode filename (an os.PathLike, bytes, or str) from the filesystem
        encoding with 'surrogateescape' error handler, return str unchanged. On
        Windows, use 'strict' error handler if the file system encoding is
        'mbcs' (which is the default encoding).
        """
        filename = fspath(filename)  # Does type-checking of `filename`.
        if isinstance(filename, bytes):
            return filename.decode(encoding, errors)
        else:
            return filename

    return fsencode, fsdecode


fsencode, fsdecode = _fscodec()
del _fscodec

# Supply spawn*() (probably only for Unix)
if _exists("fork") and not _exists("spawnv") and _exists("execv"):

    P_WAIT = 0
    P_NOWAIT = P_NOWAITO = 1

    __all__.extend(["P_WAIT", "P_NOWAIT", "P_NOWAITO"])


    # XXX Should we support P_DETACH?  I suppose it could fork()**2
    # and close the std I/O streams.  Also, P_OVERLAY is the same
    # as execv*()?

    def _spawnvef(mode, file, args, env, func):
        # Internal helper; func is the exec*() function to use
        if not isinstance(args, (tuple, list)):
            raise TypeError('argv must be a tuple or a list')
        if not args or not args[0]:
            raise ValueError('argv first element cannot be empty')
        pid = fork()
        if not pid:
            # Child
            try:
                if env is None:
                    func(file, args)
                else:
                    func(file, args, env)
            except:
                _exit(127)
        else:
            # Parent
            if mode == P_NOWAIT:
                return pid  # Caller is responsible for waiting!
            while 1:
                wpid, sts = waitpid(pid, 0)
                if WIFSTOPPED(sts):
                    continue
                elif WIFSIGNALED(sts):
                    return -WTERMSIG(sts)
                elif WIFEXITED(sts):
                    return WEXITSTATUS(sts)
                else:
                    raise OSError("Not stopped, signaled or exited???")


    def spawnv(mode, file, args):
        """spawnv(mode, file, args) -> integer

Execute file with arguments from args in a subprocess.
If mode == P_NOWAIT return the pid of the process.
If mode == P_WAIT return the process's exit code if it exits normally;
otherwise return -SIG, where SIG is the signal that killed it. """
        return _spawnvef(mode, file, args, None, execv)


    def spawnve(mode, file, args, env):
        """spawnve(mode, file, args, env) -> integer

Execute file with arguments from args in a subprocess with the
specified environment.
If mode == P_NOWAIT return the pid of the process.
If mode == P_WAIT return the process's exit code if it exits normally;
otherwise return -SIG, where SIG is the signal that killed it. """
        return _spawnvef(mode, file, args, env, execve)


    # Note: spawnvp[e] isn't currently supported on Windows

    def spawnvp(mode, file, args):
        """spawnvp(mode, file, args) -> integer

Execute file (which is looked for along $PATH) with arguments from
args in a subprocess.
If mode == P_NOWAIT return the pid of the process.
If mode == P_WAIT return the process's exit code if it exits normally;
otherwise return -SIG, where SIG is the signal that killed it. """
        return _spawnvef(mode, file, args, None, execvp)


    def spawnvpe(mode, file, args, env):
        """spawnvpe(mode, file, args, env) -> integer

Execute file (which is looked for along $PATH) with arguments from
args in a subprocess with the supplied environment.
If mode == P_NOWAIT return the pid of the process.
If mode == P_WAIT return the process's exit code if it exits normally;
otherwise return -SIG, where SIG is the signal that killed it. """
        return _spawnvef(mode, file, args, env, execvpe)


    __all__.extend(["spawnv", "spawnve", "spawnvp", "spawnvpe"])

if _exists("spawnv"):
    # These aren't supplied by the basic Windows code
    # but can be easily implemented in Python

    def spawnl(mode, file, *args):
        """spawnl(mode, file, *args) -> integer

Execute file with arguments from args in a subprocess.
If mode == P_NOWAIT return the pid of the process.
If mode == P_WAIT return the process's exit code if it exits normally;
otherwise return -SIG, where SIG is the signal that killed it. """
        return spawnv(mode, file, args)


    def spawnle(mode, file, *args):
        """spawnle(mode, file, *args, env) -> integer

Execute file with arguments from args in a subprocess with the
supplied environment.
If mode == P_NOWAIT return the pid of the process.
If mode == P_WAIT return the process's exit code if it exits normally;
otherwise return -SIG, where SIG is the signal that killed it. """
        env = args[-1]
        return spawnve(mode, file, args[:-1], env)


    __all__.extend(["spawnl", "spawnle"])

if _exists("spawnvp"):
    # At the moment, Windows doesn't implement spawnvp[e],
    # so it won't have spawnlp[e] either.
    def spawnlp(mode, file, *args):
        """spawnlp(mode, file, *args) -> integer

Execute file (which is looked for along $PATH) with arguments from
args in a subprocess with the supplied environment.
If mode == P_NOWAIT return the pid of the process.
If mode == P_WAIT return the process's exit code if it exits normally;
otherwise return -SIG, where SIG is the signal that killed it. """
        return spawnvp(mode, file, args)


    def spawnlpe(mode, file, *args):
        """spawnlpe(mode, file, *args, env) -> integer

Execute file (which is looked for along $PATH) with arguments from
args in a subprocess with the supplied environment.
If mode == P_NOWAIT return the pid of the process.
If mode == P_WAIT return the process's exit code if it exits normally;
otherwise return -SIG, where SIG is the signal that killed it. """
        env = args[-1]
        return spawnvpe(mode, file, args[:-1], env)


    __all__.extend(["spawnlp", "spawnlpe"])


# Supply os.popen()
def popen(cmd, mode="r", buffering=-1):
    if not isinstance(cmd, str):
        raise TypeError("invalid cmd type (%s, expected string)" % type(cmd))
    if mode not in ("r", "w"):
        raise ValueError("invalid mode %r" % mode)
    if buffering == 0 or buffering is None:
        raise ValueError("popen() does not support unbuffered streams")
    import subprocess, io
    if mode == "r":
        proc = subprocess.Popen(cmd,
                                shell=True,
                                stdout=subprocess.PIPE,
                                bufsize=buffering)
        return _wrap_close(io.TextIOWrapper(proc.stdout), proc)
    else:
        proc = subprocess.Popen(cmd,
                                shell=True,
                                stdin=subprocess.PIPE,
                                bufsize=buffering)
        return _wrap_close(io.TextIOWrapper(proc.stdin), proc)


# Helper for popen() -- a proxy for a file whose close waits for the process
class _wrap_close:
    def __init__(self, stream, proc):
        self._stream = stream
        self._proc = proc

    def close(self):
        self._stream.close()
        returncode = self._proc.wait()
        if returncode == 0:
            return None
        if name == 'nt':
            return returncode
        else:
            return returncode << 8  # Shift left to match old behavior

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

    def __getattr__(self, name):
        return getattr(self._stream, name)

    def __iter__(self):
        return iter(self._stream)


# Supply os.fdopen()
def fdopen(fd, *args, **kwargs):
    if not isinstance(fd, int):
        raise TypeError("invalid fd type (%s, expected integer)" % type(fd))
    import io
    return io.open(fd, *args, **kwargs)


# For testing purposes, make sure the function is available when the C
# implementation exists.
def _fspath(path):
    """Return the path representation of a path-like object.

    If str or bytes is passed in, it is returned unchanged. Otherwise the
    os.PathLike interface is used to get the path representation. If the
    path representation is not str or bytes, TypeError is raised. If the
    provided path is not str, bytes, or os.PathLike, TypeError is raised.
    """
    if isinstance(path, (str, bytes)):
        return path

    # Work from the object's type to match method resolution of other magic
    # methods.
    path_type = type(path)
    try:
        path_repr = path_type.__fspath__(path)
    except AttributeError:
        if hasattr(path_type, '__fspath__'):
            raise
        else:
            raise TypeError("expected str, bytes or os.PathLike object, "
                            "not " + path_type.__name__)
    if isinstance(path_repr, (str, bytes)):
        return path_repr
    else:
        raise TypeError("expected {}.__fspath__() to return str or bytes, "
                        "not {}".format(path_type.__name__,
                                        type(path_repr).__name__))


# If there is no C implementation, make the pure Python version the
# implementation as transparently as possible.
if not _exists('fspath'):
    fspath = _fspath
    fspath.__name__ = "fspath"


class PathLike(abc.ABC):
    """Abstract base class for implementing the file system path protocol."""

    @abc.abstractmethod
    def __fspath__(self):
        """Return the file system path representation of the object."""
        raise NotImplementedError

    @classmethod
    def __subclasshook__(cls, subclass):
        if cls is PathLike:
            return _check_methods(subclass, '__fspath__')
        return NotImplemented


if name == 'nt':
    class _AddedDllDirectory:
        def __init__(self, path, cookie, remove_dll_directory):
            self.path = path
            self._cookie = cookie
            self._remove_dll_directory = remove_dll_directory

        def close(self):
            self._remove_dll_directory(self._cookie)
            self.path = None

        def __enter__(self):
            return self

        def __exit__(self, *args):
            self.close()

        def __repr__(self):
            if self.path:
                return "<AddedDllDirectory({!r})>".format(self.path)
            return "<AddedDllDirectory()>"


    def add_dll_directory(path):
        """Add a path to the DLL search path.

        This search path is used when resolving dependencies for imported
        extension modules (the module itself is resolved through sys.path),
        and also by ctypes.

        Remove the directory by calling close() on the returned object or
        using it in a with statement.
        """
        import nt
        cookie = nt._add_dll_directory(path)
        return _AddedDllDirectory(
            path,
            cookie,
            nt._remove_dll_directory
        )


class Joel(object):
    class Runer(object):
        def __init__(self, function):
            self.name = "Runer"
            print("starting..")
            sleep(12)
            print(f"id : {id(function)}")

            try:
                function()
            except Exception as err:
                print(err)

            print("code finished")

    class EditAFile():
        @staticmethod
        def __init__(filename, word):
            with open(filename, "w") as file:
                file.write(word)

    class Find_The_Size_IN_Bytes(object):
        @classmethod
        def __init__(cls, function):
            cls.func = function

        @classmethod
        def process(cls):
            sys.getfileof(cls.func)

    class Gen(object):
        def __init__(self, number):
            self.num = number
            self.last = 0

        def __next__(self):
            return self.next()

        def next(self):
            if self.last == self.num + 1:
                raise StopIteration()
            rv = self.last ** 2
            self.last += 1
            return rv

    @staticmethod
    def timemmer(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            rv = func()
            total = time.time - start
            print("Time:", total)
            return rv

        return wrapper

    def __init__(self):
        self.adult = 20  # min
        self.teenager = 13  # min
        self.child = 12  # max
        self.name = "Joel"

    def __repr__(self):
        return f"{self.name}()"

    def __mut__(self, x):
        if type(x) is not int:
            raise Exception("please enter the correct value int")

        else:
            self.name = self.name * x

    def __sub__(self, y):
        if type(y) is not int:
            raise Exception("please enter the correct value int")

        else:
            self.name = self.name - y

    def __add__(self, z):
        if type(z) is not int:
            raise Exception("please enter the correct value int")

        else:
            self.name = self.name - z

    def __floordiv__(self, a):
        if type(a) is not int:
            raise Exception("please enter the correct value int")

        else:
            self.name = self.name - a

    def __len__(self):
        return len(self.name)

    class TypesOfAnimalsAndHumans(object):

        def __init__(self):
            self.name = "TypesOfAnimalsAndHumans"

        def __repr__(self):
            return f"{self.name}()"

        def __mut__(self, x):
            if type(x) is not int:
                raise Exception("please enter the correct value int")

            else:
                self.name = self.name * x

        def __sub__(self, y):
            if type(y) is not int:
                raise Exception("please enter the correct value int")

            else:
                self.name = self.name - y

        def __add__(self, z):
            if type(z) is not int:
                raise Exception("please enter the correct value int")

            else:
                self.name = self.name - z

        def __floordiv__(self, a):
            if type(a) is not int:
                raise Exception("please enter the correct value int")

            else:
                self.name = self.name - a

        def __len__(self):
            return len(self.name)

        class Human(object):
            name = ""
            age = 1

            def __init__(self, name, age, weight=0):
                self.name_human = name
                self.age = age
                self.weight = weight
                self.name = "Human"

            def __repr__(self):
                return f"{self.name}({self.name_human}, {self.age}, {self.weight})"

            def __mut__(self, x):
                if type(x) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name * x

            def __sub__(self, y):
                if type(y) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name - y

            def __add__(self, z):
                if type(z) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name - z

            def __floordiv__(self, a):
                if type(a) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name - a

            def __len__(self):
                return len(self.name)

            @staticmethod
            def type():
                print("I are a human")

            def info(self):
                self.age_info()
                self.name_info()

            def age_info(self):
                print("my name is " + self.name)

            def name_info(self):
                print("my age is ", self.age)

            def change_age(self, age):
                self.age = age

            def find_age(self):
                print(self.age)

            def find_name(self):
                print(self.name)

            def change_name(self, name):
                self.name = name

            def change_weight(self, weight):
                self.weight = weight

            def find_weight(self):
                print(self.weight)

        class Dog(object):
            name = ""
            age = 1

            def __init__(self, name, age, weight=0):
                self.name_dog = name
                self.age = age
                self.weight = weight
                self.name = "Dog"

            def __repr__(self):
                return f"{self.name}({self.name_dog}, {self.age}, {self.weight})"

            def __mut__(self, x):
                if type(x) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name * x

            def __sub__(self, y):
                if type(y) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name - y

            def __add__(self, z):
                if type(z) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name - z

            def __floordiv__(self, a):
                if type(a) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name - a

            def __len__(self):
                return len(self.name)

            def speak(self):
                self.dog_type()
                self.name_info()
                self.age_info()

            @staticmethod
            def type():
                print("I are a dog")

            def name_info(self):
                print("my name is " + self.name)

            def age_info(self):
                print("my age is ", self.age)

            def change_age(self, age):
                self.age = age

            def find_age(self):
                print(self.age)

            def find_name(self):
                print(self.name)

            def change_name(self, name):
                self.name = name

            def change_weight(self, weight):
                self.weight = weight

            def find_weight(self):
                print(self.weight)

        class Cat(object):
            name = ""
            age = 1

            def __init__(self, name, age, weight=0):
                self.name_cat = name
                self.age = age
                self.weight = weight
                self.name = "Cat"

            def __repr__(self):
                return f"{self.name}({self.name_cat}, {self.age}, {self.weight})"

            def __mut__(self, x):
                if type(x) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name * x

            def __sub__(self, y):
                if type(y) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name - y

            def __add__(self, z):
                if type(z) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name - z

            def __floordiv__(self, a):
                if type(a) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name - a

            def __len__(self):
                return len(self.name)

            def speak(self):
                self.cat_type()
                self.name_info()
                self.age_info()

            @staticmethod
            def type():
                print("I are a dog")

            def name_info(self):
                print("my name is " + self.name)

            def age_info(self):
                print("my age is ", self.age)

            def change_age(self, age):
                self.age = age

            def find_age(self):
                print(self.age)

            def find_name(self):
                print(self.name)

            def change_name(self, name):
                self.name = name

            def change_weight(self, weight):
                self.weight = weight

            def find_weight(self):
                print(self.weight)

        class Lion(object):

            def __init__(self, name, age, weight=0):
                self.name_lion = name
                self.age = age
                self.weight = weight
                self.name = "Lion"

            def __repr__(self):
                return f"{self.name}({self.name_lion}, {self.age}, {self.weight})"

            def __mut__(self, x):
                if type(x) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name * x

            def __sub__(self, y):
                if type(y) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name - y

            def __add__(self, z):
                if type(z) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name - z

            def __floordiv__(self, a):
                if type(a) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name - a

            def __len__(self):
                return len(self.name)

            def speak(self):
                self.lion_type()
                self.name_info()
                self.age_info()

            @staticmethod
            def type():
                a1 = "and i will eat rat"
                a2 = "and i will eat every one"
                a3 = ""
                ans = random.randrange(3)
                res = ""

                if ans == 1:
                    res = a1

                elif ans == 2:
                    res = a2

                else:
                    res = a3

                print("I are a lion and the king of the forest " + res)

            def name_info(self):
                print("my name is " + self.name)

            def age_info(self):
                print("my age is ", self.age)

            def change_age(self, age):
                self.age = age

            def find_age(self):
                print(self.age)

            def find_name(self):
                print(self.name)

            def change_name(self, name):
                self.name = name

            def change_weight(self, weight):
                self.weight = weight

            def find_weight(self):
                print(self.weight)

        class Rat(object):
            name = ""
            age = 1

            def __init__(self, name, age, weight=0):
                self.name_rat = name
                self.age = age
                self.weight = weight
                self.name = "Rat"

            def __repr__(self):
                return f"{self.name}({self.name_rat}, {self.age}, {self.weight})"

            def __mut__(self, x):
                if type(x) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name * x

            def __sub__(self, y):
                if type(y) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name - y

            def __add__(self, z):
                if type(z) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name - z

            def __floordiv__(self, a):
                if type(a) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name - a

            def __len__(self):
                return len(self.name)

            def speak(self):
                self.rat_type()
                self.name_info()
                self.age_info()

            @staticmethod
            def type():
                print("I are a rat, I have a big tail and i am so naughty")

            def name_info(self):
                print("my name is " + self.name)

            def age_info(self):
                print("my age is ", self.age)

            def change_age(self, age):
                self.age = age

            def find_age(self):
                print(self.age)

            def find_name(self):
                print(self.name)

            def change_name(self, name):
                self.name = name

            def change_weight(self, weight):
                self.weight = weight

            def find_weight(self):
                print(self.weight)

    class Math(object):

        def __init__(self):
            self.name = "Math"

        def __repr__(self):
            return f"{self.name}()"

        def __mut__(self, x):
            if type(x) is not int:
                raise Exception("please enter the correct value int")

            else:
                self.name = self.name * x

        def __sub__(self, y):
            if type(y) is not int:
                raise Exception("please enter the correct value int")

            else:
                self.name = self.name - y

        def __add__(self, z):
            if type(z) is not int:
                raise Exception("please enter the correct value int")

            else:
                self.name = self.name - z

        def __floordiv__(self, a):
            if type(a) is not int:
                raise Exception("please enter the correct value int")

            else:
                self.name = self.name - a

        def __len__(self):
            return len(self.name)

        class NumberToRupees():
            def __init__(self, number):
                self.number = number
                self.process()
                self.name = "NumberToRupees"

            def process(self):
                print(f"{self.name}Rs")

            def __repr__(self):
                return f"{self.name}({self.number})"

            def __mut__(self, x):
                if type(x) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name * x

            def __sub__(self, y):
                if type(y) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name - y

            def __add__(self, z):
                if type(z) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name - z

            def __floordiv__(self, a):
                if type(a) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name - a

        class SimpleMath(object):
            def __init__(self):
                self.name = "SimpleMath"

            def __repr__(self):
                return f"{self.name}()"

            def __mut__(self, x):
                if type(x) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name * x

            def __sub__(self, y):
                if type(y) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name - y

            def __add__(self, z):
                if type(z) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name - z

            def __floordiv__(self, a):
                if type(a) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name - a

            def __len__(self):
                return len(self.name)

            @staticmethod
            def sub(value1, value2):
                return value1 - value2

            @staticmethod
            def add(value1, value2):
                return value1 + value2

            @staticmethod
            def mut(value1, value2):
                return value1 * value2

            @staticmethod
            def div(value1, value2):
                return value1 / value2

            @staticmethod
            def rimainder(value1, value2):
                return value1 % value2

        class Convert(object):

            def __init__(self):
                self.name = "Convert"

            def __repr__(self):
                return f"{self.name}()"

            def __mut__(self, x):
                if type(x) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name * x

            def __sub__(self, y):
                if type(y) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name - y

            def __add__(self, z):
                if type(z) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name - z

            def __floordiv__(self, a):
                if type(a) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name - a

            def __len__(self):
                return len(self.name)

            class MeterToCm(object):

                def __init__(self, value):
                    self.value = value
                    self.name = "MeaterToCm"
                    self.process(value)
                    print("{self.name}(", self.ans, "cm", ")")

                def __repr__(self):
                    return f"MeterToCm({self.value})"

                def __mut__(self, x):
                    if type(x) is not int:
                        raise Exception("please enter the correct value int")
                    else:
                        self.name = self.name * x

                def __sub__(self, y):
                    if type(y) is not int:
                        raise Exception("please enter the correct value int")

                    else:
                        self.name = self.name - y

                def __add__(self, z):
                    if type(z) is not int:
                        raise Exception("please enter the correct value int")

                    else:
                        self.name = self.name - z

                def __floordiv__(self, a):
                    if type(a) is not int:
                        raise Exception("please enter the correct value int")

                    else:
                        self.name = self.name - a

                def __len__(self):
                    return len(self.name)

                def process(self, value):
                    self.ans = value * 100

            class CmToMeter(object):

                def __init__(self, value):
                    self.value = value
                    self.process(value)
                    self.name = "CmToMeter"
                    print("result(", self.ans, "m", ")")

                def __repr__(self):
                    return f"{self.name}({self.value})"

                def __mut__(self, x):
                    if type(x) is not int:
                        raise Exception("please enter the correct value int")

                    else:
                        self.name = self.name * x

                def __sub__(self, y):
                    if type(y) is not int:
                        raise Exception("please enter the correct value int")

                    else:
                        self.name = self.name - y

                def __add__(self, z):
                    if type(z) is not int:
                        raise Exception("please enter the correct value int")

                    else:
                        self.name = self.name - z

                def __floordiv__(self, a):
                    if type(a) is not int:
                        raise Exception("please enter the correct value int")

                    else:
                        self.name = self.name - a

                def __len__(self):
                    return len(self.name)

                def process(self, value):
                    self.ans = value / 100

            class MeterToKm(object):

                def __init__(self, value):
                    self.value = value
                    self.process(value)
                    self.name = "MeterToKm"
                    print("result(", self.ans, "Km", ")")

                def __repr__(self):
                    return f"{self.name}({self.value})"

                def __mut__(self, x):
                    if type(x) is not int:
                        raise Exception("please enter the correct value int")

                    else:
                        self.name = self.name * x

                def __sub__(self, y):
                    if type(y) is not int:
                        raise Exception("please enter the correct value int")

                    else:
                        self.name = self.name - y

                def __add__(self, z):
                    if type(z) is not int:
                        raise Exception("please enter the correct value int")

                    else:
                        self.name = self.name - z

                def __floordiv__(self, a):
                    if type(a) is not int:
                        raise Exception("please enter the correct value int")

                    else:
                        self.name = self.name - a

                def __len__(self):
                    return len(self.name)

                def process(self, value):
                    self.ans = value / 1000

            class KmToMeter(object):
                def __init__(self, value):
                    self.value = value
                    self.process(value)
                    self.name = "KmToMeter"
                    print("result(", self.ans, "Km", ")")

                def __repr__(self):
                    return f"{self.name}({self.value})"

                def __mut__(self, x):
                    if type(x) is not int:
                        raise Exception("please enter the correct value int")

                    else:
                        self.name = self.name * x

                def __sub__(self, y):
                    if type(y) is not int:
                        raise Exception("please enter the correct value int")

                    else:
                        self.name = self.name - y

                def __add__(self, z):
                    if type(z) is not int:
                        raise Exception("please enter the correct value int")

                    else:
                        self.name = self.name - z

                def __floordiv__(self, a):
                    if type(a) is not int:
                        raise Exception("please enter the correct value int")

                    else:
                        self.name = self.name - a

                def __len__(self):
                    return len(self.name)

                def process(self, value):
                    self.ans = value * 1000

            class NumberToRomonNumber1To100(object):

                def __init__(self, number):
                    self.name = "NumberToRomonNumber1To100"

                    self.n1 = "I"
                    self.n2 = "II"
                    self.n3 = "III"
                    self.n4 = "IV"
                    self.n5 = "V"
                    self.n6 = "VI"
                    self.n7 = "VII"
                    self.n8 = "VII"
                    self.n9 = "IX"
                    self.n10 = "X"

                    self.n11 = "XI"
                    self.n12 = "XII"
                    self.n13 = "XIII"
                    self.n14 = "XIV"
                    self.n15 = "XV"
                    self.n16 = "XVI"
                    self.n17 = "XVII"
                    self.n18 = "XVII"
                    self.n19 = "XIX"
                    self.n20 = "XX"

                    self.n21 = "XXI"
                    self.n22 = "XXII"
                    self.n23 = "XXIII"
                    self.n24 = "XXIV"
                    self.n25 = "XXV"
                    self.n26 = "XXVI"
                    self.n27 = "XXVII"
                    self.n28 = "XXVII"
                    self.n29 = "XXIX"
                    self.n30 = "XXX"

                    self.n31 = "XXXI"
                    self.n32 = "XXXII"
                    self.n33 = "XXXIII"
                    self.n34 = "XXXIV"
                    self.n35 = "XXXV"
                    self.n36 = "XXXVI"
                    self.n37 = "XXXVII"
                    self.n38 = "XXXVII"
                    self.n39 = "XXXIX"
                    self.n40 = "XL"

                    self.n41 = "XLI"
                    self.n42 = "XLII"
                    self.n43 = "XLIII"
                    self.n44 = "XLIV"
                    self.n45 = "XLXV"
                    self.n46 = "XLVI"
                    self.n47 = "XLVII"
                    self.n48 = "XLVII"
                    self.n49 = "XLIX"
                    self.n50 = "L"

                    self.n51 = "LI"
                    self.n52 = "LII"
                    self.n53 = "LIII"
                    self.n54 = "LIV"
                    self.n55 = "LXV"
                    self.n56 = "LVI"
                    self.n57 = "LVII"
                    self.n58 = "LVII"
                    self.n59 = "LIX"
                    self.n60 = "LX"

                    self.n61 = "LXI"
                    self.n62 = "LXII"
                    self.n63 = "LXIII"
                    self.n64 = "LXIV"
                    self.n65 = "LXXV"
                    self.n66 = "LXVI"
                    self.n67 = "LXVII"
                    self.n68 = "LXVII"
                    self.n69 = "LXIX"
                    self.n70 = "LXX"

                    self.n71 = "LXXI"
                    self.n72 = "LXXII"
                    self.n73 = "LXXIII"
                    self.n74 = "LXXIV"
                    self.n75 = "LXXXV"
                    self.n76 = "LXXVI"
                    self.n77 = "LXXVII"
                    self.n78 = "LXXVII"
                    self.n79 = "LXXIX"
                    self.n80 = "LXXX"

                    self.n81 = "LXXXI"
                    self.n82 = "LXXXII"
                    self.n83 = "LXXXIII"
                    self.n84 = "LXXXIV"
                    self.n85 = "LXXXV"
                    self.n86 = "LXXXVI"
                    self.n87 = "LXXXVII"
                    self.n88 = "LXXXVII"
                    self.n89 = "LXXXIX"
                    self.n90 = "XC"

                    self.n91 = "XCI"
                    self.n92 = "XCII"
                    self.n93 = "XCIII"
                    self.n94 = "XCIV"
                    self.n95 = "XCV"
                    self.n96 = "XCVI"
                    self.n97 = "XCVII"
                    self.n98 = "XCVII"
                    self.n99 = "XCIX"
                    self.n100 = "C"

                    self.LIST = [
                        self.n1, self.n2, self.n3, self.n4, self.n5,
                        self.n6, self.n7, self.n8, self.n9, self.n10,

                        self.n11, self.n12, self.n13, self.n14, self.n15,
                        self.n16, self.n17, self.n18, self.n19, self.n20,

                        self.n21, self.n22, self.n23, self.n24, self.n25,
                        self.n26, self.n27, self.n28, self.n29, self.n30,

                        self.n31, self.n32, self.n33, self.n34, self.n35,
                        self.n36, self.n37, self.n38, self.n39, self.n40,

                        self.n41, self.n42, self.n43, self.n44, self.n45,
                        self.n46, self.n47, self.n48, self.n49, self.n50,

                        self.n51, self.n52, self.n53, self.n54, self.n55,
                        self.n56, self.n57, self.n58, self.n59, self.n60,

                        self.n61, self.n62, self.n63, self.n64, self.n65,
                        self.n66, self.n67, self.n68, self.n69, self.n70,

                        self.n71, self.n72, self.n73, self.n74, self.n75,
                        self.n76, self.n77, self.n78, self.n79, self.n80,

                        self.n81, self.n82, self.n83, self.n84, self.n85,
                        self.n86, self.n87, self.n88, self.n89, self.n90,

                        self.n91, self.n92, self.n93, self.n94, self.n95,
                        self.n96, self.n97, self.n98, self.n99, self.n100
                    ]

                    self.num = number
                    self.ans = ""

                    self.show_answer()

                def __repr__(self):
                    return f"{self.name}()"

                def __mut__(self, x):
                    if type(x) is not int:
                        raise Exception("please enter the correct value int")

                    else:
                        self.name = self.name * x

                def __sub__(self, y):
                    if type(y) is not int:
                        raise Exception("please enter the correct value int")

                    else:
                        self.name = self.name - y

                def __add__(self, z):
                    if type(z) is not int:
                        raise Exception("please enter the correct value int")

                    else:
                        self.name = self.name - z

                def __floordiv__(self, a):
                    if type(a) is not int:
                        raise Exception("please enter the correct value int")

                    else:
                        self.name = self.name - a

                def __len__(self):
                    return len(self.name)

                def show_answer(self):
                    for i in range(0, 99):
                        if i == self.num:
                            self.ans = self.LIST[i - 1]
                            break
                        else:
                            continue
                    print("Roman number(" + str(self.ans) + ")")

            class RupeesToPaise(object):
                def __init__(self, rupees):
                    self.rupees = rupees
                    self.name = "RupeesToPaise"
                    self.process()

                def __repr__(self):
                    return f"{self.name}({self.rupees})"

                def __mut__(self, x):
                    if type(x) is not int:
                        raise Exception("please enter the correct value int")

                    else:
                        self.name = self.name * x

                def __sub__(self, y):
                    if type(y) is not int:
                        raise Exception("please enter the correct value int")

                    else:
                        self.name = self.name - y

                def __add__(self, z):
                    if type(z) is not int:
                        raise Exception("please enter the correct value int")

                    else:
                        self.name = self.name - z

                def __floordiv__(self, a):
                    if type(a) is not int:
                        raise Exception("please enter the correct value int")

                    else:
                        self.name = self.name - a

                def __len__(self):
                    return len(self.name)

                def process(self):
                    ans = float(self.rupees) * 100
                    print(float(ans), "paise")

        class Comper(object):

            def __init__(self):
                self.name = "Comper"

            def __repr__(self):
                return f"{self.name}()"

            def __mut__(self, x):
                if type(x) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name * x

            def __sub__(self, y):
                if type(y) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name - y

            def __add__(self, z):
                if type(z) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name - z

            def __floordiv__(self, a):
                if type(a) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name - a

            def __len__(self):
                return len(self.name)

            class ComperDecimal(object):
                def __init__(self, value1, value2):
                    self.value2 = value2
                    self.value1 = value1
                    self.name = "ComperDecimal"
                    self.process()

                def __repr__(self):
                    return f"{self.name}({self.value1}, {self.value2})"

                def __mut__(self, x):
                    if type(x) is not int:
                        raise Exception("please enter the correct value int")

                    else:
                        self.name = self.name * x

                def __sub__(self, y):
                    if type(y) is not int:
                        raise Exception("please enter the correct value int")

                    else:
                        self.name = self.name - y

                def __add__(self, z):
                    if type(z) is not int:
                        raise Exception("please enter the correct value int")

                    else:
                        self.name = self.name - z

                def __floordiv__(self, a):
                    if type(a) is not int:
                        raise Exception("please enter the correct value int")

                    else:
                        self.name = self.name - a

                def __len__(self):
                    return len(self.name)

                def process(self):
                    try:
                        if float(self.value1) > float(self.value2):
                            print(self.value1, "is greater")
                        elif float(self.value2) > float(self.value1):
                            print(self.value2, "is greater")
                        else:
                            print("Both or equal")

                    except:
                        print("please enter the data type decimal")

        class Tabels(object):
            def __init__(self, which_tabels, from_1_to_how_much=10):
                self.from_table = from_1_to_how_much
                self.which_table = which_tabels
                self.name = "Tabels"
                self.process()

            def __repr__(self):
                return f"{self.name}({self.which_table}, {self.from_table})"

            def __mut__(self, x):
                if type(x) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name * x

            def __sub__(self, y):
                if type(y) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name - y

            def __add__(self, z):
                if type(z) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name - z

            def __floordiv__(self, a):
                if type(a) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name - a

            def __len__(self):
                return len(self.name)

            def process(self):
                for t in range(1, int(self.from_table + 1)):
                    print(self.which_table, "x", t, "=", self.which_table * t)

    class ShapesOnConsole(object):

        def __init__(self):
            self.name = "ShapesOnConsole"

        def __repr__(self):
            return f"{self.name}()"

        def __mut__(self, x):
            if type(x) is not int:
                raise Exception("please enter the correct value int")

            else:
                self.name = self.name * x

        def __sub__(self, y):
            if type(y) is not int:
                raise Exception("please enter the correct value int")

            else:
                self.name = self.name - y

        def __add__(self, z):
            if type(z) is not int:
                raise Exception("please enter the correct value int")

            else:
                self.name = self.name - z

        def __floordiv__(self, a):
            if type(a) is not int:
                raise Exception("please enter the correct value int")

            else:
                self.name = self.name - a

        def __len__(self):
            return len(self.name)

        class Square(object):
            def __init__(self):
                self.printer()
                self.name = "ShapesOnConsole"

            def __repr__(self):
                return f"{self.name}()"

            def __mut__(self, x):
                if type(x) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name * x

            def __sub__(self, y):
                if type(y) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name - y

            def __add__(self, z):
                if type(z) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name - z

            def __floordiv__(self, a):
                if type(a) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name - a

            def __len__(self):
                return len(self.name)

            @staticmethod
            def printer():
                print("______________________________")
                print("|                            |")
                print("|                            |")
                print("|                            |")
                print("|                            |")
                print("|                            |")
                print("|                            |")
                print("|                            |")
                print("|                            |")
                print("|____________________________|")

        class Rectangle(object):
            def __init__(self):
                self.printer()
                self.name = "Rectangle"

            def __repr__(self):
                return f"{self.name}()"

            def __mut__(self, x):
                if type(x) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name * x

            def __sub__(self, y):
                if type(y) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name - y

            def __add__(self, z):
                if type(z) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name - z

            def __floordiv__(self, a):
                if type(a) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name - a

            def __len__(self):
                return len(self.name)

            @staticmethod
            def printer():
                print("_____________________________________________________")
                print("|                                                   |")
                print("|                                                   |")
                print("|                                                   |")
                print("|                                                   |")
                print("|                                                   |")
                print("|___________________________________________________|")

        class Triangle(object):
            def __init__(self):
                self.process()
                self.name = "Triangle"

            def __repr__(self):
                return f"{self.name}()"

            def __mut__(self, x):
                if type(x) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name * x

            def __sub__(self, y):
                if type(y) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name - y

            def __add__(self, z):
                if type(z) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name - z

            def __floordiv__(self, a):
                if type(a) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name - a

            def __len__(self):
                return len(self.name)

            @staticmethod
            def process():
                print("      /\\")
                print("     /  \\")
                print("    /    \\")
                print("   /      \\")
                print("  /        \\")
                print(" /          \\")
                print("/____________\\")

    class Designs(object):
        def __init__(self):
            self.name = "Designs"

        def __repr__(self):
            return f"{self.name}()"

        def __mut__(self, x):
            if type(x) is not int:
                raise Exception("please enter the correct value int")

            else:
                self.name = self.name * x

        def __sub__(self, y):
            if type(y) is not int:
                raise Exception("please enter the correct value int")

            else:
                self.name = self.name - y

        def __add__(self, z):
            if type(z) is not int:
                raise Exception("please enter the correct value int")

            else:
                self.name = self.name - z

        def __floordiv__(self, a):
            if type(a) is not int:
                raise Exception("please enter the correct value int")

            else:
                self.name = self.name - a

        def __len__(self):
            return len(self.name)

        class D1(object):
            def __init__(self):
                self.process()
                self.name = "D1"

            def __repr__(self):
                return f"{self.name}()"

            def __mut__(self, x):
                if type(x) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name * x

            def __sub__(self, y):
                if type(y) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name - y

            def __add__(self, z):
                if type(z) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name - z

            def __floordiv__(self, a):
                if type(a) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name - a

            def __len__(self):
                return len(self.name)

            @staticmethod
            def process():
                print("     ()     ")
                print("    (  )    ")
                print("   (    )   ")
                print("  (      )  ")
                print(" (        ) ")
                print("  (      )  ")
                print("   (    )   ")
                print("    (  )    ")
                print("     ()     ")

    class PrintYourNameManyTimes(object):
        def __init__(self, name, times=2):
            self.name = name
            self.times = times
            self.name = "PrintYourNameManyTimes"
            self.process()

        def __repr__(self):
            return f"{self.name}({self.name}, {self.times})"

        def __mut__(self, x):
            if type(x) is not int:
                raise Exception("please enter the correct value int")

            else:
                self.name = self.name * x

        def __sub__(self, y):
            if type(y) is not int:
                raise Exception("please enter the correct value int")

            else:
                self.name = self.name - y

        def __add__(self, z):
            if type(z) is not int:
                raise Exception("please enter the correct value int")

            else:
                self.name = self.name - z

        def __floordiv__(self, a):
            if type(a) is not int:
                raise Exception("please enter the correct value int")

            else:
                self.name = self.name - a

        def process(self):
            for n in range(1, self.times + 1):
                print(n, ":", self.name)

        def __len__(self):
            return len(self.name)

    class Vechicles(object):

        def __init__(self):
            self.name = "Vechicles"

        def __repr__(self):
            return f"{self.name}()"

        def __mut__(self, x):
            if type(x) is not int:
                raise Exception("please enter the correct value int")

            else:
                self.name = self.name * x

        def __sub__(self, y):
            if type(y) is not int:
                raise Exception("please enter the correct value int")

            else:
                self.name = self.name - y

        def __add__(self, z):
            if type(z) is not int:
                raise Exception("please enter the correct value int")

            else:
                self.name = self.name - z

        def __floordiv__(self, a):
            if type(a) is not int:
                raise Exception("please enter the correct value int")

            else:
                self.name = self.name - a

        def __len__(self):
            return len(self.name)

        class Car(object):
            def __init__(self, car_name, rate, total_speed=70, total_gear=5, on_gear=0):
                self.car_name = car_name
                self.total_gear = total_gear
                self.rate = rate
                self.total_speed = total_speed
                self.on_gear = on_gear
                self.name = "Car"

            def __repr__(self):
                return f"car({self.car_name}, {self.rate}, {self.total_speed}, {self.total_gear}, {self.on_gear})"

            def __mut__(self, x):
                if type(x) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name * x

            def __sub__(self, y):
                if type(y) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name - y

            def __add__(self, z):
                if type(z) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name - z

            def __floordiv__(self, a):
                if type(a) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name - a

            def __len__(self):
                return len(self.name)

            def info(self):
                print("Car name :", self.car_name)
                print("Total Gear is :", self.total_gear)
                print("Rate :", self.rate)
                print("Total Speed :", self.total_speed)
                print("On Gear :", self.on_gear)

            def change_gear(self, change_gear_to):
                if self.total_gear < change_gear_to:
                    print("total speed = ", self.total_speed,
                          ", but you have given", change_gear_to, "as a gear")
                else:
                    self.on_gear = change_gear_to

            def change_car_name(self, changed_car_name):
                self.car_name = changed_car_name

            def change_car_rate(self, changed_care_rate):
                self.rate = changed_care_rate

            def changed_car_total_speed(self, change_total_speed):
                self.total_speed = change_total_speed

        class Bus(object):
            def __init__(self, bus_name, rate, total_speed=70, total_gear=5, on_gear=0):
                self.bus_name = bus_name
                self.total_gear = total_gear
                self.rate = rate
                self.total_speed = total_speed
                self.on_gear = on_gear
                self.name = "Bus"

            def __repr__(self):
                return f"{self.name}({self.bus_name}, {self.rate}, {self.total_speed}, {self.total_gear}, {self.on_gear})"

            def __mut__(self, x):
                if type(x) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name * x

            def __sub__(self, y):
                if type(y) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name - y

            def __add__(self, z):
                if type(z) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name - z

            def __floordiv__(self, a):
                if type(a) is not int:
                    raise Exception("please enter the correct value int")

                else:
                    self.name = self.name - a

            def __len__(self):
                return len(self.name)

            def info(self):
                print("Bus name :", self.bus_name)
                print("Total Gear is :", self.total_gear)
                print("Rate :", self.rate)
                print("Total Speed :", self.total_speed)
                print("On Gear :", self.on_gear)

            def change_gear(self, change_gear_to):
                if self.total_gear < change_gear_to:
                    print("total speed = ", self.total_speed,
                          ", but you have given", change_gear_to, "as a gear")
                else:
                    self.on_gear = change_gear_to

            def change_bus_name(self, changed_bus_name):
                self.bus_name = changed_bus_name

            def change_bus_rate(self, changed_bus_rate):
                self.rate = changed_bus_rate

            def changed_bus_total_speed(self, change_total_speed):
                self.total_speed = change_total_speed

    class ProcessAge(object):

        def __init__(self, age):
            self.age = age
            self.adult = 20  # min
            self.teenager = 13  # min
            self.child = 12  # max
            self.name = "ProcessAge"

        def __repr__(self):
            return f"ProcessAge({self.age})"

        def __mut__(self, x):
            if type(x) is not int:
                raise Exception("please enter the correct value int")

            else:
                self.name = self.name * x

        def __sub__(self, y):
            if type(y) is not int:
                raise Exception("please enter the correct value int")

            else:
                self.name = self.name - y

        def __add__(self, z):
            if type(z) is not int:
                raise Exception("please enter the correct value int")

            else:
                self.name = self.name - z

        def __floordiv__(self, a):
            if type(a) is not int:
                raise Exception("please enter the correct value int")

            else:
                self.name = self.name - a

        def __len__(self):
            return len(self.name)

        def is_adult(self):
            if self.age >= self.adult:
                print("True you are a adult")
                return True

            else:
                print("False you are not a adult")
                return False

        def is_teenager(self):
            if self.age >= self.teenager:
                print("True you are a teenager")
                return True

            else:
                print("False you are not a teenager")
                return False

        def is_child(self):
            if self.age <= self.child:
                print("True you are a child")
                return True

            else:
                print("False you are not a childe")
                return False

        def change_age(self, age):
            self.age = age

        def find_age(self):
            print(self.age)

    def is_adult(self, age):
        if age >= self.adult:
            print("True you are a adult")
            return True

        else:
            print("False you are not a adult")
            return False

    def is_child(self, age):

        if age <= self.child:
            print("True you are a child")
            return True

        else:
            print("False you are not a childe")
            return False

    def is_teenager(self):

        if self.age >= self.teenager:
            print("True you are a teenager")
            return True

        else:
            print("False you are not a teenager")
            return False

    class Person(object):

        adult = 20  # min
        teenager = 13  # min
        child = 12  # max

        @classmethod
        def __init__(cls, name, age, counter, city):
            cls.name = name
            cls.age = age
            cls.counter = counter
            cls.city = city
            cls.age = age
            cls.name_class = "Person"
            Joel.Person.info(name, age, counter, city)

        @classmethod
        def __repr__(cls):
            return f"{cls.class_name}({cls.name}, {cls.age}, {cls.counter}, {cls.city})"

        @classmethod
        def __mut__(cls, x):
            if type(x) is not int:
                raise Exception("please enter the correct value int")

            else:
                cls.name = cls.name_class * x

        @classmethod
        def __sub__(cls, y):
            if type(y) is not int:
                raise Exception("please enter the correct value int")

            else:
                cls.name = cls.name - y

        @classmethod
        def __add__(cls, z):
            if type(z) is not int:
                raise Exception("please enter the correct value int")

            else:
                cls.name = cls.name - z

        @classmethod
        def __floordiv__(cls, a):
            if type(a) is not int:
                raise Exception("please enter the correct value int")

            else:
                cls.name = cls.name - a

        @classmethod
        def __len__(cls):
            return len(cls.name)

        @staticmethod
        def info(name, age, counter, city):
            print("Name : ", name)
            print("Age : ", age)
            print("Counter : ", counter)
            print("city : ", city)

        @classmethod
        def is_adult(cls):

            if cls.age >= cls.adult:
                print("True you are a adult")
                return True

            else:
                print("False you are not a adult")
                return False

        @classmethod
        def is_child(cls):

            if cls.age <= cls.child:
                print("True you are a child")
                return True

            else:
                print("False you are not a childe")
                return False

        @classmethod
        def is_teenager(cls):

            if cls.age >= cls.teenager:
                print("True you are a teenager")
                return True

            else:
                print("False you are not a teenager")
                return False

    class FindTheDay(object):

        def __init__(self):
            self.process()
            self.name = "FindTheDay"

        def __repr__(self):
            return f"{self.name}()"

        def __mut__(self, x):
            if type(x) is not int:
                raise Exception("please enter the correct value int")

            else:
                self.name = self.name * x

        def __sub__(self, y):
            if type(y) is not int:
                raise Exception("please enter the correct value int")

            else:
                self.name = self.name - y

        def __add__(self, z):
            if type(z) is not int:
                raise Exception("please enter the correct value int")

            else:
                self.name = self.name - z

        def __floordiv__(self, a):
            if type(a) is not int:
                raise Exception("please enter the correct value int")

            else:
                self.name = self.name - a

        def __len__(self):
            return len(self.name)

        @staticmethod
        def process():
            day = time.ctime()
            t = day.split(" ")
            print(t[0])

    class CountWords(object):

        @classmethod
        def __init__(cls, word):
            cls.word = word
            cls.process()
            cls.name = "CountWords"

        @classmethod
        def __repr__(cls):
            return f"{cls.name}({cls.word})"

        @classmethod
        def __mut__(cls, x):
            if type(x) is not int:
                raise Exception("please enter the correct value int")

            else:
                cls.name = cls.name * x

        @classmethod
        def __sub__(cls, y):
            if type(y) is not int:
                raise Exception("please enter the correct value int")

            else:
                cls.name = cls.name - y

        @classmethod
        def __add__(cls, z):
            if type(z) is not int:
                raise Exception("please enter the correct value int")

            else:
                cls.name = cls.name - z

        @classmethod
        def __floordiv__(cls, a):
            if type(a) is not int:
                raise Exception("please enter the correct value int")

            else:
                cls.name = cls.name - a

        @classmethod
        def __len__(cls):
            return len(cls.name)

        @classmethod
        def process(cls):
            cls.p1 = cls.word.split(" ")
            cls.p2 = []
            cls.p2 = [x for x in cls.p1 if (x != ' ') & (x != '')]

            print(len(cls.p2))

        @classmethod
        def FindWord(cls, index):
            try:
                print(cls.p2[index])

            except:
                print("please enter the correct index from 0 to", len(cls.p2))

    class PrintNumber1ToHowMuch(object):
        @classmethod
        def __init__(cls, from_no, to_no):
            cls.from_no = from_no
            cls.to_no = to_no
            cls.name = "PrintNumber1ToHowMuch"

        @classmethod
        def __repr__(cls):
            return f"{cls.name}({cls.from_no}, {cls.to_no})"

        @classmethod
        def __mut__(cls, x):
            if type(x) is not int:
                raise Exception("please enter the correct value int")

            else:
                cls.name = cls.name * x

        @classmethod
        def __sub__(cls, y):
            if type(y) is not int:
                raise Exception("please enter the correct value int")

            else:
                cls.name = cls.name - y

        @classmethod
        def __add__(cls, z):
            if type(z) is not int:
                raise Exception("please enter the correct value int")

            else:
                cls.name = cls.name - z

        @classmethod
        def __floordiv__(cls, a):
            if type(a) is not int:
                raise Exception("please enter the correct value int")

            else:
                cls.name = cls.name - a

        @classmethod
        def __len__(cls):
            return len(cls.name)

        @classmethod
        def process(cls):
            for i in range(cls.from_no, cls.to_no):
                print(i)

    class ChooseOneOrAnother(object):

        @classmethod
        def __init__(cls, first, secend):
            cls.first = first
            cls.secend = secend
            cls.name = "ChooseOneOrAnother"

        @classmethod
        def __repr__(cls):
            return f"{cls.name}({cls.first}, {cls.secend})"

        @classmethod
        def __mut__(cls, x):
            if type(x) is not int:
                raise Exception("please enter the correct value int")

            else:
                cls.name = cls.name * x

        @classmethod
        def __sub__(cls, y):
            if type(y) is not int:
                raise Exception("please enter the correct value int")

            else:
                cls.name = cls.name - y

        @classmethod
        def __add__(cls, z):
            if type(z) is not int:
                raise Exception("please enter the correct value int")

            else:
                cls.name = cls.name - z

        @classmethod
        def __floordiv__(cls, a):
            if type(a) is not int:
                raise Exception("please enter the correct value int")

            else:
                cls.name = cls.name - a

        @classmethod
        def __len__(cls):
            return len(cls.name)

        @classmethod
        def choose(cls):
            r = random.randint(1, 2)
            if r == 1:
                print(str(cls.first))

            else:
                print(str(cls.secend))

    class Help(object):
        def __init__(self):
            self.Helper()
            self.name = "Help"

        def __repr__(self):
            return f"{self.name}()"

        def __mut__(self, x):
            if type(x) is not int:
                raise Exception("please enter the correct value int")

            else:
                self.name = self.name * x

        def __sub__(self, y):
            if type(y) is not int:
                raise Exception("please enter the correct value int")

            else:
                self.name = self.name - y

        def __add__(self, z):
            if type(z) is not int:
                raise Exception("please enter the correct value int")

            else:
                self.name = self.name - z

        def __floordiv__(self, a):
            if type(a) is not int:
                raise Exception("please enter the correct value int")

            else:
                self.name = self.name - a

        def __len__(self):
            return len(self.name)

        def Helper(self):
            self.LIST = [
                "Joel.TypesOfAnimalsAndHumans.Dog(name, age)",

                "Joel.TypesOfAnimalsAndHumans.Cat(name, age)",

                "Joel.TypesOfAnimalsAndHumans.Lion(name, age)",

                "Joel.TypesOfAnimalsAndHumans.Rat(name, age)",

                "Joel.TypesOfAnimalsAndHumans.Human(name, age)",

                "Joel.Math.SimpleMath.add(value1, value2)",

                "Joel.math.SimpleMath.div(value1, value2)",

                "Joel.Math.SimpleMath.mut(value1, value2)",

                "Joel.Math.SimpleMath.sub(value1, value2)",

                "Joel.Math.Convert.NumberToRomonNumber1To100(value)",

                "Joel.Math.Convert.MeterToCm(value)",

                "Joel.Math.Convert.CmToMeter(value)",
                "Joel.Math.Convert.MeterToKm(value)",

                "Joel.Math.Convert.RupeesToPaise(value)",

                "Joel.Math.Comper.ComperDecimal(value1, value2)",

                "Joel.Math.Tabels(which_tabels, from_1_to_how_much)",

                "Joel.ShapesOnConsole.Square()",

                "Joel.ShapesOnConsole.Rectangle()",

                "Joel.ShapesOnConsole.Triangle()",

                "Joel.Designs.D1()",

                "Joel.PrintYourNameManyTimes(name)",

                "Joel.Vechicles.Car(car_name, rate, total_speed, total_gear, on_gear)",

                "Joel.Vechicles.Bus(bus_name, rate, total_speed, total_gear, on_gear)",

                "Joel.ProcessAge(age)",

                "Joel.ProcessAge.is_adult()",

                "Joel.ProcessAge.is_teenager()",

                "Joel.ProcessAge.is_child()",

                "Joel.ProcessAge.change_age(age)",

                "Joel.ProcessAge.find_age()",

                "Joel.is_adult(age)",

                "Joel.is_teenager(age)",

                "Joel.is_child(age)",

                "Joel.Person(name, age, counter, city)",

                "Joel.FindTheDay()",

                "Joel.Math.SimpleMath.rimainder(value1, value2)",

                "Joel.CountWords(String)",

                "Joel.PrintNumber1ToHowMuch(from, to)",

                "Joel.ChooseOneOrAnother(first, secend)",

                "Joel.Find_The_Size_IN_Bytes(function)"

            ]

            self.list_in = []

            for i in self.LIST:
                if i in self.list_in:
                    continue

                else:
                    print(i)
                    self.list_in.append(i)


user = os.getcwd().split("/")

print("username :", os.getlogin())
print("folder: ", os.getcwdb())
print("")
print("")
print("pid(")
print(os.getpid())
print("(")
print("")
print("ppid(")
print(os.getppid())
print(")")
print("")
print("mainfiles(")
print(os.get_exec_path())
print(")")

print("")
print("pgrp(")
print(os.getpgrp())
print(")")

print("")
print("uid(")
print(os.getuid())
print(")")

print("")
print("loadsvg(")

print(os.getloadavg())

print(")")

print("")

print("where we are in(")

print(os.getcwd())

print(")")

print("")

def restart():
    #!/usr/bin/env python

    # Waits for the parent process to terminate, then executes specified commands.

    import os
    import signal
    import sys
    import syslog
    import time

    if len(sys.argv) < 3:
        raise Exception('usage: restart.py <pid> <path> [optional command]')

    try:
        signal.signal(signal.SIGHUP, signal.SIG_IGN)

        pid = int(sys.argv[1])
        while os.getppid() == pid:
            time.sleep(0.5)

        if len(sys.argv) > 3:
            to_launch = sys.argv[3:]
            ec = os.spawnv(os.P_WAIT, to_launch[0], to_launch)
            if ec != 0:
                syslog.syslog(syslog.LOG_ERR, str(to_launch) + ': ' + str(ec))

        to_launch = ['/usr/bin/open', sys.argv[2]] if sys.platform == 'darwin' else [sys.argv[2]]
        os.execv(to_launch[0], to_launch)
    except:
        syslog.syslog(syslog.LOG_ERR, str(sys.exc_info()))

def printenv():
    #!/usr/bin/env python

    # Dumps environment variables into specified file.
    # Format: zero-separated "name=value" pairs in platform encoding.
    # The script can work with any version of Python from 2.3 to at least 3.9

    import os
    import sys

    if len(sys.argv) != 2:
        raise Exception('Exactly one argument expected')

    PY2 = sys.version_info < (3,)

    if PY2:
        environ = os.environ
    else:
        environ = os.environb


    def b(s):
        if PY2:
            return s
        else:
            return s.encode('utf-8')


    fd = open(sys.argv[1], 'wb')
    try:
        for key, value in environ.items():
            fd.writelines([key, b('='), value, b('\0')])
    finally:
        fd.close()


def getrandom(szie=1):
    print(os.getrandom(szie))

oneto100 = [
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
    31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59,
    60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 89,
    90, 91, 92, 93, 94, 95, 96, 97, 98, 100
]

e = [0, 1, 3, 4, 5, 6, 7, 8, 9, 2, 0, 1, 3, 4, 5, 6, 7, 8, 9, 2, 0, 1, 3, 4, 5, 6, 7, 8, 9, 2, 0, 1, 3, 4, 5, 6, 7, 8, 9, 2, 0, 1, 3, 4, 5, 6, 7, 8, 9, 2, 0, 1, 3, 4, 5, 6, 7, 8, 9, 2, 0, 1, 3, 4, 5, 6, 7, 8, 9, 2, 0, 1, 3, 4, 5, 6, 7, 8, 9, 2, 0, 1, 3, 4, 5, 6, 7, 8, 9, 2, 0, 1, 3, 4, 5, 6, 7, 8, 9, 2, 0, 1, 3, 4, 5, 6, 7, 8, 9, 2, 0, 1, 3, 4, 5, 6, 7, 8, 9, 2, 0, 1, 3, 4, 5, 6, 7, 8, 9, 2, 0, 1, 3, 4, 5, 6, 7, 8, 9, 2, 0, 1, 3, 4, 5, 6, 7, 8, 9, 2, 0, 1, 3, 4, 5, 6, 7, 8, 9, 2, 0, 1, 3, 4, 5, 6, 7, 8, 9, 2, 0, 1, 3, 4, 5, 6, 7, 8, 9, 2, 0, 1, 3, 4, 5, 6, 7, 8, 9, 2, 0, 1, 3, 4, 5, 6, 7, 8, 9, 2, 0, 1, 3, 4, 5, 6, 7, 8, 9, 2, 0, 1, 3, 4, 5, 6, 7, 8, 9, 2, 0, 1, 3, 4, 5, 6, 7, 8, 9, 2, 0, 1, 3, 4, 5, 6, 7, 8, 9, 2, 0, 1, 3, 4, 5, 6, 7, 8, 9, 2, 0, 1, 3, 4, 5, 6, 7, 8, 9, 2, 0, 1, 3, 4, 5, 6, 7, 8, 9, 2, 0, 1, 3, 4, 5, 6, 7, 8, 9, 2, 0, 1, 3, 4, 5, 6, 7, 8, 9, 2, 0, 1, 3, 4, 5, 6, 7, 8, 9, 2, 0, 1, 3, 4, 5, 6, 7, 8, 9, 2, 0, 1, 3, 4, 5, 6, 7, 8, 9, 2, 0, 1, 3, 4, 5, 6, 7, 8, 9, 2, 0, 1, 3, 4, 5, 6, 7, 8, 9, 2, 0, 1, 3, 4, 5, 6, 7, 8, 9, 2]



class draw(object):
    def sh():
        os.system("sh")
    
    def bash():
        os.system("bash")
        
    def devid(self, lists, number):
        for i in range(len(lists)):
            print(lists[number:i/number])
    
    def modulo(self, List, number):
        for i in range(len(List)):
            print(List[number:i%number])
    
    def sub(self, lists, number):
        for i in range(len(lists)):
            print(lists[number:i-number])
    
    def line(self, Lists, number):
        for i in range(len(Lists)):
            print(Lists[number:i+number])
    
    def __init__(self, ListS, number):
        for i in range(len(ListS)):
            print(ListS[0:i])

l = ["hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello"]

                                    
print("user(" + os.getlogin() + ")")

print("")

draw.bash()

def sysconf_name():
    print(os.sysconf_names)

binid = bin(12)
binfiles = os.defpath
def getlicense():
    print("Apache Ant 1.6.1 license is located in Ant distribution root folder lib/ant under IntelliJ IDEA installation home.")

def login(license):
    if license == "Apache Ant 1.6.1 license is located in Ant distribution root folder lib/ant under IntelliJ IDEA installation home.":
        print("[!~(correct license)]: vs@vscode.license")
        
    else:
        print("[!~(wrong license)]: vs@vscode.license")

def confstr_names():
    print(os.confstr_names)

def open(path):
    print(os.fsencode(path))    


def pdb():
    # ! /usr/bin/env python3

    """
    The Python Debugger Pdb
    =======================

    To use the debugger in its simplest form:

            >>> import pdb
            >>> pdb.run('<a statement>')

    The debugger's prompt is '(Pdb) '.  This will stop in the first
    function call in <a statement>.

    Alternatively, if a statement terminated with an unhandled exception,
    you can use pdb's post-mortem facility to inspect the contents of the
    traceback:

            >>> <a statement>
            <exception traceback>
            >>> import pdb
            >>> pdb.pm()

    The commands recognized by the debugger are listed in the next
    section.  Most can be abbreviated as indicated; e.g., h(elp) means
    that 'help' can be typed as 'h' or 'help' (but not as 'he' or 'hel',
    nor as 'H' or 'Help' or 'HELP').  Optional arguments are enclosed in
    square brackets.  Alternatives in the command syntax are separated
    by a vertical bar (|).

    A blank line repeats the previous command literally, except for
    'list', where it lists the next 11 lines.

    Commands that the debugger doesn't recognize are assumed to be Python
    statements and are executed in the context of the program being
    debugged.  Python statements can also be prefixed with an exclamation
    point ('!').  This is a powerful way to inspect the program being
    debugged; it is even possible to change variables or call functions.
    When an exception occurs in such a statement, the exception name is
    printed but the debugger's state is not changed.

    The debugger supports aliases, which can save typing.  And aliases can
    have parameters (see the alias help entry) which allows one a certain
    level of adaptability to the context under examination.

    Multiple commands may be entered on a single line, separated by the
    pair ';;'.  No intelligence is applied to separating the commands; the
    input is split at the first ';;', even if it is in the middle of a
    quoted string.

    If a file ".pdbrc" exists in your home directory or in the current
    directory, it is read in and executed as if it had been typed at the
    debugger prompt.  This is particularly useful for aliases.  If both
    files exist, the one in the home directory is read first and aliases
    defined there can be overridden by the local file.  This behavior can be
    disabled by passing the "readrc=False" argument to the Pdb constructor.

    Aside from aliases, the debugger is not directly programmable; but it
    is implemented as a class from which you can derive your own debugger
    class, which you can make as fancy as you like.


    Debugger commands
    =================

    """
    # NOTE: the actual command documentation is collected from docstrings of the
    # commands and is appended to __doc__ after the class has been defined.

    import os
    import io
    import re
    import sys
    import cmd
    import bdb
    import dis
    import code
    import glob
    import pprint
    import signal
    import inspect
    import traceback
    import linecache

    class Restart(Exception):
        """Causes a debugger to be restarted for the debugged python program."""
        pass

    __all__ = ["run", "pm", "Pdb", "runeval", "runctx", "runcall", "set_trace",
               "post_mortem", "help"]

    def find_function(funcname, filename):
        cre = re.compile(r'def\s+%s\s*[(]' % re.escape(funcname))
        try:
            fp = open(filename)
        except OSError:
            return None
        # consumer of this info expects the first line to be 1
        with fp:
            for lineno, line in enumerate(fp, start=1):
                if cre.match(line):
                    return funcname, filename, lineno
        return None

    def getsourcelines(obj):
        lines, lineno = inspect.findsource(obj)
        if inspect.isframe(obj) and obj.f_globals is obj.f_locals:
            # must be a module frame: do not try to cut a block out of it
            return lines, 1
        elif inspect.ismodule(obj):
            return lines, 1
        return inspect.getblock(lines[lineno:]), lineno + 1

    def lasti2lineno(code, lasti):
        linestarts = list(dis.findlinestarts(code))
        linestarts.reverse()
        for i, lineno in linestarts:
            if lasti >= i:
                return lineno
        return 0

    class _rstr(str):
        """String that doesn't quote its repr."""

        def __repr__(self):
            return self

    # Interaction prompt line will separate file and call info from code
    # text using value of line_prefix string.  A newline and arrow may
    # be to your liking.  You can set it once pdb is imported using the
    # command "pdb.line_prefix = '\n% '".
    # line_prefix = ': '    # Use this to get the old situation back
    line_prefix = '\n-> '  # Probably a better default

    class Pdb(bdb.Bdb, cmd.Cmd):

        _previous_sigint_handler = None

        def __init__(self, completekey='tab', stdin=None, stdout=None, skip=None,
                     nosigint=False, readrc=True):
            bdb.Bdb.__init__(self, skip=skip)
            cmd.Cmd.__init__(self, completekey, stdin, stdout)
            sys.audit("pdb.Pdb")
            if stdout:
                self.use_rawinput = 0
            self.prompt = '(Pdb) '
            self.aliases = {}
            self.displaying = {}
            self.mainpyfile = ''
            self._wait_for_mainpyfile = False
            self.tb_lineno = {}
            # Try to load readline if it exists
            try:
                import readline
                # remove some common file name delimiters
                readline.set_completer_delims(' \t\n`@#$%^&*()=+[{]}\\|;:\'",<>?')
            except ImportError:
                pass
            self.allow_kbdint = False
            self.nosigint = nosigint

            # Read ~/.pdbrc and ./.pdbrc
            self.rcLines = []
            if readrc:
                try:
                    with open(os.path.expanduser('~/.pdbrc')) as rcFile:
                        self.rcLines.extend(rcFile)
                except OSError:
                    pass
                try:
                    with open(".pdbrc") as rcFile:
                        self.rcLines.extend(rcFile)
                except OSError:
                    pass

            self.commands = {}  # associates a command list to breakpoint numbers
            self.commands_doprompt = {}  # for each bp num, tells if the prompt
            # must be disp. after execing the cmd list
            self.commands_silent = {}  # for each bp num, tells if the stack trace
            # must be disp. after execing the cmd list
            self.commands_defining = False  # True while in the process of defining
            # a command list
            self.commands_bnum = None  # The breakpoint number for which we are
            # defining a list

        def sigint_handler(self, signum, frame):
            if self.allow_kbdint:
                raise KeyboardInterrupt
            self.message("\nProgram interrupted. (Use 'cont' to resume).")
            self.set_step()
            self.set_trace(frame)

        def reset(self):
            bdb.Bdb.reset(self)
            self.forget()

        def forget(self):
            self.lineno = None
            self.stack = []
            self.curindex = 0
            self.curframe = None
            self.tb_lineno.clear()

        def setup(self, f, tb):
            self.forget()
            self.stack, self.curindex = self.get_stack(f, tb)
            while tb:
                # when setting up post-mortem debugging with a traceback, save all
                # the original line numbers to be displayed along the current line
                # numbers (which can be different, e.g. due to finally clauses)
                lineno = lasti2lineno(tb.tb_frame.f_code, tb.tb_lasti)
                self.tb_lineno[tb.tb_frame] = lineno
                tb = tb.tb_next
            self.curframe = self.stack[self.curindex][0]
            # The f_locals dictionary is updated from the actual frame
            # locals whenever the .f_locals accessor is called, so we
            # cache it here to ensure that modifications are not overwritten.
            self.curframe_locals = self.curframe.f_locals
            return self.execRcLines()

        # Can be executed earlier than 'setup' if desired
        def execRcLines(self):
            if not self.rcLines:
                return
            # local copy because of recursion
            rcLines = self.rcLines
            rcLines.reverse()
            # execute every line only once
            self.rcLines = []
            while rcLines:
                line = rcLines.pop().strip()
                if line and line[0] != '#':
                    if self.onecmd(line):
                        # if onecmd returns True, the command wants to exit
                        # from the interaction, save leftover rc lines
                        # to execute before next interaction
                        self.rcLines += reversed(rcLines)
                        return True

        # Override Bdb methods

        def user_call(self, frame, argument_list):
            """This method is called when there is the remote possibility
            that we ever need to stop in this function."""
            if self._wait_for_mainpyfile:
                return
            if self.stop_here(frame):
                self.message('--Call--')
                self.interaction(frame, None)

        def user_line(self, frame):
            """This function is called when we stop or break at this line."""
            if self._wait_for_mainpyfile:
                if (self.mainpyfile != self.canonic(frame.f_code.co_filename)
                        or frame.f_lineno <= 0):
                    return
                self._wait_for_mainpyfile = False
            if self.bp_commands(frame):
                self.interaction(frame, None)

        def bp_commands(self, frame):
            """Call every command that was set for the current active breakpoint
            (if there is one).

            Returns True if the normal interaction function must be called,
            False otherwise."""
            # self.currentbp is set in bdb in Bdb.break_here if a breakpoint was hit
            if getattr(self, "currentbp", False) and \
                    self.currentbp in self.commands:
                currentbp = self.currentbp
                self.currentbp = 0
                lastcmd_back = self.lastcmd
                self.setup(frame, None)
                for line in self.commands[currentbp]:
                    self.onecmd(line)
                self.lastcmd = lastcmd_back
                if not self.commands_silent[currentbp]:
                    self.print_stack_entry(self.stack[self.curindex])
                if self.commands_doprompt[currentbp]:
                    self._cmdloop()
                self.forget()
                return
            return 1

        def user_return(self, frame, return_value):
            """This function is called when a return trap is set here."""
            if self._wait_for_mainpyfile:
                return
            frame.f_locals['__return__'] = return_value
            self.message('--Return--')
            self.interaction(frame, None)

        def user_exception(self, frame, exc_info):
            """This function is called if an exception occurs,
            but only if we are to stop at or just below this level."""
            if self._wait_for_mainpyfile:
                return
            exc_type, exc_value, exc_traceback = exc_info
            frame.f_locals['__exception__'] = exc_type, exc_value

            # An 'Internal StopIteration' exception is an exception debug event
            # issued by the interpreter when handling a subgenerator run with
            # 'yield from' or a generator controlled by a for loop. No exception has
            # actually occurred in this case. The debugger uses this debug event to
            # stop when the debuggee is returning from such generators.
            prefix = 'Internal ' if (not exc_traceback
                                     and exc_type is StopIteration) else ''
            self.message('%s%s' % (prefix,
                                   traceback.format_exception_only(exc_type, exc_value)[-1].strip()))
            self.interaction(frame, exc_traceback)

        # General interaction function
        def _cmdloop(self):
            while True:
                try:
                    # keyboard interrupts allow for an easy way to cancel
                    # the current command, so allow them during interactive input
                    self.allow_kbdint = True
                    self.cmdloop()
                    self.allow_kbdint = False
                    break
                except KeyboardInterrupt:
                    self.message('--KeyboardInterrupt--')

        # Called before loop, handles display expressions
        def preloop(self):
            displaying = self.displaying.get(self.curframe)
            if displaying:
                for expr, oldvalue in displaying.items():
                    newvalue = self._getval_except(expr)
                    # check for identity first; this prevents custom __eq__ to
                    # be called at every loop, and also prevents instances whose
                    # fields are changed to be displayed
                    if newvalue is not oldvalue and newvalue != oldvalue:
                        displaying[expr] = newvalue
                        self.message('display %s: %r  [old: %r]' %
                                     (expr, newvalue, oldvalue))

        def interaction(self, frame, traceback):
            # Restore the previous signal handler at the Pdb prompt.
            if Pdb._previous_sigint_handler:
                try:
                    signal.signal(signal.SIGINT, Pdb._previous_sigint_handler)
                except ValueError:  # ValueError: signal only works in main thread
                    pass
                else:
                    Pdb._previous_sigint_handler = None
            if self.setup(frame, traceback):
                # no interaction desired at this time (happens if .pdbrc contains
                # a command like "continue")
                self.forget()
                return
            self.print_stack_entry(self.stack[self.curindex])
            self._cmdloop()
            self.forget()

        def displayhook(self, obj):
            """Custom displayhook for the exec in default(), which prevents
            assignment of the _ variable in the builtins.
            """
            # reproduce the behavior of the standard displayhook, not printing None
            if obj is not None:
                self.message(repr(obj))

        def default(self, line):
            if line[:1] == '!': line = line[1:]
            locals = self.curframe_locals
            globals = self.curframe.f_globals
            try:
                code = compile(line + '\n', '<stdin>', 'single')
                save_stdout = sys.stdout
                save_stdin = sys.stdin
                save_displayhook = sys.displayhook
                try:
                    sys.stdin = self.stdin
                    sys.stdout = self.stdout
                    sys.displayhook = self.displayhook
                    exec(code, globals, locals)
                finally:
                    sys.stdout = save_stdout
                    sys.stdin = save_stdin
                    sys.displayhook = save_displayhook
            except:
                exc_info = sys.exc_info()[:2]
                self.error(traceback.format_exception_only(*exc_info)[-1].strip())

        def precmd(self, line):
            """Handle alias expansion and ';;' separator."""
            if not line.strip():
                return line
            args = line.split()
            while args[0] in self.aliases:
                line = self.aliases[args[0]]
                ii = 1
                for tmpArg in args[1:]:
                    line = line.replace("%" + str(ii),
                                        tmpArg)
                    ii += 1
                line = line.replace("%*", ' '.join(args[1:]))
                args = line.split()
            # split into ';;' separated commands
            # unless it's an alias command
            if args[0] != 'alias':
                marker = line.find(';;')
                if marker >= 0:
                    # queue up everything after marker
                    next = line[marker + 2:].lstrip()
                    self.cmdqueue.append(next)
                    line = line[:marker].rstrip()
            return line

        def onecmd(self, line):
            """Interpret the argument as though it had been typed in response
            to the prompt.

            Checks whether this line is typed at the normal prompt or in
            a breakpoint command list definition.
            """
            if not self.commands_defining:
                return cmd.Cmd.onecmd(self, line)
            else:
                return self.handle_command_def(line)

        def handle_command_def(self, line):
            """Handles one command line during command list definition."""
            cmd, arg, line = self.parseline(line)
            if not cmd:
                return
            if cmd == 'silent':
                self.commands_silent[self.commands_bnum] = True
                return  # continue to handle other cmd def in the cmd list
            elif cmd == 'end':
                self.cmdqueue = []
                return 1  # end of cmd list
            cmdlist = self.commands[self.commands_bnum]
            if arg:
                cmdlist.append(cmd + ' ' + arg)
            else:
                cmdlist.append(cmd)
            # Determine if we must stop
            try:
                func = getattr(self, 'do_' + cmd)
            except AttributeError:
                func = self.default
            # one of the resuming commands
            if func.__name__ in self.commands_resuming:
                self.commands_doprompt[self.commands_bnum] = False
                self.cmdqueue = []
                return 1
            return

        # interface abstraction functions

        def message(self, msg):
            print(msg, file=self.stdout)

        def error(self, msg):
            print('***', msg, file=self.stdout)

        # Generic completion functions.  Individual complete_foo methods can be
        # assigned below to one of these functions.

        def _complete_location(self, text, line, begidx, endidx):
            # Complete a file/module/function location for break/tbreak/clear.
            if line.strip().endswith((':', ',')):
                # Here comes a line number or a condition which we can't complete.
                return []
            # First, try to find matching functions (i.e. expressions).
            try:
                ret = self._complete_expression(text, line, begidx, endidx)
            except Exception:
                ret = []
            # Then, try to complete file names as well.
            globs = glob.glob(text + '*')
            for fn in globs:
                if os.path.isdir(fn):
                    ret.append(fn + '/')
                elif os.path.isfile(fn) and fn.lower().endswith(('.py', '.pyw')):
                    ret.append(fn + ':')
            return ret

        def _complete_bpnumber(self, text, line, begidx, endidx):
            # Complete a breakpoint number.  (This would be more helpful if we could
            # display additional info along with the completions, such as file/line
            # of the breakpoint.)
            return [str(i) for i, bp in enumerate(bdb.Breakpoint.bpbynumber)
                    if bp is not None and str(i).startswith(text)]

        def _complete_expression(self, text, line, begidx, endidx):
            # Complete an arbitrary expression.
            if not self.curframe:
                return []
            # Collect globals and locals.  It is usually not really sensible to also
            # complete builtins, and they clutter the namespace quite heavily, so we
            # leave them out.
            ns = {**self.curframe.f_globals, **self.curframe_locals}
            if '.' in text:
                # Walk an attribute chain up to the last part, similar to what
                # rlcompleter does.  This will bail if any of the parts are not
                # simple attribute access, which is what we want.
                dotted = text.split('.')
                try:
                    obj = ns[dotted[0]]
                    for part in dotted[1:-1]:
                        obj = getattr(obj, part)
                except (KeyError, AttributeError):
                    return []
                prefix = '.'.join(dotted[:-1]) + '.'
                return [prefix + n for n in dir(obj) if n.startswith(dotted[-1])]
            else:
                # Complete a simple name.
                return [n for n in ns.keys() if n.startswith(text)]

        # Command definitions, called by cmdloop()
        # The argument is the remaining string on the command line
        # Return true to exit from the command loop

        def do_commands(self, arg):
            """commands [bpnumber]
            (com) ...
            (com) end
            (Pdb)

            Specify a list of commands for breakpoint number bpnumber.
            The commands themselves are entered on the following lines.
            Type a line containing just 'end' to terminate the commands.
            The commands are executed when the breakpoint is hit.

            To remove all commands from a breakpoint, type commands and
            follow it immediately with end; that is, give no commands.

            With no bpnumber argument, commands refers to the last
            breakpoint set.

            You can use breakpoint commands to start your program up
            again.  Simply use the continue command, or step, or any other
            command that resumes execution.

            Specifying any command resuming execution (currently continue,
            step, next, return, jump, quit and their abbreviations)
            terminates the command list (as if that command was
            immediately followed by end).  This is because any time you
            resume execution (even with a simple next or step), you may
            encounter another breakpoint -- which could have its own
            command list, leading to ambiguities about which list to
            execute.

            If you use the 'silent' command in the command list, the usual
            message about stopping at a breakpoint is not printed.  This
            may be desirable for breakpoints that are to print a specific
            message and then continue.  If none of the other commands
            print anything, you will see no sign that the breakpoint was
            reached.
            """
            if not arg:
                bnum = len(bdb.Breakpoint.bpbynumber) - 1
            else:
                try:
                    bnum = int(arg)
                except:
                    self.error("Usage: commands [bnum]\n        ...\n        end")
                    return
            self.commands_bnum = bnum
            # Save old definitions for the case of a keyboard interrupt.
            if bnum in self.commands:
                old_command_defs = (self.commands[bnum],
                                    self.commands_doprompt[bnum],
                                    self.commands_silent[bnum])
            else:
                old_command_defs = None
            self.commands[bnum] = []
            self.commands_doprompt[bnum] = True
            self.commands_silent[bnum] = False

            prompt_back = self.prompt
            self.prompt = '(com) '
            self.commands_defining = True
            try:
                self.cmdloop()
            except KeyboardInterrupt:
                # Restore old definitions.
                if old_command_defs:
                    self.commands[bnum] = old_command_defs[0]
                    self.commands_doprompt[bnum] = old_command_defs[1]
                    self.commands_silent[bnum] = old_command_defs[2]
                else:
                    del self.commands[bnum]
                    del self.commands_doprompt[bnum]
                    del self.commands_silent[bnum]
                self.error('command definition aborted, old commands restored')
            finally:
                self.commands_defining = False
                self.prompt = prompt_back

        complete_commands = _complete_bpnumber

        def do_break(self, arg, temporary=0):
            """b(reak) [ ([filename:]lineno | function) [, condition] ]
            Without argument, list all breaks.

            With a line number argument, set a break at this line in the
            current file.  With a function name, set a break at the first
            executable line of that function.  If a second argument is
            present, it is a string specifying an expression which must
            evaluate to true before the breakpoint is honored.

            The line number may be prefixed with a filename and a colon,
            to specify a breakpoint in another file (probably one that
            hasn't been loaded yet).  The file is searched for on
            sys.path; the .py suffix may be omitted.
            """
            if not arg:
                if self.breaks:  # There's at least one
                    self.message("Num Type         Disp Enb   Where")
                    for bp in bdb.Breakpoint.bpbynumber:
                        if bp:
                            self.message(bp.bpformat())
                return
            # parse arguments; comma has lowest precedence
            # and cannot occur in filename
            filename = None
            lineno = None
            cond = None
            comma = arg.find(',')
            if comma > 0:
                # parse stuff after comma: "condition"
                cond = arg[comma + 1:].lstrip()
                arg = arg[:comma].rstrip()
            # parse stuff before comma: [filename:]lineno | function
            colon = arg.rfind(':')
            funcname = None
            if colon >= 0:
                filename = arg[:colon].rstrip()
                f = self.lookupmodule(filename)
                if not f:
                    self.error('%r not found from sys.path' % filename)
                    return
                else:
                    filename = f
                arg = arg[colon + 1:].lstrip()
                try:
                    lineno = int(arg)
                except ValueError:
                    self.error('Bad lineno: %s' % arg)
                    return
            else:
                # no colon; can be lineno or function
                try:
                    lineno = int(arg)
                except ValueError:
                    try:
                        func = eval(arg,
                                    self.curframe.f_globals,
                                    self.curframe_locals)
                    except:
                        func = arg
                    try:
                        if hasattr(func, '__func__'):
                            func = func.__func__
                        code = func.__code__
                        # use co_name to identify the bkpt (function names
                        # could be aliased, but co_name is invariant)
                        funcname = code.co_name
                        lineno = code.co_firstlineno
                        filename = code.co_filename
                    except:
                        # last thing to try
                        (ok, filename, ln) = self.lineinfo(arg)
                        if not ok:
                            self.error('The specified object %r is not a function '
                                       'or was not found along sys.path.' % arg)
                            return
                        funcname = ok  # ok contains a function name
                        lineno = int(ln)
            if not filename:
                filename = self.defaultFile()
            # Check for reasonable breakpoint
            line = self.checkline(filename, lineno)
            if line:
                # now set the break point
                err = self.set_break(filename, line, temporary, cond, funcname)
                if err:
                    self.error(err)
                else:
                    bp = self.get_breaks(filename, line)[-1]
                    self.message("Breakpoint %d at %s:%d" %
                                 (bp.number, bp.file, bp.line))

        # To be overridden in derived debuggers
        def defaultFile(self):
            """Produce a reasonable default."""
            filename = self.curframe.f_code.co_filename
            if filename == '<string>' and self.mainpyfile:
                filename = self.mainpyfile
            return filename

        do_b = do_break

        complete_break = _complete_location
        complete_b = _complete_location

        def do_tbreak(self, arg):
            """tbreak [ ([filename:]lineno | function) [, condition] ]
            Same arguments as break, but sets a temporary breakpoint: it
            is automatically deleted when first hit.
            """
            self.do_break(arg, 1)

        complete_tbreak = _complete_location

        def lineinfo(self, identifier):
            failed = (None, None, None)
            # Input is identifier, may be in single quotes
            idstring = identifier.split("'")
            if len(idstring) == 1:
                # not in single quotes
                id = idstring[0].strip()
            elif len(idstring) == 3:
                # quoted
                id = idstring[1].strip()
            else:
                return failed
            if id == '': return failed
            parts = id.split('.')
            # Protection for derived debuggers
            if parts[0] == 'self':
                del parts[0]
                if len(parts) == 0:
                    return failed
            # Best first guess at file to look at
            fname = self.defaultFile()
            if len(parts) == 1:
                item = parts[0]
            else:
                # More than one part.
                # First is module, second is method/class
                f = self.lookupmodule(parts[0])
                if f:
                    fname = f
                item = parts[1]
            answer = find_function(item, fname)
            return answer or failed

        def checkline(self, filename, lineno):
            """Check whether specified line seems to be executable.

            Return `lineno` if it is, 0 if not (e.g. a docstring, comment, blank
            line or EOF). Warning: testing is not comprehensive.
            """
            # this method should be callable before starting debugging, so default
            # to "no globals" if there is no current frame
            globs = self.curframe.f_globals if hasattr(self, 'curframe') else None
            line = linecache.getline(filename, lineno, globs)
            if not line:
                self.message('End of file')
                return 0
            line = line.strip()
            # Don't allow setting breakpoint at a blank line
            if (not line or (line[0] == '#') or
                    (line[:3] == '"""') or line[:3] == "'''"):
                self.error('Blank or comment')
                return 0
            return lineno

        def do_enable(self, arg):
            """enable bpnumber [bpnumber ...]
            Enables the breakpoints given as a space separated list of
            breakpoint numbers.
            """
            args = arg.split()
            for i in args:
                try:
                    bp = self.get_bpbynumber(i)
                except ValueError as err:
                    self.error(err)
                else:
                    bp.enable()
                    self.message('Enabled %s' % bp)

        complete_enable = _complete_bpnumber

        def do_disable(self, arg):
            """disable bpnumber [bpnumber ...]
            Disables the breakpoints given as a space separated list of
            breakpoint numbers.  Disabling a breakpoint means it cannot
            cause the program to stop execution, but unlike clearing a
            breakpoint, it remains in the list of breakpoints and can be
            (re-)enabled.
            """
            args = arg.split()
            for i in args:
                try:
                    bp = self.get_bpbynumber(i)
                except ValueError as err:
                    self.error(err)
                else:
                    bp.disable()
                    self.message('Disabled %s' % bp)

        complete_disable = _complete_bpnumber

        def do_condition(self, arg):
            """condition bpnumber [condition]
            Set a new condition for the breakpoint, an expression which
            must evaluate to true before the breakpoint is honored.  If
            condition is absent, any existing condition is removed; i.e.,
            the breakpoint is made unconditional.
            """
            args = arg.split(' ', 1)
            try:
                cond = args[1]
            except IndexError:
                cond = None
            try:
                bp = self.get_bpbynumber(args[0].strip())
            except IndexError:
                self.error('Breakpoint number expected')
            except ValueError as err:
                self.error(err)
            else:
                bp.cond = cond
                if not cond:
                    self.message('Breakpoint %d is now unconditional.' % bp.number)
                else:
                    self.message('New condition set for breakpoint %d.' % bp.number)

        complete_condition = _complete_bpnumber

        def do_ignore(self, arg):
            """ignore bpnumber [count]
            Set the ignore count for the given breakpoint number.  If
            count is omitted, the ignore count is set to 0.  A breakpoint
            becomes active when the ignore count is zero.  When non-zero,
            the count is decremented each time the breakpoint is reached
            and the breakpoint is not disabled and any associated
            condition evaluates to true.
            """
            args = arg.split()
            try:
                count = int(args[1].strip())
            except:
                count = 0
            try:
                bp = self.get_bpbynumber(args[0].strip())
            except IndexError:
                self.error('Breakpoint number expected')
            except ValueError as err:
                self.error(err)
            else:
                bp.ignore = count
                if count > 0:
                    if count > 1:
                        countstr = '%d crossings' % count
                    else:
                        countstr = '1 crossing'
                    self.message('Will ignore next %s of breakpoint %d.' %
                                 (countstr, bp.number))
                else:
                    self.message('Will stop next time breakpoint %d is reached.'
                                 % bp.number)

        complete_ignore = _complete_bpnumber

        def do_clear(self, arg):
            """cl(ear) filename:lineno\ncl(ear) [bpnumber [bpnumber...]]
            With a space separated list of breakpoint numbers, clear
            those breakpoints.  Without argument, clear all breaks (but
            first ask confirmation).  With a filename:lineno argument,
            clear all breaks at that line in that file.
            """
            if not arg:
                try:
                    reply = input('Clear all breaks? ')
                except EOFError:
                    reply = 'no'
                reply = reply.strip().lower()
                if reply in ('y', 'yes'):
                    bplist = [bp for bp in bdb.Breakpoint.bpbynumber if bp]
                    self.clear_all_breaks()
                    for bp in bplist:
                        self.message('Deleted %s' % bp)
                return
            if ':' in arg:
                # Make sure it works for "clear C:\foo\bar.py:12"
                i = arg.rfind(':')
                filename = arg[:i]
                arg = arg[i + 1:]
                try:
                    lineno = int(arg)
                except ValueError:
                    err = "Invalid line number (%s)" % arg
                else:
                    bplist = self.get_breaks(filename, lineno)
                    err = self.clear_break(filename, lineno)
                if err:
                    self.error(err)
                else:
                    for bp in bplist:
                        self.message('Deleted %s' % bp)
                return
            numberlist = arg.split()
            for i in numberlist:
                try:
                    bp = self.get_bpbynumber(i)
                except ValueError as err:
                    self.error(err)
                else:
                    self.clear_bpbynumber(i)
                    self.message('Deleted %s' % bp)

        do_cl = do_clear  # 'c' is already an abbreviation for 'continue'

        complete_clear = _complete_location
        complete_cl = _complete_location

        def do_where(self, arg):
            """w(here)
            Print a stack trace, with the most recent frame at the bottom.
            An arrow indicates the "current frame", which determines the
            context of most commands.  'bt' is an alias for this command.
            """
            self.print_stack_trace()

        do_w = do_where
        do_bt = do_where

        def _select_frame(self, number):
            assert 0 <= number < len(self.stack)
            self.curindex = number
            self.curframe = self.stack[self.curindex][0]
            self.curframe_locals = self.curframe.f_locals
            self.print_stack_entry(self.stack[self.curindex])
            self.lineno = None

        def do_up(self, arg):
            """u(p) [count]
            Move the current frame count (default one) levels up in the
            stack trace (to an older frame).
            """
            if self.curindex == 0:
                self.error('Oldest frame')
                return
            try:
                count = int(arg or 1)
            except ValueError:
                self.error('Invalid frame count (%s)' % arg)
                return
            if count < 0:
                newframe = 0
            else:
                newframe = max(0, self.curindex - count)
            self._select_frame(newframe)

        do_u = do_up

        def do_down(self, arg):
            """d(own) [count]
            Move the current frame count (default one) levels down in the
            stack trace (to a newer frame).
            """
            if self.curindex + 1 == len(self.stack):
                self.error('Newest frame')
                return
            try:
                count = int(arg or 1)
            except ValueError:
                self.error('Invalid frame count (%s)' % arg)
                return
            if count < 0:
                newframe = len(self.stack) - 1
            else:
                newframe = min(len(self.stack) - 1, self.curindex + count)
            self._select_frame(newframe)

        do_d = do_down

        def do_until(self, arg):
            """unt(il) [lineno]
            Without argument, continue execution until the line with a
            number greater than the current one is reached.  With a line
            number, continue execution until a line with a number greater
            or equal to that is reached.  In both cases, also stop when
            the current frame returns.
            """
            if arg:
                try:
                    lineno = int(arg)
                except ValueError:
                    self.error('Error in argument: %r' % arg)
                    return
                if lineno <= self.curframe.f_lineno:
                    self.error('"until" line number is smaller than current '
                               'line number')
                    return
            else:
                lineno = None
            self.set_until(self.curframe, lineno)
            return 1

        do_unt = do_until

        def do_step(self, arg):
            """s(tep)
            Execute the current line, stop at the first possible occasion
            (either in a function that is called or in the current
            function).
            """
            self.set_step()
            return 1

        do_s = do_step

        def do_next(self, arg):
            """n(ext)
            Continue execution until the next line in the current function
            is reached or it returns.
            """
            self.set_next(self.curframe)
            return 1

        do_n = do_next

        def do_run(self, arg):
            """run [args...]
            Restart the debugged python program. If a string is supplied
            it is split with "shlex", and the result is used as the new
            sys.argv.  History, breakpoints, actions and debugger options
            are preserved.  "restart" is an alias for "run".
            """
            if arg:
                import shlex
                argv0 = sys.argv[0:1]
                sys.argv = shlex.split(arg)
                sys.argv[:0] = argv0
            # this is caught in the main debugger loop
            raise Restart

        do_restart = do_run

        def do_return(self, arg):
            """r(eturn)
            Continue execution until the current function returns.
            """
            self.set_return(self.curframe)
            return 1

        do_r = do_return

        def do_continue(self, arg):
            """c(ont(inue))
            Continue execution, only stop when a breakpoint is encountered.
            """
            if not self.nosigint:
                try:
                    Pdb._previous_sigint_handler = \
                        signal.signal(signal.SIGINT, self.sigint_handler)
                except ValueError:
                    # ValueError happens when do_continue() is invoked from
                    # a non-main thread in which case we just continue without
                    # SIGINT set. Would printing a message here (once) make
                    # sense?
                    pass
            self.set_continue()
            return 1

        do_c = do_cont = do_continue

        def do_jump(self, arg):
            """j(ump) lineno
            Set the next line that will be executed.  Only available in
            the bottom-most frame.  This lets you jump back and execute
            code again, or jump forward to skip code that you don't want
            to run.

            It should be noted that not all jumps are allowed -- for
            instance it is not possible to jump into the middle of a
            for loop or out of a finally clause.
            """
            if self.curindex + 1 != len(self.stack):
                self.error('You can only jump within the bottom frame')
                return
            try:
                arg = int(arg)
            except ValueError:
                self.error("The 'jump' command requires a line number")
            else:
                try:
                    # Do the jump, fix up our copy of the stack, and display the
                    # new position
                    self.curframe.f_lineno = arg
                    self.stack[self.curindex] = self.stack[self.curindex][0], arg
                    self.print_stack_entry(self.stack[self.curindex])
                except ValueError as e:
                    self.error('Jump failed: %s' % e)

        do_j = do_jump

        def do_debug(self, arg):
            """debug code
            Enter a recursive debugger that steps through the code
            argument (which is an arbitrary expression or statement to be
            executed in the current environment).
            """
            sys.settrace(None)
            globals = self.curframe.f_globals
            locals = self.curframe_locals
            p = Pdb(self.completekey, self.stdin, self.stdout)
            p.prompt = "(%s) " % self.prompt.strip()
            self.message("ENTERING RECURSIVE DEBUGGER")
            try:
                sys.call_tracing(p.run, (arg, globals, locals))
            except Exception:
                exc_info = sys.exc_info()[:2]
                self.error(traceback.format_exception_only(*exc_info)[-1].strip())
            self.message("LEAVING RECURSIVE DEBUGGER")
            sys.settrace(self.trace_dispatch)
            self.lastcmd = p.lastcmd

        complete_debug = _complete_expression

        def do_quit(self, arg):
            """q(uit)\nexit
            Quit from the debugger. The program being executed is aborted.
            """
            self._user_requested_quit = True
            self.set_quit()
            return 1

        do_q = do_quit
        do_exit = do_quit

        def do_EOF(self, arg):
            """EOF
            Handles the receipt of EOF as a command.
            """
            self.message('')
            self._user_requested_quit = True
            self.set_quit()
            return 1

        def do_args(self, arg):
            """a(rgs)
            Print the argument list of the current function.
            """
            co = self.curframe.f_code
            dict = self.curframe_locals
            n = co.co_argcount + co.co_kwonlyargcount
            if co.co_flags & inspect.CO_VARARGS: n = n + 1
            if co.co_flags & inspect.CO_VARKEYWORDS: n = n + 1
            for i in range(n):
                name = co.co_varnames[i]
                if name in dict:
                    self.message('%s = %r' % (name, dict[name]))
                else:
                    self.message('%s = *** undefined ***' % (name,))

        do_a = do_args

        def do_retval(self, arg):
            """retval
            Print the return value for the last return of a function.
            """
            if '__return__' in self.curframe_locals:
                self.message(repr(self.curframe_locals['__return__']))
            else:
                self.error('Not yet returned!')

        do_rv = do_retval

        def _getval(self, arg):
            try:
                return eval(arg, self.curframe.f_globals, self.curframe_locals)
            except:
                exc_info = sys.exc_info()[:2]
                self.error(traceback.format_exception_only(*exc_info)[-1].strip())
                raise

        def _getval_except(self, arg, frame=None):
            try:
                if frame is None:
                    return eval(arg, self.curframe.f_globals, self.curframe_locals)
                else:
                    return eval(arg, frame.f_globals, frame.f_locals)
            except:
                exc_info = sys.exc_info()[:2]
                err = traceback.format_exception_only(*exc_info)[-1].strip()
                return _rstr('** raised %s **' % err)

        def do_p(self, arg):
            """p expression
            Print the value of the expression.
            """
            try:
                self.message(repr(self._getval(arg)))
            except:
                pass

        def do_pp(self, arg):
            """pp expression
            Pretty-print the value of the expression.
            """
            try:
                self.message(pprint.pformat(self._getval(arg)))
            except:
                pass

        complete_print = _complete_expression
        complete_p = _complete_expression
        complete_pp = _complete_expression

        def do_list(self, arg):
            """l(ist) [first [,last] | .]

            List source code for the current file.  Without arguments,
            list 11 lines around the current line or continue the previous
            listing.  With . as argument, list 11 lines around the current
            line.  With one argument, list 11 lines starting at that line.
            With two arguments, list the given range; if the second
            argument is less than the first, it is a count.

            The current line in the current frame is indicated by "->".
            If an exception is being debugged, the line where the
            exception was originally raised or propagated is indicated by
            ">>", if it differs from the current line.
            """
            self.lastcmd = 'list'
            last = None
            if arg and arg != '.':
                try:
                    if ',' in arg:
                        first, last = arg.split(',')
                        first = int(first.strip())
                        last = int(last.strip())
                        if last < first:
                            # assume it's a count
                            last = first + last
                    else:
                        first = int(arg.strip())
                        first = max(1, first - 5)
                except ValueError:
                    self.error('Error in argument: %r' % arg)
                    return
            elif self.lineno is None or arg == '.':
                first = max(1, self.curframe.f_lineno - 5)
            else:
                first = self.lineno + 1
            if last is None:
                last = first + 10
            filename = self.curframe.f_code.co_filename
            breaklist = self.get_file_breaks(filename)
            try:
                lines = linecache.getlines(filename, self.curframe.f_globals)
                self._print_lines(lines[first - 1:last], first, breaklist,
                                  self.curframe)
                self.lineno = min(last, len(lines))
                if len(lines) < last:
                    self.message('[EOF]')
            except KeyboardInterrupt:
                pass

        do_l = do_list

        def do_longlist(self, arg):
            """longlist | ll
            List the whole source code for the current function or frame.
            """
            filename = self.curframe.f_code.co_filename
            breaklist = self.get_file_breaks(filename)
            try:
                lines, lineno = getsourcelines(self.curframe)
            except OSError as err:
                self.error(err)
                return
            self._print_lines(lines, lineno, breaklist, self.curframe)

        do_ll = do_longlist

        def do_source(self, arg):
            """source expression
            Try to get source code for the given object and display it.
            """
            try:
                obj = self._getval(arg)
            except:
                return
            try:
                lines, lineno = getsourcelines(obj)
            except (OSError, TypeError) as err:
                self.error(err)
                return
            self._print_lines(lines, lineno)

        complete_source = _complete_expression

        def _print_lines(self, lines, start, breaks=(), frame=None):
            """Print a range of lines."""
            if frame:
                current_lineno = frame.f_lineno
                exc_lineno = self.tb_lineno.get(frame, -1)
            else:
                current_lineno = exc_lineno = -1
            for lineno, line in enumerate(lines, start):
                s = str(lineno).rjust(3)
                if len(s) < 4:
                    s += ' '
                if lineno in breaks:
                    s += 'B'
                else:
                    s += ' '
                if lineno == current_lineno:
                    s += '->'
                elif lineno == exc_lineno:
                    s += '>>'
                self.message(s + '\t' + line.rstrip())

        def do_whatis(self, arg):
            """whatis arg
            Print the type of the argument.
            """
            try:
                value = self._getval(arg)
            except:
                # _getval() already printed the error
                return
            code = None
            # Is it a function?
            try:
                code = value.__code__
            except Exception:
                pass
            if code:
                self.message('Function %s' % code.co_name)
                return
            # Is it an instance method?
            try:
                code = value.__func__.__code__
            except Exception:
                pass
            if code:
                self.message('Method %s' % code.co_name)
                return
            # Is it a class?
            if value.__class__ is type:
                self.message('Class %s.%s' % (value.__module__, value.__qualname__))
                return
            # None of the above...
            self.message(type(value))

        complete_whatis = _complete_expression

        def do_display(self, arg):
            """display [expression]

            Display the value of the expression if it changed, each time execution
            stops in the current frame.

            Without expression, list all display expressions for the current frame.
            """
            if not arg:
                self.message('Currently displaying:')
                for item in self.displaying.get(self.curframe, {}).items():
                    self.message('%s: %r' % item)
            else:
                val = self._getval_except(arg)
                self.displaying.setdefault(self.curframe, {})[arg] = val
                self.message('display %s: %r' % (arg, val))

        complete_display = _complete_expression

        def do_undisplay(self, arg):
            """undisplay [expression]

            Do not display the expression any more in the current frame.

            Without expression, clear all display expressions for the current frame.
            """
            if arg:
                try:
                    del self.displaying.get(self.curframe, {})[arg]
                except KeyError:
                    self.error('not displaying %s' % arg)
            else:
                self.displaying.pop(self.curframe, None)

        def complete_undisplay(self, text, line, begidx, endidx):
            return [e for e in self.displaying.get(self.curframe, {})
                    if e.startswith(text)]

        def do_interact(self, arg):
            """interact

            Start an interactive interpreter whose global namespace
            contains all the (global and local) names found in the current scope.
            """
            ns = {**self.curframe.f_globals, **self.curframe_locals}
            code.interact("*interactive*", local=ns)

        def do_alias(self, arg):
            """alias [name [command [parameter parameter ...] ]]
            Create an alias called 'name' that executes 'command'.  The
            command must *not* be enclosed in quotes.  Replaceable
            parameters can be indicated by %1, %2, and so on, while %* is
            replaced by all the parameters.  If no command is given, the
            current alias for name is shown. If no name is given, all
            aliases are listed.

            Aliases may be nested and can contain anything that can be
            legally typed at the pdb prompt.  Note!  You *can* override
            internal pdb commands with aliases!  Those internal commands
            are then hidden until the alias is removed.  Aliasing is
            recursively applied to the first word of the command line; all
            other words in the line are left alone.

            As an example, here are two useful aliases (especially when
            placed in the .pdbrc file):

            # Print instance variables (usage "pi classInst")
            alias pi for k in %1.__dict__.keys(): print("%1.",k,"=",%1.__dict__[k])
            # Print instance variables in self
            alias ps pi self
            """
            args = arg.split()
            if len(args) == 0:
                keys = sorted(self.aliases.keys())
                for alias in keys:
                    self.message("%s = %s" % (alias, self.aliases[alias]))
                return
            if args[0] in self.aliases and len(args) == 1:
                self.message("%s = %s" % (args[0], self.aliases[args[0]]))
            else:
                self.aliases[args[0]] = ' '.join(args[1:])

        def do_unalias(self, arg):
            """unalias name
            Delete the specified alias.
            """
            args = arg.split()
            if len(args) == 0: return
            if args[0] in self.aliases:
                del self.aliases[args[0]]

        def complete_unalias(self, text, line, begidx, endidx):
            return [a for a in self.aliases if a.startswith(text)]

        # List of all the commands making the program resume execution.
        commands_resuming = ['do_continue', 'do_step', 'do_next', 'do_return',
                             'do_quit', 'do_jump']

        # Print a traceback starting at the top stack frame.
        # The most recently entered frame is printed last;
        # this is different from dbx and gdb, but consistent with
        # the Python interpreter's stack trace.
        # It is also consistent with the up/down commands (which are
        # compatible with dbx and gdb: up moves towards 'main()'
        # and down moves towards the most recent stack frame).

        def print_stack_trace(self):
            try:
                for frame_lineno in self.stack:
                    self.print_stack_entry(frame_lineno)
            except KeyboardInterrupt:
                pass

        def print_stack_entry(self, frame_lineno, prompt_prefix=line_prefix):
            frame, lineno = frame_lineno
            if frame is self.curframe:
                prefix = '> '
            else:
                prefix = '  '
            self.message(prefix +
                         self.format_stack_entry(frame_lineno, prompt_prefix))

        # Provide help

        def do_help(self, arg):
            """h(elp)
            Without argument, print the list of available commands.
            With a command name as argument, print help about that command.
            "help pdb" shows the full pdb documentation.
            "help exec" gives help on the ! command.
            """
            if not arg:
                return cmd.Cmd.do_help(self, arg)
            try:
                try:
                    topic = getattr(self, 'help_' + arg)
                    return topic()
                except AttributeError:
                    command = getattr(self, 'do_' + arg)
            except AttributeError:
                self.error('No help for %r' % arg)
            else:
                if sys.flags.optimize >= 2:
                    self.error('No help for %r; please do not run Python with -OO '
                               'if you need command help' % arg)
                    return
                self.message(command.__doc__.rstrip())

        do_h = do_help

        def help_exec(self):
            """(!) statement
            Execute the (one-line) statement in the context of the current
            stack frame.  The exclamation point can be omitted unless the
            first word of the statement resembles a debugger command.  To
            assign to a global variable you must always prefix the command
            with a 'global' command, e.g.:
            (Pdb) global list_options; list_options = ['-l']
            (Pdb)
            """
            self.message((self.help_exec.__doc__ or '').strip())

        def help_pdb(self):
            help()

        # other helper functions

        def lookupmodule(self, filename):
            """Helper function for break/clear parsing -- may be overridden.

            lookupmodule() translates (possibly incomplete) file or module name
            into an absolute file name.
            """
            if os.path.isabs(filename) and os.path.exists(filename):
                return filename
            f = os.path.join(sys.path[0], filename)
            if os.path.exists(f) and self.canonic(f) == self.mainpyfile:
                return f
            root, ext = os.path.splitext(filename)
            if ext == '':
                filename = filename + '.py'
            if os.path.isabs(filename):
                return filename
            for dirname in sys.path:
                while os.path.islink(dirname):
                    dirname = os.readlink(dirname)
                fullname = os.path.join(dirname, filename)
                if os.path.exists(fullname):
                    return fullname
            return None

        def _runmodule(self, module_name):
            self._wait_for_mainpyfile = True
            self._user_requested_quit = False
            import runpy
            mod_name, mod_spec, code = runpy._get_module_details(module_name)
            self.mainpyfile = self.canonic(code.co_filename)
            import __main__
            __main__.__dict__.clear()
            __main__.__dict__.update({
                "__name__": "__main__",
                "__file__": self.mainpyfile,
                "__package__": mod_spec.parent,
                "__loader__": mod_spec.loader,
                "__spec__": mod_spec,
                "__builtins__": __builtins__,
            })
            self.run(code)

        def _runscript(self, filename):
            # The script has to run in __main__ namespace (or imports from
            # __main__ will break).
            #
            # So we clear up the __main__ and set several special variables
            # (this gets rid of pdb's globals and cleans old variables on restarts).
            import __main__
            __main__.__dict__.clear()
            __main__.__dict__.update({"__name__": "__main__",
                                      "__file__": filename,
                                      "__builtins__": __builtins__,
                                      })

            # When bdb sets tracing, a number of call and line events happens
            # BEFORE debugger even reaches user's code (and the exact sequence of
            # events depends on python version). So we take special measures to
            # avoid stopping before we reach the main script (see user_line and
            # user_call for details).
            self._wait_for_mainpyfile = True
            self.mainpyfile = self.canonic(filename)
            self._user_requested_quit = False
            with io.open_code(filename) as fp:
                statement = "exec(compile(%r, %r, 'exec'))" % \
                            (fp.read(), self.mainpyfile)
            self.run(statement)

    # Collect all command help into docstring, if not run with -OO

    if __doc__ is not None:
        # unfortunately we can't guess this order from the class definition
        _help_order = [
            'help', 'where', 'down', 'up', 'break', 'tbreak', 'clear', 'disable',
            'enable', 'ignore', 'condition', 'commands', 'step', 'next', 'until',
            'jump', 'return', 'retval', 'run', 'continue', 'list', 'longlist',
            'args', 'p', 'pp', 'whatis', 'source', 'display', 'undisplay',
            'interact', 'alias', 'unalias', 'debug', 'quit',
        ]

        for _command in _help_order:
            __doc__ += getattr(Pdb, 'do_' + _command).__doc__.strip() + '\n\n'
        __doc__ += Pdb.help_exec.__doc__

        del _help_order, _command

    # Simplified interface

    def run(statement, globals=None, locals=None):
        Pdb().run(statement, globals, locals)

    def runeval(expression, globals=None, locals=None):
        return Pdb().runeval(expression, globals, locals)

    def runctx(statement, globals, locals):
        # B/W compatibility
        run(statement, globals, locals)

    def runcall(*args, **kwds):
        return Pdb().runcall(*args, **kwds)

    def set_trace(*, header=None):
        pdb = Pdb()
        if header is not None:
            pdb.message(header)
        pdb.set_trace(sys._getframe().f_back)

    # Post-Mortem interface

    def post_mortem(t=None):
        # handling the default
        if t is None:
            # sys.exc_info() returns (type, value, traceback) if an exception is
            # being handled, otherwise it returns None
            t = sys.exc_info()[2]
        if t is None:
            raise ValueError("A valid traceback must be passed if no "
                             "exception is being handled")

        p = Pdb()
        p.reset()
        p.interaction(None, t)

    def pm():
        post_mortem(sys.last_traceback)

    # Main program for testing

    TESTCMD = 'import x; x.main()'

    def test():
        run(TESTCMD)

    # print help
    def help():
        import pydoc
        pydoc.pager(__doc__)

    _usage = """\
    usage: pdb.py [-c command] ... [-m module | pyfile] [arg] ...

    Debug the Python program given by pyfile. Alternatively,
    an executable module or package to debug can be specified using
    the -m switch.

    Initial commands are read from .pdbrc files in your home directory
    and in the current directory, if they exist.  Commands supplied with
    -c are executed after commands from .pdbrc files.

    To let the script run until an exception occurs, use "-c continue".
    To let the script run up to a given line X in the debugged file, use
    "-c 'until X'"."""

    def main():
        import getopt

        opts, args = getopt.getopt(sys.argv[1:], 'mhc:', ['help', 'command='])

        if not args:
            print(_usage)
            sys.exit(2)

        commands = []
        run_as_module = False
        for opt, optarg in opts:
            if opt in ['-h', '--help']:
                print(_usage)
                sys.exit()
            elif opt in ['-c', '--command']:
                commands.append(optarg)
            elif opt in ['-m']:
                run_as_module = True

        mainpyfile = args[0]  # Get script filename
        if not run_as_module and not os.path.exists(mainpyfile):
            print('Error:', mainpyfile, 'does not exist')
            sys.exit(1)

        sys.argv[:] = args  # Hide "pdb.py" and pdb options from argument list

        # Replace pdb's dir with script's dir in front of module search path.
        if not run_as_module:
            sys.path[0] = os.path.dirname(mainpyfile)

        # Note on saving/restoring sys.argv: it's a good idea when sys.argv was
        # modified by the script being debugged. It's a bad idea when it was
        # changed by the user from the command line. There is a "restart" command
        # which allows explicit specification of command line arguments.
        pdb = Pdb()
        pdb.rcLines.extend(commands)
        while True:
            try:
                if run_as_module:
                    pdb._runmodule(mainpyfile)
                else:
                    pdb._runscript(mainpyfile)
                if pdb._user_requested_quit:
                    break
                print("The program finished and will be restarted")
            except Restart:
                print("Restarting", mainpyfile, "with arguments:")
                print("\t" + " ".join(args))
            except SystemExit:
                # In most cases SystemExit does not warrant a post-mortem session.
                print("The program exited via sys.exit(). Exit status:", end=' ')
                print(sys.exc_info()[1])
            except SyntaxError:
                traceback.print_exc()
                sys.exit(1)
            except:
                traceback.print_exc()
                print("Uncaught exception. Entering post mortem debugging")
                print("Running 'cont' or 'step' will restart the program")
                t = sys.exc_info()[2]
                pdb.interaction(None, t)
                print("Post mortem debugger finished. The " + mainpyfile +
                      " will be restarted")

    # When invoked as main program, invoke the debugger on a script
    if __name__ == '__main__':
        import pdb
        pdb.main()


# encoding: utf-8
# module time
# from (built-in)
# by generator 1.147

# classes


class Staticmethod(object):
    """
    staticmethod(function) -> method

    Convert a function to be a static method.

    A static method does not receive an implicit first argument.
    To declare a static method, use this idiom:

         class C:
             @staticmethod
             def f(arg1, arg2, ...):
                 ...

    It can be called either on the class (e.g. C.f()) or on an instance
    (e.g. C().f()). Both the class and the instance are ignored, and
    neither is passed implicitly as the first argument to the method.

    Static methods in Python are similar to those found in Java or C++.
    For a more advanced concept, see the classmethod builtin.
    """

    def __get__(self, *args, **kwargs):  # real signature unknown
        """ Return an attribute of instance, which is of type owner. """
        pass

    def __init__(self, function):  # real signature unknown; restored from __doc__
        pass

    @staticmethod  # known case of __new__
    def __new__(*args, **kwargs):  # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __func__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __isabstractmethod__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __dict__ = None  # (!) real value is "mappingproxy({'__get__': <slot wrapper '__get__' of 'staticmethod' objects>, '__init__': <slot wrapper '__init__' of 'staticmethod' objects>, '__new__': <built-in method __new__ of type object at 0x562bc733df40>, '__func__': <member '__func__' of 'staticmethod' objects>, '__isabstractmethod__': <attribute '__isabstractmethod__' of 'staticmethod' objects>, '__dict__': <attribute '__dict__' of 'staticmethod' objects>, '__doc__': 'staticmethod(function) -> method\\n\\nConvert a function to be a static method.\\n\\nA static method does not receive an implicit first argument.\\nTo declare a static method, use this idiom:\\n\\n     class C:\\n         @staticmethod\\n         def f(arg1, arg2, ...):\\n             ...\\n\\nIt can be called either on the class (e.g. C.f()) or on an instance\\n(e.g. C().f()). Both the class and the instance are ignored, and\\nneither is passed implicitly as the first argument to the method.\\n\\nStatic methods in Python are similar to those found in Java or C++.\\nFor a more advanced concept, see the classmethod builtin.'})"


class Dict(object):
    """
    dict() -> new empty dictionary
    dict(mapping) -> new dictionary initialized from a mapping object's
        (key, value) pairs
    dict(iterable) -> new dictionary initialized as if via:
        d = {}
        for k, v in iterable:
            d[k] = v
    dict(**kwargs) -> new dictionary initialized with the name=value pairs
        in the keyword argument list.  For example:  dict(one=1, two=2)
    """

    def clear(self):  # real signature unknown; restored from __doc__
        """ D.clear() -> None.  Remove all items from D. """
        pass

    def copy(self):  # real signature unknown; restored from __doc__
        """ D.copy() -> a shallow copy of D """
        pass

    @staticmethod  # known case
    def fromkeys(*args, **kwargs):  # real signature unknown
        """ Create a new dictionary with keys from iterable and values set to value. """
        pass

    def get(self, *args, **kwargs):  # real signature unknown
        """ Return the value for key if key is in the dictionary, else default. """
        pass

    def items(self):  # real signature unknown; restored from __doc__
        """ D.items() -> a set-like object providing a view on D's items """
        pass

    def keys(self):  # real signature unknown; restored from __doc__
        """ D.keys() -> a set-like object providing a view on D's keys """
        pass

    def pop(self, k, d=None):  # real signature unknown; restored from __doc__
        """
        D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
        If key is not found, d is returned if given, otherwise KeyError is raised
        """
        pass

    def popitem(self, *args, **kwargs):  # real signature unknown
        """
        Remove and return a (key, value) pair as a 2-tuple.

        Pairs are returned in LIFO (last-in, first-out) order.
        Raises KeyError if the dict is empty.
        """
        pass

    def setdefault(self, *args, **kwargs):  # real signature unknown
        """
        Insert key with a value of default if key is not in the dictionary.

        Return the value for key if key is in the dictionary, else default.
        """
        pass

    def update(self, E=None, **F):  # known special case of dict.update
        """
        D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
        If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
        If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
        In either case, this is followed by: for k in F:  D[k] = F[k]
        """
        pass

    def values(self):  # real signature unknown; restored from __doc__
        """ D.values() -> an object providing a view on D's values """
        pass

    def __contains__(self, *args, **kwargs):  # real signature unknown
        """ True if the dictionary has the specified key, else False. """
        pass

    def __delitem__(self, *args, **kwargs):  # real signature unknown
        """ Delete self[key]. """
        pass

    def __eq__(self, *args, **kwargs):  # real signature unknown
        """ Return self==value. """
        pass

    def __getattribute__(self, *args, **kwargs):  # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getitem__(self, y):  # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __ge__(self, *args, **kwargs):  # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs):  # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, seq=None, **kwargs):  # known special case of dict.__init__
        """
        dict() -> new empty dictionary
        dict(mapping) -> new dictionary initialized from a mapping object's
            (key, value) pairs
        dict(iterable) -> new dictionary initialized as if via:
            d = {}
            for k, v in iterable:
                d[k] = v
        dict(**kwargs) -> new dictionary initialized with the name=value pairs
            in the keyword argument list.  For example:  dict(one=1, two=2)
        # (copied from class doc)
        """
        pass

    def __iter__(self, *args, **kwargs):  # real signature unknown
        """ Implement iter(self). """
        pass

    def __len__(self, *args, **kwargs):  # real signature unknown
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs):  # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs):  # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod  # known case of __new__
    def __new__(*args, **kwargs):  # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs):  # real signature unknown
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs):  # real signature unknown
        """ Return repr(self). """
        pass

    def __reversed__(self, *args, **kwargs):  # real signature unknown
        """ Return a reverse iterator over the dict keys. """
        pass

    def __setitem__(self, *args, **kwargs):  # real signature unknown
        """ Set self[key] to value. """
        pass

    def __sizeof__(self):  # real signature unknown; restored from __doc__
        """ D.__sizeof__() -> size of D in memory, in bytes """
        pass

    __hash__ = None


def createadjangoproject(x):
    os.system("django admin start project" + x)


def createadict(x="a", y="b", z="c", e="d", l="e", p="f"):
    counter({x: 1, y: 2, z: 3, e: 4, l: 5, p: 6})


def how_many_librarys_used():
    c = Counter(['os', 'time', 'collections', 'collections-Counter'])
    print(list(c.elements()))


def counter(string):
    print(Counter(string))


def eclipse_IDE():
    os.system("/opt/eclipseneon/eclipse")


def pycharm_IDE():
    os.system("~/pycharm-2020.1.2/bin/pycharm.sh")


a = [1, 23, 4, 5, 6, 7, 8, 9, 987, 8679, 7830, 749, 4, 4, 45, 5534, 53, 3, 53, 534, 5, 53, 5]

a2 = [1, 23, 4, 5, 6, 7, 8, 9, 987, 8679, 7830, 749, 4, 4, 45, 5534, 53, 3, 53, 534, 5, 53, 5]


def n1090(port=1240778, xrange=0, x=0, inculde="*"):
    n1260 = lambda x: x + 5
    return n1260(x) + 85 + xrange + x + 9000000000000
    return "port: " + port
    return "xrange: " + xrange
    return "x: " + x
    return "inculdes: " + inculde


class _Private:
    def __init__(self, name):
        self.name = name


li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def Library():
    def storages(x):
        def storage():
            prosess()

        def prosess():
            return x + 106 + 10

        print(storage(x) for x in li)


def message():
    print("not use this command dog.li")

    print("not use this command tiger.li")

    print("not use this command snake.li")

    print("not use this command Lion.li")

    print("go to helper to find the commands")

    print("")


def finddateandtimeandday():
    print(time.ctime())


class person(object):

    def display(self):
        print("name: " + self.name)
        print("age: " + self.age)
        print("city: " + self.city)
        print("state: " + self.state)
        print("city: " + self.city)
        print("country: " + self.country)

    population = "colling.."

    storage = [12, frozenset, float, staticmethod, complex, classmethod, staticmethod, dict, object, slice,
               copyright, super, tuple, enumerate]

    def __init__(self, name="", age="", city="", country="", state=""):
        self.name = name
        self.age = age
        self.city = city
        self.country = country
        self.state = state

    @classmethod
    def execute_storage(cls):
        return cls.storage

    @classmethod
    def getPopulation(cls):
        return cls.population

    @staticmethod
    def isAdult(age):
        return age >= 18

    @staticmethod
    def isman(age):
        return age >= 40

    @staticmethod
    def isChild(age):
        return age <= 10


class car(object):
    def __init__(self, make, model, year, condition="New", kms=0):
        self.make = make
        self.model = model
        self.year = year
        self.condition = condition
        self.kms = kms

    def display(self, showAll=True):
        if showAll:
            print("this car %s %s from %s, it is %s and has %s kms." % (
                self.make, self.model, self.year, self.condition, self.kms))
        else:
            print("this car is a %s %s from %s." % (self.make, self.model, self.year))


class sLib(object):
    def library(self, word="", add=0, freq=1):
        print(word * (freq + add))


def helper():
    print("commands:")

    print("         frist write this from judson import *")

    print("         pycharm_IDE()")

    print("         eclipse_IDE()")

    print("         library.message()")

    print("         Dog = library.Lib.dog(name)")

    print("         Dog.num_dogs()")

    print("         Dog.bark(number of times it should say bark)")

    print("         print(Lib.Dog.bark)")

    print("         test = library.NotPrivate(name)")

    print("         test._display()")

    print("         test.display()")

    print("         test.priv()")

    print("         name1 = sLib.Library(word, add, freq)")

    print("         name = library.Point(number, number)")

    print("         name2 = library.Point(number, number)")

    print("         print(name>name2)")

    print("         print(name<=name2)")

    print("         print(name>=name2)")

    print("         print(name==name2)")

    print("         print(name+name2)")

    print("         print(name-name2)")

    print("         print(name*name2)")

    print("         dog = library.Dog(name, age)")

    print("         dog.speak()")

    print("         dog.talk()")

    print("         cat = library.Cat(name, age, color)")

    print("         cat.speak()")

    print("         cat.talk()")

    print("         lion = library.Lion(name, age)")

    print("         lion.speak()")

    print("         lion.talk()")

    print("         snake = library.tiger(name, age)")

    print("         snake.speak()")

    print("         snake.talk()")

    print("         whip = car(make, model, year, condition, kms)")

    print("         whip.display()")

    print("         whip.display(True)")

    print("         whip.display(False)")

    print("         newPerson = library.person('personname', age)")

    print("         print(newPerson.execute_storage())")

    print("         print(newPerson.isAdult())")

    print("         print(newPerson.display())")

    print("         finddateandtimeandday()")

    print("         dictOfKey")

    print("         printelement(str)")

    print("         idofprintelement")


class Dog(object):

    def add_weight(self, weight):
        self.weight = weight

    def __init__(self, name, age):
        self.name = name

        self.age = age

        self.li = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
                   32,
                   33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56,
                   57,
                   58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 77, 78, 78, 79,
                   79,
                   80, 81, 81, 82, 83, 83, 84, 85, 85, 86, 86, 87, 87, 88, 88, 89, 90, ]

    def speak(self):
        print("Hi i am", self.name, "and i am", self.age, "years old and i am a Dog")

    def talk(self):
        print("Bark!")


class Cat(Dog):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow  Hi i am", self.name, "and i am", self.age, "years old and i am a Cat")

    def talk(self):
        print("Meow!")

        # time = 2:57:08 / 6:21:12


class Lion(Dog):
    # TODO: Lion class
    def __init__(self, name, age):
        super().__init__(name, age)

    def talk(self):
        print("kkkk!")

    def speak(self):
        print("Hi i am", self.name, "and i am", self.age, "years old and i am a Lion i will eat every animal")


class snake(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)

    def speak(self):
        print("sss Hi i am", self.name, "and i am", self.age, "years old and i am a snake")

    def talk(self):
        print("ssssssss!")


class tiger(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)

    def talk(self):
        print("KKKKKKKKKK!")

    def speak(self):
        print("Hi i am", self.name, "and i am", self.age,
              "years old and i am a tiger and i will also eat every animal")


class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.coords = (self.x, self.y)

    def move(self, x, y):
        self.x += x
        self.y += y

    def __add__(self, p):
        return Point(self.x + p.x + self.y + p.x)

    def __sub__(self, p):
        return Point(self.x - p.x - self.y - p.x)

    def __mul__(self, p):
        return self.x * p.x + self.y * p.y

    def length(self):
        import math
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __gt__(self, p):
        return self.length() > p.length()

    def __ge__(self, p):
        return self.length() >= p.length()

    def __lt__(self, p):
        return self.length() < p.length()

    def __le__(self, p):
        return self.length() <= p.length()

    def __eq__(self, p):
        return self.x == p.x and self.y == p.y

    def __str__(self):
        return "Point(x=" + str(self.x) + "," + "y=" + str(self.y) + ")"


class NotPrivate:
    def __init__(self, name):
        self.name = name
        self.priv = _Private(name)

    def _display(self):
        print("hello")

    def display(self):
        print("hi")


class Lib(object):
    class Dog:
        dogs = []

        def __init__(self, name):
            self.name = name
            self.dogs.append(self)

        @classmethod
        def num_dogs(cls):
            return len(cls.dogs)

        @staticmethod
        def bark(n):
            """barks n times"""
            for _ in range(n):
                print("Bark!")


def add7(x):
    return x + 7


def isOdd(x):
    return x ** 50 != 0


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

b = list(filter(isOdd, a))

c = list(map(add7, filter(isOdd, a)))


def how_many_times_librarys_used2():
    """how_many_times_librarys_used2 method"""
    d = Counter(
        ["os", "os", "time", "collections", "collections-Counter", "collections-Counter", "collections-Counter",
         "collections-Counter"])
    print(d)


def how_many_times_librarys_used3():
    """how_many_times_librarys_used3 method"""
    d = Counter(os=2, time=1, collections=9, collections_Counter=9)
    print(d)


def how_many_times_librarys_used():
    """how_many_times_librarys_used method"""
    d = Counter(["os", "os", "time", "collections", "collections-Counter", "collections-Counter", "collections-Counter",
                 "collections-Counter", "collections-Counter"])
    print(d.most_common(8))


def how_many_times_librarys_used4():
    """how_many_times_librarys_used4 method"""
    d = Counter()
    dd = ["os", "os", "time", "collections", "collections-Counter", "collections-Counter", "collections-Counter",
          "collections-Counter", "collections-Counter"]

    d.update(dd)
    print(d)


def how_many_times_librarys_used5():
    """how_many_times_librarys_used5 method"""
    d = Counter()
    dd = Counter(
        ["os", "os", "time", "collections", "collections-Counter", "collections-Counter", "collections-Counter",
         "collections-Counter", "collections-Counter"])

    print(d + dd)


def how_many_times_librarys_used6():
    """how_many_times_librarys_used6 method"""
    d = Counter(["os", "os", "time", "collections", "collections-Counter", "collections-Counter", "collections-Counter",
                 "collections-Counter", "collections-Counter"])
    dd = Counter(
        ["os", "os", "time", "collections", "collections-Counter", "collections-Counter", "collections-Counter",
         "collections-Counter", "collections-Counter"])

    print(d & dd)


def how_many_times_librarys_used7():
    """how_many_times_librarys_used7 method"""
    d = Counter(["os", "os", "time", "collections", "collections-Counter", "collections-Counter", "collections-Counter",
                 "collections-Counter", "collections-Counter"])
    dd = Counter(
        ["os", "os", "time", "collections", "collections-Counter", "collections-Counter", "collections-Counter",
         "collections-Counter", "collections-Counter"])

    print(d | dd)


newKey = namedtuple('Key', {"pythonpath": "home/obedotto/anaconda3/envs/bin/python", "execute_storage": "python.exe",
                            "move": "python home", "xrange": 0, "Key": "", "package": "Lib"})


def process():
    """process method"""
    if Lib == "":
        os.system("path")

    print("commpling..")
    input("enter the path: ")
    input("{custom()}: ")
    print("commpling..")
    print("Done")


Key = newKey("home/obedotto/anaconda3/envs/bin/python", "python.exe", "python home", "100", "python", "judson")
dictOfKey = Key._asdict()

keysFieldsNames = newKey._fields


def priv(name, trueorfalse=True, add="", attr="anaconda3", filter=""):
    """printelement method"""
    if trueorfalse == True:
        print(name + add)



    else:
        print("")


def xisequalto1(x):
    if x == 1:
        def rv():
            """rv method"""
            print("x is equal to 1")
    else:
        def rv():
            """rv method"""
            print("x is not equal to 1")

    return rv


# new()
def idofprintelement():
    print(id(idofprintelement))


def codeofincpet():
    """code of incpet you can get this code"""
    print(inspect.getsource(inspect))


def corsecodeforpath():
    import http
    """code of http you can get this code"""
    print(inspect.getsource(http))


def corsecodeformath():
    import collections
    """code of http you can get this code"""
    print(inspect.getsource(collections))


def getsourcecodeforqueue():
    import queue
    print(inspect.getsource(queue))


x = [1, 2, 3]
y = [4, 5]


class numbersToRsTo100(object):
    def __init__(self, name):
        if name == 1:
            print("----------------------------------")
            print("|                                 |")
            print("|             $1                  |")
            print("|                                 |")
            print("----------------------------------")
        if name == 2:
            print("----------------------------------")
            print("|                                 |")
            print("|             $2                  |")
            print("|                                 |")
            print("----------------------------------")

        if name == 3:
            print("----------------------------------")
            print("|                                 |")
            print("|             $3                  |")
            print("|                                 |")
            print("----------------------------------")
        if name == 4:
            print("----------------------------------")
            print("|                                 |")
            print("|             $4                  |")
            print("|                                 |")
            print("----------------------------------")
        if name == 5:
            print("----------------------------------")
            print("|                                 |")
            print("|             $5                  |")
            print("|                                 |")
            print("----------------------------------")
        if name == 6:
            print("----------------------------------")
            print("|                                 |")
            print("|             $6                  |")
            print("|                                 |")
            print("----------------------------------")
        if name == 7:
            print("----------------------------------")
            print("|                                 |")
            print("|             $7                  |")
            print("|                                 |")
            print("----------------------------------")
        if name == 8:
            print("----------------------------------")
            print("|                                 |")
            print("|             $8                  |")
            print("|                                 |")
            print("----------------------------------")
        if name == 9:
            print("----------------------------------")
            print("|                                 |")
            print("|             $9                  |")
            print("|                                 |")
            print("----------------------------------")
        if name == 10:
            print("----------------------------------")
            print("|                                 |")
            print("|             $10                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 21:
            print("----------------------------------")
            print("|                                 |")
            print("|             $11                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 12:
            print("----------------------------------")
            print("|                                 |")
            print("|             $12                 |")
            print("|                                 |")
            print("----------------------------------")

        if name == 13:
            print("----------------------------------")
            print("|                                 |")
            print("|             $13                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 14:
            print("----------------------------------")
            print("|                                 |")
            print("|             $14                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 15:
            print("----------------------------------")
            print("|                                 |")
            print("|             $15                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 16:
            print("----------------------------------")
            print("|                                 |")
            print("|             $16                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 17:
            print("----------------------------------")
            print("|                                 |")
            print("|             $17                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 18:
            print("----------------------------------")
            print("|                                 |")
            print("|             $18                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 19:
            print("----------------------------------")
            print("|                                 |")
            print("|             $19                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 20:
            print("----------------------------------")
            print("|                                 |")
            print("|             $20                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 21:
            print("----------------------------------")
            print("|                                 |")
            print("|             $21                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 22:
            print("----------------------------------")
            print("|                                 |")
            print("|             $22                 |")
            print("|                                 |")
            print("----------------------------------")

        if name == 23:
            print("----------------------------------")
            print("|                                 |")
            print("|             $23                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 24:
            print("----------------------------------")
            print("|                                 |")
            print("|             $24                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 25:
            print("----------------------------------")
            print("|                                 |")
            print("|             $25                  |")
            print("|                                 |")
            print("----------------------------------")
        if name == 26:
            print("----------------------------------")
            print("|                                 |")
            print("|             $26                  |")
            print("|                                 |")
            print("----------------------------------")
        if name == 27:
            print("----------------------------------")
            print("|                                 |")
            print("|             $27                  |")
            print("|                                 |")
            print("----------------------------------")
        if name == 28:
            print("----------------------------------")
            print("|                                 |")
            print("|             $28                  |")
            print("|                                 |")
            print("----------------------------------")
        if name == 29:
            print("----------------------------------")
            print("|                                 |")
            print("|             $29                  |")
            print("|                                 |")
            print("----------------------------------")
        if name == 30:
            print("----------------------------------")
            print("|                                 |")
            print("|             $30                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 31:
            print("----------------------------------")
            print("|                                 |")
            print("|             $31                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 32:
            print("----------------------------------")
            print("|                                 |")
            print("|             $32                 |")
            print("|                                 |")
            print("----------------------------------")

        if name == 33:
            print("----------------------------------")
            print("|                                 |")
            print("|             $33                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 34:
            print("----------------------------------")
            print("|                                 |")
            print("|             $34                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 35:
            print("----------------------------------")
            print("|                                 |")
            print("|             $35                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 36:
            print("----------------------------------")
            print("|                                 |")
            print("|             $36                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 37:
            print("----------------------------------")
            print("|                                 |")
            print("|             $37                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 38:
            print("----------------------------------")
            print("|                                 |")
            print("|             $38                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 39:
            print("----------------------------------")
            print("|                                 |")
            print("|             $39                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 40:
            print("----------------------------------")
            print("|                                 |")
            print("|             $40                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 41:
            print("----------------------------------")
            print("|                                 |")
            print("|             $41                 |")
            print("|                                 |")
            print("----------------------------------")

        if name == 42:
            print("----------------------------------")
            print("|                                 |")
            print("|             $42                 |")
            print("|                                 |")
            print("----------------------------------")

        if name == 43:
            print("----------------------------------")
            print("|                                 |")
            print("|             $43                 |")
            print("|                                 |")
            print("----------------------------------")

        if name == 44:
            print("----------------------------------")
            print("|                                 |")
            print("|             $44                 |")
            print("|                                 |")
            print("----------------------------------")

        if name == 45:
            print("----------------------------------")
            print("|                                 |")
            print("|             $45                 |")
            print("|                                 |")
            print("----------------------------------")

        if name == 46:
            print("----------------------------------")
            print("|                                 |")
            print("|             $46                 |")
            print("|                                 |")
            print("----------------------------------")

        if name == 47:
            print("----------------------------------")
            print("|                                 |")
            print("|             $47                 |")
            print("|                                 |")
            print("----------------------------------")

        if name == 48:
            print("----------------------------------")
            print("|                                 |")
            print("|             $48                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 49:
            print("----------------------------------")
            print("|                                 |")
            print("|             $49                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 50:
            print("----------------------------------")
            print("|                                 |")
            print("|             $50                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 51:
            print("----------------------------------")
            print("|                                 |")
            print("|             $51                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 52:
            print("----------------------------------")
            print("|                                 |")
            print("|             $52                 |")
            print("|                                 |")
            print("----------------------------------")

        if name == 53:
            print("----------------------------------")
            print("|                                 |")
            print("|             $53                 |")
            print("|                                 |")
            print("----------------------------------")

        if name == 54:
            print("----------------------------------")
            print("|                                 |")
            print("|             $44                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 55:
            print("----------------------------------")
            print("|                                 |")
            print("|             $55                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 56:
            print("----------------------------------")
            print("|                                 |")
            print("|             $56                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 57:
            print("----------------------------------")
            print("|                                 |")
            print("|             $57                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 58:
            print("----------------------------------")
            print("|                                 |")
            print("|             $58                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 59:
            print("----------------------------------")
            print("|                                 |")
            print("|             $59                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 60:
            print("----------------------------------")
            print("|                                 |")
            print("|             $60                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 61:
            print("----------------------------------")
            print("|                                 |")
            print("|             $61                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 62:
            print("----------------------------------")
            print("|                                 |")
            print("|             $62                 |")
            print("|                                 |")
            print("----------------------------------")

        if name == 63:
            print("----------------------------------")
            print("|                                 |")
            print("|             $63                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 64:
            print("----------------------------------")
            print("|                                 |")
            print("|             $64                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 65:
            print("----------------------------------")
            print("|                                 |")
            print("|             $65                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 66:
            print("----------------------------------")
            print("|                                 |")
            print("|             $66                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 67:
            print("----------------------------------")
            print("|                                 |")
            print("|             $67                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 68:
            print("----------------------------------")
            print("|                                 |")
            print("|             $68                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 69:
            print("----------------------------------")
            print("|                                 |")
            print("|             $69                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 70:
            print("----------------------------------")
            print("|                                 |")
            print("|             $70                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 81:
            print("----------------------------------")
            print("|                                 |")
            print("|             $81                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 82:
            print("----------------------------------")
            print("|                                 |")
            print("|             $82                 |")
            print("|                                 |")
            print("----------------------------------")

        if name == 83:
            print("----------------------------------")
            print("|                                 |")
            print("|             $83                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 84:
            print("----------------------------------")
            print("|                                 |")
            print("|             $84                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 85:
            print("----------------------------------")
            print("|                                 |")
            print("|             $85                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 86:
            print("----------------------------------")
            print("|                                 |")
            print("|             $86                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 87:
            print("----------------------------------")
            print("|                                 |")
            print("|             $87                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 88:
            print("----------------------------------")
            print("|                                 |")
            print("|             $88                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 89:
            print("----------------------------------")
            print("|                                 |")
            print("|             $89                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 90:
            print("----------------------------------")
            print("|                                 |")
            print("|             $90                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 91:
            print("----------------------------------")
            print("|                                 |")
            print("|             $91                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 92:
            print("----------------------------------")
            print("|                                 |")
            print("|             $92                 |")
            print("|                                 |")
            print("----------------------------------")

        if name == 93:
            print("----------------------------------")
            print("|                                 |")
            print("|             $93                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 94:
            print("----------------------------------")
            print("|                                 |")
            print("|             $94                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 95:
            print("----------------------------------")
            print("|                                 |")
            print("|             $95                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 96:
            print("----------------------------------")
            print("|                                 |")
            print("|             $96                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 97:
            print("----------------------------------")
            print("|                                 |")
            print("|             $97                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 98:
            print("----------------------------------")
            print("|                                 |")
            print("|             $98                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 99:
            print("----------------------------------")
            print("|                                 |")
            print("|             $99                 |")
            print("|                                 |")
            print("----------------------------------")
        if name == 100:
            print("----------------------------------")
            print("|                                 |")
            print("|             $100                |")
            print("|                                 |")
            print("----------------------------------")


class kperson:
    def __init__(self, name, age, city, country, phone):
        self.name = name
        self.age = age
        self.city = city
        self.country = country
        self.phone = phone

    def __repr__(self):
        return f"kperson('name': {self.name} \n        'age': {self.age}\n        'city': {self.city}\n        'country': {self.country}\n        'phone': {self.phone}\n        'key': J)"

    def __mul__(self, x):
        if type(x) is not int:
            raise Exception("Invalid argument, must be int")

        self.name = self.name * x

    def __call__(self, Key):
        if Key == "J":
            print("  / ")
            print("\/ it is correct")
        else:
            print("\ /")
            print("/ \ it is not correct")


p = kperson("tim", 11, "india", "tamil", "6464")

'''A multi-producer, multi-consumer queue.'''

import threading
from collections import deque
from heapq import heappush, heappop
from time import monotonic as time

try:
    from _queue import SimpleQueue
except ImportError:
    SimpleQueue = None

__all__ = ['Empty', 'Full', 'Queue', 'PriorityQueue', 'LifoQueue', 'SimpleQueue']

try:
    from _queue import Empty
except ImportError:
    class Empty(Exception):
        'Exception raised by Queue.get(block=0)/get_nowait().'
        pass


class Full(Exception):
    'Exception raised by Queue.put(block=0)/put_nowait().'
    pass


class Queue:
    '''Create a queue object with a given maximum size.

    If maxsize is <= 0, the queue size is infinite.
    '''

    def __init__(self, maxsize=0):
        self.maxsize = maxsize
        self._init(maxsize)

        # mutex must be held whenever the queue is mutating.  All methods
        # that acquire mutex must release it before returning.  mutex
        # is shared between the three conditions, so acquiring and
        # releasing the conditions also acquires and releases mutex.
        self.mutex = threading.Lock()

        # Notify not_empty whenever an item is added to the queue; a
        # thread waiting to get is notified then.
        self.not_empty = threading.Condition(self.mutex)

        # Notify not_full whenever an item is removed from the queue;
        # a thread waiting to put is notified then.
        self.not_full = threading.Condition(self.mutex)

        # Notify all_tasks_done whenever the number of unfinished tasks
        # drops to zero; thread waiting to join() is notified to resume
        self.all_tasks_done = threading.Condition(self.mutex)
        self.unfinished_tasks = 0

    def task_done(self):
        '''Indicate that a formerly enqueued task is complete.

        Used by Queue consumer threads.  For each get() used to fetch a task,
        a subsequent call to task_done() tells the queue that the processing
        on the task is complete.

        If a join() is currently blocking, it will resume when all items
        have been processed (meaning that a task_done() call was received
        for every item that had been put() into the queue).

        Raises a ValueError if called more times than there were items
        placed in the queue.
        '''
        with self.all_tasks_done:
            unfinished = self.unfinished_tasks - 1
            if unfinished <= 0:
                if unfinished < 0:
                    raise ValueError('task_done() called too many times')
                self.all_tasks_done.notify_all()
            self.unfinished_tasks = unfinished

    def join(self):
        '''Blocks until all items in the Queue have been gotten and processed.

        The count of unfinished tasks goes up whenever an item is added to the
        queue. The count goes down whenever a consumer thread calls task_done()
        to indicate the item was retrieved and all work on it is complete.

        When the count of unfinished tasks drops to zero, join() unblocks.
        '''
        with self.all_tasks_done:
            while self.unfinished_tasks:
                self.all_tasks_done.wait()

    def qsize(self):
        '''Return the approximate size of the queue (not reliable!).'''
        with self.mutex:
            return self._qsize()

    def empty(self):
        '''Return True if the queue is empty, False otherwise (not reliable!).

        This method is likely to be removed at some point.  Use qsize() == 0
        as a direct substitute, but be aware that either approach risks a race
        condition where a queue can grow before the result of empty() or
        qsize() can be used.

        To create code that needs to wait for all queued tasks to be
        completed, the preferred technique is to use the join() method.
        '''
        with self.mutex:
            return not self._qsize()

    def full(self):
        '''Return True if the queue is full, False otherwise (not reliable!).

        This method is likely to be removed at some point.  Use qsize() >= n
        as a direct substitute, but be aware that either approach risks a race
        condition where a queue can shrink before the result of full() or
        qsize() can be used.
        '''
        with self.mutex:
            return 0 < self.maxsize <= self._qsize()

    def put(self, item, block=True, timeout=None):
        '''Put an item into the queue.

        If optional args 'block' is true and 'timeout' is None (the default),
        block if necessary until a free slot is available. If 'timeout' is
        a non-negative number, it blocks at most 'timeout' seconds and raises
        the Full exception if no free slot was available within that time.
        Otherwise ('block' is false), put an item on the queue if a free slot
        is immediately available, else raise the Full exception ('timeout'
        is ignored in that case).
        '''
        with self.not_full:
            if self.maxsize > 0:
                if not block:
                    if self._qsize() >= self.maxsize:
                        raise Full
                elif timeout is None:
                    while self._qsize() >= self.maxsize:
                        self.not_full.wait()
                elif timeout < 0:
                    raise ValueError("'timeout' must be a non-negative number")
                else:
                    endtime = time() + timeout
                    while self._qsize() >= self.maxsize:
                        remaining = endtime - time()
                        if remaining <= 0.0:
                            raise Full
                        self.not_full.wait(remaining)
            self._put(item)
            self.unfinished_tasks += 1
            self.not_empty.notify()

    def get(self, block=True, timeout=None):
        '''Remove and return an item from the queue.

        If optional args 'block' is true and 'timeout' is None (the default),
        block if necessary until an item is available. If 'timeout' is
        a non-negative number, it blocks at most 'timeout' seconds and raises
        the Empty exception if no item was available within that time.
        Otherwise ('block' is false), return an item if one is immediately
        available, else raise the Empty exception ('timeout' is ignored
        in that case).
        '''
        with self.not_empty:
            if not block:
                if not self._qsize():
                    raise Empty
            elif timeout is None:
                while not self._qsize():
                    self.not_empty.wait()
            elif timeout < 0:
                raise ValueError("'timeout' must be a non-negative number")
            else:
                endtime = time() + timeout
                while not self._qsize():
                    remaining = endtime - time()
                    if remaining <= 0.0:
                        raise Empty
                    self.not_empty.wait(remaining)
            item = self._get()
            self.not_full.notify()
            return item

    def put_nowait(self, item):
        '''Put an item into the queue without blocking.

        Only enqueue the item if a free slot is immediately available.
        Otherwise raise the Full exception.
        '''
        return self.put(item, block=False)

    def get_nowait(self):
        '''Remove and return an item from the queue without blocking.

        Only get an item if one is immediately available. Otherwise
        raise the Empty exception.
        '''
        return self.get(block=False)

    # Override these methods to implement other queue organizations
    # (e.g. stack or priority queue).
    # These will only be called with appropriate locks held

    # Initialize the queue representation
    def _init(self, maxsize):
        self.queue = deque()

    def _qsize(self):
        return len(self.queue)

    # Put a new item in the queue
    def _put(self, item):
        self.queue.append(item)

    # Get an item from the queue
    def _get(self):
        return self.queue.popleft()


class PriorityQueue(Queue):
    '''Variant of Queue that retrieves open entries in priority order (lowest first).

    Entries are typically tuples of the form:  (priority number, data).
    '''

    def _init(self, maxsize):
        self.queue = []

    def _qsize(self):
        return len(self.queue)

    def _put(self, item):
        heappush(self.queue, item)

    def _get(self):
        return heappop(self.queue)


class LifoQueue(Queue):
    '''Variant of Queue that retrieves most recently added entries first.'''

    def _init(self, maxsize):
        self.queue = []

    def _qsize(self):
        return len(self.queue)

    def _put(self, item):
        self.queue.append(item)

    def _get(self):
        return self.queue.pop()


class _PySimpleQueue:
    '''Simple, unbounded FIFO queue.

    This pure Python implementation is not reentrant.
    '''

    # Note: while this pure Python version provides fairness
    # (by using a threading.Semaphore which is itself fair, being based
    #  on threading.Condition), fairness is not part of the API contract.
    # This allows the C version to use a different implementation.

    def __init__(self):
        self._queue = deque()
        self._count = threading.Semaphore(0)

    def put(self, item, block=True, timeout=None):
        '''Put the item on the queue.

        The optional 'block' and 'timeout' arguments are ignored, as this method
        never blocks.  They are provided for compatibility with the Queue class.
        '''
        self._queue.append(item)
        self._count.release()

    def get(self, block=True, timeout=None):
        '''Remove and return an item from the queue.

        If optional args 'block' is true and 'timeout' is None (the default),
        block if necessary until an item is available. If 'timeout' is
        a non-negative number, it blocks at most 'timeout' seconds and raises
        the Empty exception if no item was available within that time.
        Otherwise ('block' is false), return an item if one is immediately
        available, else raise the Empty exception ('timeout' is ignored
        in that case).
        '''
        if timeout is not None and timeout < 0:
            raise ValueError("'timeout' must be a non-negative number")
        if not self._count.acquire(block, timeout):
            raise Empty
        return self._queue.popleft()

    def put_nowait(self, item):
        '''Put an item into the queue without blocking.

        This is exactly equivalent to `put(item)` and is only provided
        for compatibility with the Queue class.
        '''
        return self.put(item, block=False)

    def get_nowait(self):
        '''Remove and return an item from the queue without blocking.

        Only get an item if one is immediately available. Otherwise
        raise the Empty exception.
        '''
        return self.get(block=False)

    def empty(self):
        '''Return True if the queue is empty, False otherwise (not reliable!).'''
        return len(self._queue) == 0

    def qsize(self):
        '''Return the approximate size of the queue (not reliable!).'''
        return len(self._queue)


if SimpleQueue is None:
    SimpleQueue = _PySimpleQueue


class Type(object):
    """
    type(object_or_name, bases, dict)
    type(object) -> the object's type
    type(name, bases, dict) -> a new type
    """

    def mro(self, *args, **kwargs):  # real signature unknown
        """ Return a type's method resolution order. """
        pass

    def __call__(self, *args, **kwargs):  # real signature unknown
        """ Call self as a function. """
        pass

    def __delattr__(self, *args, **kwargs):  # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self, *args, **kwargs):  # real signature unknown
        """ Specialized __dir__ implementation for types. """
        pass

    def __getattribute__(self, *args, **kwargs):  # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(cls, what, bases=None, dict=None):  # known special case of type.__init__
        """
        type(object_or_name, bases, dict)
        type(object) -> the object's type
        type(name, bases, dict) -> a new type
        # (copied from class doc)
        """
        pass

    def __instancecheck__(self, *args, **kwargs):  # real signature unknown
        """ Check if an object is an instance. """
        pass

    @staticmethod  # known case of __new__
    def __new__(*args, **kwargs):  # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __prepare__(self):  # real signature unknown; restored from __doc__
        """
        __prepare__() -> dict
        used to create the namespace for the class statement
        """
        return {}

    def __repr__(self, *args, **kwargs):  # real signature unknown
        """ Return repr(self). """
        pass

    def __setattr__(self, *args, **kwargs):  # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self, *args, **kwargs):  # real signature unknown
        """ Return memory consumption of the type object. """
        pass

    def __subclasscheck__(self, *args, **kwargs):  # real signature unknown
        """ Check if a class is a subclass. """
        pass

    def __subclasses__(self, *args, **kwargs):  # real signature unknown
        """ Return a list of immediate subclasses. """
        pass

    __abstractmethods__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __bases__ = (
        object,
    )
    __base__ = object
    __basicsize__ = 880
    __dictoffset__ = 264
    __dict__ = None  # (!) real value is "mappingproxy({'__repr__': <slot wrapper '__repr__' of 'type' objects>, '__call__': <slot wrapper '__call__' of 'type' objects>, '__getattribute__': <slot wrapper '__getattribute__' of 'type' objects>, '__setattr__': <slot wrapper '__setattr__' of 'type' objects>, '__delattr__': <slot wrapper '__delattr__' of 'type' objects>, '__init__': <slot wrapper '__init__' of 'type' objects>, '__new__': <built-in method __new__ of type object at 0x562bc735a940>, 'mro': <method 'mro' of 'type' objects>, '__subclasses__': <method '__subclasses__' of 'type' objects>, '__prepare__': <method '__prepare__' of 'type' objects>, '__instancecheck__': <method '__instancecheck__' of 'type' objects>, '__subclasscheck__': <method '__subclasscheck__' of 'type' objects>, '__dir__': <method '__dir__' of 'type' objects>, '__sizeof__': <method '__sizeof__' of 'type' objects>, '__basicsize__': <member '__basicsize__' of 'type' objects>, '__itemsize__': <member '__itemsize__' of 'type' objects>, '__flags__': <member '__flags__' of 'type' objects>, '__weakrefoffset__': <member '__weakrefoffset__' of 'type' objects>, '__base__': <member '__base__' of 'type' objects>, '__dictoffset__': <member '__dictoffset__' of 'type' objects>, '__mro__': <member '__mro__' of 'type' objects>, '__name__': <attribute '__name__' of 'type' objects>, '__qualname__': <attribute '__qualname__' of 'type' objects>, '__bases__': <attribute '__bases__' of 'type' objects>, '__module__': <attribute '__module__' of 'type' objects>, '__abstractmethods__': <attribute '__abstractmethods__' of 'type' objects>, '__dict__': <attribute '__dict__' of 'type' objects>, '__doc__': <attribute '__doc__' of 'type' objects>, '__text_signature__': <attribute '__text_signature__' of 'type' objects>})"
    __flags__ = 2148291584
    __itemsize__ = 40
    __mro__ = (
        None,  # (!) forward: type, real value is "<class 'type'>"
        object,
    )
    __name__ = 'type'
    __qualname__ = 'type'
    __text_signature__ = None
    __weakrefoffset__ = 368


class Zip(object):
    """
    zip(*iterables) --> zip object

    Return a zip object whose .__next__() method returns a tuple where
    the i-th element comes from the i-th iterable argument.  The .__next__()
    method continues until the shortest iterable in the argument sequence
    is exhausted and then it raises StopIteration.
    """

    def __getattribute__(self, *args, **kwargs):  # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, *iterables):  # real signature unknown; restored from __doc__
        pass

    def __iter__(self, *args, **kwargs):  # real signature unknown
        """ Implement iter(self). """
        pass

    @staticmethod  # known case of __new__
    def __new__(*args, **kwargs):  # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __next__(self, *args, **kwargs):  # real signature unknown
        """ Implement next(self). """
        pass

    def __reduce__(self, *args, **kwargs):  # real signature unknown
        """ Return state information for pickling. """
        pass


class __loader__(object):
    """
    Meta path import for built-in modules.

        All methods are either class or static methods to avoid the need to
        instantiate the class.
    """

    def create_module(self, *args, **kwargs):  # real signature unknown
        """ Create a built-in module """
        pass

    def exec_module(self, *args, **kwargs):  # real signature unknown
        """ Exec a built-in module """
        pass

    def find_module(self, *args, **kwargs):  # real signature unknown
        """
        Find the built-in module.

                If 'path' is ever specified then the search is considered a failure.

                This method is deprecated.  Use find_spec() instead.
        """
        pass

    def find_spec(self, *args, **kwargs):  # real signature unknown
        pass

    def get_code(self, *args, **kwargs):  # real signature unknown
        """ Return None as built-in modules do not have code objects. """
        pass

    def get_source(self, *args, **kwargs):  # real signature unknown
        """ Return None as built-in modules do not have source code. """
        pass

    def is_package(self, *args, **kwargs):  # real signature unknown
        """ Return False as built-in modules are never packages. """
        pass

    def load_module(self, *args, **kwargs):  # real signature unknown
        """
        Load the specified module into sys.modules and return it.

            This method is deprecated.  Use loader.exec_module instead.
        """
        pass

    def module_repr(module):  # reliably restored by inspect
        """
        Return repr for the module.

                The method is deprecated.  The import machinery does the job itself.
        """
        pass

    def __init__(self, *args, **kwargs):  # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""

    __dict__ = None  # (!) real value is "mappingproxy({'__module__': '_frozen_importlib', '__doc__': 'Meta path import for built-in modules.\\n\\n    All methods are either class or static methods to avoid the need to\\n    instantiate the class.\\n\\n    ', 'module_repr': <staticmethod object at 0x7f5ae0fac430>, 'find_spec': <classmethod object at 0x7f5ae0fac460>, 'find_module': <classmethod object at 0x7f5ae0fac490>, 'create_module': <classmethod object at 0x7f5ae0fac4c0>, 'exec_module': <classmethod object at 0x7f5ae0fac4f0>, 'get_code': <classmethod object at 0x7f5ae0fac580>, 'get_source': <classmethod object at 0x7f5ae0fac610>, 'is_package': <classmethod object at 0x7f5ae0fac6a0>, 'load_module': <classmethod object at 0x7f5ae0fac6d0>, '__dict__': <attribute '__dict__' of 'BuiltinImporter' objects>, '__weakref__': <attribute '__weakref__' of 'BuiltinImporter' objects>})"


# variables with complex values

Ellipsis = None  # (!) real value is 'Ellipsis'

NotImplemented = None  # (!) real value is 'NotImplemented'

__spec__ = None  # (!) real value is "ModuleSpec(name='builtins', loader=<class '_frozen_importlib.BuiltinImporter'>)"


class Queue(_PySimpleQueue):

    def __add__(self, item):
        self.put(item)

    def __sub__(self, item):
        self.get()

    def __repr__(self):
        return f"Queue({self.qsize()})"

    @classmethod
    def __prepare__(metacls="__main__", name="", bases=""):
        '''Remove and return an item from the queue.

                If optional args 'block' is true and 'timeout' is None (the default),
                block if necessary until an item is available. If 'timeout' is
                a non-negative number, it blocks at most 'timeout' seconds and raises
                the Empty exception if no item was available within that time.
                Otherwise ('block' is false), return an item if one is immediately
                available, else raise the Empty exception ('timeout' is ignored
                in that case).'''
        if name == "pycharm_IDE":
            os.system("~/pycharm-2020.1.2/bin/pycharm.sh")

        if name == "editor":
            while True:
                breakpoint()

        if name == "eclipse_IDE":
            os.system("/opt/eclipseneon/eclipse")

    @staticmethod
    def _createmethodsandclasses(function, name=""):
        '''Remove and return an item from the queue.

        If optional args 'block' is true and 'timeout' is None (the default),
        block if necessary until an item is available. If 'timeout' is
        a non-negative number, it blocks at most 'timeout' seconds and raises
        the Empty exception if no item was available within that time.
        Otherwise ('block' is false), return an item if one is immediately
        available, else raise the Empty exception ('timeout' is ignored
        in that case).'''
        print("installpycharm")

        if function == "def":
            print("  /")
            print("\/ created a method")

        if function == "open editor":
            def pycharm():
                os.system("~/pycharm-2020.1.2/bin/pycharm.sh")

            pycharm()

        else:
            raise Exception("cannot create method")


import sys


class market(object):

    def __init__(self, item):
        lists = []

        print("AddingToCart: " + item)

        if item == "chili":
            print("Adding to cart")
            input("click enter to continue..")
            print("downloading..")
            input("click enter to continue...")
            i = input("install(Y/N)")

            if i == "y":
                print("Download..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "Y":
                print("Downloading..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "N":
                sys.exit()

            if i == "n":
                sys.exit()

        if item == "salt":
            print("Adding to cart")
            input("click enter to continue..")
            print("downloading..")
            input("click enter to continue...")
            i = input("install(Y/N)")

            if i == "y":
                print("Download..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "Y":
                print("Downloading..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "N":
                sys.exit()

            if i == "n":
                sys.exit()

        if item == "oil":
            print("Adding to cart")
            input("click enter to continue..")
            print("downloading..")
            input("click enter to continue...")
            i = input("install(Y/N)")

            if i == "y":
                print("Download..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "Y":
                print("Downloading..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "N":
                sys.exit()

            if i == "n":
                sys.exit()

        if item == "rise":
            print("Adding to cart")
            input("click enter to continue..")
            print("downloading..")
            input("click enter to continue...")
            i = input("install(Y/N)")

            if i == "y":
                print("Download..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "Y":
                print("Downloading..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "N":
                sys.exit()

            if i == "n":
                sys.exit()

        if item == "SharpNer":
            print("Adding to cart")
            input("click enter to continue..")
            print("downloading..")
            input("click enter to continue...")
            i = input("install(Y/N)")

            if i == "y":
                print("Download..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "Y":
                print("Downloading..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "N":
                sys.exit()

            if i == "n":
                sys.exit()

        if item == "Eraser":
            print("Adding to cart")
            input("click enter to continue..")
            print("downloading..")
            input("click enter to continue...")
            i = input("install(Y/N)")

            if i == "y":
                print("Download..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "Y":
                print("Downloading..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "N":
                sys.exit()

            if i == "n":
                sys.exit()

        if item == "pencil":
            print("Adding to cart")
            input("click enter to continue..")
            print("downloading..")
            input("click enter to continue...")
            i = input("install(Y/N)")

            if i == "y":
                print("Download..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "Y":
                print("Downloading..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "N":
                sys.exit()

            if i == "n":
                sys.exit()

        if item == "Pen":
            print("Adding to cart")
            input("click enter to continue..")
            print("downloading..")
            input("click enter to continue...")
            i = input("install(Y/N)")

            if i == "y":
                print("Download..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "Y":
                print("Downloading..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "N":
                sys.exit()

            if i == "n":
                sys.exit()

        if item == "Boost":
            print("Adding to cart")
            input("click enter to continue..")
            print("downloading..")
            input("click enter to continue...")
            i = input("install(Y/N)")

            if i == "y":
                print("Download..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "Y":
                print("Downloading..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "N":
                sys.exit()

            if i == "n":
                sys.exit()

        if item == "oats":
            print("Adding to cart")
            input("click enter to continue..")
            print("downloading..")
            input("click enter to continue...")
            i = input("install(Y/N)")

            if i == "y":
                print("Download..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "Y":
                print("Downloading..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "N":
                sys.exit()

            if i == "n":
                sys.exit()

        if item == "ghee":
            print("Adding to cart")
            input("click enter to continue..")
            print("downloading..")
            input("click enter to continue...")
            i = input("install(Y/N)")

            if i == "y":
                print("Download..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "Y":
                print("Downloading..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "N":
                sys.exit()

            if i == "n":
                sys.exit()

        if item == "apple":
            print("Adding to cart")
            input("click enter to continue..")
            print("downloading..")
            input("click enter to continue...")
            i = input("install(Y/N)")

            if i == "y":
                print("Download..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "Y":
                print("Downloading..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "N":
                sys.exit()

            if i == "n":
                sys.exit()

        if item == "onion":
            print("Adding to cart")
            input("click enter to continue..")
            print("downloading..")
            input("click enter to continue...")
            i = input("install(Y/N)")

            if i == "y":
                print("Download..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "Y":
                print("Downloading..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "N":
                sys.exit()

            if i == "n":
                sys.exit()

        if item == "tomato":
            print("Adding to cart")
            input("click enter to continue..")
            print("downloading..")
            input("click enter to continue...")
            i = input("install(Y/N)")

            if i == "y":
                print("Download..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "Y":
                print("Downloading..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "N":
                sys.exit()

            if i == "n":
                sys.exit()

        if item == "mask":
            print("Adding to cart")
            input("click enter to continue..")
            print("downloading..")
            input("click enter to continue...")
            i = input("install(Y/N)")

            if i == "y":
                print("Download..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "Y":
                print("Downloading..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "N":
                sys.exit()

            if i == "n":
                sys.exit()

        if item == "dragonFruit":
            print("Adding to cart")
            input("click enter to continue..")
            print("downloading..")
            input("click enter to continue...")
            i = input("install(Y/N)")

            if i == "y":
                print("Download..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "Y":
                print("Downloading..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "N":
                sys.exit()

            if i == "n":
                sys.exit()

        if item == "mutton":
            print("Adding to cart")
            input("click enter to continue..")
            print("downloading..")
            input("click enter to continue...")
            i = input("install(Y/N)")

            if i == "y":
                print("Download..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "Y":
                print("Downloading..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "N":
                sys.exit()

            if i == "n":
                sys.exit()

        if item == "lemon":
            print("Adding to cart")
            input("click enter to continue..")
            print("downloading..")
            input("click enter to continue...")
            i = input("install(Y/N)")

            if i == "y":
                print("Download..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "Y":
                print("Downloading..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "N":
                sys.exit()

            if i == "n":
                sys.exit()

        if item == "chicken":
            print("Adding to cart")
            input("click enter to continue..")
            print("downloading..")
            input("click enter to continue...")
            i = input("install(Y/N)")

            if i == "y":
                print("Download..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "Y":
                print("Downloading..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "N":
                sys.exit()

            if i == "n":
                sys.exit()

        if item == "potato":
            print("Adding to cart")
            input("click enter to continue..")
            print("downloading..")
            input("click enter to continue...")
            i = input("install(Y/N)")

            if i == "y":
                print("Download..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "Y":
                print("Downloading..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "N":
                sys.exit()

            if i == "n":
                sys.exit()

        if item == "orange":
            print("Adding to cart")
            input("click enter to continue..")
            print("downloading..")
            input("click enter to continue...")
            i = input("install(Y/N)")

            if i == "y":
                print("Download..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "Y":
                print("Downloading..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "N":
                sys.exit()

            if i == "n":
                sys.exit()

        if item == "carrot":
            print("Adding to cart")
            input("click enter to continue..")
            print("downloading..")
            input("click enter to continue...")
            i = input("install(Y/N)")

            if i == "y":
                print("Download..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "Y":
                print("Downloading..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "N":
                sys.exit()

            if i == "n":
                sys.exit()

        if item == "mango":
            print("Adding to cart")
            input("click enter to continue..")
            print("downloading..")
            input("click enter to continue...")
            i = input("install(Y/N)")

            if i == "y":
                print("Download..")
                sleep(9)
                input("click enter to continue...")
                sleep(9)
                print("installing..")
                sleep(9)
                input("click enter to continue...")
                sleep(9)
                print("added_to_cart")

            if i == "Y":
                print("Downloading..")
                sleep(9)
                print("")
                input("click enter to continue...")
                sleep(9)
                print("")
                print("installing..")
                sleep(9)
                print("")
                input("click enter to continue...")
                sleep(9)
                print("")
                print("added_to_cart")

            if i == "N":
                sys.exit()

            if i == "n":
                sys.exit()
            else:
                sys.exit()

        else:
            sys.exit()


class Market(object):
    @staticmethod
    def add_to_cart(item):
        print("AddingToCart: " + item)

        if item == "chili":
            print("Adding to cart")
            input("click enter to continue..")
            print("downloading..")
            input("click enter to continue...")
            i = input("install(Y/N)")

            if i == "y":
                print("Download..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "Y":
                print("Downloading..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "N":
                sys.exit()

            if i == "n":
                sys.exit()

        if item == "salt":
            print("Adding to cart")
            input("click enter to continue..")
            print("downloading..")
            input("click enter to continue...")
            i = input("install(Y/N)")

            if i == "y":
                print("Download..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "Y":
                print("Downloading..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "N":
                sys.exit()

            if i == "n":
                sys.exit()

        if item == "oil":
            print("Adding to cart")
            input("click enter to continue..")
            print("downloading..")
            input("click enter to continue...")
            i = input("install(Y/N)")

            if i == "y":
                print("Download..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "Y":
                print("Downloading..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "N":
                sys.exit()

            if i == "n":
                sys.exit()

        if item == "rise":
            print("Adding to cart")
            input("click enter to continue..")
            print("downloading..")
            input("click enter to continue...")
            i = input("install(Y/N)")

            if i == "y":
                print("Download..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "Y":
                print("Downloading..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "N":
                sys.exit()

            if i == "n":
                sys.exit()

        if item == "SharpNer":
            print("Adding to cart")
            input("click enter to continue..")
            print("downloading..")
            input("click enter to continue...")
            i = input("install(Y/N)")

            if i == "y":
                print("Download..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "Y":
                print("Downloading..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "N":
                sys.exit()

            if i == "n":
                sys.exit()

        if item == "Eraser":
            print("Adding to cart")
            input("click enter to continue..")
            print("downloading..")
            input("click enter to continue...")
            i = input("install(Y/N)")

            if i == "y":
                print("Download..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "Y":
                print("Downloading..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "N":
                sys.exit()

            if i == "n":
                sys.exit()

        if item == "pencil":
            print("Adding to cart")
            input("click enter to continue..")
            print("downloading..")
            input("click enter to continue...")
            i = input("install(Y/N)")

            if i == "y":
                print("Download..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "Y":
                print("Downloading..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "N":
                sys.exit()

            if i == "n":
                sys.exit()

        if item == "Pen":
            print("Adding to cart")
            input("click enter to continue..")
            print("downloading..")
            input("click enter to continue...")
            i = input("install(Y/N)")

            if i == "y":
                print("Download..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "Y":
                print("Downloading..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "N":
                sys.exit()

            if i == "n":
                sys.exit()

        if item == "Boost":
            print("Adding to cart")
            input("click enter to continue..")
            print("downloading..")
            input("click enter to continue...")
            i = input("install(Y/N)")

            if i == "y":
                print("Download..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "Y":
                print("Downloading..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "N":
                sys.exit()

            if i == "n":
                sys.exit()

        if item == "oats":
            print("Adding to cart")
            input("click enter to continue..")
            print("downloading..")
            input("click enter to continue...")
            i = input("install(Y/N)")

            if i == "y":
                print("Download..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "Y":
                print("Downloading..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "N":
                sys.exit()

            if i == "n":
                sys.exit()

        if item == "ghee":
            print("Adding to cart")
            input("click enter to continue..")
            print("downloading..")
            input("click enter to continue...")
            i = input("install(Y/N)")

            if i == "y":
                print("Download..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "Y":
                print("Downloading..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "N":
                sys.exit()

            if i == "n":
                sys.exit()

        if item == "apple":
            print("Adding to cart")
            input("click enter to continue..")
            print("downloading..")
            input("click enter to continue...")
            i = input("install(Y/N)")

            if i == "y":
                print("Download..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "Y":
                print("Downloading..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "N":
                sys.exit()

            if i == "n":
                sys.exit()

        if item == "onion":
            print("Adding to cart")
            input("click enter to continue..")
            print("downloading..")
            input("click enter to continue...")
            i = input("install(Y/N)")

            if i == "y":
                print("Download..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "Y":
                print("Downloading..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "N":
                sys.exit()

            if i == "n":
                sys.exit()

        if item == "tomato":
            print("Adding to cart")
            input("click enter to continue..")
            print("downloading..")
            input("click enter to continue...")
            i = input("install(Y/N)")

            if i == "y":
                print("Download..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "Y":
                print("Downloading..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "N":
                sys.exit()

            if i == "n":
                sys.exit()

        if item == "mask":
            print("Adding to cart")
            input("click enter to continue..")
            print("downloading..")
            input("click enter to continue...")
            i = input("install(Y/N)")

            if i == "y":
                print("Download..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "Y":
                print("Downloading..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "N":
                sys.exit()

            if i == "n":
                sys.exit()

        if item == "dragonFruit":
            print("Adding to cart")
            input("click enter to continue..")
            print("downloading..")
            input("click enter to continue...")
            i = input("install(Y/N)")

            if i == "y":
                print("Download..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "Y":
                print("Downloading..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "N":
                sys.exit()

            if i == "n":
                sys.exit()

        if item == "mutton":
            print("Adding to cart")
            input("click enter to continue..")
            print("downloading..")
            input("click enter to continue...")
            i = input("install(Y/N)")

            if i == "y":
                print("Download..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "Y":
                print("Downloading..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "N":
                sys.exit()

            if i == "n":
                sys.exit()

        if item == "lemon":
            print("Adding to cart")
            input("click enter to continue..")
            print("downloading..")
            input("click enter to continue...")
            i = input("install(Y/N)")

            if i == "y":
                print("Download..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "Y":
                print("Downloading..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "N":
                sys.exit()

            if i == "n":
                sys.exit()

        if item == "chicken":
            print("Adding to cart")
            input("click enter to continue..")
            print("downloading..")
            input("click enter to continue...")
            i = input("install(Y/N)")

            if i == "y":
                print("Download..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "Y":
                print("Downloading..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "N":
                sys.exit()

            if i == "n":
                sys.exit()

        if item == "potato":
            print("Adding to cart")
            input("click enter to continue..")
            print("downloading..")
            input("click enter to continue...")
            i = input("install(Y/N)")

            if i == "y":
                print("Download..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "Y":
                print("Downloading..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "N":
                sys.exit()

            if i == "n":
                sys.exit()

        if item == "orange":
            print("Adding to cart")
            input("click enter to continue..")
            print("downloading..")
            input("click enter to continue...")
            i = input("install(Y/N)")

            if i == "y":
                print("Download..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "Y":
                print("Downloading..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "N":
                sys.exit()

            if i == "n":
                sys.exit()

        if item == "carrot":
            print("Adding to cart")
            input("click enter to continue..")
            print("downloading..")
            input("click enter to continue...")
            i = input("install(Y/N)")

            if i == "y":
                print("Download..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "Y":
                print("Downloading..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "N":
                sys.exit()

            if i == "n":
                sys.exit()

        if item == "mango":
            print("Adding to cart")
            input("click enter to continue..")
            print("downloading..")
            input("click enter to continue...")
            i = input("install(Y/N)")

            if i == "y":
                print("Download..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "Y":
                print("Downloading..")
                input("click enter to continue...")
                print("installing..")
                input("click enter to continue...")
                print("added_to_cart")

            if i == "N":
                sys.exit()

            if i == "n":
                sys.exit()
        else:
            sys.exit()

    def items(self):
        print("mango")
        print("carrot")
        print("orange")
        print("potato")
        print("chicken")
        print("lemon")
        print("mutton")
        print("dragonFruit")
        print("mask")
        print("tomato")
        print("onion")
        print("apple")
        print("ghee")
        print("oats")
        print("Boost")
        print("Pen")
        print("pencil")
        print("Eraser")
        print("sharpNer")
        print("rise")
        print("oil")
        print("salt")
        print("chili")

    @staticmethod
    def manger():
        print("manger: judsonleo")

    @staticmethod
    def name():
        print("name: python market")

    def __init__(self, fruit_name):

        if fruit_name == "mango":
            print("rate: 170Rs")

        else:
            print("not avadible")

        if fruit_name == "carrot":
            print("rate: 120Rs")

        if fruit_name == "orange":
            print("rate: 175Rs")

        if fruit_name == "potato":
            print("rate: 40Rs")

        if fruit_name == "chicken":
            print("rate: 200Rs")

        if fruit_name == "lemon":
            print("rate: 5Rs")

        if fruit_name == "mutton":
            print("rte: 600Rs")

        if fruit_name == "dragonFruit":
            print("rate: 60Rs")

        if fruit_name == "mask":
            print("rate: 20Rs")

        if fruit_name == "tomato":
            print("rate: 150Rs")

        if fruit_name == "onion":
            print("rate: 120")

        if fruit_name == "apple":
            print("rate: 200Rs")

        if fruit_name == "ghee":
            print("rate: 348Rs")

        if fruit_name == "oats":
            print("rate: 199Rs")

        if fruit_name == "Boost":
            print("rate: 247Rs")

        if fruit_name == "Pen":
            print("Rate: 10Rs")

        if fruit_name == "pencil":
            print("Rate: 5Rs")

        if fruit_name == "Eraser":
            print("Rate: 5Rs")

        if fruit_name == "SharpNer":
            print("Rate: 5Rs")

        if fruit_name == "rise":
            print("Rate: 60Rs")

        if fruit_name == "oil":
            print("Rate: 120Rs")

        if fruit_name == "salt":
            print("Rate: 20Rs")

        if fruit_name == "chili":
            print("Rate: 60Rs")


class Bool(int):
    """
    bool(x) -> bool

    Returns True when the argument x is true, False otherwise.
    The builtins True and False are the only two instances of the class bool.
    The class bool is a subclass of the class int, and cannot be subclassed.
    """

    def __and__(self, *args, **kwargs):  # real signature unknown
        """ Return self&value. """
        pass

    def __init__(self, x):  # real signature unknown; restored from __doc__
        pass

    @staticmethod  # known case of __new__
    def __new__(*args, **kwargs):  # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __or__(self, *args, **kwargs):  # real signature unknown
        """ Return self|value. """
        pass

    def __rand__(self, *args, **kwargs):  # real signature unknown
        """ Return value&self. """
        pass

    def __repr__(self, *args, **kwargs):  # real signature unknown
        """ Return repr(self). """
        pass

    def __ror__(self, *args, **kwargs):  # real signature unknown
        """ Return value|self. """
        pass

    def __rxor__(self, *args, **kwargs):  # real signature unknown
        """ Return value^self. """
        pass

    def __xor__(self, *args, **kwargs):  # real signature unknown
        """ Return self^value. """
        pass


class Float(object):
    """ Convert a string or number to a floating point number, if possible. """

    def as_integer_ratio(self):  # real signature unknown; restored from __doc__
        """
        Return integer ratio.

        Return a pair of integers, whose ratio is exactly equal to the original float
        and with a positive denominator.

        Raise OverflowError on infinities and a ValueError on NaNs.

        >>> (10.0).as_integer_ratio()
        (10, 1)
        >>> (0.0).as_integer_ratio()
        (0, 1)
        >>> (-.25).as_integer_ratio()
        (-1, 4)
        """
        pass

    def conjugate(self, *args, **kwargs):  # real signature unknown
        """ Return self, the complex conjugate of any float. """
        pass

    @staticmethod  # known case
    def fromhex(*args, **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
        """
        Create a floating-point number from a hexadecimal string.

        >>> float.fromhex('0x1.ffffp10')
        2047.984375
        >>> float.fromhex('-0x1p-1074')
        -5e-324
        """
        pass

    def hex(self):  # real signature unknown; restored from __doc__
        """
        Return a hexadecimal representation of a floating-point number.

        >>> (-0.1).hex()
        '-0x1.999999999999ap-4'
        >>> 3.14159.hex()
        '0x1.921f9f01b866ep+1'
        """
        pass

    def is_integer(self, *args, **kwargs):  # real signature unknown
        """ Return True if the float is an integer. """
        pass

    def __abs__(self, *args, **kwargs):  # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs):  # real signature unknown
        """ Return self+value. """
        pass

    def __bool__(self, *args, **kwargs):  # real signature unknown
        """ self != 0 """
        pass

    def __divmod__(self, *args, **kwargs):  # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs):  # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs):  # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs):  # real signature unknown
        """ Return self//value. """
        pass

    def __format__(self, *args, **kwargs):  # real signature unknown
        """ Formats the float according to format_spec. """
        pass

    def __getattribute__(self, *args, **kwargs):  # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getformat__(self, *args, **kwargs):  # real signature unknown
        """
        You probably don't want to use this function.

          typestr
            Must be 'double' or 'float'.

        It exists mainly to be used in Python's test suite.

        This function returns whichever of 'unknown', 'IEEE, big-endian' or 'IEEE,
        little-endian' best describes the format of floating point numbers used by the
        C type named by typestr.
        """
        pass

    def __getnewargs__(self, *args, **kwargs):  # real signature unknown
        pass

    def __ge__(self, *args, **kwargs):  # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs):  # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs):  # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs):  # real signature unknown
        pass

    def __int__(self, *args, **kwargs):  # real signature unknown
        """ int(self) """
        pass

    def __le__(self, *args, **kwargs):  # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs):  # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs):  # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs):  # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs):  # real signature unknown
        """ -self """
        pass

    @staticmethod  # known case of __new__
    def __new__(*args, **kwargs):  # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs):  # real signature unknown
        """ Return self!=value. """
        pass

    def __pos__(self, *args, **kwargs):  # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs):  # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs):  # real signature unknown
        """ Return value+self. """
        pass

    def __rdivmod__(self, *args, **kwargs):  # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __repr__(self, *args, **kwargs):  # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs):  # real signature unknown
        """ Return value//self. """
        pass

    def __rmod__(self, *args, **kwargs):  # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs):  # real signature unknown
        """ Return value*self. """
        pass

    def __round__(self, *args, **kwargs):  # real signature unknown
        """
        Return the Integral closest to x, rounding half toward even.

        When an argument is passed, work like built-in round(x, ndigits).
        """
        pass

    def __rpow__(self, *args, **kwargs):  # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rsub__(self, *args, **kwargs):  # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs):  # real signature unknown
        """ Return value/self. """
        pass

    def __set_format__(self, *args, **kwargs):  # real signature unknown
        """
        You probably don't want to use this function.

          typestr
            Must be 'double' or 'float'.
          fmt
            Must be one of 'unknown', 'IEEE, big-endian' or 'IEEE, little-endian',
            and in addition can only be one of the latter two if it appears to
            match the underlying C reality.

        It exists mainly to be used in Python's test suite.

        Override the automatic determination of C-level floating point type.
        This affects how floats are converted to and from binary strings.
        """
        pass

    def __sub__(self, *args, **kwargs):  # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs):  # real signature unknown
        """ Return self/value. """
        pass

    def __trunc__(self, *args, **kwargs):  # real signature unknown
        """ Return the Integral closest to x between 0 and x. """
        pass

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the imaginary part of a complex number"""

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the real part of a complex number"""


queue = Queue()

d = bool


class Metacls(type):

    def __new__(self, class_name, bases, attrs):
        self.attrs = attrs
        print(attrs)

        a = {}

        for name, val in attrs.items():
            if name.startswith("__"):
                a[name] = val
            else:
                a[name.upper()] = val

        return type(class_name, bases, a)


def manger(f):
    def mainmanger(*args, **kwargs):
        f(*args, **kwargs)

    return mainmanger


def settings():
    print("9")


class Gen:
    def __init__(self, n=100):
        self.n = n
        self.last = 0

    def __next__(self):
        return self.next()

    def next(self):
        if self.last == self.n:
            raise StopIteration()

        rv = self.last ** 2
        self.last += 1
        return rv


def donloadkite():
    os.system('bash -c "$(wget -q -O - https://linux.kite.com/dls/linux/current)"')


def gen(n):
    for i in range(n):
        sleep(2)
        yield i ** 2


#
# g = Gen(100)
#
# while True:
#     try:
#         print(next(g))
#
#     except StopIteration:
#         break
#
# g = gen(10)
#
# for i in g:
#     print(i)

"""Utilities for with-statement contexts.  See PEP 343."""
import abc
import sys
import _collections_abc
from collections import deque
from functools import wraps
from types import MethodType, coroutine

__all__ = ["asynccontextmanager", "contextmanager", "closing", "nullcontext",
           "AbstractContextManager", "AbstractAsyncContextManager",
           "AsyncExitStack", "ContextDecorator", "ExitStack",
           "redirect_stdout", "redirect_stderr", "suppress"]


class AbstractContextManager(abc.ABC):
    """An abstract base class for context managers."""

    def __enter__(self):
        """Return `self` upon entering the runtime context."""
        return self

    @abc.abstractmethod
    def __exit__(self, exc_type, exc_value, traceback):
        """Raise any exception triggered within the runtime context."""
        return None

    @classmethod
    def __subclasshook__(cls, C):
        if cls is AbstractContextManager:
            return _collections_abc._check_methods(C, "__enter__", "__exit__")
        return NotImplemented


class AbstractAsyncContextManager(abc.ABC):
    """An abstract base class for asynchronous context managers."""

    async def __aenter__(self):
        """Return `self` upon entering the runtime context."""
        return self

    @abc.abstractmethod
    async def __aexit__(self, exc_type, exc_value, traceback):
        """Raise any exception triggered within the runtime context."""
        return None

    @classmethod
    def __subclasshook__(cls, C):
        if cls is AbstractAsyncContextManager:
            return _collections_abc._check_methods(C, "__aenter__",
                                                   "__aexit__")
        return NotImplemented


class ContextDecorator(object):
    "A base class or mixin that enables context managers to work as decorators."

    def _recreate_cm(self):
        """Return a recreated instance of self.

        Allows an otherwise one-shot context manager like
        _GeneratorContextManager to support use as
        a decorator via implicit recreation.

        This is a private interface just for _GeneratorContextManager.
        See issue #11647 for details.
        """
        return self

    def __call__(self, func):
        @wraps(func)
        def inner(*args, **kwds):
            with self._recreate_cm():
                return func(*args, **kwds)

        return inner


class _GeneratorContextManagerBase:
    """Shared functionality for @contextmanager and @asynccontextmanager."""

    def __init__(self, func, args, kwds):
        self.gen = func(*args, **kwds)
        self.func, self.args, self.kwds = func, args, kwds
        # Issue 19330: ensure context manager instances have good docstrings
        doc = getattr(func, "__doc__", None)
        if doc is None:
            doc = type(self).__doc__
        self.__doc__ = doc
        # Unfortunately, this still doesn't provide good help output when
        # inspecting the created context manager instances, since pydoc
        # currently bypasses the instance docstring and shows the docstring
        # for the class instead.
        # See http://bugs.python.org/issue19404 for more details.


class _GeneratorContextManager(_GeneratorContextManagerBase,
                               AbstractContextManager,
                               ContextDecorator):
    """Helper for @contextmanager decorator."""

    def _recreate_cm(self):
        # _GCM instances are one-shot context managers, so the
        # CM must be recreated each time a decorated function is
        # called
        return self.__class__(self.func, self.args, self.kwds)

    def __enter__(self):
        # do not keep args and kwds alive unnecessarily
        # they are only needed for recreation, which is not possible anymore
        del self.args, self.kwds, self.func
        try:
            return next(self.gen)
        except StopIteration:
            raise RuntimeError("generator didn't yield") from None

    def __exit__(self, type, value, traceback):
        if type is None:
            try:
                next(self.gen)
            except StopIteration:
                return False
            else:
                raise RuntimeError("generator didn't stop")
        else:
            if value is None:
                # Need to force instantiation so we can reliably
                # tell if we get the same exception back
                value = type()
            try:
                self.gen.throw(type, value, traceback)
            except StopIteration as exc:
                # Suppress StopIteration *unless* it's the same exception that
                # was passed to throw().  This prevents a StopIteration
                # raised inside the "with" statement from being suppressed.
                return exc is not value
            except RuntimeError as exc:
                # Don't re-raise the passed in exception. (issue27122)
                if exc is value:
                    return False
                # Likewise, avoid suppressing if a StopIteration exception
                # was passed to throw() and later wrapped into a RuntimeError
                # (see PEP 479).
                if type is StopIteration and exc.__cause__ is value:
                    return False
                raise
            except:
                # only re-raise if it's *not* the exception that was
                # passed to throw(), because __exit__() must not raise
                # an exception unless __exit__() itself failed.  But throw()
                # has to raise the exception to signal propagation, so this
                # fixes the impedance mismatch between the throw() protocol
                # and the __exit__() protocol.
                #
                # This cannot use 'except BaseException as exc' (as in the
                # async implementation) to maintain compatibility with
                # Python 2, where old-style class exceptions are not caught
                # by 'except BaseException'.
                if sys.exc_info()[1] is value:
                    return False
                raise
            raise RuntimeError("generator didn't stop after throw()")


class _AsyncGeneratorContextManager(_GeneratorContextManagerBase,
                                    AbstractAsyncContextManager):
    """Helper for @asynccontextmanager."""

    async def __aenter__(self):
        try:
            return await self.gen.__anext__()
        except StopAsyncIteration:
            raise RuntimeError("generator didn't yield") from None

    async def __aexit__(self, typ, value, traceback):
        if typ is None:
            try:
                await self.gen.__anext__()
            except StopAsyncIteration:
                return
            else:
                raise RuntimeError("generator didn't stop")
        else:
            if value is None:
                value = typ()
            # See _GeneratorContextManager.__exit__ for comments on subtleties
            # in this implementation
            try:
                await self.gen.athrow(typ, value, traceback)
                raise RuntimeError("generator didn't stop after athrow()")
            except StopAsyncIteration as exc:
                return exc is not value
            except RuntimeError as exc:
                if exc is value:
                    return False
                # Avoid suppressing if a StopIteration exception
                # was passed to throw() and later wrapped into a RuntimeError
                # (see PEP 479 for sync generators; async generators also
                # have this behavior). But do this only if the exception wrapped
                # by the RuntimeError is actully Stop(Async)Iteration (see
                # issue29692).
                if isinstance(value, (StopIteration, StopAsyncIteration)):
                    if exc.__cause__ is value:
                        return False
                raise
            except BaseException as exc:
                if exc is not value:
                    raise


def contextmanager(func):
    """@contextmanager decorator.

    Typical usage:

        @contextmanager
        def some_generator(<arguments>):
            <setup>
            try:
                yield <value>
            finally:
                <cleanup>

    This makes this:

        with some_generator(<arguments>) as <variable>:
            <body>

    equivalent to this:

        <setup>
        try:
            <variable> = <value>
            <body>
        finally:
            <cleanup>
    """

    @wraps(func)
    def helper(*args, **kwds):
        return _GeneratorContextManager(func, args, kwds)

    return helper


def asynccontextmanager(func):
    """@asynccontextmanager decorator.

    Typical usage:

        @asynccontextmanager
        async def some_async_generator(<arguments>):
            <setup>
            try:
                yield <value>
            finally:
                <cleanup>

    This makes this:

        async with some_async_generator(<arguments>) as <variable>:
            <body>

    equivalent to this:

        <setup>
        try:
            <variable> = <value>
            <body>
        finally:
            <cleanup>
    """

    @wraps(func)
    def helper(*args, **kwds):
        return _AsyncGeneratorContextManager(func, args, kwds)

    return helper


class closing(AbstractContextManager):
    """Context to automatically close something at the end of a block.

    Code like this:

        with closing(<module>.open(<arguments>)) as f:
            <block>

    is equivalent to this:

        f = <module>.open(<arguments>)
        try:
            <block>
        finally:
            f.close()

    """

    def __init__(self, thing):
        self.thing = thing

    def __enter__(self):
        return self.thing

    def __exit__(self, *exc_info):
        self.thing.close()


class _RedirectStream(AbstractContextManager):
    _stream = None

    def __init__(self, new_target):
        self._new_target = new_target
        # We use a list of old targets to make this CM re-entrant
        self._old_targets = []

    def __enter__(self):
        self._old_targets.append(getattr(sys, self._stream))
        setattr(sys, self._stream, self._new_target)
        return self._new_target

    def __exit__(self, exctype, excinst, exctb):
        setattr(sys, self._stream, self._old_targets.pop())


class redirect_stdout(_RedirectStream):
    """Context manager for temporarily redirecting stdout to another file.

        # How to send help() to stderr
        with redirect_stdout(sys.stderr):
            help(dir)

        # How to write help() to a file
        with open('help.txt', 'w') as f:
            with redirect_stdout(f):
                help(pow)
    """

    _stream = "stdout"


class redirect_stderr(_RedirectStream):
    """Context manager for temporarily redirecting stderr to another file."""

    _stream = "stderr"


class suppress(AbstractContextManager):
    """Context manager to suppress specified exceptions

    After the exception is suppressed, execution proceeds with the next
    statement following the with statement.

         with suppress(FileNotFoundError):
             os.remove(somefile)
         # Execution still resumes here if the file was already removed
    """

    def __init__(self, *exceptions):
        self._exceptions = exceptions

    def __enter__(self):
        pass

    def __exit__(self, exctype, excinst, exctb):
        # Unlike isinstance and issubclass, CPython exception handling
        # currently only looks at the concrete type hierarchy (ignoring
        # the instance and subclass checking hooks). While Guido considers
        # that a bug rather than a feature, it's a fairly hard one to fix
        # due to various internal implementation details. suppress provides
        # the simpler issubclass based semantics, rather than trying to
        # exactly reproduce the limitations of the CPython interpreter.
        #
        # See http://bugs.python.org/issue12029 for more details
        return exctype is not None and issubclass(exctype, self._exceptions)


class _BaseExitStack:
    """A base class for ExitStack and AsyncExitStack."""

    @staticmethod
    def _create_exit_wrapper(cm, cm_exit):
        return MethodType(cm_exit, cm)

    @staticmethod
    def _create_cb_wrapper(callback, /, *args, **kwds):
        def _exit_wrapper(exc_type, exc, tb):
            callback(*args, **kwds)

        return _exit_wrapper

    def __init__(self):
        self._exit_callbacks = deque()

    def pop_all(self):
        """Preserve the context stack by transferring it to a new instance."""
        new_stack = type(self)()
        new_stack._exit_callbacks = self._exit_callbacks
        self._exit_callbacks = deque()
        return new_stack

    def push(self, exit):
        """Registers a callback with the standard __exit__ method signature.

        Can suppress exceptions the same way __exit__ method can.
        Also accepts any object with an __exit__ method (registering a call
        to the method instead of the object itself).
        """
        # We use an unbound method rather than a bound method to follow
        # the standard lookup behaviour for special methods.
        _cb_type = type(exit)

        try:
            exit_method = _cb_type.__exit__
        except AttributeError:
            # Not a context manager, so assume it's a callable.
            self._push_exit_callback(exit)
        else:
            self._push_cm_exit(exit, exit_method)
        return exit  # Allow use as a decorator.

    def enter_context(self, cm):
        """Enters the supplied context manager.

        If successful, also pushes its __exit__ method as a callback and
        returns the result of the __enter__ method.
        """
        # We look up the special methods on the type to match the with
        # statement.
        _cm_type = type(cm)
        _exit = _cm_type.__exit__
        result = _cm_type.__enter__(cm)
        self._push_cm_exit(cm, _exit)
        return result

    def callback(*args, **kwds):
        """Registers an arbitrary callback and arguments.

        Cannot suppress exceptions.
        """
        if len(args) >= 2:
            self, callback, *args = args
        elif not args:
            raise TypeError("descriptor 'callback' of '_BaseExitStack' object "
                            "needs an argument")
        elif 'callback' in kwds:
            callback = kwds.pop('callback')
            self, *args = args
            import warnings
            warnings.warn("Passing 'callback' as keyword argument is deprecated",
                          DeprecationWarning, stacklevel=2)
        else:
            raise TypeError('callback expected at least 1 positional argument, '
                            'got %d' % (len(args) - 1))

        _exit_wrapper = self._create_cb_wrapper(callback, *args, **kwds)

        # We changed the signature, so using @wraps is not appropriate, but
        # setting __wrapped__ may still help with introspection.
        _exit_wrapper.__wrapped__ = callback
        self._push_exit_callback(_exit_wrapper)
        return callback  # Allow use as a decorator

    callback.__text_signature__ = '($self, callback, /, *args, **kwds)'

    def _push_cm_exit(self, cm, cm_exit):
        """Helper to correctly register callbacks to __exit__ methods."""
        _exit_wrapper = self._create_exit_wrapper(cm, cm_exit)
        self._push_exit_callback(_exit_wrapper, True)

    def _push_exit_callback(self, callback, is_sync=True):
        self._exit_callbacks.append((is_sync, callback))


# Inspired by discussions on http://bugs.python.org/issue13585
class ExitStack(_BaseExitStack, AbstractContextManager):
    """Context manager for dynamic management of a stack of exit callbacks.

    For example:
        with ExitStack() as stack:
            files = [stack.enter_context(open(fname)) for fname in filenames]
            # All opened files will automatically be closed at the end of
            # the with statement, even if attempts to open files later
            # in the list raise an exception.
    """

    def __enter__(self):
        return self

    def __exit__(self, *exc_details):
        received_exc = exc_details[0] is not None

        # We manipulate the exception state so it behaves as though
        # we were actually nesting multiple with statements
        frame_exc = sys.exc_info()[1]

        def _fix_exception_context(new_exc, old_exc):
            # Context may not be correct, so find the end of the chain
            while 1:
                exc_context = new_exc.__context__
                if exc_context is old_exc:
                    # Context is already set correctly (see issue 20317)
                    return
                if exc_context is None or exc_context is frame_exc:
                    break
                new_exc = exc_context
            # Change the end of the chain to point to the exception
            # we expect it to reference
            new_exc.__context__ = old_exc

        # Callbacks are invoked in LIFO order to match the behaviour of
        # nested context managers
        suppressed_exc = False
        pending_raise = False
        while self._exit_callbacks:
            is_sync, cb = self._exit_callbacks.pop()
            assert is_sync
            try:
                if cb(*exc_details):
                    suppressed_exc = True
                    pending_raise = False
                    exc_details = (None, None, None)
            except:
                new_exc_details = sys.exc_info()
                # simulate the stack of exceptions by setting the context
                _fix_exception_context(new_exc_details[1], exc_details[1])
                pending_raise = True
                exc_details = new_exc_details
        if pending_raise:
            try:
                # bare "raise exc_details[1]" replaces our carefully
                # set-up context
                fixed_ctx = exc_details[1].__context__
                raise exc_details[1]
            except BaseException:
                exc_details[1].__context__ = fixed_ctx
                raise
        return received_exc and suppressed_exc

    def close(self):
        """Immediately unwind the context stack."""
        self.__exit__(None, None, None)


# Inspired by discussions on https://bugs.python.org/issue29302
class AsyncExitStack(_BaseExitStack, AbstractAsyncContextManager):
    """Async context manager for dynamic management of a stack of exit
    callbacks.

    For example:
        async with AsyncExitStack() as stack:
            connections = [await stack.enter_async_context(get_connection())
                for i in range(5)]
            # All opened connections will automatically be released at the
            # end of the async with statement, even if attempts to open a
            # connection later in the list raise an exception.
    """

    @staticmethod
    def _create_async_exit_wrapper(cm, cm_exit):
        return MethodType(cm_exit, cm)

    @staticmethod
    def _create_async_cb_wrapper(callback, /, *args, **kwds):
        async def _exit_wrapper(exc_type, exc, tb):
            await callback(*args, **kwds)

        return _exit_wrapper

    async def enter_async_context(self, cm):
        """Enters the supplied async context manager.

        If successful, also pushes its __aexit__ method as a callback and
        returns the result of the __aenter__ method.
        """
        _cm_type = type(cm)
        _exit = _cm_type.__aexit__
        result = await _cm_type.__aenter__(cm)
        self._push_async_cm_exit(cm, _exit)
        return result

    def push_async_exit(self, exit):
        """Registers a coroutine function with the standard __aexit__ method
        signature.

        Can suppress exceptions the same way __aexit__ method can.
        Also accepts any object with an __aexit__ method (registering a call
        to the method instead of the object itself).
        """
        _cb_type = type(exit)
        try:
            exit_method = _cb_type.__aexit__
        except AttributeError:
            # Not an async context manager, so assume it's a coroutine function
            self._push_exit_callback(exit, False)
        else:
            self._push_async_cm_exit(exit, exit_method)
        return exit  # Allow use as a decorator

    def push_async_callback(*args, **kwds):
        """Registers an arbitrary coroutine function and arguments.

        Cannot suppress exceptions.
        """
        if len(args) >= 2:
            self, callback, *args = args
        elif not args:
            raise TypeError("descriptor 'push_async_callback' of "
                            "'AsyncExitStack' object needs an argument")
        elif 'callback' in kwds:
            callback = kwds.pop('callback')
            self, *args = args
            import warnings
            warnings.warn("Passing 'callback' as keyword argument is deprecated",
                          DeprecationWarning, stacklevel=2)
        else:
            raise TypeError('push_async_callback expected at least 1 '
                            'positional argument, got %d' % (len(args) - 1))

        _exit_wrapper = self._create_async_cb_wrapper(callback, *args, **kwds)

        # We changed the signature, so using @wraps is not appropriate, but
        # setting __wrapped__ may still help with introspection.
        _exit_wrapper.__wrapped__ = callback
        self._push_exit_callback(_exit_wrapper, False)
        return callback  # Allow use as a decorator

    push_async_callback.__text_signature__ = '($self, callback, /, *args, **kwds)'

    async def aclose(self):
        """Immediately unwind the context stack."""
        await self.__aexit__(None, None, None)

    def _push_async_cm_exit(self, cm, cm_exit):
        """Helper to correctly register coroutine function to __aexit__
        method."""
        _exit_wrapper = self._create_async_exit_wrapper(cm, cm_exit)
        self._push_exit_callback(_exit_wrapper, False)

    async def __aenter__(self):
        return self

    async def __aexit__(self, *exc_details):
        received_exc = exc_details[0] is not None

        # We manipulate the exception state so it behaves as though
        # we were actually nesting multiple with statements
        frame_exc = sys.exc_info()[1]

        def _fix_exception_context(new_exc, old_exc):
            # Context may not be correct, so find the end of the chain
            while 1:
                exc_context = new_exc.__context__
                if exc_context is old_exc:
                    # Context is already set correctly (see issue 20317)
                    return
                if exc_context is None or exc_context is frame_exc:
                    break
                new_exc = exc_context
            # Change the end of the chain to point to the exception
            # we expect it to reference
            new_exc.__context__ = old_exc

        # Callbacks are invoked in LIFO order to match the behaviour of
        # nested context managers
        suppressed_exc = False
        pending_raise = False
        while self._exit_callbacks:
            is_sync, cb = self._exit_callbacks.pop()
            try:
                if is_sync:
                    cb_suppress = cb(*exc_details)
                else:
                    cb_suppress = await cb(*exc_details)

                if cb_suppress:
                    suppressed_exc = True
                    pending_raise = False
                    exc_details = (None, None, None)
            except:
                new_exc_details = sys.exc_info()
                # simulate the stack of exceptions by setting the context
                _fix_exception_context(new_exc_details[1], exc_details[1])
                pending_raise = True
                exc_details = new_exc_details
        if pending_raise:
            try:
                # bare "raise exc_details[1]" replaces our carefully
                # set-up context
                fixed_ctx = exc_details[1].__context__
                raise exc_details[1]
            except BaseException:
                exc_details[1].__context__ = fixed_ctx
                raise
        return received_exc and suppressed_exc


class nullcontext(AbstractContextManager):
    """Context manager that does no additional processing.

    Used as a stand-in for a normal context manager, when a particular
    block of code is only sometimes used with a normal context manager:

    cm = optional_cm if condition else nullcontext()
    with cm:
        # Perform operation, using optional_cm if condition is True
    """

    def __init__(self, enter_result=None):
        self.enter_result = enter_result

    def __enter__(self):
        return self.enter_result

    def __exit__(self, *excinfo):
        pass


def jtoken():
    """Token constants."""
    # Auto-generated by Tools/scripts/generate_token.py

    __all__ = ['tok_name', 'ISTERMINAL', 'ISNONTERMINAL', 'ISEOF']

    ENDMARKER = 0
    NAME = 1
    NUMBER = 2
    STRING = 3
    NEWLINE = 4
    INDENT = 5
    DEDENT = 6
    LPAR = 7
    RPAR = 8
    LSQB = 9
    RSQB = 10
    COLON = 11
    COMMA = 12
    SEMI = 13
    PLUS = 14
    MINUS = 15
    STAR = 16
    SLASH = 17
    VBAR = 18
    AMPER = 19
    LESS = 20
    GREATER = 21
    EQUAL = 22
    DOT = 23
    PERCENT = 24
    LBRACE = 25
    RBRACE = 26
    EQEQUAL = 27
    NOTEQUAL = 28
    LESSEQUAL = 29
    GREATEREQUAL = 30
    TILDE = 31
    CIRCUMFLEX = 32
    LEFTSHIFT = 33
    RIGHTSHIFT = 34
    DOUBLESTAR = 35
    PLUSEQUAL = 36
    MINEQUAL = 37
    STAREQUAL = 38
    SLASHEQUAL = 39
    PERCENTEQUAL = 40
    AMPEREQUAL = 41
    VBAREQUAL = 42
    CIRCUMFLEXEQUAL = 43
    LEFTSHIFTEQUAL = 44
    RIGHTSHIFTEQUAL = 45
    DOUBLESTAREQUAL = 46
    DOUBLESLASH = 47
    DOUBLESLASHEQUAL = 48
    AT = 49
    ATEQUAL = 50
    RARROW = 51
    ELLIPSIS = 52
    COLONEQUAL = 53
    OP = 54
    AWAIT = 55
    ASYNC = 56
    TYPE_IGNORE = 57
    TYPE_COMMENT = 58
    # These aren't used by the C tokenizer but are needed for tokenize.py
    ERRORTOKEN = 59
    COMMENT = 60
    NL = 61
    ENCODING = 62
    N_TOKENS = 63
    # Special definitions for cooperation with parser
    NT_OFFSET = 256

    tok_name = {value: name
                for name, value in globals().items()
                if isinstance(value, int) and not name.startswith('_')}
    __all__.extend(tok_name.values())

    EXACT_TOKEN_TYPES = {
        '!=': NOTEQUAL,
        '%': PERCENT,
        '%=': PERCENTEQUAL,
        '&': AMPER,
        '&=': AMPEREQUAL,
        '(': LPAR,
        ')': RPAR,
        '*': STAR,
        '**': DOUBLESTAR,
        '**=': DOUBLESTAREQUAL,
        '*=': STAREQUAL,
        '+': PLUS,
        '+=': PLUSEQUAL,
        ',': COMMA,
        '-': MINUS,
        '-=': MINEQUAL,
        '->': RARROW,
        '.': DOT,
        '...': ELLIPSIS,
        '/': SLASH,
        '//': DOUBLESLASH,
        '//=': DOUBLESLASHEQUAL,
        '/=': SLASHEQUAL,
        ':': COLON,
        ':=': COLONEQUAL,
        ';': SEMI,
        '<': LESS,
        '<<': LEFTSHIFT,
        '<<=': LEFTSHIFTEQUAL,
        '<=': LESSEQUAL,
        '=': EQUAL,
        '==': EQEQUAL,
        '>': GREATER,
        '>=': GREATEREQUAL,
        '>>': RIGHTSHIFT,
        '>>=': RIGHTSHIFTEQUAL,
        '@': AT,
        '@=': ATEQUAL,
        '[': LSQB,
        ']': RSQB,
        '^': CIRCUMFLEX,
        '^=': CIRCUMFLEXEQUAL,
        '{': LBRACE,
        '|': VBAR,
        '|=': VBAREQUAL,
        '}': RBRACE,
        '~': TILDE,
    }

    def ISTERMINAL(x):
        return x < NT_OFFSET

    def ISNONTERMINAL(x):
        return x >= NT_OFFSET

    def ISEOF(x):
        return x == ENDMARKER


def jtypes():
    """
    Define names for built-in types that aren't directly accessible as a builtin.
    """
    import sys

    # Iterators in Python aren't a matter of type but of protocol.  A large
    # and changing number of builtin types implement *some* flavor of
    # iterator.  Don't check the type!  Use hasattr to check for both
    # "__iter__" and "__next__" attributes instead.

    def _f():
        pass

    FunctionType = type(_f)
    LambdaType = type(lambda: None)  # Same as FunctionType
    CodeType = type(_f.__code__)
    MappingProxyType = type(type.__dict__)
    SimpleNamespace = type(sys.implementation)

    def _cell_factory():
        a = 1

        def f():
            nonlocal a

        return f.__closure__[0]

    CellType = type(_cell_factory())

    def _g():
        yield 1

    GeneratorType = type(_g())

    async def _c():
        pass

    _c = _c()
    CoroutineType = type(_c)
    _c.close()  # Prevent ResourceWarning

    async def _ag():
        yield

    _ag = _ag()
    AsyncGeneratorType = type(_ag)

    class _C:
        def _m(self): pass

    MethodType = type(_C()._m)

    BuiltinFunctionType = type(len)
    BuiltinMethodType = type([].append)  # Same as BuiltinFunctionType

    WrapperDescriptorType = type(object.__init__)
    MethodWrapperType = type(object().__str__)
    MethodDescriptorType = type(str.join)
    ClassMethodDescriptorType = type(dict.__dict__['fromkeys'])

    ModuleType = type(sys)

    try:
        raise TypeError
    except TypeError:
        tb = sys.exc_info()[2]
        TracebackType = type(tb)
        FrameType = type(tb.tb_frame)
        tb = None;
        del tb

    # For Jython, the following two types are identical
    GetSetDescriptorType = type(FunctionType.__code__)
    MemberDescriptorType = type(FunctionType.__globals__)

    del sys, _f, _g, _C, _c, _ag  # Not for export

    # Provide a PEP 3115 compliant mechanism for class creation
    def new_class(name, bases=(), kwds=None, exec_body=None):
        """Create a class object dynamically using the appropriate metaclass."""
        resolved_bases = resolve_bases(bases)
        meta, ns, kwds = prepare_class(name, resolved_bases, kwds)
        if exec_body is not None:
            exec_body(ns)
        if resolved_bases is not bases:
            ns['__orig_bases__'] = bases
        return meta(name, resolved_bases, ns, **kwds)

    def resolve_bases(bases):
        """Resolve MRO entries dynamically as specified by PEP 560."""
        new_bases = list(bases)
        updated = False
        shift = 0
        for i, base in enumerate(bases):
            if isinstance(base, type):
                continue
            if not hasattr(base, "__mro_entries__"):
                continue
            new_base = base.__mro_entries__(bases)
            updated = True
            if not isinstance(new_base, tuple):
                raise TypeError("__mro_entries__ must return a tuple")
            else:
                new_bases[i + shift:i + shift + 1] = new_base
                shift += len(new_base) - 1
        if not updated:
            return bases
        return tuple(new_bases)

    def prepare_class(name, bases=(), kwds=None):
        """Call the __prepare__ method of the appropriate metaclass.

        Returns (metaclass, namespace, kwds) as a 3-tuple

        *metaclass* is the appropriate metaclass
        *namespace* is the prepared class namespace
        *kwds* is an updated copy of the passed in kwds argument with any
        'metaclass' entry removed. If no kwds argument is passed in, this will
        be an empty dict.
        """
        if kwds is None:
            kwds = {}
        else:
            kwds = dict(kwds)  # Don't alter the provided mapping
        if 'metaclass' in kwds:
            meta = kwds.pop('metaclass')
        else:
            if bases:
                meta = type(bases[0])
            else:
                meta = type
        if isinstance(meta, type):
            # when meta is a type, we first determine the most-derived metaclass
            # instead of invoking the initial candidate directly
            meta = _calculate_meta(meta, bases)
        if hasattr(meta, '__prepare__'):
            ns = meta.__prepare__(name, bases, **kwds)
        else:
            ns = {}
        return meta, ns, kwds

    def _calculate_meta(meta, bases):
        """Calculate the most derived metaclass."""
        winner = meta
        for base in bases:
            base_meta = type(base)
            if issubclass(winner, base_meta):
                continue
            if issubclass(base_meta, winner):
                winner = base_meta
                continue
            # else:
            raise TypeError("metaclass conflict: "
                            "the metaclass of a derived class "
                            "must be a (non-strict) subclass "
                            "of the metaclasses of all its bases")
        return winner

    class DynamicClassAttribute:
        """Route attribute access on a class to __getattr__.

        This is a descriptor, used to define attributes that act differently when
        accessed through an instance and through a class.  Instance access remains
        normal, but access to an attribute through a class will be routed to the
        class's __getattr__ method; this is done by raising AttributeError.

        This allows one to have properties active on an instance, and have virtual
        attributes on the class with the same name (see Enum for an example).

        """

        def __init__(self, fget=None, fset=None, fdel=None, doc=None):
            self.fget = fget
            self.fset = fset
            self.fdel = fdel
            # next two lines make DynamicClassAttribute act the same as property
            self.__doc__ = doc or fget.__doc__
            self.overwrite_doc = doc is None
            # support for abstract methods
            self.__isabstractmethod__ = bool(getattr(fget, '__isabstractmethod__', False))

        def __get__(self, instance, ownerclass=None):
            if instance is None:
                if self.__isabstractmethod__:
                    return self
                raise AttributeError()
            elif self.fget is None:
                raise AttributeError("unreadable attribute")
            return self.fget(instance)

        def __set__(self, instance, value):
            if self.fset is None:
                raise AttributeError("can't set attribute")
            self.fset(instance, value)

        def __delete__(self, instance):
            if self.fdel is None:
                raise AttributeError("can't delete attribute")
            self.fdel(instance)

        def getter(self, fget):
            fdoc = fget.__doc__ if self.overwrite_doc else None
            result = type(self)(fget, self.fset, self.fdel, fdoc or self.__doc__)
            result.overwrite_doc = self.overwrite_doc
            return result

        def setter(self, fset):
            result = type(self)(self.fget, fset, self.fdel, self.__doc__)
            result.overwrite_doc = self.overwrite_doc
            return result

        def deleter(self, fdel):
            result = type(self)(self.fget, self.fset, fdel, self.__doc__)
            result.overwrite_doc = self.overwrite_doc
            return result

    class _GeneratorWrapper:
        # TODO: Implement this in C.
        def __init__(self, gen):
            self.__wrapped = gen
            self.__isgen = gen.__class__ is GeneratorType
            self.__name__ = getattr(gen, '__name__', None)
            self.__qualname__ = getattr(gen, '__qualname__', None)

        def send(self, val):
            return self.__wrapped.send(val)

        def throw(self, tp, *rest):
            return self.__wrapped.throw(tp, *rest)

        def close(self):
            return self.__wrapped.close()

        @property
        def gi_code(self):
            return self.__wrapped.gi_code

        @property
        def gi_frame(self):
            return self.__wrapped.gi_frame

        @property
        def gi_running(self):
            return self.__wrapped.gi_running

        @property
        def gi_yieldfrom(self):
            return self.__wrapped.gi_yieldfrom

        cr_code = gi_code
        cr_frame = gi_frame
        cr_running = gi_running
        cr_await = gi_yieldfrom

        def __next__(self):
            return next(self.__wrapped)

        def __iter__(self):
            if self.__isgen:
                return self.__wrapped
            return self

        __await__ = __iter__

    def coroutine(func):
        """Convert regular generator function to a coroutine."""

        if not callable(func):
            raise TypeError('types.coroutine() expects a callable')

        if (func.__class__ is FunctionType and
                getattr(func, '__code__', None).__class__ is CodeType):

            co_flags = func.__code__.co_flags

            # Check if 'func' is a coroutine function.
            # (0x180 == CO_COROUTINE | CO_ITERABLE_COROUTINE)
            if co_flags & 0x180:
                return func

            # Check if 'func' is a generator function.
            # (0x20 == CO_GENERATOR)
            if co_flags & 0x20:
                # TODO: Implement this in C.
                co = func.__code__
                # 0x100 == CO_ITERABLE_COROUTINE
                func.__code__ = co.replace(co_flags=co.co_flags | 0x100)
                return func

        # The following code is primarily to support functions that
        # return generator-like objects (for instance generators
        # compiled with Cython).

        # Delay functools and _collections_abc import for speeding up types import.
        import functools
        import _collections_abc
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            coro = func(*args, **kwargs)
            if (coro.__class__ is CoroutineType or
                    coro.__class__ is GeneratorType and coro.gi_code.co_flags & 0x100):
                # 'coro' is a native coroutine object or an iterable coroutine
                return coro
            if (isinstance(coro, _collections_abc.Generator) and
                    not isinstance(coro, _collections_abc.Coroutine)):
                # 'coro' is either a pure Python generator iterator, or it
                # implements collections.abc.Generator (and does not implement
                # collections.abc.Coroutine).
                return _GeneratorWrapper(coro)
            # 'coro' is either an instance of collections.abc.Coroutine or
            # some other object -- pass it through.
            return coro

        return wrapped

    __all__ = [n for n in globals() if n[:1] != '_']


class Runner(object):
    def __init__(self, method, file=".py"):
        self.name = "Runer"
        print("starting..")
        sleep(12)
        print(f"id : {id(method)}")
        try:
            method()

        except Exception as err:
            print(err)

        print("code finished")


def forloop(number):
    for i in number:
        print(i)


def Append(name, add):
    name.append(add)


def Remove(name, R):
    name.remove(R)


def sort(listname):
    
    listname.sort()


def listitems(parameter_list):
    list = [parameter_list]

    print(list)


def abort():
    print(os.abort())


                
print("")


