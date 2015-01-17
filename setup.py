from __future__ import division, print_function

import string
from setuptools import setup, find_packages


VERSION = '0.2'
DISTNAME = 'pickleable'
DESCRIPTION = 'Picklify python objects'
with open('README.markdown') as f:
    LONG_DESCRIPTION = f.read()
MAINTAINER = 'Jim Holmstrom'
MAINTAINER_EMAIL = 'jim.holmstroem@gmail.com'
with open('LICENSE') as f:
    LICENSE = f.read()
DOWNLOAD_URL = 'https://github.com/Jim-Holmstroem/pickleable.git'
URL = DOWNLOAD_URL
with open('requirements.txt') as f:
    INSTALL_REQUIREMENTS = filter(None, map(string.strip, f))


setup(
    name=DISTNAME,
    packages=find_packages(),
    include_package_data=True,
    version=VERSION,
    zip_safe=False,
    maintainer=MAINTAINER,
    maintainer_email=MAINTAINER_EMAIL,
    install_requires=INSTALL_REQUIREMENTS,
    download_url=DOWNLOAD_URL,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    license=LICENSE,
    classifiers=[
        'Intended Audience :: Parallel Computing',
        'Programming Language :: Python',
        'Topic :: Software Development',
        'Operating System :: Unix',
    ],
    py_modules=[
    ],
    entry_points={
    },
)
