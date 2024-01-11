#!/usr/bin/python3
""" cript (based on the file 2-do_deploy_web_static.py) that creates and
distributes an archive to your web servers, using the function deploy """
from datetime import datetime
from fabric.api import *
from os.path import exists, splitext

env.hosts = ['54.87.180.223', '52.23.245.155', 'localhost']


@task
def do_pack():
    """Function that archive web_static folder """
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    mkdir = "mkdir -p versions"
    path = "versions/web_static_{}.tgz".format(date)
    print("Packing web_static to {}".format(path))
    if local('{} && tar -cvzf {} web_static'.format(mkdir, path)).succeeded:
        return path
        print("web_static packed: {} -> {}Bytes".format(path, size))
    return None


@task
def do_deploy(archive_path):
    """ func deply archive """

    if not exists(archive_path):
        return False

    arch = archive_path.split('/')[1]
    file = splitext(arch)[0]
    tmp = "/tmp/{}".format(arch)
    data = "/data/web_static/releases/{}".format(file)

    put(archive_path, '/tmp/')
    run('mkdir -p {}'.format(data))
    run('tar -xzf {}  -C {}'.format(tmp, data))
    run('rm {}'.format(tmp))
    run('mv {}/web_static/* {}/'.format(data, data))
    run('rm -rf {}/web_static'.format(data))
    run('rm -rf /data/web_static/current')
    run('ln -s {} /data/web_static/current'.format(data))
    print("New version deployed!")
    return True


@task
def deploy():
    """ func that creates web servers """
    path = do_pack()
    if path is None:
        return False
    return do_deploy(path)
