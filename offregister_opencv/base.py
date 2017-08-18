from fabric.api import run
from fabric.context_managers import shell_env, cd
from fabric.operations import sudo
from offregister_fab_utils.apt import apt_depends
from offregister_fab_utils.fs import cmd_avail
from offregister_fab_utils.git import clone_or_update


def dl_install_opencv(branch='2.4', extra_cmake_args=''):
    apt_depends('build-essential', 'cmake', 'git', 'libgtk2.0-dev', 'pkg-config', 'libavcodec-dev',
                'libavformat-dev', 'libswscale-dev', 'python-dev', 'python-numpy', 'libtbb2',
                'libtbb-dev', 'libjpeg-dev', 'libpng-dev', 'libtiff-dev', 'libjasper-dev', 'libdc1394-22-dev')
    with cd('$HOME/repos'):
        clone_or_update(repo='opencv', team='opencv', branch=branch, skip_reset=True)
        run('mkdir -p opencv-build')
        with cd('opencv-build'):
            run('cmake -D CMAKE_BUILD_TYPE=RELEASE '
                '-D CMAKE_INSTALL_PREFIX=/usr/local {} ../opencv'.format(extra_cmake_args))
            run('make')
            sudo('make install')
