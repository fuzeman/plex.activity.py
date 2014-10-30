from plex_activity import __version__

from setuptools import setup

setup(
    name='plex.activity.py',
    version=__version__,
    license='MIT',
    url='https://github.com/fuzeman/plex.activity.py',

    author='Dean Gardiner',
    author_email='me@dgardiner.net',

    description='Real-time activity extension for plex.py',
    packages=['plex_activity'],
    platforms='any',

    install_requires=[
        'plex.py',
        'plex.metadata.py',

        'asio'
        'pyemitter'
        'websocket-client'
    ],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ]
)
