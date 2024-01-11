#!/usr/bin/python3
"""Generates a .tgz archive from the contents of the web_static folder."""
from fabric.api import local
import time


def do_pack():
    """Generate an tgz archive from web_static folder"""
    try:
        time_str = time.strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/"
              .format(time_str))
        return ("versions/web_static_{}.tgz".format(time_str))
    except Except:
        return None
