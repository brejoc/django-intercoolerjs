import os

from codecs import open
from setuptools import setup, find_packages

repo_path = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(repo_path, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

with open(os.path.join(repo_path, 'requirements.txt')) as f:
    requirements = f.read().splitlines()

setup(
    name='django-intercoolerjs',
    version='1.1.1.0',
    url="https://github.com/brejoc/django-intercoolerjs",
    description='Django wrapper for intercooler.js - AJAX With Attributes: There is no need to be complex.',
    long_description=long_description,
    author='Jochen Breuer',
    author_email='brejoc@gmail.com',
    license='MIT',
    keywords='django jquery zepto staticfiles intercoolerjs'.split(),
    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
    packages=find_packages(),
    package_data={'intercoolerjs': ['static/intercoolerjs/js//*']},
    install_requires=requirements,
    zip_safe=False,
)
