import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "sources")
src = "https://github.com/lambdaconcept/minerva"

# Module version
version_str = "0.0.post171"
version_tuple = (0, 0, 171)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post171")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post99"
data_version_tuple = (0, 0, 99)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post99")
except ImportError:
    pass
data_git_hash = "0b5f6b2466367f262f9a16a83f9c86fc7f008edf"
data_git_describe = "v0.0-99-g0b5f6b2"
data_git_msg = """\
commit 0b5f6b2466367f262f9a16a83f9c86fc7f008edf
Author: Jean-François Nguyen <jf@lambdaconcept.com>
Date:   Fri Jan 22 15:20:35 2021 +0100

    fetch: workaround YosysHQ/yosys#2035.

"""

# Tool version info
tool_version_str = "0.0.post72"
tool_version_tuple = (0, 0, 72)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post72")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_minerva."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_minerva".format(f))
    return fn
