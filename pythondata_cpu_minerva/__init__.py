import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "sources")
src = "https://github.com/lambdaconcept/minerva"

# Module version
version_str = "0.0.post164"
version_tuple = (0, 0, 164)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post164")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post98"
data_version_tuple = (0, 0, 98)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post98")
except ImportError:
    pass
data_git_hash = "536d6c3ac175cd946777f3dd5b64339552f0130a"
data_git_describe = "v0.0-98-g536d6c3"
data_git_msg = """\
commit 536d6c3ac175cd946777f3dd5b64339552f0130a
Author: Jean-François Nguyen <jf@lambdaconcept.com>
Date:   Wed Sep 9 14:29:00 2020 +0200

    Update README.

"""

# Tool version info
tool_version_str = "0.0.post66"
tool_version_tuple = (0, 0, 66)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post66")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_minerva."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_minerva".format(f))
    return fn
