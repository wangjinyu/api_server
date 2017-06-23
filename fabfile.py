# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from fabric.api import *

env.user = 'root'
env.password = 'WJYwjy14'
env.host_string = '47.93.28.55'
env.port = '22'
TAR_FILE_NAME = 'api_server.tar.gz'

@task
def pack():
    tar_files = ['api_server/*', 'static/*'];
    exclude_files = ['db.sqlite3', 'api_server/__pycache__', 'conf/*', 'manager.py', 'fabfile.py', 'media/*', '__pycache__', '.DS_Store', '*/.DS_Store', '*.tar.gz']
    exclude_files = ['--exclude=\'%s\'' % t for t in exclude_files]
    print('删除上次打包的文件')
    local('rm -f %s' % TAR_FILE_NAME)
    print('正在打包本地工程文件...')
    local('tar -czvf %s %s %s' % (TAR_FILE_NAME, ' '.join(exclude_files), ' '.join(tar_files)))
    print('在当前目录创建一个打包文件: %s' % TAR_FILE_NAME)

@task
def deploy() :
    pack()

    # 远程服务器临时文件
    remote_tmp_tar = '/tmp/%s' % TAR_FILE_NAME

    # 删除远程服务器的压缩文件
    run('rm -rf %s' % remote_tmp_tar)

    # 把本地工程文件上传至服务器, local_path, remote_path.
    print('上传本地压缩包到服务器')
    put(TAR_FILE_NAME, remote_tmp_tar)
    print('上传本地压缩包到服务器完成')
    print('进入到服务器 tmp 目录')
    with cd('/tmp'):
        print('解压文件 %s' % TAR_FILE_NAME)
        run('tar -xzvf %s' % TAR_FILE_NAME)
        with cd('/usr/python_projects/api_server'):
            print('拷贝工程文件...')
            run('mv -bf /tmp/api_server/ /usr/python_projects/api_server/')

            print('拷贝static文件...')
            run('mv -bf /tmp/static /usr/python_projects/api_server/')

            print('部署完成')

            print('清理临时压缩文件')
            run('rm -rf %s' % remote_tmp_tar)

            print('清理临时工程文件')
            run('rm -rf /tmp/api_server')
            run('rm -rf api_server~')

            print('清理临时static文件')
            run('rm -rf /tmp/static')
            run('rm -rf static~')

            print('清理本地压缩文件')
            local('rm -rf %s' % TAR_FILE_NAME)

@task
def sqlite() :
    put("db.sqlite3", '/usr/python_projects/api_server/db.sqlite3')

