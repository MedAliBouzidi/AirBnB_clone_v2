#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
"""

import time
from fabric.api import *
import os

env.hosts = ["100.24.236.248", "100.26.151.181"]


@runs_once
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


@task
def do_deploy(archive_path):
    """
        Distribute archive.
    """
    if not os.path.exists(archive_path):
        return False

    try:
        archived_file = archive_path[9:]
        newest_version = "/data/web_static/releases/" + archived_file[:-4]
        archived_file = "/tmp/" + archived_file
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(newest_version))
        run("sudo tar -xzf {} -C {}/".format(archived_file, newest_version))
        run("sudo rm {}".format(archived_file))
        run("sudo mv {}/web_static/* {}".format(newest_version, newest_version))
        run("sudo rm -rf {}/web_static".format(newest_version))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(newest_version))

        print("New version deployed!")
        return True
    
    except Exception:
        return False
