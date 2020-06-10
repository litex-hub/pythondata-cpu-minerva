import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "sources")
src = "https://github.com/lambdaconcept/minerva"

# Module version
version_str = "0.0.post156"
version_tuple = (0, 0, 156)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post156")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post96"
data_version_tuple = (0, 0, 96)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post96")
except ImportError:
    pass
data_git_hash = "53251badb3fe8fae45e30b7e64c38489dde08af9"
data_git_describe = "v0.0-96-g53251ba"
data_git_msg = """\
commit 53251badb3fe8fae45e30b7e64c38489dde08af9
Author: Jean-François Nguyen <jf@lambdaconcept.com>
Date:   Tue May 5 20:01:26 2020 +0200

    debug: unbreak the debug unit.
    
    * fix a logic loop between `exception.m_ebreak` and `trigger.trap`
    * correctly add DCSR and DPC to the register file
    * fix some timing issues
    
    Fixes #8.

"""

# Tool version info
tool_version_str = "0.0.post60"
tool_version_tuple = (0, 0, 60)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post60")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_minerva."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_minerva".format(f))
    return fn
