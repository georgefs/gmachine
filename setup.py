import os

from setuptools import setup
from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))


with open(os.path.join(here, 'README.md')) as f:
        README = f.read()

        REQUIREMENTS = []

setup(
    name='gmachine',
    version='0.1',
    description='gmachine',
    author='georgefs',
    author_email='georgefs@gmail.com',
    long_description=README,
    scripts=[],
    url='https://github.com/georgefs/gmachine.git',
    packages=find_packages(),
    license='MIT License',
    platforms='Posix; MacOS X; Windows',
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIREMENTS,
    entry_points={
        'console_scripts': [
            'gmachine = gmachine.cmd:main',
        ]
    },
    package_data = {
        '': ['bin/*'],
    },
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet',
    ]
)
