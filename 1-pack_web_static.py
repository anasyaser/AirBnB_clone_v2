#!/usr/bin/python3
"""Prepare current web static files and compress them"""
from datetime import datetime
from fabric.operations import local


def do_pack():
    """Compress files on local machine"""
    local("mkdir -p versions")
    archive_name = "web_static_{}.tgz"\
        .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S"))
    result = local("tar -cvzf versions/{} web_static".format(archive_name),
                   capture=True)
    if result.failed:
        return
    return "versions/{}".format(archive_name)
