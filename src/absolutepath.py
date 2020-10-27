from pathlib import Path
import os.path


def absolutepath(filepath):
    scriptpath = os.path.dirname(__file__)
    filename = os.path.join(scriptpath, filepath)
    return filename
    # relative = Path(filepath)
    # return relative.absolute()