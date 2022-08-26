from offregister_fab_utils.apt import apt_depends
from offregister_fab_utils.git import clone_or_update


def dl_install_opencv(branch="master", tag="4.1.1", extra_cmake_args=""):
    distro = c.run("lsb_release -cs", hide=True)
    if (
        c.run(
            "grep '^[[:blank:]]*[^[:blank:]#;]' /etc/apt/sources.list | grep -qF '-security main'",
            warn=True,
        ).exited
        != 0
    ):
        c.sudo(
            'add-apt-repository -y "deb http://security.ubuntu.com/ubuntu {distro}-security main"'.format(
                distro=distro
            )
        )
        c.sudo("apt update")
    apt_depends(
        c,
        "build-essential",
        "checkinstall",
        "cmake",
        "pkg-config",
        "yasm",
        "git",
        "gfortran",
        "libjpeg8-dev",
        "libpng-dev",
        "software-properties-common",
        "libtiff-dev",
        "libavcodec-dev",
        "libavformat-dev",
        "libswscale-dev",
        "libdc1394-22-dev",
        "libxine2-dev",
        "libv4l-dev",
        "libgstreamer1.0-dev",
        "libgstreamer-plugins-base1.0-dev",
        "libgtk2.0-dev",
        "libtbb-dev",
        "qt5-default",
        "libatlas-base-dev",
        "libfaac-dev",
        "libmp3lame-dev",
        "libtheora-dev",
        "libvorbis-dev",
        "libxvidcore-dev",
        "libopencore-amrnb-dev",
        "libopencore-amrwb-dev",
        "libavresample-dev",
        "x264",
        "v4l-utils",
        "libprotobuf-dev",
        "protobuf-compiler",
        "libgoogle-glog-dev",
        "libgflags-dev",
        "libgphoto2-dev",
        "libeigen3-dev",
        "libhdf5-dev",
        "doxygen",
        "python3-dev",
        "python3-pip",
        "python3-numpy",
        "python3-testresources",
        "libeigen3-dev",
        # Hmm:
        "libopencv-dev",
        "opencv-data",
    )
    c.run("mkdir -p '$HOME/repos'", shell_escape=False)
    with c.cd("$HOME/repos"):
        clone_or_update(
            repo="opencv", team="opencv", branch=branch, tag=tag, skip_reset=True
        )
        c.run("mkdir -p opencv-build")
        with c.cd("opencv-build"):
            c.run(
                "cmake -D CMAKE_BUILD_TYPE=RELEASE "
                "-D CMAKE_INSTALL_PREFIX=/usr/local {} ../opencv".format(
                    extra_cmake_args
                )
            )
            c.run("make")
            c.sudo("make install")
