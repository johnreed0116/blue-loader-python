#from distribute_setup import use_setuptools
#use_setuptools()

from setuptools import setup, find_packages
from os.path import dirname, join

here = dirname(__file__)
setup(
    name='ledgerblue',
    version='0.1.1',
    author='Ledger',
    author_email='hello@ledger.fr',
    description='Python library to communicate with Ledger Blue',
    long_description=open(join(here, 'README.md')).read(),
    packages=find_packages(),
    install_requires=['hidapi>=0.7.99', 'secp256k1>=0.12.1', 'pycrypto>=2.6.1'],
    extras_require = {
	'smartcard': [ 'python-pyscard>=1.6.12-4build1' ]
    },
    include_package_data=True,
    zip_safe=False,
    classifiers=[
	'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Operating System :: POSIX :: Windows',
	'Operating System :: MacOS :: MacOS X'
    ]
)

