import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "sources")
src = "https://github.com/lambdaconcept/minerva"

# Module version
version_str = "0.0.post233"
version_tuple = (0, 0, 233)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post233")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post112"
data_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post112")
except ImportError:
    pass
data_git_hash = "3cb469f8fe451838ee2105842d8d4695a64d234c"
data_git_describe = "v0.0-112-g3cb469f"
data_git_msg = """\
commit 3cb469f8fe451838ee2105842d8d4695a64d234c
Author: Catherine <whitequark@whitequark.org>
Date:   Sun Dec 12 15:39:03 2021 +0000

    nMigen has been renamed to Amaranth HDL.

"""

# Tool version info
tool_version_str = "0.0.post121"
tool_version_tuple = (0, 0, 121)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post121")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_minerva."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_minerva".format(f))
    return fn
