#!/usr/bin/python3
""" script (based on the file 1-pack_web_static.py) that distributes
an archive to your web servers, using the function do_deploy """
from os.path import exists, splitext
from fabric.api import *

env.hosts = ['54.87.180.223', '52.23.245.155']


@task
def do_deploy(archive_path):
    """ func deply archive"""

    if not exists(archive_path):
        return False

    arch_name = archive_path.split('/')[1]
    file_name = splitext(arch_name)[0]
    tmp_path = "/tmp/{}".format(arch_name)
    data_path = "/data/web_static/releases/{}".format(file_name)

    put(archive_path, '/tmp/')
    run('mkdir -p {}'.format(data_path))
    run('tar -xzf {}  -C {}'.format(tmp_path, data_path))
    run('rm {}'.format(tmp_path))
    run('mv {}/web_static/* {}/'.format(data_path, data_path))
    run('rm -rf {}/web_static'.format(data_path))
    run('rm -rf /data/web_static/current')
    run('ln -s {} /data/web_static/current'.format(data_path))
    print("New version deployed!")
    return True
