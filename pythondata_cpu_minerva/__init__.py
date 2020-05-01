import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "sources")
src = "http://github.com/lambdaconcept/minerva"

# Module version
version_str = "0.0.post135"
version_tuple = (0, 0, 135)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post135")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post84"
data_version_tuple = (0, 0, 84)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post84")
except ImportError:
    pass
data_git_hash = "d06b5d2fd354cad3040f0efaf58b2f206395b7d0"
data_git_describe = "v0.0-84-gd06b5d2"
data_git_msg = """\
commit d06b5d2fd354cad3040f0efaf58b2f206395b7d0
Author: Jean-François Nguyen <jf@lambdaconcept.com>
Date:   Wed Apr 1 23:55:41 2020 +0200

    Revert "Use nmigen_soc.wishbone.Interface."
    
    This reverts commit 8c4d4eb3f74786bc44a721a9c9ce28cf37ee8cf4.
    
    The PyPI release of nmigen-soc doesn't allow nmigen versions above 0.1.
    We will wait for a new release before merging 8c4d4eb3f.

"""

# Tool version info
tool_version_str = "0.0.post51"
tool_version_tuple = (0, 0, 51)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post51")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_minerva."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_minerva".format(f))
    return fn
