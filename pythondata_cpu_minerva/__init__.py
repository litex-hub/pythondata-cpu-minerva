import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "sources")
src = "https://github.com/lambdaconcept/minerva"

# Module version
version_str = "0.0.post223"
version_tuple = (0, 0, 223)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post223")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post111"
data_version_tuple = (0, 0, 111)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post111")
except ImportError:
    pass
data_git_hash = "6e800e7b0add6faa13677857e2d3e2ef57aed4dc"
data_git_describe = "v0.0-111-g6e800e7"
data_git_msg = """\
commit 6e800e7b0add6faa13677857e2d3e2ef57aed4dc
Author: Jean-François Nguyen <jf@lambdaconcept.com>
Date:   Tue Jun 22 14:41:43 2021 +0200

    Factor out the gpr.File implementation as a ForwardingMemory.
    
    The L1 cache also needs it.

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_minerva."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_minerva".format(f))
    return fn
