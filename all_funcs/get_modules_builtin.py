# %%
#######################################
def get_modules_builtin():
    """Returns a tuple of the built-in module names.

    Example:
        >>> get_modules_builtin()\n
        ('_abc', '_ast', '_bisect', '_blake2', '_codecs', '_collections', '_csv', '_datetime', '_elementtree', '_functools', '_heapq', '_imp', '_io', '_locale', '_md5', '_operator', '_pickle', '_posixsubprocess', '_random', '_sha1', '_sha256', '_sha3', '_sha512', '_signal', '_socket', '_sre', '_stat', '_statistics', '_string', '_struct', '_symtable', '_thread', '_tracemalloc', '_warnings', '_weakref', 'array', 'atexit', 'binascii', 'builtins', 'cmath', 'errno', 'faulthandler', 'fcntl', 'gc', 'grp', 'itertools', 'marshal', 'math', 'posix', 'pwd', 'pyexpat', 'select', 'spwd', 'sys', 'syslog', 'time', 'unicodedata', 'xxsubtype', 'zlib')
        
    References:
        https://stackoverflow.com/questions/8370206/how-to-get-a-list-of-built-in-modules-in-python

    Returns:
        tuple: Returns a tuple
    """
    import sys
    return sys.builtin_module_names

