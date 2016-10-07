import os
from distutils.core import setup
from distutils.command.install import INSTALL_SCHEMES
from setuptools import find_packages
from steering import __version__, __description__

def read(*rnames):
    with open(os.path.join(os.path.dirname(__file__), *rnames)) as ff:
        return ff.read()

setup(
    name='sdc',
    version=__version__,
    author='Piensa Labs',
    author_email='hello@piensa.co',
    url='https://github.com/piensa/sdc-steering',
    download_url='https://github.com/piensa/sdc-steering',
    description='Self Driving Car - Challenge #2',
    long_description=(read('README.md')),
    classifiers=[
        'Development Status :: 1 - Planning',
    ],
    license="MIT",
    keywords="self driving car keras tensorflow",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
      'keras',
    ]
)
