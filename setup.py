#!/usr/bin/env python

from setuptools import setup

setup(name='BnW',
    version='0.1',
    description='Microblogging service',
    author='Stiletto',
    author_email='blasux@blasux.ru',
    url='http://github.com/stiletto/bnw',
    packages=['bnw', 'bnw.core', 'bnw.formatting', 'bnw.handlers', 'bnw.scripts', 'bnw.search', 'bnw.web', 'bnw.xmpp'],
    dependency_links=['http://github.com/mongodb/motor/tarball/0.6.2#egg=motor-0.6.2',
                      'http://github.com/mongodb/mongo-python-driver/tarball/master#egg=pymongo',
                      'http://github.com/stiletto/linkshit/tarball/master#egg=linkshit'],

    install_requires=['tornado==4.3', 'twisted==16.2.0', 'Pillow', 'PyRSS2Gen', 'python-dateutil', 'misaka<2.0.0', 'motor', 'linkshit', 'libthumbor'],
    package_data={'bnw.web': ['templates/*.html','static/*.*', 'static/flot/*', 'static/web-socket-js/*']},
    entry_points = {
        'console_scripts': [
            'bnw = bnw.scripts.entry:instance',
            'bnw-search = bnw.scripts.entry:search',
            'bnw-admin = bnw.scripts.admin:main',
        ],
    }
)
