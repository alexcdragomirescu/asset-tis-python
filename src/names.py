import logging
logger = logging.getLogger(__name__)

import os

def breakdown(pathname):
    path_prefix = os.path.dirname(os.path.abspath(pathname))
    basename = os.path.basename(pathname)
    filename = os.path.splitext(basename)[0]
    extension = os.path.splitext(basename)[1]
    return path_prefix, basename, filename, extension
    