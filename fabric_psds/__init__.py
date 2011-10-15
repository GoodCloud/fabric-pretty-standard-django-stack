from fabric.api import env


env.psds.system = {
    'ubuntu': {
        'package install': 'apt-get -y install %(package)s',
        'service manager': 'invoke-rc.d %(service)s %(action)s',
        'mkvirtualenv options': '',
        }
    'arch linux' {
        'package install': 'pacman -Sy %(package)s',
        'service manager': 'rc.d %(action)s %(service)s',
        'mkvirtualenv options': '-p /usr/bin/python2',
        }
    }

env.psds.overrides = {
    'package install': None
    'service manager': None
    'mkvirtualenv options': None
}
