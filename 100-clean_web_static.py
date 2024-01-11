#!/usr/bin/python3
""" script (based on the file 3-deploy_web_static.py) that deletes
out-of-date archives, using the function do_clean """

from fabric.api import *
import os

env.hosts = ['54.87.180.223', '52.23.245.155']


def do_clean(number=0):
    """ deletes archives date """

    number = int(number)

    if number == 0 or number == 1:
        number = 2

    archives = sorted(os.listdir("versions"))

    for i in range(0, number):
        archives.pop()

    with lcd("versions"):
        for archive in archives:
            local("rm -rf {}".format(archive))

    with cd("/data/web_static/releases"):
        for archive in archives:
            run("rm -rf {}".format(archive))

    return True
