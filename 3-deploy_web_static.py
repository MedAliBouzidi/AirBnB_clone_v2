#!/usr/bin/python3
"""Create and distributes an archive to web servers"""
import os.path
import time
from fabric.api import local, runs_once, task
from fabric.operations import env, put, run


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
    """Distribute an archive to web servers"""
    if (os.path.isfile(archive_path) is False):
        return False

    try:
        file = archive_path.split("/")[-1]
        folder = ("/data/web_static/releases/" + file.split(".")[0])
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(folder))
        run("tar -xzf /tmp/{} -C {}".format(file, folder))
        run("rm /tmp/{}".format(file))
        run("mv {}/web_static/* {}/".format(folder, folder))
        run("rm -rf {}/web_static".format(folder))
        run('rm -rf /data/web_static/current')
        run("ln -s {} /data/web_static/current".format(folder))
        print("Deployment done")
        return True
    except Exception:
        return False


@task
def deploy():
    """Create and distributes an archive to web servers"""
    try:
        path = do_pack()
        return do_deploy(path)
    except Exception:
        return False
