from setuptools import setup

name = 'memrise'
version = '1.0.0'
install_requires = ['requests','bs4','mateco','googletrans==4.0.0rc1']
description = 'Scaping Memrise course infomation'


with open("README.md",'r',encoding='utf-8') as fh:
    long_description = fh.read()

keywords = [name]

classifiers = [
    'Intended Audience :: Education',
    'Intended Audience :: Information Technology',
    'Intended Audience :: Developers',
    'Intended Audience :: End Users/Desktop',
    'Natural Language :: French',
    'Development Status :: 1 - Planning',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
]
###################################################
setup(
    name=name,
    version = version,
    package_dir = {'','src'}
    packages=[name],
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers = classifiers,
    install_requires = install_requires,
    include_package_data=True,
    license='MIT',
)