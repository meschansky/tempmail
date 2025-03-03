import os
from setuptools import setup, find_packages


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


long_description = read('README.rst')


setup(
    name='tempMail2',
    version='1.0.3',
    license='MIT',
    description='Python wrapper for online service which provides '
                'temporary email address: https://temp-mail.org/ V2',
    long_description=long_description,
    keywords='temporary temp mail email address wrapper api anon '
             'anonymous secure free disposable',
    url='https://github.com/meschansky/tempmail',
    author='Oyetoke Toby',
    author_email='oyetoketoby80@gmail.com',
    include_package_data=True,
    packages=find_packages(),
    install_requires=['requests'],
    download_url='https://github.com/meschansky/tempmail/archive/1.0.3.tar.gz',
    py_modules=['tempmail2'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet :: WWW/HTTP'
    ],
)
