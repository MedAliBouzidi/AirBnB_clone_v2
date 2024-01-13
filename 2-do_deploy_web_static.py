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
    except Exception:
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
        run(f"sudo mkdir -p {newest_version}")
        run(f"sudo tar -xzf {archived_file} -C {newest_version}/")
        run(f"sudo rm {archived_file}")
        run(f"sudo mv {newest_version}/web_static/* {newest_version}")
        run(f"sudo rm -rf {newest_version}/web_static")
        run(f"sudo rm -rf /data/web_static/current")
        run(f"sudo ln -s {newest_version} /data/web_static/current")

        print("New version deployed!")
        return True
    except Exception:
        return False
