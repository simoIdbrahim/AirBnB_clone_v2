#!/usr/bin/python3
""" script (based on the file 1-pack_web_static.py) that distributes an
archive to your web servers, using the function do_deploy """
from datetime import datetime
from os import path, mkdir
from fabric.api import local, put, run, env

env.hosts = ['3.85.196.229', '34.207.221.84']


def do_pack():
    """ do_pack function """
    date = datetime.now().strftime("%Y%m%d%H%M%S")

    file = "versions/web_static_{}.tgz".format(date)

    if not path.exists("versions"):
        mkdir("versions")

    local("tar -cvzf {} web_static".format(file))

    if path.exists(file):
        return file
    else:
        return None


def do_deploy(archive_path):
    """ do_deploy function """
    if not path.exists(archive_path):
        return False

    try:
        put(archive_path, "/tmp/")
        file_name = archive_path.split("/")[-1]
        name = file_name.split('.')[0]
        dir_release = "/data/web_static/releases/{}".format(name)
        run("mkdir -p {}".format(dir_release))
        run("tar -xzf /tmp/{} -C {}".format(file_name, dir_release))
        run("rm /tmp/{}".format(file_name))
        run('mv {0}/web_static/* {0}/'.format(dir_release))
        run('rm -rf {}/web_static'.format(dir_release))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(dir_release))
        print("New version deployed!")
        return True
    except Exception:
        print("No new version deployed!")
        return False
