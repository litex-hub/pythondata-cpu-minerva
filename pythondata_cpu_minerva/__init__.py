import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "sources")
src = "https://github.com/minerva-cpu/minerva"

# Module version
version_str = "0.0.post294"
version_tuple = (0, 0, 294)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post294")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post139"
data_version_tuple = (0, 0, 139)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post139")
except ImportError:
    pass
data_git_hash = "d393a7b4367d2d2c1c5d26be03039cdee45010c0"
data_git_describe = "v0.0-139-gd393a7b"
data_git_msg = """\
commit d393a7b4367d2d2c1c5d26be03039cdee45010c0
Author: Jean-François Nguyen <jf@jfng.fr>
Date:   Wed Feb 19 19:28:12 2025 +0100

    gpr: remove unused d_{rp1,rp2}_en ports.

"""

# Tool version info
tool_version_str = "0.0.post155"
tool_version_tuple = (0, 0, 155)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post155")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_minerva."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_minerva".format(f))
    return fn
