#!/usr/bin/python3
"""Prepare current web static files, compress and deploy them"""
from datetime import datetime
from fabric.operations import local, run, put
from fabric.api import *
import os


env.hosts = ['107.22.142.160', '100.25.22.111']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


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


def do_deploy(archive_path):
    """Deploy Current version to all my servers"""
    if not os.path.exists(archive_path):
        return False

    arch_name = archive_path.split('/')[-1]
    arch_name_no_exten = arch_name.split('.')[0]
    try:
        put(archive_path, '/tmp/')
        run('mkdir -p /data/web_static/releases/{}'.format(arch_name_no_exten))
        run('tar -zxf /tmp/{} -C /data/web_static/releases/{}/'
            .format(arch_name, arch_name_no_exten))
        run('rm /tmp/{}'.format(arch_name))
        run('mv /data/web_static/releases/{}/web_static/* \
        /data/web_static/releases/{}/'.format(arch_name_no_exten,
                                              arch_name_no_exten))
        run('rm -rf /data/web_static/releases/{}/web_static'
            .format(arch_name_no_exten))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
            .format(arch_name_no_exten))
    except Exception as e:
        return False
    print("New version deployed!")
    return True


def deploy():
    """pack new version and deploy"""
    file_path = do_pack()
    if not file_path:
        return False
    return do_deploy(file_path)

def do_clean(number=0):
    """Remove archive files and keep most recent"""
    arch_list = sorted(os.listdir('versions'))
    number = int(number)
    if len(arch_list) == number:
        return
    if number == 0:
        arch_list.pop()
    while (number > 0):
        arch_list.pop()
        number -= 1
    for fl in arch_list:
        os.remove("versions/{}".format(fl))
