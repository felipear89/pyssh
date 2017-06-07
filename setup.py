"""The setup.py file for Save Your Time SSH."""

from setuptools import setup
from pip.req import parse_requirements

REQUIREMENTS = parse_requirements('requirements.txt', session='hack')
INSTALL_REQUIRES = [str(ir.req) for ir in REQUIREMENTS]

setup(
    name='sytssh',
    version='0.0.5',
    description='A ssh helper to save your time',
    long_description='''
        Utility to manage your hosts and environments that you often need to connect
    ''',
    author='Felipe Alexandre Rodrigues',
    author_email='felipear89@gmail.com',
    url='https://github.com/felipear89/pyssh',
    license='GNU',
    package_dir={'': 'src'},
    packages=[''],
    entry_points={
        'console_scripts': [
            'sytssh = sytssh:main'
        ]
    },
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    install_requires=INSTALL_REQUIRES
)
