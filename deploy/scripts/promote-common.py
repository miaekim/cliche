#!/usr/bin/python3
import errno
import pathlib
import platform
import sys
import subprocess


def main():
    dist = platform.dist()
    if dist[0] != 'debian' and dist[0] != 'Ubuntu':
        print('This script can only be run on Debian GNU/Linux or Ubuntu.')
        sys.exit(errno.EPERM)

    workdir = pathlib.Path(__file__).resolve().parent.parent
    with (workdir / 'etc' / 'revision.txt').open('r') as revision_file:
        revision = (revision_file.readline().strip())
    venv_dir = pathlib.Path('/home/cliche/venv_{}'.format(revision)).resolve()

    subprocess.check_call(
        [
            'sudo',
            '-ucliche',
            'rm',
            '-f',
            '/home/cliche/etc/prod.cfg.yml',
        ]
    )

    subprocess.check_call(
        [
            'sudo',
            '-ucliche',
            'ln',
            '-fs',
            str(venv_dir / 'etc' / 'prod.cfg.yml'),
            '/home/cliche/etc/prod.cfg.yml',
        ]
    )


if __name__ == '__main__':
    main()
